#Exercise 3  
#Python provides a built-in function called len that returns the length of a string, so the value of len('allen') is 5.
#Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.
def right_justify(s):

	l=len(s)
	d=70-l
	print (''*d+s)
right_justify("allen")
		

