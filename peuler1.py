# PROBLEM: sum of all multiples of (3, 5) bellow 100
# STATUS: solved!
# AUTHOR: KeizerZilla

# main code

sum = 0;

for i in range(3, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(sum)
