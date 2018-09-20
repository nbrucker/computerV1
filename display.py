def displayReduce(reduce):
	i = 0
	new = ''
	while (i < len(reduce)):
		if (reduce[i] >= 0 and i != 0):
			new += '+ '
		elif (reduce[i] < 0):
			new += '-'
			if (i != 0):
				new += ' '
		new += str(abs(reduce[i])) + ' * X^' + str(i) + ' '
		i += 1
	new += '= 0'
	print('Reduced form: ' + new)


def displayDeg(reduce):
	print('Polynomial degree: ' + str(len(reduce) - 1))
