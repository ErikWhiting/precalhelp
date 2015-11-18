from __future__ import division #to make fractions evaluate to floats
import fractions #for divisor funtion to simplify fractions

def Degrees_To_Radians() :
	degrees = eval(raw_input("enter number of degrees "))
	if degrees >= 360 :
		j = degrees // 360
		degrees = degrees - (360 * j)
	
	radians = degrees / 180
	divisor = fractions.gcd(degrees, 180)
	numerator = degrees / divisor
	denominator = 180 / divisor
	if numerator == 0 :
		print 0
	elif numerator != 1 : #to avoid 1pi/denominator
		print numerator, "pi /", denominator
	else :
		print "pi/", denominator
		
def Radians_To_Degrees() :
	radians = eval(raw_input("enter number of radians "))
	degrees = radians * 180.0
	print degrees, " degrees"

def Get_Answer() :
	print """
		[1] For degrees to radians
		[2] For radians to degrees
		"""
	userInput = eval(raw_input("> "))
	if userInput == 1 :
		Degrees_To_Radians()
	else :
		Radians_To_Degrees()
