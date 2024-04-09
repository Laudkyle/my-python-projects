hall0 ={
	"name": input("Please enter  the name of the first hall : "),
	"Capacity": int(input("Please enter the lecture hall capacity : ")),
	"state": "Empty"
}
hall1 ={
	"name": input("Please enter  the name of the second hall : " ),
	"Capacity": int(input("Please enter the lecture  hall capacity : ")),
	"state": "Empty"
}
hall2 ={
	"name": input("Please enter  the name of the third hall : " ),
	"Capacity": int(input("Please enter the lecture  hall capacity : ")),
	"state": "Empty"
}
hall3 ={
	"name": input("Please enter  the name of the forth hall : " ),
	"Capacity": int(input("Please enter the lecture  hall capacity : ")),
	"state": "Empty"
}
hall4 ={
	"name": input("Please enter  the name of the Fifth hall : " ),
	"Capacity": int(input("Please enter the lecture  hall capacity : ")),
	"state": "Empty"
}
cap = int(input("Please enter the capacity of thenp"))
halls =[hall0, hall1, hall2, hall3, hall4]
# Hall Assignment
def hall_assignment(hall, cap):
	for hall in halls:
		if hall["state"] == "Empty" and hall["Capacity"] <= cap:
			hall["state"] = "Occupied"
			print(f"{hall['name']} is ", hall["state"])
		else:
			hall["state"] = "Empty"
			print(f"{hall['name']} is ", hall["state"])
   
# Calling the 
hall_assignment(halls, cap)