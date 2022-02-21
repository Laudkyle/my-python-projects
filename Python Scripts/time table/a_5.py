hall0 ={
	"name": "LECTURE HALL 1",
	"capacity": 50,
	"period 1": "Empty",
	"period 2": "Empty",
	"period 3": "Empty",
}
hall1 ={
	"name": "LECTURE HALL 2",
	"capacity": 50,
	"period 1": "Empty",
	"period 2": "Empty",
	"period 3": "Empty",
}
hall2 ={
	"name": "LECTURE HALL 3",
	"capacity": 60,
	"period 1": "Empty",
	"period 2": "Empty",
	"period 3": "Empty",
}
hall3 ={
	"name": "LECTURE HALL 4",
	"capacity": 50,
	"period 1": "Empty",
	"period 2": "Empty",
	"period 3": "Empty",
}
hall4 ={
	"name": "LECTURE HALL 5",
	"capacity": 70,
	"period 1": "Empty",
	"period 2": "Empty",
	"period 3": "Empty",
}

cap_1 = int(input("Please enter the capacity of the class : "))

halls =[hall0, hall1, hall2, hall3, hall4]


# HALL ASSIGNMENT FUNCTION 1
def hall_Assignment_1(hall, cap_1):
	for hall in halls:
		
# Checking period 1
		if hall["period 1"]=="Empty"and hall["capacity"] >= cap_1:
			hall["period 1"]="Occupied"
# Checking period 2
		elif hall["period 2"]=="Empty"and hall["capacity"] >= cap_1:
			hall["period 2"]="Occupied"
# Checking period 3
		elif hall["period 3"]=="Empty"and hall["capacity"] >= cap_1:
			hall["period 3"]="Occupied"
		for key, value in hall.items():
			print(f'{key.upper()} : {value}')

cap_2 = int(input("Please enter the capacity of the second class : "))	

				
# HALL ASSIGNMENT FUNCTION 2
def hall_Assignment_2(hall, cap_2):
	for hall in halls:
# Checking period 1
		if hall["period 1"]=="Empty"and hall["capacity"] >= cap_2:
			hall["period 1"]="Occupied"
# Checking period 2
		elif hall["period 2"]=="Empty"and hall["capacity"] >= cap_2:
			hall["period 2"]="Occupied"
# Checking period 3
		elif hall["period 3"]=="Empty"and hall["capacity"] >= cap_2:
			hall["period 3"]="Occupied"
		for key, value in hall.items():
			print(f'{key.upper()} : {value}')

# First Hall Assignment
hall_Assignment_1(halls, cap_1)
print()
print("END OF THE FIRST ASSIGNMEMT")
print()

# Second Hall Assignment
print()
hall_Assignment_2(halls, cap_2)
print()
print("END OF THE SECOND ASSIGNMEMT")
		