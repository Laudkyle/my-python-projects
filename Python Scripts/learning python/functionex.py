def convertGender(gender = "Unknown"):
	if gender.upper() == "M":
		return "Male"
	elif gender.upper() == "F":
		return "Female"
	else:
		return f"Gender is {gender}"
print(convertGender("M"))
print(convertGender("f"))
print(convertGender("F"))
print(convertGender("m"))
print(convertGender())
	
