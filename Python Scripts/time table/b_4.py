# Defining hall class
from typing import List


class Hall:
	def __init__(self, name, capacity, period_1, period_2, period_3):
		self.name= name
		self.capacity = capacity
		self.period_1 = period_1
		self.period_2 = period_2
		self.period_3 = period_3
	
	def __str__(self) -> str:
		return f"Name : {self.name}\nCapacity : {self.capacity}\nPeriod 1 : {self.period_1}\nPeriod 2 : {self.period_2}\nPeriod 3 : {self.period_3}"

rng_0= int(input("How many lecture halls are present : "))
rng_1 = rng_0 +1

# Hall printing
def print_hall(obj):
	print(
			f"Name : {obj.name}\nCapacity : {obj.capacity}\nPeriod 1 : {obj.period_1}\nPeriod 2 : {obj.period_2}\nPeriod 3 : {obj.period_3}")

#	Halls printing
def print_halls(list):
	for obj in list:
		print(
			f"Name : {obj.name}\nCapacity : {obj.capacity}\nPeriod 1 : {obj.period_1}\nPeriod 2 : {obj.period_2}\nPeriod 3 : {obj.period_3}")
			
# Creating halls
halls=[]
hallCap_1= int(input("Please enter the Capacity of the first set of Lecture halls : "))
for hall in range(1,rng_1):
	hall_name= f"LT_{hall}"
	h_n=f"LT{hall}"
	h_n= Hall(hall_name, hallCap_1, "Empty", "Empty", "Empty")
	halls.append(h_n)
print("HERE ARE THE  LECTURE HALLS PRESENT")
print_halls(halls)
print()
print()

# Hall Searching
l_n =str(input("Name of lecture hall : "))
def hall_searcher(lname,fname):

	for obj in lname:
		if fname == obj.name:
			print_hall(obj)
		else:
			continue
hall_searcher(halls,l_n)