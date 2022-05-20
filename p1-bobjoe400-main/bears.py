
# int -> booelan
# Given integer n, returns True or False based on reachabilty of goal
def bears(n):
    return 42 in createlist(n) #checks if we reached 42 somewhere in our calculations
def createlist(n):
    if n<42: #checking for values less than 42
        return []
    elif n == 42: #base case
        return[42]
    else:
        list = [n] #we create a new list with the head of n
        nA = (-1,n-(n//2))[n%2==0] #the next 3 lines calculate the options, setting to -1 if not possible
        nB = int((-1,n-(int(str(n)[-1])*int(str(n)[-2])))[n%3==0 or n%4==0]) #getting the last two digits by converting to a str getting the last to chars, then back to an int for multiplication, then forcing int multiplication
        nC = (-1,n-42)[n%5==0]
        for i in (nA,nB,nC):
            if i != -1 and i>=42 and i!=n: #checks if each option is possible, if the option results in a number greater than 42, and if there is a change in n
                list = list + createlist(i) #recursively concatinates the list with the possible options
        return list #finally, returns the list
