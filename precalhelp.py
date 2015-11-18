import factor
import trigfunctions
import raddegree

def getFactors() :
	print "enter number to be factored"
	x = eval(raw_input("> "))
	factor.Factor(x)
	User_Prompt()

def getFunctions() :
	trigfunctions.Find_Functions()		
	User_Prompt()
	
def Conversion() :
	raddegree.Get_Answer()
	User_Prompt()

def User_Prompt() :
	print """
		What would you like to do?
		[1] Find factors of a number.
		[2] Find trigonometric functions.
		[3] Convert radians to degrees or degrees to radians
		[4] Exit
		"""
	userInput = eval(raw_input("> "))
	if userInput == 1 :
		getFactors()
	elif userInput == 2 :
		getFunctions()
	elif userInput == 3 :
		Conversion()
	elif userInput == 4 :
		exit()

User_Prompt() 
