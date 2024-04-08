# Random exam  Questions selector
import random

class quest:
	def __init__(self, question, op1, op2, ans):
		self.question = question
		self.op1 = op1
		self.op2 = op2
		self.ans = ans
	def __str__(self) -> str:
		return f"{self.question}\nA.{self.op1}\nB.{self.op2}"	


qset =[]
qset1 =[]
marks = 0
line = "------------------------------------------------"
numb_questions= int(input("What is the total number of questions : "))

# Defining the random question selector function
def qselector(list):
	index = random.randint(0,len(list)-1)
	selected = list.pop(index)
	return selected

 # Population question list 
for  q in range(numb_questions):
	print()
	print("Please add question  : ")
	question = quest(input("Please write the question "), input("First possible answer : "), input("Second possible answer : "), input("Option for correct answer(A or B) : "))
	qset.append(question)
	
# Questions printer
print(line)
questions = int(input('How many question do you want to set : '))
print(line)
print("QUESTIONS")
print(line)
for i in range(questions):
	q = qselector(qset)
	print(f"{i+1}.{q}")
	qset1.append(q)
	print()
	
# Answer collection
print(line)
print("ANSWERS")
print(line)
for i in range(questions):
	answer = input(f"Please input answer for question {i+1} : ")
	if qset1[i].ans == answer:
		print("CORRECT ANSWER")
		marks += 1
	else:
		print("WRONG ANSWER")
print(f"Your total marks is {marks}")