sub_list =[]
sumCredits = 0
# Calling course populator
credit_hours = int(input("Please enter the total credit hours : "))
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
				sub_list.append(courseCode)
			print(sub_list)
			sumCredits +=  credits
			print(sumCredits)
			
# Calling function
		
while sumCredits < credit_hours:
		course_populator(credit_hours)
