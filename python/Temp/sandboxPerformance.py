class Starter(object):
	def __init__(self):
		bucket = []
		for i in range(0, 1000000):
			grain = Grain(self, i)
			bucket.append(grain)


	def compute(self, a):
		return a + a


class Grain(object):
	def __init__(self, parent, num):
		#self.compute(num)
		self.text = " "
		parent.compute(num)


	def compute(self, a):
		return a + a


starter = Starter()