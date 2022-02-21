#We are attempting to take inputs for the scores of students and manipulate it to get their grades and cummulative grade points
import math

print('_____________________________________UNIVERSITY OF CAPE COAST________________________________________')
print('                                                        motto:  veritas nobis lumen                      ')
print('                                                                     est_1962                                       ')      
print('_'*106)
print("Hello, you are welcome to University of Cape Coast, the platform of higher learning.")
print("We will ask you some few questions to get you signed in.")
print('')

#Student details
name=input('Enter your name: ')
age=input('How old are you?')
sch=input('Which University do you attend?')
level=input('Enter your level:')
pro=input('Which program do you read?')
print('_'*106)
user=eval(input('Please enter your password:'))
for conf in range(1):
        conf=eval(input('Confirm your password:'))
if user==conf:
          print('Login successful')
else:
          print('Wrong password')
print ('All is set and done')
print('Thank you for your coperation')
print('_'*106)
print('                                                          Here are your details')
print('Your name is ', name)
print('You are ', age ,'years of age')
print('You attend ', sch ,'and currently you are in level ', level ,'reading ', pro)

#Grade interpretations
grade1='A (first class)'
grade2='B+ (second class upper) '
grade3='B (second class lower)'
grade4='C+ (third class upper)'
grade5='C (third class)'
grade6='D+ (fair)'
grade7='D (pass)'
grade8='E (fail)'
#Taking inputs for results obtained in MAT101
print('_'*106)
print('                                                      Academic Records for End of Semester')
cr_hr1=3
cs1='MAT 101'
cs1a='assessment'
cs1b='exams score'
sm101a=eval(input('What is your score in MAT101 for your assessment?'))
sm101b=eval(input('What is your score in MAT101 for your exams out of 100?'))
mat101_ass=sm101a
mat101_exams=sm101b*(6/10)
tscore_mat101=mat101_ass+mat101_exams
#Conditions for obtaining a grade 
if tscore_mat101>=80:
    print('With ',sm101a, 'marks out of 40 for your assessment and',sm101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade1,'with a total marks of',tscore_mat101,'in ',cs1)
if tscore_mat101>=75 and tscore_mat101<80:
    print('With ',sm101a, 'marks out of 40 for your assessment and',sm101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade2,'with a total marks of',tscore_mat101,'in ',cs1)
if tscore_mat101>=70 and tscore_mat101<75:
    print('With ',sm101a, 'marks out of 40 for your assessment and',sm101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade3,'with a total marks of',tscore_mat101,'in ',cs1)
if tscore_mat101>=65 and tscore_mat101<70:
    print('With ',sm101a, 'marks out of 40 for your assessment and',sm101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade4,'with a total marks of',tscore_mat101,'in ',cs1)
if tscore_mat101>=60 and tscore_mat101<65:
    print('With ',sm101a, 'marks out of 40 for your assessment and',sm101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade5,'with a total marks of',tscore_mat101,'in ',cs1)
if tscore_mat101>=55 and tscore_mat101<60:
    print('With ',sm101a, 'marks out of 40 for your assessment and',sm101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade6,'with a total marks of',tscore_mat101,'in ',cs1)
if tscore_mat101>=50 and tscore_mat101<55:
    print('With ',sm101a, 'marks out of 40 for your assessment and',sm101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade7,'with a total marks of',tscore_mat101,'in ',cs1)
if tscore_mat101>=0 and tscore_mat101<50:
        print('With ',sm101a, 'marks for your assessment and',sm101b, 'marks for your exams score, ', end='')
        print('you had a grade ',grade8,'with a total marks of',tscore_mat101,'in ',cs1)
#Taking inputs for Phy101
cr_hr2=2
cs2='PHY 101'
cs2a='assessment'
cs2b='exams score'
sp101a=eval(input('What is your score in PHY101 for your assessment?'))
sp101b=eval(input('What is your score in PHY101 for your exams out of 100?'))
#Assigning inputs for assessment and exams score
phy101_ass=sp101a
phy101_exams=sp101b*(6/10)
tscore_phy101=phy101_ass+phy101_exams
#conditions for obtaining a particular grade
if tscore_phy101>=80:
    print('With ',sp101a, 'marks out of 40 for your assessment and',sp101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade1,'with a total marks of',tscore_phy101,'in ',cs2)
if tscore_phy101>=75 and tscore_phy101<80:
    print('With ',sp101a, 'marks out of 40 for your assessment and',sp101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade2,'with a total marks of',tscore_phy101,'in ',cs2)
