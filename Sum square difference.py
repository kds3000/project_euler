"""
The sum of the squares of the first ten natural numbers is 385

The square of the sum of the first ten natural numbers is 3025

Hence the difference between the sum of the squares of the first ten natural numbers and
the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def square_difference(max_number):
    sum_of_squares = 0
    _sum = 0

    for i in range(1, max_number + 1):
        sum_of_squares += i ** 2
        _sum += i

    return _sum ** 2 - sum_of_squares


if __name__ == "__main__":
    print(square_difference(100))
