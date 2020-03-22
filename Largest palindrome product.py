"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def largest_palindrome(digit_count):
    max_number = int('9' * digit_count)
    a = b = max_number
    result = {'digit count': 0,
              'first number': 0,
              'second number': 0,
              'product': 0
              }
    while a > 100:
        product = a * b
        if palindrome_check(product) and product > result['product']:
            result['digit count'] = digit_count
            result['first number'] = a
            result['second number'] = b
            result['product'] = product
        b -= 1
        if b == 100:
            b = max_number
            a -= 1
    return result


def palindrome_check(number):

    str_number = str(number)
    number_len = len(str_number)
    middle = number_len // 2

    first_half = []
    second_half = []

    for i in range(middle):
        first_half.append(str_number[i])

    for i in range(middle if number_len % 2 == 0 else middle + 1,
                   number_len):
        second_half.append(str_number[i])

    second_half.reverse()

    return True if first_half == second_half else False


if __name__ == "__main__":
    result = largest_palindrome(3)
    print("Largest palindrome made from the product of two {0}-digit numbers is {1}. "
          "It has been gotten by multiplying {2} and {3} ".format(str(result['digit count']),
                                                                  str(result['product']),
                                                                  str(result['first number']),
                                                                  str(result['second number'])
                                                                  )
          )
