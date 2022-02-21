import random
from typing import List

# Obtaining credit hour and subject list
sub_list = []
sumCredits = 0
line ="---------------------------------------------------------------"
print("Acquiring the subject list")
print(line)
credit_hours = int(input("Please enter the total credit hours : "))


# Defining the course selector function

def course_selector(course):
    index = random.randint(0, len(course) - 1)
    removed = course.pop(index)
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
    def __init__(self, name, capacity, period_1, period_2, period_3, period_4, period_5, period_6, period_7, period_8, period_9):
        self.name = name
        self.capacity = capacity
        self.period_1 = period_1
        self.period_2 = period_2
        self.period_3 = period_3
        self.period_4 = period_4
        self.period_5 = period_5
        self.period_6 = period_6
        self.period_7 = period_7
        self.period_8 = period_8
        self.period_9 = period_9


    def __str__(self) -> str:
        return f"Name : {self.name}\nCapacity : {self.capacity}\nPeriod 1 : {self.period_1}\nPeriod 2 : {self.period_2}\nPeriod 3 : {self.period_3}\nPeriod 4 : {self.period_4}\nPeriod 5 : {self.period_5}\nPeriod 6 : {self.period_6}\nPeriod 7 : {self.period_7}\nPeriod 8 : {self.period_8}\nPeriod 9 : {self.period_9}"


rng_0 = int(input("How many lecture halls are present : "))
rng_1 = rng_0 + 1


# Hall printing
def print_hall(obj):
    print(
        f"Name : {obj.name}\nCapacity : {obj.capacity}\nPeriod 1 : {obj.period_1}\nPeriod 2 : {obj.period_2}\nPeriod 3 : {obj.period_3}\nPeriod 4 : {obj.period_4}\nPeriod 5 : {obj.period_5}\nPeriod 6 : {obj.period_6}\nPeriod 7 : {obj.period_7}\nPeriod 8 : {obj.period_8}\nPeriod 9 : {self.period_9}6")


#	Halls printing
def print_halls(list):
    for obj in list:
        print(
            f"Name : {obj.name}\nCapacity : {obj.capacity}\nPeriod 1 : {obj.period_1}\nPeriod 2 : {obj.period_2}\nPeriod 3 : {obj.period_3}\nPeriod 4 : {obj.period_4}\nPeriod 5 : {obj.period_5}\nPeriod 6 : {obj.period_6}\nPeriod 7 : {obj.period_7}\nPeriod 8 : {obj.period_8}\nPeriod 9 : {obj.period_9}6")


# Creating halls
halls = []
hallCap_1 = int(input("Please enter the Capacity of the first set of Lecture halls : "))
for hall in range(1, rng_1):
    hall_name = f"LT_{hall}"
    h_n = f"LT{hall}"
    h_n = Hall(hall_name, hallCap_1, "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty")
    halls.append(h_n)
print("HERE ARE THE  LECTURE HALLS PRESENT")
print_halls(halls)
print()


# Hall printing
def print_hall(obj):
    print(
        f"Name : {obj.name}\nCapacity : {obj.capacity}\nPeriod 1 : {obj.period_1}\nPeriod 2 : {obj.period_2}\nPeriod 3 : {obj.period_3}\nPeriod 4 : {obj.period_4}\nPeriod 5 : {obj.period_5}\nPeriod 6 : {obj.period_6}\nPeriod 7 : {obj.period_7}\nPeriod 8 : {obj.period_8}\nPeriod 9 : {obj.period_9}6")


#	Halls printing
def print_halls(list):
    for obj in list:
        print(
            f"Name : {obj.name}\nCapacity : {obj.capacity}\nPeriod 1 : {obj.period_1}\nPeriod 2 : {obj.period_2}\nPeriod 3 : {obj.period_3}\nPeriod 4 : {obj.period_4}\nPeriod 5 : {obj.period_5}\nPeriod 6 : {obj.period_6}\nPeriod 7 : {obj.period_7}\nPeriod 8 : {obj.period_8}\nPeriod 9 : {obj.period_9}6")


# Hall Searching
def hall_searcher(lname, fname):
    for obj in lname:
        if fname == obj.name:
            print_hall(obj)
        else:
            continue


# Defining the subject distribution function

def hallAssignment(hall, cap):
    for hall in halls:
        hall_searcher(halls, hall)
        while hall.period_1 == "Empty" or hall.period_2 == "Empty" or hall.period_3 == "Empty" or hall.period_4 == "Empty" or hall.period_5 == "Empty" or hall.period_6 == "Empty" or hall.period_7 == "Empty" or hall.period_8 == "Empty" or hall.period_9 == "Empty":
            for hall in halls:
                hall_searcher(halls, hall)

                # Checking period 1
                if hall.period_1 == "Empty" and hall.capacity >= cap and len(sub_list) >= 1:
                    hall.period_1 = course_selector(sub_list)

                # Checking period 2
                elif hall.period_2 == "Empty" and hall.capacity >= cap and len(sub_list) >= 1:
                    hall.period_2 = course_selector(sub_list)

                # Checking period 3
                elif hall.period_3 == "Empty" and hall.capacity >= cap and len(sub_list) >= 1:
                    hall.period_3 = course_selector(sub_list)

                # Checking period 4
                elif hall.period_4 == "Empty" and hall.capacity >= cap and len(sub_list) >= 1:
                    hall.period_4 = course_selector(sub_list)

                # Checking period 5
                elif hall.period_5 == "Empty" and hall.capacity >= cap and len(sub_list) >= 1:
                    hall.period_5 = course_selector(sub_list)

                # Checking period 6
                elif hall.period_6 == "Empty" and hall.capacity >= cap and len(sub_list) >= 1:
                    hall.period_6 = course_selector(sub_list)

                # Checking period 7
                elif hall.period_7 == "Empty" and hall.capacity >= cap and len(sub_list) >= 1:
                    hall.period_7 = course_selector(sub_list)

                # Checking period 8
                elif hall.period_8 == "Empty" and hall.capacity >= cap and len(sub_list) >= 1:
                    hall.period_8 = course_selector(sub_list)

                # Checking period 9
                elif hall.period_9 == "Empty" and hall.capacity >= cap and len(sub_list) >= 1:
                    hall.period_9 = course_selector(sub_list)
                elif len(sub_list) == 0:
                    break
            break

    print_halls(halls)
    print(f"Courses remaining : {sub_list}")


print("------------------------------------------------")
hallAssignment(halls, 40)
closure = input("Please press Y to close : ")
