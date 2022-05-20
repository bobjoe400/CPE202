# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
def perm_gen_lex(str_in):
    list = []
    if len(str_in) <= 1: #Checking the end cases, either is length 1 or its empty
        return [str_in]
    else:
        for i in str_in: #iterates through each char of the input string
            str = str_in.replace(i,"") #removes the current character and creates a string without it
            list = list + [i+ str for str in perm_gen_lex(str)] #adds to the current list the list of the inner permuntations
        return list
