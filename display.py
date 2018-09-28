def displayReduce(reduce):
	i = 0
	new = ''
	while (i < len(reduce[0])):
		if (reduce[0][i] >= 0 and i != 0):
			new += '+ '
		elif (reduce[0][i] < 0):
			new += '-'
			if (i != 0):
				new += ' '
		new += str(abs(reduce[0][i])) + ' * X^' + str(reduce[1][i]) + ' '
		i += 1
	new += '= 0'
	print('Reduced form: ' + new)


def displayDeg(reduce):
	print('Polynomial degree: ' + str(reduce[1][0]))

def displayTwo(a, b, delta, sign):
	new = ''
	new += '-' + str(abs(b)) + ' ' + sign + ' i('
	new += str(abs(delta)) + ')'
	new += ' / 2 * ' + str(abs(a))
	print new
