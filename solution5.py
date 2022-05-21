# 5. Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not.

# A palindrome is a word that is the same when it is reversed, such as madam, radar, kayak, or tacocat.


def is_palindrome(string):
    if len(string) <= 1:
        return True
    elif string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False


print(is_palindrome("radar"))
print(is_palindrome("kayak"))
print(is_palindrome("Landen"))
