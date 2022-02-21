hall0 ={
	"name": "LECTURE HALL 1",
	"Capacity": 50,
	"period 1": "Empty",
	"period 2": "Empty",
	"period 3": "Empty",
}
hall1 ={
	"name": "LECTURE HALL 2",
	"Capacity": 50,
	"period 1": "Empty",
	"period 2": "Empty",
	"period 3": "Empty",
}
hall2 ={
	"name": "LECTURE HALL 3",
	"Capacity": 60,
	"period 1": "Empty",
	"period 2": "Empty",
	"period 3": "Empty",
}
hall3 ={
	"name": "LECTURE HALL 4",
	"Capacity": 50,
	"period 1": "Empty",
	"period 2": "Empty",
	"period 3": "Empty",
}
hall4 ={
	"name": "LECTURE HALL 5",
	"Capacity": 70,
	"period 1": "Empty",
	"period 2": "Empty",
	"period 3": "Empty",
}

cap = int(input("Please enter the capacity of the class : "))
halls =[hall0, hall1, hall2, hall3, hall4]
# Hall Assignment
def hall_Assignment(hall, cap):
	for hall in halls:
# Checking period 1
		if hall["period 1"]=="Empty"and hall["Capacity"] >= cap:
			hall["period 1"]="Occupied"
# Checking period 2
		elif hall["period 2"]=="Empty"and hall["Capacity"] >= cap:
			hall["period 2"]="Occupied"
# Checking period 3
		elif hall["period 3"]=="Empty"and hall["Capacity"] >= cap:
			hall["period 3"]="Occupied"
		for key, value in hall.items():
			print(f'{key.upper()} : {value}')

hall_Assignment(halls, cap)
		