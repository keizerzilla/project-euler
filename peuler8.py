# PROBLEM: the bigest number from the product of the 13 adjacent digit in a 1000-digit number
# STATUS: solved!
# AUTHOR: KeizerZilla


# main code

# open file and translate the number into a list
file = open("bignumber.txt", "r")
bignumber = []
line = file.readline()
while line != '':
    for i in range(0, 50):
        bignumber.append(int(line[i]))
    
    line = file.readline()

# scan using a 13-digit window thru the list, calculating the product and saving the max found
maxFound = 0
for i in range(0, len(bignumber)-13):
    number = 1

    for w in range(i, i+13):
        number *= bignumber[w]

    if number > maxFound:
        maxFound = number

print(maxFound)