if tscore_phy101>=70 and tscore_phy101<75:
    print('With ',sp101a, 'marks out of 40 for your assessment and',sp101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade3,'with a total marks of',tscore_phy101,'in ',cs2)
if tscore_phy101>=65 and tscore_phy101<70:
    print('With ',sp101a, 'marks out of 40 for your assessment and',sp101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade4,'with a total marks of',tscore_phy101,'in ',cs2)
if tscore_phy101>=60 and tscore_phy101<65:
    print('With ',sp101a, 'marks out of 40 for your assessment and',sp101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade5,'with a total marks of',tscore_phy101,'in ',cs2)
if tscore_phy101>=55 and tscore_phy101<60:
    print('With ',sp101a, 'marks out of 40 for your assessment and',sp101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade6,'with a total marks of',tscore_phy101,'in ',cs2)
if tscore_phy101>=50 and tscore_phy101<55:
    print('With ',sp101a, 'marks out of 40 for your assessment and',sp101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade7,'with a total marks of',tscore_phy101,'in ',cs2)
if tscore_phy101>=0 and tscore_phy101<50:
        print('With ',sp101a, 'marks for your assessment and',sp101b, 'marks for your exams score, ', end='')
        print('you had a grade ',grade8,'with a total marks of',tscore_phy101,'in ',cs2)
#Taking inputs for PHY 103
cr_hr8=1
cs8='PHY 103'
cs8a='assessment'
cs8b='exams score'
sp103a=eval(input('What is your score in PHY 103 for your assessment?'))
sp103b=eval(input('What is your score in PHY 103 for your exams out of 100?'))
#Assigning inputs for assessment and exams score
phy103_ass=sp103a
phy103_exams=sp103b*(6/10)
tscore_phy103=phy103_ass+phy103_exams
tscore_csc107=tscore_phy103
sc107a=sp103a
sc107b=sp103b
cs4=cs8
#conditions for obtaining a particular grade
if tscore_csc107>=80:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade1,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=75 and tscore_csc107<80:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade2,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=70 and tscore_csc107<75:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade3,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=65 and tscore_csc107<70:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade4,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=60 and tscore_csc107<65:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade5,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=55 and tscore_csc107<60:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade6,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=50 and tscore_csc107<55:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade7,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=0 and tscore_csc107<50:
        print('With ',sc107a, 'marks for your assessment and',sc107b, 'marks for your exams score, ', end='')
        print('you had a grade ',grade8,'with a total marks of',tscore_csc107,'in ',cs4)
#Taking inputs for CSC 101
cr_hr3=3
cs3='CSC 101'
cs3a='assessment'
cs3b='exams score'
sc101a=eval(input('What is your score in CSC 101 for your assessment?'))
sc101b=eval(input('What is your score in CSC 101 for your exams out of 100?'))
#Assigning inputs for assessment and exams score
csc101_ass=sc101a
csc101_exams=sc101b*(6/10)
tscore_csc101=csc101_ass+csc101_exams
#conditions for obtaining a particular grade
if tscore_csc101>=80:
    print('With ',sc101a, 'marks out of 40 for your assessment and',sc101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade1,'with a total marks of',tscore_csc101,'in ',cs3)
if tscore_csc101>=75 and tscore_csc101<80:
    print('With ',sc101a, 'marks out of 40 for your assessment and',sc101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade2,'with a total marks of',tscore_csc101,'in ',cs3)
if tscore_csc101>=70 and tscore_csc101<75:
    print('With ',sc101a, 'marks out of 40 for your assessment and',sc101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade3,'with a total marks of',tscore_csc101,'in ',cs3)
if tscore_csc101>=65 and tscore_csc101<70:
    print('With ',sc101a, 'marks out of 40 for your assessment and',sc101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade4,'with a total marks of',tscore_csc101,'in ',cs3)
if tscore_csc101>=60 and tscore_csc101<65:
    print('With ',sc101a, 'marks out of 40 for your assessment and',sc101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade5,'with a total marks of',tscore_csc101,'in ',cs3)
if tscore_csc101>=55 and tscore_csc101<60:
    print('With ',sc101a, 'marks out of 40 for your assessment and',sc101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade6,'with a total marks of',tscore_csc101,'in ',cs3)
if tscore_csc101>=50 and tscore_csc101<55:
    print('With ',sc101a, 'marks out of 40 for your assessment and',sc101b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade7,'with a total marks of',tscore_csc101,'in ',cs3)
