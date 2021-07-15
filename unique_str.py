# Given a string, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.

def unique_char(string):
    list_of_letters = [letter if letter.isalnum() else '' for letter in string]
    uniques = []
    duplicates = []
    for i in list_of_letters:
        if i not in uniques:
            uniques.append(i)
        else:
            duplicates.append(i)
    diff_lists = list(set(uniques) - set(duplicates))
    if len(diff_lists) > 0:
        return string.index(diff_lists[0])
    else:
        return -1

print(unique_char('stringstring'))

