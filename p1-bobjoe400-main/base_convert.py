# int, int -> string
# Given integer num and base b, converts num to a string representation in base b
numerals = "0123456789ABCDF" #allows for easy access to the different values at different bases
def convert(num, b):
    if(num//b==0): #check if we are at the lowest quotient
        return numerals[num%b]
    else:
        return convert(num//b,b)+numerals[num%b] #recursivly returns the remainder of the next quotient + the current remiander
