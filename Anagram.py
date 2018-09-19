def anagram(s1,s2):
    """
    Function checks if two strings are anagrams. 
    It initially removes all white spaces and transforms
    all letters into lower case. Then, it compares length
    of strings as an edge case check. If lengths are equal, it
    uses hash table method(dict) to count occurences of letters
    for each string. By subtracting occurences it determines
    if strings are anagrams.
    """

    # Remove spaces and lowercase letters
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    # Edge Case to check if same number of letters
    if len(s1) != len(s2):
        return False
    
    #Create counting dictionary (Note could use DefaultDict from Collections module)
    count = {}
           
    # Fill dictionary for first string (add counts)
    for letter in s1:          #loop over letters in string s1
        if letter in count:    #if letter is already in count, add value 1 to specific letter key
            count[letter] += 1 
        else:
            count[letter] = 1  #otherwise set it to one
            
    # Fill dictionary for second string (subtract counts)
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    # Check that all counts are 0
    for k in count:
        if count[k] != 0:
            return False

    # Otherwise they're anagrams
    return True
