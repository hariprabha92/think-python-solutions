#Exercise 13.3. Modify the program from the previous exercise to print the 20 most frequently-used words in the book.
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
def most_common_words(hist):
        wordlist=[(value,key) for key,value in hist.items()]
        wordlist.sort(reverse=True)
        for freq,word in wordlist[:20]:
                print(word)
        return(wordlist)

def find_book(books):
        words=[]
        dictionary={}#this dict stores book_name as key and unique words as keys
        for book in books:
                book_name=book
                book=open(book,'r')
                words=extract(book)
                book.close()
                print('%s has a total of %d words and %d unique words'%(book_name,len(words),len(histogram(words))))

		print('The most common 20 words are \n')
                most_common_words(histogram(words))
                dictionary[book_name]=dictionary.get(book_name,0)+len(histogram(words))
                l=[key for key,value in sorted(dictionary.items(),reverse=True)]
                print("The author of the book %s has the most extensive vocabulary"%(l[0]))
find_book(books)