if tscore_csc101>=0 and tscore_csc101<50:
        print('With ',sc101a, 'marks for your assessment and',sc101b, 'marks for your exams score, ', end='')
        print('you had a grade ',grade8,'with a total marks of',tscore_csc101,'in ',cs3)
#Taking inputs for CSC 107
cr_hr4=3
cs4='CSC 107'
cs4a='assessment'
cs4b='exams score'
sc107a=eval(input('What is your score in CSC 107 for your assessment?'))
sc107b=eval(input('What is your score in CSC 107 for your exams out of 100?'))
#Assigning inputs for assessment and exams score
csc107_ass=sc107a
csc107_exams=sc107b*(6/10)
tscore_csc107=csc107_ass+csc107_exams
#conditions for obtaining a particular grade
if tscore_csc107>=80:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade1,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=75 and tscore_csc107<80:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade2,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=70 and tscore_csc107<75:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade3,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=65 and tscore_csc107<70:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade4,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=60 and tscore_csc107<65:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade5,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=55 and tscore_csc107<60:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade6,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=50 and tscore_csc107<55:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade7,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=0 and tscore_csc107<50:
        print('With ',sc107a, 'marks for your assessment and',sc107b, 'marks for your exams score, ', end='')
        print('you had a grade ',grade8,'with a total marks of',tscore_csc107,'in ',cs4)
#Taking inputs for LSB 102
cr_hr5=3
cs5='LSB 102'
cs5a='assessment'
cs5b='exams score'
sl102a=eval(input('What is your score in LSB 102 for your assessment?'))
sl102b=eval(input('What is your score in LSB 102 for your exams out of 100?'))
#Assigning inputs for assessment and exams score
lsb102_ass=sl102a
lsb102_exams=sl102b*(6/10)
tscore_lsb102=lsb102_ass+lsb102_exams
tscore_csc107=tscore_lsb102
sc107a=sl102a
sc107b=sl102b
cs4=cs5
#conditions for obtaining a particular grade
if tscore_csc107>=80:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade1,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=75 and tscore_csc107<80:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade2,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=70 and tscore_csc107<75:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade3,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=65 and tscore_csc107<70:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade4,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=60 and tscore_csc107<65:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade5,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=55 and tscore_csc107<60:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade6,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=50 and tscore_csc107<55:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade7,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=0 and tscore_csc107<50:
        print('With ',sc107a, 'marks for your assessment and',sc107b, 'marks for your exams score, ', end='')
        print('you had a grade ',grade8,'with a total marks of',tscore_csc107,'in ',cs4)
#Taking inputs for ILT 102
cr_hr6=1
cs6='ILT 102'
cs6a='assessment'
cs6b='exams score'
si102a=eval(input('What is your score in ILT 102 for your assessment?'))
si102b=eval(input('What is your score in ILT 102 for your exams out of 100?'))
#Assigning inputs for assessment and exams score
ilt102_ass=si102a
ilt102_exams=si102b*(6/10)
tscore_ilt102=lsb102_ass+ilt102_exams
tscore_csc107=tscore_ilt102
sc107a=si102a
sc107b=si102b
cs4=cs6
#conditions for obtaining a particular grade
if tscore_csc107>=80:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade1,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=75 and tscore_csc107<80:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade2,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=70 and tscore_csc107<75:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade3,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=65 and tscore_csc107<70:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade4,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=60 and tscore_csc107<65:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade5,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=55 and tscore_csc107<60:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade6,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=50 and tscore_csc107<55:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade7,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=0 and tscore_csc107<50:
        print('With ',sc107a, 'marks for your assessment and',sc107b, 'marks for your exams score, ', end='')
        print('you had a grade ',grade8,'with a total marks of',tscore_csc107,'in ',cs4)
#Taking inputs for CMS107
cr_hr7=3
cs7='CMS 107'
cs7a='assessment'
cs7b='exams score'
scm107a=eval(input('What is your score in CMS 107 for your assessment?'))
scm107b=eval(input('What is your score in CMS 107 for your exams out of 100?'))
#Assigning inputs for assessment and exams score
cms107_ass=scm107a
cms107_exams=scm107b*(6/10)
tscore_cms107=cms107_ass+cms107_exams
tscore_csc107=tscore_cms107
sc107a=scm107a
sc107b=scm107b
cs4=cs7
#conditions for obtaining a particular grade
if tscore_csc107>=80:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade1,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=75 and tscore_csc107<80:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade2,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=70 and tscore_csc107<75:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade3,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=65 and tscore_csc107<70:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade4,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=60 and tscore_csc107<65:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade5,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=55 and tscore_csc107<60:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade6,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=50 and tscore_csc107<55:
    print('With ',sc107a, 'marks out of 40 for your assessment and',sc107b, 'marks out of 100 for your exams score, ', end='')
    print('you had a grade ',grade7,'with a total marks of',tscore_csc107,'in ',cs4)
