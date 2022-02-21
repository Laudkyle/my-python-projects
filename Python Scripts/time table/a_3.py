hall0 ={
	"name": "LECTURE HALL 1",
	"Capacity": 50,
	"state": "Empty"
}
hall1 ={
	"name": "LECTURE HALL 2",
	"Capacity": 60,
	"state": "Empty"
}
hall2 ={
	"name": "LECTURE HALL 3" ,
	"Capacity": 70,
	"state": "Empty"
}
hall3 ={
	"name": "LECTURE HALL 4",
	"Capacity": 80,
	"state": "Empty"
}
hall4 ={
	"name": "LECTURE HALL 5",
	"Capacity": 99,
	"state": "Empty"
}
cap = int(input("Please enter the capacity of the class : "))
halls =[hall0, hall1, hall2, hall3, hall4]
# Hall Assignment
def hall_assignment(hall, cap):
	for hall in halls:
		if hall["state"] == "Empty" and hall["Capacity"] >= cap:
			hall["state"] = "Occupied"
			print(f"{hall['name']} is ", hall["state"])
		else:
			hall["state"] = "Empty"
			print(f"{hall['name']} is ", hall["state"])
hall_assignment(halls, cap)