# PROBLEM: find the 10001st prime number
# STATUS: solved!
# AUTHOR: KeizerZilla

import math

# function isPrime
# returns True if n is a prime number, False otherwise

def isPrime(n):
    count = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

# main code

count = 1
number = 3
found = 0

while count < 10001:
    if isPrime(number):
        found = number
        count += 1
        #print("PRIMES FOUND = " + str(count))
    
    number += 2

print(found)
