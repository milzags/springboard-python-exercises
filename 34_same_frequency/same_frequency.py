def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    first = list(str(num1))
    second = list(str(num2))
    first.sort(), second.sort()
    return first == second

print(same_frequency(551122, 221515)) # true