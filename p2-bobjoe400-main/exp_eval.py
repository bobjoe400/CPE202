from stack_array import Stack
import operator

#as using String.eval() was not allowed, i decided to implement the operator class
#which has methods which are 'a set of efficent functions corrosponding to the intrisic operators of Python"
#this seems fair to me as these fuctions act the same as (x+y), which use the intrinsic values of the items.
#it saved time from me writings functions such as
# def add(a,b):
#     return float(a) + float(b)
#
#or for the bitwise
# def lshift(a,b):
#   try:                '''this creates an issue where you cannot create a binary number of a float'''
#       return a<<b     '''the above is important because x<<y is the same as x * 2 ** y, and this needs
#                        to come out as an integer number, because it must return a binary, so the bits of
#                        the new data can be converted to their non-binary data-types, and the only way for thes
#                        above to be true would be for all of the numbers need to be integers because floats can have
#                        some inaccuracy to them when you multiply and divide'''
#   except:
#       raise TypeError
#
#and also saved time on tests since everything was able to be covered with one test file, as both test and
#test_helper are the same.

#our dictionary of acceptable operators, their related functions, their precedence, and their assaignment

OPER = {'+': [operator.add, 0, 'L'],
        '-': [operator.sub, 0, 'L'],
        '*': [operator.mul, 1, 'L'],
        '/': [operator.truediv, 1, 'L'],
        '**': [operator.pow, 2, 'R'],
        '<<': [operator.lshift, 3, 'L'],
        '>>': [operator.rshift, 3, 'L']}

class PostfixFormatException(Exception):
    pass

#this function we take in a string, and iterate through it, creating a stack that is mutated and will
#eventually be reduced to a single number (assuming its well formatted)

def postfix_eval(input_str):
    '''Evaluates a postfix expression
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation.
    Raises an PostfixFormatException if the input is not well-formed'''

    expr = input_str.split() #spliitting the string, checking if its empty, and creating an empty stack of max size
                             #30 as described by the project assignment
    if len(expr) == 0:
        raise PostfixFormatException('Empty input')
    numbers = Stack(30)
    for i in expr:                       #iterating through the split expression
        if is_digit(i):
            try:                         #pushing the correct number type to the push it to the stack
                numbers.push(int(i))
            except ValueError:
                numbers.push(float(i))
        else:
            try:                         #trying to calculate what the new list will look like and raising the error if there is one
                numbers = calc(i, numbers)
            except PostfixFormatException as err:
                raise err
    if numbers.size() != 1:              #checks if we have any other different setup than 1 number left in the stack
        raise PostfixFormatException('Too many operands')
    if  round(numbers.peek() - int(numbers.peek()),3) == 0: #returns the number and converts it to an int if it is an integer
        return int(numbers.pop())
    else:
        return numbers.pop()

#this function follows the psuedocode written out in the lab almost exactly. Iterate through the passed in string,
#perform the necessary actions for each operand/operator, combine in to a larger string, return said string

def infix_to_postfix(input_str):
    '''Converts an infix expression to an equivalent postfix expression
    Input argument:  a string containing an infix expression where tokens are
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression '''
    expr = input_str.split()
    post = Stack(30) #the stack of current operators
    rpn = []
    for i in expr:
        if is_digit(i):
            rpn.append(i) #since we are returning a string we dont need to convert to an int like the prev method
        elif i == '(': #as in the psuedocode, if we see a opening parenthese we just push it
            post.push(i)
        elif OPER.get(i,None) is not None: #now, if we get to an operator, eg if its in our dictionary, do
            if post.size() != 0:           #something with it, where we first check if the operator stack is
                o1 = OPER.get(i)           #empty, and if its not, then we proceed to use the operator algorithim
                                           #for determining what order the operators should be in at that time
                def order(op1,list): #recursive function to go through and reorder the necessary operators
                    if list.is_empty(): #this is if we get to the end of the post while reordering
                        return
                    else:
                        op2 = OPER.get(post.peek(),None) #because we can't have an empty list at this point, we can just peek
                        if op2 is not None: #if the next in the list isn't a '('
                            if (op1[2] == 'L' and op1[1] <= op2[1]) or (op1[2] == 'R' and op1[1] < op2[1]):
                                rpn.append(post.pop()) #appends the popped operator
                                order(op1,post) #checks for order in the next operator
                        else:
                            return
                order(o1,post)
                                    #explaination of the above if statement:
                                    #if o1 (the newest oeprator in the expression) is left-assigned and its
                                    #precedent is lower than -or equal to- that of the top operator in the stack
                                    #or if o1 is right-assigned and its precedent is only lower than that of the top
                                    #operator in the stack, then pop the top operator and append it to the current
                                    #RPN expression, and then check the next value in the stack (if possible)
            post.push(i)            #finally, push o1, which is the next operator, to the top of the operator stack
        else:
            while post.peek() is not '(': #as from the psudocode, and also assuming a well formatted string
                rpn.append(post.pop()) #this is saying to start popping and appending all values in the stack,
                                       #until we see post.peek() is a '(', signifying the end of that expression
            post.pop() #remove the '('
    while not post.is_empty(): #when finish through origional expression, we must now appended what is left of our
        rpn.append(post.pop()) #operators stack to complete the RPN
    return " ".join(rpn) #use a simple array join, with " ",to get the string of the expression

def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    Input argument:  a string containing a prefix expression where tokens are
    space separated.  Tokens are either operators + - * / ** >> << or numbers
    Returns a String containing a postfix expression (tokens are space separated)'''
    reversed = input_str[::-1].split() #reverse and splits the string
    post = Stack(30) #creates our stack to be used
    for i in reversed:
        if is_digit(i): #if its a number simply push
            post.push(i)
        else: #if its an operator, and because we know it will be well formatted, we pop the next two elements in the stack, and append the operator at the end, the push it to the stack.
            num1 = post.pop()
            num2 = post.pop()
            post.push(num1+' '+num2+' '+i)
    return post.pop() #we will only have one string at the top of the stack and we pop it to get our now postfix epression

#simpy returns true or false if the str is 'float-able'
def is_digit(str):
    try:
        float(str)
        return True
    except:
        return False

#mutates the passed in stack based on the requested operation
def calc(opr, num):
    expr = OPER.get(opr, None)
    if expr is not None: #checks if the token is valid
        try: #trys to grab the top two numbers from the stack, and if so, does the operation
            num2 = num.pop() #because our stack is a reverse of our expression, we need to set the b in the equation (a expr b) to be the top of the stack
            num1 = num.pop()
            calculated = expr[0](num1,num2) #calculates the numbers based on the operation that we grab from our dictionary
            num.push(calculated)
            return num
        except ZeroDivisionError: #we get a zero division error if we divide by zero
            raise ValueError('Cannot divide by zero')
        except TypeError: #we get this if we try to use a float in a bit shift operation because you cant shift by a decimal of a bit
            raise PostfixFormatException('Illegal bit shift operand')
        except IndexError: #we get this error when we dont have enough numbers in the stack
            raise PostfixFormatException('Insufficient operands')
    else: #we get this error when we try to pass an invalid operator
        raise PostfixFormatException('Invalid token')
