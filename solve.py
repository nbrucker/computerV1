import math
import sys
from display import displayTwo

def findOption(option, x):
	i = 0
	while (i < len(option)):
		if (option[i] == x):
			return True
		i += 1
	return False

def findDeg(reduce, x):
	i = 0
	while (i < len(reduce[1])):
		if (reduce[1][i] == x):
			return reduce[0][i]
		i += 1
	return 0

def solveZero(reduce, option):
	a = findDeg(reduce, 0)
	if (a == 0 and findOption(option, 'c') == True):
		print('Every number is a solution')
	elif (a == 0):
		print('Every real number is a solution')
	else:
		print('No solution')

def solveOne(reduce):
	a = findDeg(reduce, 1)
	b = findDeg(reduce, 0)
	print('The solution is:')
	result = float(b * -1) / a
	if (int(result) == result):
		print(int(result))
	else:
		print(result)

def solveTwo(reduce, option):
	a = findDeg(reduce, 2)
	b = findDeg(reduce, 1)
	c = findDeg(reduce, 0)
	delta = (b ** 2) - (4 * a * c)
	if (findOption(option, 'd') == True):
		print('Delta: ' + str(round(delta, 6)))
	if (delta > 0):
		print('Discriminant is strictly positive, the two solutions are:')
		print(round(((-b - math.sqrt(delta)) / (2 * a)), 6))
		print(round(((-b + math.sqrt(delta)) / (2 * a)), 6))
	elif (delta == 0):
		print('Discriminant is nul, the solution is:')
		print(round((float(-b) / (2 * a)), 6))
	elif (delta < 0 and findOption(option, 'c') == True):
		print ("Discriminant is stricly negatve, there are two solution in C:")
		displayTwo(a, b, delta, '-')
		displayTwo(a, b, delta, '+')
	else:
		print('Discriminant is strictly negative, no solution in R')

def	solve(reduce, option):
	deg = reduce[1][0]
	if (deg == 0):
		solveZero(reduce, option)
	elif (deg == 1):
		solveOne(reduce)
	elif (deg == 2):
		solveTwo(reduce, option)
	elif (deg > 2):
		print('The polynomial degree is stricly greater than 2, I can\'t solve.')
	else:
		print('I can\'t solve.')
