# PROBLEM: find the sum of the even-valued terms of the fibonacci sequence up to less than 4kk
# STATUS: solved!
# AUTHOR: KeizerZilla

def fibo(limit):
    sequence = []
    sequence.append(1)
    sequence.append(2)

    index = 1
    l = sequence[index] + sequence[index-1]
    while l < limit:
        sequence.append(l)
        index += 1
        l = sequence[index] + sequence[index-1]

    return sequence

sum = 0;
for value in fibo(4000000):
    if value % 2 == 0:
        sum += value

print(str(sum))
