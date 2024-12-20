#Loops in pythons 
'''
it is a way ro repeat loops until certain conditions are met
two types of loops

#WHILE LOOPS
works with an expression works like the if statements

the first thing to run is the expression outside of the loop
works like the if statement inside  statements

'''
#EXAMPLE
#A BOT THAT ACCEPTS MESSEGES
'''
message=str(input("enter your message"))
while message=="done":
    print("we got your message!")
'''
#Example 2
'''
passwords = input("Enter your password")
while passwords!="12345" and passwords != "54321":
    passwords= input("WORNG! try again")
print("welcome to  your account")


#EXAMPLE 3
houses = str(input("which house do you want to buy?"))
while houses=="mansion" or houses=="beach house" or houses=="villa" or houses=="getaway":
    houses== input("No try it elsewhere")
    print("We have some options you want to check out")
'''    

#example 4
#counter variables
''' 
counter= 0
while counter < 100:
    name=input("Enter the name")
    print("congrats",name,"you saved 20%")
    counter+=1
print("all done")   
    
counter=0
while counter < 1:
    coupon=input("Enter the coupon")
    if coupon=="3b234":
        print("congrats",coupon,"you saved 10% money on the tickect purchased")
    else:
        print("coupon used")
counter-=1
'''

#example 4
"""
tries=0
code=""

while tries <4 and code != "python":
    code=str(input("Enter the a prgramming language"))
    
    print("it took you",tries)"""

#EXAMPLE 5
#PRINTING A TICKET

"""
trian_ticket =input("Enter 1 to book or 2 to end booking")
i=1
while trian_ticket!="1":
    if trian_ticket == "1":
        print("train ticket:",str(1))
        i+=1
trian_ticket =input("Enter 1 to book or 2 to end booking")

"""   
#FOR LOOP
"""
doing something with each variable in the code
it is normally used to search for somethie
repeat a number of times it uses the  function range()

used in the list and dictionary sections

for element in (sequence)--------------- for every element in my variable run the code
                                            goes thru every letter in the variable used to check if something in the variable
     code                                       the for loop is reaally powerful used for searching for something somethingcode ----------------------
                                                checks the entire code and prints out the results
loop 

the first code ouside the loop will run as=fter the loop ends


username=input("Enter your username")
wrong_username=("!@#$%^&&*")
for letter in username:
    if letter in wrong_username:
        print("Please enter the corrrect Username",letter)
        
        
the range element

for element in range(range(number))
    run code
    
range takes one number can take 2 numbers separate by a comma

"""
#EXAMPLE

"""
passcode=(input("Enter your passcode:"))
error="!@#$%^&*"
for i in passcode:
    if i in error:
        print("Please enter the corect passcode",i)



"""
#Example 2
#the vowel checker
"""
vowel="aeiou"
const ="bqwrtyplkjhgfdszxcvbnnm"

word=str(input("Enter your word:"))
vowel_num = 0
for i in word:
    if i in vowel:
        vowel_num += 1
    elif i in const: 
        vowel_num += 0
print ("there are ",vowel_num,"in the letters")
    

"""
"""
phone=input("Enter your phone number")
valid_phone ="233"

for number in phone:
    if number not in valid_phone:
        print ("Invalid phone number")
        

"""
"""
id_number = input("Enter your id number")
valid_id_number ="0089"
for i in id_number:
    if i not in valid_id_number:
        print("access denied")
    elif i in valid_id_number:
        print("access granted")

not operator was introduced

"""
#the range function
'''
guests=int(input("enter the number of the guest"))
for i in range(guests):
    name=(input("Enter your name:"))
    age=int(input("Enter your age:"))
    if age>=21:
        print("welcome to the party!")
    else:
        print("under age!")
        print("no way!")       


for i in range(5):
    username=input("Enter your username")
    password=input("Enter your password")
    
    if username=="admin" and password=="password":
        print("Welcome admin!")
        
        break
        
    if username!="admin" and password!="password":
        print("you are not the admin!")
'''
'''
year=input("Enter the year")
valid="2000"
for i in year:
    if year not in valid:
        print("try again")
'''
#NEW PROJECTS































