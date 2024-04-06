# Random  Questions FOr exams/quizzes
import random

qset =[]
line = "------------------------------------------------"
numb_questions= int(input("What is the total exam number of questions : "))

# Defining the random question selector function
def qselector(list):
	index = random.randint(0,len(list)-1)
	selected = list.pop(index)
	return selected

 # Population question list 
for  q in range(numb_questions):
	print()
	print("Please add question  : ")
	question = input()
	qset.append(question)

# Reading the question list	
#print(line)
#print("QUESTION SET")
#print(line)
#for question in qset:
#	print(ques
questions = int(input('How many questions do you need : '))
print(line)
print("QUESTIONS")
print(line)
# Questions printer
for i in range(questions):
	print(f"{i+1}.{qselector(qset)}")
