import copy
class time:
	hour=0
	minute=0
	second=0

def main():
	t1=time()
	t2=copy.copy(t1)
	t1.hour=4
	t1.minut=23
	t1.second=56
	t2.hour=1
	t2.minut=20
	t2.second=45
	print(t1<t2)

if __name__=='__main__' :
  main()

