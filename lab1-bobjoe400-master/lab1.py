# CPE 202 Lab 1

# Data definitions:

# Maybe_List is either
# Python List
# or
# None

# Maybe_integer is either
# integer
# or
# None

# Signature: Maybe_List -> Maybe_integer
# Purpose: Find the index of the largest number
def max_list_iter(int_list):
    '''Finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError'''
    if not int_list:
        if int_list is None:
            raise ValueError('No list!')
        return None
    else:
        max = float('-inf')
        for i in int_list:
            if i > max:
                max = i
        return max 

# Signature: Maybe_List -> Maybe_List
# Purpose: Return the reverse of the input list 
def reverse_list(int_list):
    '''Returns the reverse of the input list, but does not mutate the input list
    If list is None, raises ValueError'''
    if int_list is None:
        raise ValueError('No list!')
    else:
        newlist = []
        for i in range(len(int_list)-1,-1,-1):
            newlist.append(int_list[i])
        return newlist

# Signature: Maybe_List -> None
# Purpose: Reverse the original input list 
def reverse_list_mutate(int_list):
    '''Reverses a list, modifying the input list
    If list is None, raises ValueError'''
    if int_list is None:
        raise ValueError('No list')
    else:
        for i in range(len(int_list)):
            int_list.insert(i,int_list.pop())
    return int_list

# Signature: Maybe_List -> Maybe_List
# Purpose: Return the reverse of the input list using recursion
def reverse_rec(int_list):   # must use recursion
    '''Returns the reverse of the input list, but does not mutate the input list.
    May NOT mutate the original list. If list is None, raises ValueError'''
    if int_list is None:
        raise ValueError('No list')
    if len(int_list)==1:
        return [int_list[0]]
    else:
        rev =  [int_list[-1]]
        tmplist = int_list[:len(int_list)-1]
        rev+=reverse_rec(tmplist)
        return rev
