def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """

    total_length = len(phrase)

    if n < 3:
        return 'Truncation must be at least 3 characters'
    else:

        if total_length > n:
            return phrase[0:n-3] + '...'
        elif total_length < n:
            return phrase
    
print(truncate('Hello World', 6))
print(truncate("Problem solving is the best!", 10))
print(truncate('Cool', 1))
print(truncate("Woah", 4)) #this is the only string that doesn't return correct value
print(truncate("Woah", 3))