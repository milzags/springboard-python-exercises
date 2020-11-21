def print_upper_words(list):
    """ print a list of words on separate lines, but in all uppercase """
    for word in list:
        upper_case = word.upper()
        print(upper_case)

print_upper_words(['hello','hey','yo','yes'])

def print_specific_words(list, letter):
    """ print a list of words on separate lines if they start with a 
    specific letter """
    for word in list:
        if word.startswith(letter):
            print(word)

print_specific_words(['hello','hey','yo','yes'], 'y')