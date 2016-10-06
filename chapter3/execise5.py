Exercise 5  
#Write a function that draws a grid like the following:
#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +


def g():
        print "+ ","- "*4,
def i():
        print "|"," "*9,"|"," "*9,"|"
        print "|"," "*9,"|"," "*9,"|"
def a(h):
        h()
        h()
def print_row():
        a(g)
        print "+"
def f():
        print_row()
        a(i)

def print_grid():
        a(f)
        print_row()
print_grid()
