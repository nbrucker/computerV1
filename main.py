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


def parse(x):
	tab = x.split(' ')
	new = []
	i = 0
	while (i < len(tab)):
		if (isDigit(tab[i])):
			sign = 1
			if (i > 0 and tab[i - 1] == '-'):
				sign = -1
			new.append(toDigit(tab[i]) * sign)
		i += 1
	return new

def reduceForm(before, after):
	new = []
	x = len(after)
	if (x < len(before)):
		x = len(before)
	i = 0
	while (i < x):
		if (i >= len(after)):
			new.append(before[i])
		elif (i >= len(before)):
			new.append(after[i])
		else:
			new.append(before[i] - after[i])
		i += 1
	return new

def removeEmpty(reduce):
	i = len(reduce) - 1
	while (i > 0):
		if (reduce[i] == 0):
			del reduce[i]
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
            i += 2
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

def fixSpace(s):
    s = s.replace(" ", "")
    i = 0
    while (i < len(s)):
        if (isDigit(s[i]) or s[i] == '+' or s[i] == '*' or s[i] == '='):
            i += 1
            s = s[:i] + ' ' + s[i:]
        elif (s[i] == '-' and i != 0):
            i += 1
            s = s[:i] + ' ' + s[i:]
        elif (s[i] == 'X' and i + 1 < len(s) and s[i + 1] != '^'):
            i += 1
            s = s[:i] + ' ' + s[i:]
        i += 1
    return s

if __name__ == "__main__":
	if (len(sys.argv) != 2):
		error('python main.py [equation]')
	equation = sys.argv[1]
	# parser/lexer
	equation = fixSpace(equation)
	before, after = equation.split('=')
	before = fix(before)
	before = parse(before)
	after = parse(after)
	reduce = reduceForm(before, after)
	reduce = removeEmpty(reduce)
	displayReduce(reduce)
	displayDeg(reduce)
	solve(reduce)
