import math

class Vector:
	def __init__(self, x):
		self.x = x


	def createVector(self):
		for i in range(len(self.x)):
			i = int(input())
			self.x.append(i)
		
			
	def getVector(self):
		return self.x

	def compare(self,v1):
		if self.x == v1.x:
			return True
		else: return False	

	def sumOfVectors(self,v1):
		a = 0
		while a < len(self.x):
			i = self.x[a] + v1.x[a]
			v1.x[a] = i	
			a += 1
		return v1

	def subOfVectors(self,v1):
		a = 0
		while a < len(self.x):
			i = self.x[a] - v1.x[a]
			v1.x[a] = i	
			a += 1
		return v1

	def multipy(self, a):

		i = 0
		while i < len(self.x):
			v = (self.x[i] * a)
			self.x[i] = v
			i += 1 	
		

	def innerProduct(self,v1):
		result = 0
		i = 0
		while i < len(self.x):
			result += self.x[i] * v1.x[i]
			i += 1
		return result			

	def countlen(self):
		i = 0
		result = 0
		while i < len(self.x):
			result += (self.x[i]**2) 
			i += 1
		length = math.sqrt(result)	
		return length	

if __name__ == '__main__':
	
	vector1 = Vector([1,2,4])
	vector2 = Vector([0,1,1])
	print(vector1.getVector())
	print(vector2.getVector())
	print(vector1.compare(vector2))
	print(vector1.sumOfVectors(vector2).getVector())
	print(vector1.multipy(3))
	print(vector1.innerProduct(vector2))
	print(vector1.countlen())






	
