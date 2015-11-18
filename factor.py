def Factor(x) :
	for i in range(1, x) :
		if x % i == 0 :
			factorNumber = x / i
			if factorNumber > i :
				print "%i  x  %i " % (factorNumber, i)
