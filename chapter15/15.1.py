"Write a function called distance_between_points that takes two Points as arguments and returns the distance between them."
import math
class points:
	x=0
	y=0

def distance(p1,p2):
	dx=p2.x-p1.x
	dy=p2.y-p1.y
	distance=math.sqrt(dx**2-dy**2)
	return(distance)

def main():
	p1=points()
	p1.x=0
	p1.y=0
	p2=points()
	p2.x=10
	p2.x=10
	print(distance(p1,p2)) 

if __name__=='__main__':
  main()