if tscore_csc107>=0 and tscore_csc107<50:
        print('With ',sc107a, 'marks for your assessment and',sc107b, 'marks for your exams score, ', end='')
        print('you had a grade ',grade8,'with a total marks of',tscore_csc107,'in ',cs4)
print('__________________________________________________________________________________________')
print ('End of the Data Collection')
print('__________________________________________________________________________________________')
print ('Details')
print('__________________________________________________________________________________________')
#summary
#Summing up the total marks obtained for the various courses multiplied by their credit hours
t_marks=(tscore_mat101*cr_hr1)+(tscore_phy101*cr_hr2)+(tscore_csc101*cr_hr3)+(tscore_phy103*cr_hr8)+(tscore_cms107*cr_hr7)+(tscore_ilt102*cr_hr6)+(tscore_lsb102*cr_hr5)+(tscore_csc107*cr_hr4)
#Summing up the credit hours for the various courses
tcre_hrs=cr_hr1+cr_hr2+cr_hr3+cr_hr4+cr_hr5+cr_hr6+cr_hr7+cr_hr8
#Finding the average obtained by dividing the total marks by total credit hours
t_av=t_marks//tcre_hrs
print('Total marks for ',cs1, ',',cs2, ', ',cs3, ', ',cs4,', ',cs5,', ',cs6,', ',cs7,', and ', cs8, 'is ',t_marks)
print('__________________________________________________________________________________________')
print('Your average mark is ',t_av)
print('__________________________________________________________________________________________')
#Assinging t_marks to sc101a to prevent typing the whole thing again
sc101a=t_marks
#Assinging t_av to sc101b to prevent typing the whole thing again
sc101b=t_av
#Conditions for obtaining a grade and a class
if t_av>=80:
    print('With ',sc101a, 'marks out of 1900 for the  courses you read with reference to the credit hours and an average of ',sc101b, 'marks out of 100, ', end='')
    print('you had a grade ',grade1,)
    print('____________________________________________________________________________________________________________________')
    print('CONGRATULATIONS!!! Mr. ',name, ', you stand the chance of winning the Best Student Award for the 2020/2021 academic year')
    print('____________________________________________________________________________________________________________________')
    print(sch,' is proud of you')
if t_av>=75 and t_av<80:
     print('With ',sc101a, 'marks out of 1900  for the  courses you read with reference to the credit hours and an average of ',sc101b, 'marks out of 100, ', end='')
     print('you had a grade ',grade2,)
if t_av>=70 and t_av<75:
     print('With ',sc101a, 'marks out of 1900 for the  courses you read with reference to the credit hours and an average of ',sc101b, 'marks out of 100, ', end='')
     print('you had a grade ',grade3,)
if t_av>=65 and t_av<70:
     print('With ',sc101a, 'marks out of 1900 for the  courses you read with reference to the credit hours and an average of ',sc101b, 'marks out of 100, ', end='')
     print('you had a grade ',grade4,)
if t_av>=60 and t_av<65:
     print('With ',sc101a, 'marks out of 1900 for the  courses you read with reference to the credit hours and an average of ',sc101b, 'marks out of 100, ', end='')
     print('you had a grade ',grade5,)
if t_av>=55 and t_av<60:
     print('With ',sc101a, 'marks out of 1900 for the  courses you read with reference to the credit hours and an average of ',sc101b, 'marks out of 100, ', end='')
     print('you had a grade ',grade6,)
if t_av>=50 and t_av<55:
    print('With ',sc101a, 'marks out of 1900 for the  courses you read with reference to the credit hours and an average of ',sc101b, 'marks out of 100, ', end='')
    print('you had a grade ',grade7,)
if t_av>=0 and t_av<50:
    print('With ',sc101a, 'marks out of 1900 for the  courses you read with reference to the credit hours and an average of ',sc101b, 'marks out of 100, ', end='')
    print('you had a grade ',grade8,)
    print('See your departmental head for the schedules of your resit. Thank you.')
