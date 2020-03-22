"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def evenly_div_min(max_divisor):
    result = 0
    while True:
        result += max_divisor
        for i in range(max_divisor, 1, -1):
            if result % i != 0:
                break
            if i == 2:
                return result


if __name__ == "__main__":
    print(evenly_div_min(20))
