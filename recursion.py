
def reverse(s):
    """
    Recursive function to reverse the string.
    """
    #base case
    if len(s) <= 1:
        return s
    else:
        #join last element to the reverse of the rest
        return s[-1] + reverse(s[:-1])


    
def permute(s):
    """
    Recursive function to find all permutations of 
    a given string.
    """
    out = [] #empty list
    #base case
    if len(s) <= 1:
        out = [s]
    else:
        #for each element in a string
        for i, let in enumerate(s):
            #permute the remaining recursivaly
            for perm in permute(s[:i] + s[i+1:]):
                #and append 'ele + perm' to a list
                out += [let + perm]
                
    return out           
                                
