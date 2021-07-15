#in this exercise I will define a function to reverse a string

def reverse_str(string):
    rev = string[::-1]
    return rev

print(reverse_str('try this!'))


def reverse_num(num):

    str_num = str(num)
    if str_num[0] == '-':
        rev = str(num[:0:-1])
    else:
        rev = str(num[::-1])
    return rev

print(reverse_num('-57'))
