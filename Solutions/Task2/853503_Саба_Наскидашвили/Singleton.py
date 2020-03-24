class Singleton(type):  
	instance = None  

	def __call__(cls, *args, **kwargs):  
		if cls.instance is None:  
			cls.instance = super().__call__(*args, **kwargs)  
		return cls.instance  

class User(metaclass=Singleton):  

	def __init__(self, name):  
		self.name = name  

	def __repr__(self):  
		return f'<User: {self.name}>'

class LapTop(metaclass = Singleton):
	def __init__(self,name):
		self.name = name

	def __repr__(self):  
		return f'<LapTop: {self.name}>'			



u1 = User('Pavel')  
# Начиная с этого момента все пользователи будут Павлами
u2 = User('Stepan',3,5)

print(u1)
print(u2) 

l1 = LapTop('MacBook')
# Начиная с этого момента все Ноутбуки будут Макбуками
l2 = LapTop('Asus', 19.2, 37)

print(l1)
print(l2)         
