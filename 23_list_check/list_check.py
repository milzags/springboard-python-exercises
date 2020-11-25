def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    for item in lst:
        return any(isinstance(item, list))
        
     
print(list_check([[1], [2, 3]]))
print(list_check([[1], "nope"]))