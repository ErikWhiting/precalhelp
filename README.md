# precalhelp
CLI interface that automates some repetitive tasks inherent in Precal/Trig homework.

By github user erik-d-w

November 17, 2015

OVERVIEW
Precalhelp is a command-line script written in Python that automates tedious tasks while doing precalculus or trigonometry
homework. The three functions are : 

factoring - give the program a number and it will find integral factors.  Useful for simplifying quadratic equations.

6 trig functions - prompts the user for information and then calculates and displays sine, cosine, tangent, secant, cosecant
and cotangent.

Radians-Degrees-Radians - Will quickly convert Radians to degrees or degrees to radians.  Useful when dealing with the
unit cirlce or special triangles. (Or just getting a quick answer on your homework early in the semester)

HISTORY

The functions in this program were initially scripts I wrote to automate some things while doing precalculus homework.  
That's what programming is about, leaving the tedium up to your computer.  Anyway, I eventually wrote a program that
imported the main functions I used.  With some tweaking, I made it into a self sustaining program that ran until I told
it to stop (unlike before, when the scripts would terminate after their functions ran).

As I see it, there are two main problems with this program as it is now.  First--and most glaring-- of which, is the fact
that the command line is a weird place to have this program.  It would work so much better with a GUI.  I will rewrite
this program using HTML, CSS, and JavaScript so that navigating the features is easier.  Although I'm sure a similar and
better program already exists on the web. The second problem is, it's terribly inefficient.  I know Python has extensive
libraries for doing advanced calculations, but I am not familiar with them.  Also, some parts of the code are spaghetti-ish.
For this reason, I invite anyone to make changes to this program to make it more usable and more efficient.

INSTALL AND USE

There are 4 -.py files you need to download:
factor.py - contains the factor function
trigfunctions.py - contains the algorithms for calculating the 6 trigonmetric function ***NEEDS THE MOST REWRITING***
raddegree.py - contains function for converting radians to degrees and vice versa.
precalhelp.py - the "user interface" if you will.  Contains the prompts and function calls to make it into one program.

Download these four files and keep them in the same folder.  Run the script in its entirety with a shell prompt by typing
"python precalhelp.py" and pressing enter or "./precalhelp.py" and pressing enter.  If you're running it from a DOS prompt,
just type "precalhelp.py" and press enter.  If you want to run it in the Python shell, just type "import precalhelp" and 
press enter.  Or import one of the other files if you just want to use one specific function.  Really, this whole thing is
designed to save you a few minutes on tedious homework problems.  You can figure it out.  I believe in you.
