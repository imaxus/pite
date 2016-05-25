class Pascal_Triangle:
	def __init__(self,rows):
		self.row=[1.0]
		self.n=0
		self.rows = rows

	def __iter__(self):
		return self

	def __next__(self):
		line = [1.0]
		for k in range(self.n):
			line.append(line[k] * (self.n-k) / (k+1))
		self.n+=1
		if self.n>self.rows:
			raise StopIteration
		return line
p = Pascal_Triangle(5)
print(next(p))
