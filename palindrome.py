# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.

def is_palindrome(string):
    num_pal = 0
    for i in range(len(string)):
        str_replace = string.replace(string[i], "")
        if str_replace[::-1] == str_replace:
            num_pal +=1
    if num_pal > 0:
        return True
    return False

print(is_palindrome('aba'))
print(is_palindrome('abc'))
print(is_palindrome('abca'))


