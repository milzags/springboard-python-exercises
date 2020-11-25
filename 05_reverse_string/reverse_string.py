def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reversed_string = ''.join(reversed(phrase))
    return reversed_string

print(reverse_string('awesome'))
print(reverse_string('sauce'))
