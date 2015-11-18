def Know_Sine(y, r) :
	xsquared = abs((r**2) - (y**2))
	x = xsquared**.5
	if r > y :
		x = x*-1
	if (x % 1 != 0 and x > 0) :
		x  = "sqrt%i" % xsquared
	if (x % 1 != 0 and x < 0) :
		x = "-sqrt%i" % xsquared
	return x

def Know_Cosine(x, r) :
	ysquared = abs((r**2) - (x**2))
	y = ysquared**.5
	if r > x :
		y = y*-1
	if (y % 1 != 0 and y > 0) :
		y = "sqrt%i" % ysquared
	if (y % 1 != 0 and y < 0) :
		y = "sqrt%i" % ysquared
	return y

def Know_Tangent(x, y) :
	rsquared = abs((x**2) + (y**2))
	r = rsquared**.5
	if (r % 1 != 0) :
		r = "sqrt%i" % rsquared
	return r

def Print_Functions(y, x, r) :
	print "Sine = ", y, "/", r
	print "Cosine = ", x, "/", r
	print "Tangent = ", y, "/", x
	print "Cosecant = ", r, "/", y
	print "Secant = ", r, "/", x
	print "Cotangent = ", x, "/", y

def Find_Functions() :		
	print """
			[1] - I know two sides.
			[2] - I know a side and hypotenuse.
			[3] - I know a function.
			"""
	userResponse = eval(raw_input("Enter 1, 2, or 3 "))

	if userResponse == 1 :
		opposite = eval(raw_input("enter opposite side "))
		adjacent  = eval(raw_input("enter adjacent side "))
		r = Know_Tangent(opposite, adjacent)
		Print_Functions(opposite, adjacent, r)
	elif userResponse == 2 :
		r = eval(raw_input("enter hypotenuse "))
		x = eval(raw_input("enter adjacent side "))
		y = Know_Cosine(x, r)
		Print_Functions(y, x, r)
	elif userResponse == 3 :
		print """
			Which do you know?
			[1] Sine	[4] Cosecant
			[2] Cosine	[5] Secant
			[3] Tangent	[6] Cotangent
			"""
		secondResponse = eval(raw_input("> "))
		if secondResponse == 1 :
			y = eval(raw_input("enter numerator "))
			r = eval(raw_input("enter denominator "))
			x = Know_Sine(y, r)
			Print_Functions(y, x, r)
		elif secondResponse == 2 :
			x = eval(raw_input("enter numerator "))
			r = eval(raw_input("enter denominator "))
			y = Know_Cosine(x, r)
			Print_Functions(y, x, r)
		elif secondResponse == 3 :
			y = eval(raw_input("enter numerator "))
			x = eval(raw_input("enter denominator "))
			r = Know_Tangent(x, y)
			Print_Functions(y, x, r)
		elif secondResponse == 4 :
			r = eval(raw_input("enter numerator "))
			y = eval(raw_input("enter denominator "))
			x = Know_Sine(y, r)
			Print_Functions(y, x, r)
		elif secondResponse == 5 :
			r = eval(raw_input("enter numerator "))
			x = eval(raw_input("enter denominator "))
			y = Know_Cosine(x, r)
			Print_Functions(y, x, r)
		elif secondResponse == 6 :
			x = eval(raw_input("enter numerator "))
			y = eval(raw_input("enter denominator "))
			r = Know_Tangent(x, y)
			Print_Functions(y, x, r)
