"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def nth_prime_number(n):

    number = 1
    value = 2

    while number != n:
        value += 1
        for i in range(2, value):
            if value % i == 0:
                break
            if i == value - 1:
                number += 1
                print(number)

    return value


if __name__ == "__main__":
    print(nth_prime_number(10001))
