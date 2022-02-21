#ATM
# Defining person class
class person:
	def __init__(self, name, passcode, accountNumber, currentBalance):
		self.name = name
		self.passcode = passcode
		self.accountNumber = int(accountNumber)
		self.currentBalance = float(currentBalance)
# Person details printing
def print_person(name):
		print(f"Name : {name.name}\nAccount Number : {name.accountNumber}\nCurrent Balance : {name.currentBalance}")
		
line = "______________________________________________"
person1= person("Joe",9876,884988098787,0.00)
print_person(person1)

#Account crediting function
def credit(name):
	name.currentBalance += 99999
	print("Your account has been creditted with GH¢99999")
	print(line)

# Account Debiting function
def debit(name):
	name.currentBalance -=10000
	print("Your account has been debited with GH¢ 10000")
	print(line)

# Calling functions
credit(person1)	
print_person(person1)	
debit(person1)
print_person(person1)