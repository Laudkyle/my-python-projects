import random 

sub_list= ["Mat101", "Phy101", "Ilt101","Mat101", "Phy101", "Ilt101", "Mat101", "Phy101", "Ilt101", "Mat101", "Phy101", "Ilt101","Mat101", "Phy101", "Ilt101", "Mat101", "Phy101", "Ilt101"]

hall0 ={
	"name": "LECTURE HALL 1",
	"capacity": 50,
	"period_1 ": "Empty",
	"period_2 ": "Empty",
	"period_3": "Empty",
}
hall1 ={
	"name": "LECTURE HALL 2",
	"capacity": 80,
	"period_1 ": "Empty",
	"period_2 ": "Empty",
	"period_3": "Empty",
}
hall2 ={
	"name": "LECTURE HALL 3",
	"capacity": 60,
	"period_1 ": "Empty",
	"period_2 ": "Empty",
	"period_3": "Empty",
}
hall3 ={
	"name": "LECTURE HALL 4",
	"capacity": 50,
	"period_1 ": "Empty",
	"period_2 ": "Empty",
	"period_3": "Empty",
}
hall4 ={
	"name": "LECTURE HALL 5",
	"capacity": 70,
	"period_1 ": "Empty",
	"period_2 ": "Empty",
	"period_3": "Empty",
}

cap_1 = int(input("Please enter the capacity of the class : "))

halls =[hall0, hall1, hall2, hall3, hall4]
def course_selector(course):
	index = random.randint(1, len(course)-1)
	removed =course.pop(index)
	return removed

# HALL ASSIGNMENT FUNCTION 1
def hall_Assignment_1(hall, cap_1):
	for hall in halls:
		
# Checking period_1 
		if hall["period_1 "]=="Empty"and hall["capacity"] >= cap_1:
			hall["period_1 "]= course_selector(sub_list)
			
# Checking period_2 
		elif hall["period_2 "]=="Empty"and hall["capacity"] >= cap_1:
			hall["period_2 "]=course_selector(sub_list)
			
# Checking period_3
		elif hall["period_3"]=="Empty"and hall["capacity"] >= cap_1:
			hall["period_3"]=course_selector(sub_list)
			
		for key, value in hall.items():
			print(f'{key.upper()} : {value}\n')
			

cap_2 = int(input("Please enter the capacity of the second class : "))	
print()

# HALL ASSIGNMENT FUNCTION 2
def hall_Assignment_2(hall, cap_2):
	for hall in halls:
		
# Checking period_1 
		if hall["period_1 "]=="Empty"and hall["capacity"] >= cap_1:
			hall["period_1 "]= course_selector(sub_list)
			
# Checking period_2 
		elif hall["period_2 "]=="Empty"and hall["capacity"] >= cap_1:
			hall["period_2 "]=course_selector(sub_list)
			
# Checking period_3
		elif hall["period_3"]=="Empty"and hall["capacity"] >= cap_1:
			hall["period_3"]=course_selector(sub_list)
			
		for key, value in hall.items():
			print(f'{key.upper()} : {value}\n')


# First Hall Assignment
print("-----------------------------------------------")
hall_Assignment_1(halls, cap_1)
print("-----------------------------------------------")
print("END OF THE FIRST ASSIGNMEMT")
print()

# Second Hall Assignment
print("-----------------------------------------------")
hall_Assignment_2(halls, cap_2)
print()
print("-----------------------------------------------")
print("END OF THE SECOND ASSIGNMEMT")
print("-----------------------------------------------")		