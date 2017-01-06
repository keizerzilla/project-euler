# PROBLEM: largest prime factor of 600851475143
# STATUS: wip
# AUTHOR: KeizerZilla

# function is_prime(n)
# returns True if n is a prime number, False otherwise

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

# main code

number = 600851475143
div = 2
ret = div

print("SEARCHING...")

while number > 1:
    if(is_prime(div)):
        if(number % div == 0):
            ret = div
            number /= div
            div -= 1
            print("CANDIDATE: " + str(ret))

    div += 1

print("MATCH: " + str(ret))
