# Parameters and arguements
def greet(name, age = -1):
	print(f"Hello {name}, how are you?")
	if age >= 0:
		print(f"I know your age is {age}")
	
greet("Joe",12)
greet("Kyle")