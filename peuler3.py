# PROBLEM: largest prime factor of 600851475143
# STATUS: wip
# AUTHOR: KeizerZilla

import platform
import os

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True

clear_cmd = ""
if platform.system() == "Windows":
    clear_cmd = "cls"
else:
    clear_cmd = "clear"

number = 13195
div = number

while True:
    if(div % 2 != 0):
        if(number % div == 0):
            if(is_prime(div)):
                break
    div -= 1
    os.system(clear_cmd)
    print("TESTING: " + str(div))

print("MATCH: " + str(div))
