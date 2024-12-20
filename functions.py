#CREATING YOUR OWN FUNCTIONS TO REUSE THRU THE PROGRAM
#PRINT INT INPUT STR RANGE

#A FUNTION IS REUSABLE CODE WITH A UNIQUE NAME
"""
 TO CREATE A FUNCTION WE USE 
 
    def benji_moore (parameter1, parameter2):
        code--------------------------------
        code--------------------------------
    benji_moore(parameter1, parameter2)
    
functions must have a unique name
the variables are called parameters

return we cannot read the variable but we can do something with it
local variables can be used within a function,
global variables can be used outside a function
"""
#EXAMPLE 1
'''
def student_info(name,age,gender):
    print("welcome",name)
    print("You are",age)
    print("your are",gender)

number = int(input("Enter score"))
for i in range(number):
    name=input("Enter your name:").capitalize()
    age=int(input("Enter your age:"))
    gender=input("Enter your gender:")
    student_info(name,age,gender)
'''

'''
4 TASKS FOR CREATING AND DEFINING MY OWN FUNCTIONS
'''
#EXAMPLE 2
'''
def grade(score):
    print("Your score is :")
    if score >0 and score <=50:
        print("You suck! Improve your grade")
    
    elif score >50 and score <=70:
        print("Better sit up")
    
    elif score >80 and score <=90:
        print("Good job!")
    else:
        print("You are the best in class!")    
   
#calling the funtion we defined
score=int(input("Enter your score"))
grade(score)    


'''
#Example 3

def flight_charges(price):
    upgrade=input("Would you like to upgrade to (Yes/No)?").strip().lower()
    if upgrade== "Yes":
        price+=99
        





























