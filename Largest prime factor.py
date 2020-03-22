"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


def prime_check(number):
    flag = True
    for i in range(2, number):
        if number % i == 0:
            flag = False
            break
    return flag


def largest_prime_factor(number):
    half = number // 2 + 1
    for i in range(2, half):
        if number % i == 0:
            factor = number // i
            if prime_check(factor):
                return factor


if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
