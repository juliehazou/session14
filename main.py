import random
import china, austria
from austria import cook as austria_cook
from china import cook as china_cook
from latm.argentina import cook as argentina_cook
from latm.brazil import cook as brazil_cook
from latm.mexico.yucantan import cook as yucatan_cook

import sys

def cook():
    print("we are making paella")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    print("prime numbers")
    print(is_prime(5))
    print(is_prime(7))
    print(is_prime(19))
    print(is_prime(101))

    print("not prime numbers")
    print(is_prime(6))
    print(is_prime(9))
    print(is_prime(8))



print("a random number is: ", random.randint(1, 10))
china_cook()
china.greet()
austria_cook()
austria.greet()
cook()
argentina_cook()
brazil_cook()
yucatan_cook()



