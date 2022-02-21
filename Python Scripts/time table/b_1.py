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
	hallname = f"LT{hall}"
	LT= Hall(hallname, 80, "Empty", "Empty", "Empty")
	halls.append(hallname)
	print(LT)
print("HERE ARE THE  LECTURE HALLS PRESENT")
print(halls) 
