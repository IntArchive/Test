class Time:
	"""Represents the time of day"""
	def __init__(self,a=30):
		self.hour=10
		self.minute=9
		self.second=30
	def print_time(self):
		"""Print time on screen
		:self:
		:return: None
		"""
		print("It's %.2d:%.2d:%.2d"%(self.hour,self.minute,self.second))
		return None
#As an exercise, rewrite time_to_int (from Section 16.4) as a method.
	def time_to_int(self,prin="y"):
		"""As an exercise, rewrite time_to_int (from Section 16.4) as a method."""
		integer=self.hour*3600+self.minute*60+self.second
		if prin=="y":
			print("Time %.2d:%.2d:%.2d is %d"%(self.hour,self.minute,self.second,integer))
		else:
			return integer

a=Time()
#a.time_to_int(prin="n")