#Exercise 13.1. Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and converts them to lowercase.
from  string import punctuation,whitespace,digits
def word():
	f=open("think_python.txt",'r')
	lines=f.read().split()
#	for line in lines:
#		words = line.split()
	for word in lines:
		word=word.strip(punctuation + whitespace + digits).lower()
		print (word)
word()
