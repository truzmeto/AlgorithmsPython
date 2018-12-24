
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
                                


def fibo_rec(n):
    """
    Recursive function to find n-th Fibonachi number
    """
    #base case
    if n == 0:
        return 0
    elif n == 1 :
        return 1
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)   



    
n = 60
cache = [None] * (n + 1)

def fibo_dyn(n):
    """
    Cached implementation of fibonachi number calculation.
    I saves already calculated Fib. number in a cache so that
    it can be retrieved faster next time. This is efficient
    solution only if we do multiple calls to a function. Otherwise
    it is same as recursive solution.
    """
    
    #base case
    if n == 0 or n == 1:
        return n
    else:
        #check cache
        if cache[n] != None:
            return cache[n]
        
        cache[n] = fibo_dyn(n-1) + fibo_dyn(n-2)   
    
    return cache[n]
