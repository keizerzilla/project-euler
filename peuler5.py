# PROBLEM: smallest positive number thar is evenly divisible by all of the numbers from 1 to 20
# STATUS: solved!
# AUTHOR: KeizerZilla

# function is_divisible_1to20(n)
# returns True if n is divisible by all number from 1 to 20, False otherwise

def is_divisible_1to20(n):
    for i in range(2, 21):
        if n % i != 0:
            return False
    return True

# main code

number = 20
while True:
    if is_divisible_1to20(number):
        break
    number += 20

print(str(number))
