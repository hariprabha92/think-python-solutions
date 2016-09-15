
class Time:
	hour=0
	minute=0
	second=0
def time_to_int(time):
	minutes = time.hour * 60 + time.minute
	seconds = minutes * 60 + time.second
	return seconds
def int_to_time(seconds):
	time = Time()
	minutes, time.second = divmod(seconds, 60)
	time.hour, time.minute = divmod(minutes, 60)
	return time
def add_time(time,seconds):
	initial_time=time_to_int(time)
	total_seconds=initial_time + seconds
	time=int_to_time(total_seconds)
	return(time)

def main():
	time=Time()
	time.hour=2
	time.minute=45
	time.second=46
	seconds=6
	newtime=Time()
	newtime=add_time(time,seconds)  
	print('new te -> %d:%d:%d'%(newtime.hour,newtime.minute,newtime.second))

if __name__=='__main__':
  main()           
