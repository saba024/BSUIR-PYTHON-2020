class User:
	def __init__(self,name,age,active,balance,other_names,friends):
		self.name = name
		self.age = age
		self.active = active
		self.balance = balance
		self.other_names = other_names
		self.friends = friends


def converttodict(obj):
	objdict = {
		"__class__": obj.__class__.__name__,
		"__module__": obj.__module__
	}
	objdict.update(obj.__dict__)
	return objdict

newuser = User(
	name = "Saba",
	age = 18,
	friends = ["Jane","John"],
	balance = 345.80,
	other_names = ["Doe","Joe"],
	active = True)
print(converttodict(newuser))
