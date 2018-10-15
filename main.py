import sys
from error import error
from display import displayReduce, displayDeg
from solve import solve

def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def toDigit(x):
	try:
		return int(x)
	except ValueError:
		return float(x)

def expoCheck(tab, x):
    i = 0
    while (i < len(tab)):
        if (tab[i] == x):
            return i
        i += 1
    return -1

def parse(x):
	tab = x.split(' ')
	new = []
	num = []
	expo = []
	i = 0
	while (i < len(tab)):
		if (isDigit(tab[i])):
			sign = 1
			if (i > 0 and tab[i - 1] == '-'):
				sign = -1
			if (i + 2 < len(tab)):
				n = expoCheck(expo, toDigit(tab[i + 2][2:]))
				if (n == -1):
					num.append(toDigit(tab[i]) * sign)
					expo.append(toDigit(tab[i + 2][2:]))
				else:
					num[n] += toDigit(tab[i]) * sign
		i += 1
	new.append(num)
	new.append(expo)
	return new

def reduceForm(before, after):
	new = []
	num = []
	expo = []
	i = 0
	while (i < len(before[1])):
		n = expoCheck(after[1], before[1][i])
		if (n == -1):
			num.append(before[0][i])
		else:
			num.append(before[0][i] - after[0][n])
			del after[0][n]
			del after[1][n]
		expo.append(before[1][i])
		i += 1
	i = 0
	while (i < len(after[1])):
		num.append(-after[0][i])
		expo.append(after[1][i])
		i += 1
	new.append(num)
	new.append(expo)
	return new

def removeEmpty(reduce):
	i = len(reduce[0]) - 1
	while (i > 0):
		if (reduce[0][i] == 0):
			del reduce[0][i]
			del reduce[1][i]
		else:
			return reduce
		i -= 1
	return reduce

def fix(s):
    i = 0
    while (i < len(s)):
        while (i < len(s) and not isDigit(s[i]) and s[i] != 'X'):
            i += 1
        if (i < len(s) and s[i] == 'X'):
            s = s[:i] + '1 * ' + s[i:]
            i += 5
            if (i < len(s) and s[i] != '^'):
                s = s[:i] + '^1' + s[i:]
        if (i < len(s) and isDigit(s[i])):
            i = digitLen(s, i) + 1
            if (i < len(s) and s[i] == '*'):
                i += 3
                if (i < len(s) and s[i] != '^'):
                    s = s[:i] + '^1' + s[i:]
            else:
                s = s[:i] + '* X^0 ' + s[i:]
        while (i < len(s) and s[i] != '+' and s[i] != '-'):
            i += 1
        i += 1
    return s

def digitLen(s, i):
    while (i < len(s) and (isDigit(s[i]) or s[i] == '.')):
        i += 1
    return i

def fixSpace(s):
    s = s.replace(" ", "")
    i = 0
    while (i < len(s)):
        if (s[i] == '+' or s[i] == '*' or s[i] == '='):
            i += 1
            s = s[:i] + ' ' + s[i:]
        elif (isDigit(s[i])):
            i = digitLen(s, i)
            s = s[:i] + ' ' + s[i:]
        elif (s[i] == '-' and i != 0 and s[i - 1] != '^'):
            i += 1
            s = s[:i] + ' ' + s[i:]
        elif (s[i] == 'X' and i + 1 < len(s) and s[i + 1] != '^'):
            i += 1
            s = s[:i] + ' ' + s[i:]
        i += 1
    return s

def check(eq):
    i = 0
    equal = 0
    while (i < len(eq)):
        if (eq[i] == '='):
            equal += 1
            i += 1
        elif (isDigit(eq[i]) or eq[i] == '^' or eq[i] == '+' or eq[i] == '-'
         or eq[i] == ' ' or eq[i] == '*' or eq[i] == '.' or eq[i] == 'X'):
            i += 1
        else:
            return False
    if (equal != 1):
        return False
    else:
        return True

def sort(reduce):
	i = 0
	while (i < len(reduce[0])):
		j = i
		while (j < len(reduce[0])):
			if (reduce[1][i] < reduce[1][j]):
				tmp = reduce[0][i]
				reduce[0][i] = reduce[0][j]
				reduce[0][j] = tmp
				tmp = reduce[1][i]
				reduce[1][i] = reduce[1][j]
				reduce[1][j] = tmp
			j += 1
		i += 1
	return reduce

def OptionCheck(option):
	if (len(option) < 2 or option[0] != '-'):
		error('Bad options')
	i = 1
	while (i < len(option)):
		if (option[i] == "c" or option[i] == "d"):
			i += 1
		else:
			error('Bad options')

if __name__ == "__main__":
	if (len(sys.argv) == 2):
		equation = sys.argv[1]
		option = list("")
	elif (len(sys.argv) == 3):
		option = list(sys.argv[1])
		OptionCheck(option)
		equation = sys.argv[2]
	else:
		error('python main.py [-dc] [equation]')
	if (check(equation) == False):
		error('Unvalid equation')
	equation = fixSpace(equation)
	before, after = equation.split('=')
	before = fix(before)
	after = fix(after)
	before = parse(before)
	after = parse(after)
	reduce = reduceForm(before, after)
	reduce = removeEmpty(reduce)
	reduce = sort(reduce)
	displayReduce(reduce)
	displayDeg(reduce)
	solve(reduce, option)
