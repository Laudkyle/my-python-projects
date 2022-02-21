import random
from typing import List

# Obtaining credit hour and subject list
sub_list = []
sumCredits = 0
print("Acquiring the subject list")
credit_hours = int(input("Please enter the total credit hours : "))

# Defining the course selector function

def course_selector(course):
	index = random.randint(0, len(course)-1)
	removed =course.pop(index)
	return removed

# Defining the course populator function
def course_populator(credit_hours):
    global sumCredits
    courseCode = str(input("Please enter course : "))
    credits = int(input("Please enter credit for course : "))
    if (sumCredits + credits) > credit_hours:
        print()
        print("Input exceeds total credit hours")
        print()
    else:
        for course in range(credits):
            sub_list.append(courseCode.upper())
        print()
        print("LIST OF SUBJECTS")
        print(sub_list)
        sumCredits += credits
        print(f"Credit hours accumulated : {sumCredits} / {credit_hours}")
        print()

# Calling the course populator function

while sumCredits < credit_hours:
    course_populator(credit_hours)

# Defining the Hall class
class Hall:
    def __init__(self, name, capacity, period_1, period_2, period_3):
        self.name = name
        self.capacity = capacity
        self.period_1 = period_1
        self.period_2 = period_2
        self.period_3 = period_3

    def __str__(self) -> str:
        return f"Name : {self.name}\nCapacity : {self.capacity}\nPeriod 1 : {self.period_1}\nPeriod 2 : {self.period_2}\nPeriod 3 : {self.period_3}"


rng_0 = int(input("How many lecture halls are present : "))
rng_1 = rng_0 + 1


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

# Hall printing
def print_hall(obj):
    print(
        f"Name : {obj.name}\nCapacity : {obj.capacity}\nPeriod 1 : {obj.period_1}\nPeriod 2 : {obj.period_2}\nPeriod 3 : {obj.period_3}")


#	Halls printing
def print_halls(list):
    for obj in list:
        print(
            f"Name : {obj.name}\nCapacity : {obj.capacity}\nPeriod 1 : {obj.period_1}\nPeriod 2 : {obj.period_2}\nPeriod 3 : {obj.period_3}")
# Hall Searching
def hall_searcher(lname,fname):

	for obj in lname:
		if fname == obj.name:
			print_hall(obj)
		else:
			continue

# Defining the subject distribution function

def hallAssignment_1(hall, cap):
    for hall in halls:
        hall_searcher(halls,hall)
        if hall.period_1 == "Empty" and hall.capacity >= cap  and len(sub_list) >= 1:
            hall.period_1 = course_selector(sub_list)
    print_halls(halls)
print("------------------------------------------------")
hallAssignment_1(halls, 40)