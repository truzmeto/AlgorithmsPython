
def pair_sum(arr,k):
    """
    The O(N) algorithm uses the set data structure. We perform a linear
    pass from the beginning and for each element we check whether k-element
    is in the set of seen numbers. If it is, then we found a pair of sum k and
    add it to the output. If not, this element doesn’t belong to a pair yet, and w
    e add it to the set of seen elements.

    The algorithm is really simple once we figure out using a set. The complexity is
    O(N) because we do a single linear scan of the array, and for each element we just
    check whether the corresponding number to form a pair is in the set or add the
    current element to the set. Insert and find operations of a set are both average O(1),
    so the algorithm is O(N) in total.
    """
    
    if len(arr)<2:
        return
    
    # Sets for tracking
    seen = set()
    output = set()
    
    # For every number in array
    for num in arr:
    
        # Set target difference
        target = k-num
    
        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
        else:
            # Add a tuple with the corresponding pair
            output.add( (min(num,target),  max(num,target)) )
            
    return len(output)
