def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    frequency = {}
    for char in phrase:
        frequency[char] = phrase.count(char)
    return frequency

print(multiple_letter_count('yay'))
print(multiple_letter_count('Yay'))

# will return a dictionary of key-value pairs for all occurences of the letter in the phrase
