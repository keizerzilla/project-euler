# PROBLEM: diff between the sum of the squares and the square of the sum of the first 100 natural numbers
# STATUS: solved!
# AUTHOR: KeizerZilla

# main code

sum_of_squares = 0
square_of_sum = 0
for i in range(1, 101):
	sum_of_squares += i * i
	square_of_sum += i

square_of_sum *= square_of_sum

print(str(sum_of_squares - square_of_sum))
