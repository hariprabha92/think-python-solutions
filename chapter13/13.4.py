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
def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

def find_book(books):
        words1=[]
	words2=[]
        dictionary1={}#this dict stores book_name as key and unique words as keys
	dictionary2={}
       # for book in books:
	book_name='sherlock.txt'

        book=open(book_name,'r')
        words1=extract(book)
        book.close()
	print('%s has a total of %d words and %d unique words'%(book_name,len(words1),len(histogram(words1))))

        dictionary1[book_name]=dictionary1.get(book_name,0)+len(histogram(words1))
               # l=[key for key,value in sorted(dictionary.items(),reverse=True)]
               # print("The author of the book %s has the most extensive vocabulary"%(l[0]))
	book_name='huck.txt'

	book=open(book_name,'r')
	words2=extract(book)
	book.close()
	print('%s has a total of %d words and %d unique words'%(book_name,len(words2),len(histogram(words2))))

	dictionary2[book_name]=dictionary2.get(book_name,0)+len(histogram(words2))
	#diff=subtract(dictionary1,dictionary2)
	diff=subtract(words1,words2)

	print "The words in the book that aren't in the word list are:"
	for word in diff.keys():
    		print word

find_book(books)
                                                                                                                                              
                                                                                                                     

