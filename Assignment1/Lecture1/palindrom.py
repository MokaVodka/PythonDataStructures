def is_palindrome(s, first, last):
    sameFirstLast = first == last

    # Find the betweens and check if palindrome
    betweenIsPalindrome = True
    between = s[1:len(s) - 1]
    if len(between) > 1:
        betweenIsPalindrome = is_palindrome(between, between[0], between[-1])

    return sameFirstLast and betweenIsPalindrome


def check_palindrome(s):

    # Base case, empty string and length = 1
    if len(s) <= 1:
        return True

    # Recursive step
    else:
        return is_palindrome(s, s[0], s[-1])


# -- Main Program --
def simple_palindrome():

    # Change input here
    stringInput = 'Anna'

    isPalindrome = check_palindrome(stringInput)
    print(f'"{stringInput}" is {'' if isPalindrome else 'not '}a palindrome')


simple_palindrome()
