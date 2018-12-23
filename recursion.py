
def reverse(s):
    """
    Recursive function to reverse the string.
    """
    
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])


    
def permute(s):
    """
    Recursive function to find all permutations of 
    a given string.
    """
    out = []
    if len(s) <= 1:
        out = [s]
    else:
        
        for i, let in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                
                out += [let + perm]
                
    return out           
                                
