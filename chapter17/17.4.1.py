
        hour=0
        minute=0
        second=0
        def __init__(self, hour=0, minute=0, second=0):
                self.hour = hour
                self.minute = minute
                self.second = second
#        def print_time(self):
#                print('Hour -> %d \n Minute -> %d \n Second -> %d'%(self.hour,self.minute,self.second))
	def __str__(self):
		  return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
	def __add__(self,other):
		seconds = self.time_to_int() + other.time_to_int()
	def increment(self, seconds):
		seconds += self.time_to_int()
		return int_to_time(seconds)

	def time_to_int(Time):
        	minutes = time.hour * 60 + time.minute
        	seconds = minutes * 60 + time.second
        	return seconds
	def int_to_time(seconds):
        	time = Time()
        	minutes, time.second = divmod(seconds, 60)
        	time.hour, time.minute = divmod(minutes, 60)
        	return time

start = Time(9, 45)
duration = Time(1, 35)
print start + duration


