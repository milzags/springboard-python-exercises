def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    for char in phrase:
        if char == to_swap and char.islower():
            return char.upper()
        elif char == to_swap and char.isupper():
            return char.lower()
    

print(flip_case('Aaaahhh','a'))
