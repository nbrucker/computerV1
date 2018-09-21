import math

def solveZero(reduce):
	if (reduce[0] == 0):
		print('Every real number is a solution')
	else:
		print('No solution')

def solveOne(reduce):
	print('The solution is:')
	result = float(reduce[0] * -1) / reduce[1]
	if (int(result) == result):
		print(int(result))
	else:
		print(result)

def solveTwo(reduce):
	delta = (reduce[1]**2) - (4 * reduce[2] * reduce[0])
	if (delta > 0):
		print('Discriminant is strictly positive, the two solutions are:')
		print(round(((-reduce[1] - math.sqrt(delta)) / (2 * reduce[2])), 6))
		print(round(((-reduce[1] + math.sqrt(delta)) / (2 * reduce[2])), 6))
	elif (delta == 0):
		print('Discriminant is nul, the solution is:')
		print(round((float(-reduce[1]) / (2 * reduce[2])), 6))
	else:
		print('Discriminant is strictly negative, no solution')

def	solve(reduce):
	deg = len(reduce) - 1
	if (deg < 1):
		solveZero(reduce)
	elif (deg == 1):
		solveOne(reduce)
	elif (deg == 2):
		solveTwo(reduce)
	elif (deg > 2):
		print('The polynomial degree is stricly greater than 2, I can\'t solve.')
