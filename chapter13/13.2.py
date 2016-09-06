#go to Project Gutenberg ( http: // gutenberg. org ) and download your favorite out-of-copyright book in plain text format.

#Modify your program from the previous exercise to read the book you downloaded, skip over the header information at the beginning of the file, and process the rest of the words as before.

#Then modify the program to count the total number of words in the book, and the number of times each word is used.

#Print the number of different words used in the book. Compare different books by different authors,written in different eras. Which author uses the most extensive vocabulary? 
from string import digits,punctuation,whitespace
books={'origin.txt','huck.txt','great.txt', 'sherlock.txt'}
def extract(book):

	vocabulary = []
	flag = False
	start_line = "*** START OF"
	for line in book:
		if (flag == False) and (start_line in line):
			flag=True
		elif flag == True:
			for word in line.split():
				word = word.strip(punctuation + whitespace + digits).lower()
				vocabulary.append(word)
		else:
			pass
	return vocabulary
def histogram(word_list):
	hist={}
	for word in word_list:
		hist[word]=hist.get(word,0)+1
    
	return(hist)


def find_book(books):
	words=[]
	dictionary={}#this dict stores book_name as key and unique words as keys
	for book in books:
		book_name=book
		book=open(book,'r')
		words=extract(book)
		book.close()
		print('%s has a total of %d words and %d unique words'%(book_name,len(words),len(histogram(words))))
	
		dictionary[book_name]=dictionary.get(book_name,0)+len(histogram(words))
		l=[key for key,value in sorted(dictionary.items(),reverse=True)]
		print("The author of the book %s has the most extensive vocabulary"%(l[0]))
find_book(books)
