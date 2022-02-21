# Defining hall class
class Hall:
	def __init__(self, name, capacity, period_1, period_2, period_3):
		self.name= name
		self.capacity = capacity
		self.period_1 = period_1
		self.period_2 = period_2
		self.period_3 = period_3
	
	def __str__(self) -> str:
		return f"Name : {self.name}\nCapacity : {self.capacity}\nPeriod 1 : {self.period_1}\nPeriod 2 : {self.period_2}\nPeriod 3 : {self.period_3}"
		
# Range of lecture halls

rng_0= int(input("How many lecture halls are present : "))
rng_1 = rng_0 +1

# Creating halls

halls=[]
for hall in range(1,rng_1):
	hn= f"LT_{hall}"
	h_n=f"LT{hall}"
	h_n= Hall(hn, 80, "Empty", "Empty", "Empty")
	halls.append(h_n)
	print(hn)
print("HERE ARE THE  LECTURE HALLS PRESENT")

def printb(obj):
	return print(f"Name : {obj.name}\nCapacity : {obj.capacity}\nPeriod 1 : {obj.period_1}\nPeriod 2 : {obj.period_2}\nPeriod 3 : {obj.period_3}")
	
printb(halls[0])
#halls[0].period_1="Occupied"
#printb(halls[0])