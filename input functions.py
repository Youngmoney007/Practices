""" THE MULTIPLE LINE COMMENTS."""
#print("item cost"
#The discount
#pint((25*4) * 0.8)
#print("funds to send", 200*5 * 6000/8  + 5000)
#print(500%8)
#print("i like food alot")
#print("pay to:", "ama sarfo", "pay this amount:", 25000)


#VARIABLES . They are WORDS that hold a value. Variables have their own name
# it has a lower case ,number and u can use an underscore no special characters. use the assignment operator to name thw variables.
#Python reads  top to bottom.
#must not be too generic and too long and too short
#must be creative
#Can hold diffrent kinds of data
#INT DECIMAL/FLOAT


#ONE

"""
flight_fare=500.6
insurance= 200.16
passport=499.99
baggage=50.50
# 5 ppl are travelling

total = (flight_fare+insurance+passport+baggage) *5
print("totalcost",total)
"""


#TWO

"""
adult=2
children=10

adult_price= 49.99
children_price=29.99

total=(adult*adult_price)+(children*children_price)

print("PAY",total)
print("Have a nice trip!")
"""


#THREE

"""
price=500
days=7

total=(price*days)*0.7

print("special discount", total)

items_cost=500
tax=2
e_levy=6
total=(items_cost-tax-e_levy)

print("Pay",total) 
"""


#Input allows a user to enter data. basically to take date from the users.
""" GATEHRING INFORMAING FOR EVERY LESSON"""



#EXAMPLE ONE
"""
first_Name= input ("Enter your first name")
last_Name= input("Enter Your Last name")
country=input("What is your country?")
city=input("What is your city?")

print(first_Name,last_Name,"is from",city,"in",country)
"""



#EXMAPLE 2
"""
CONVERTING THE DATA TYPES
#THE INPUTS ARE STRINGS. WE HAVE TO CONVERT THEM TO NUMBER OR THE CODE WONT RUN SINCE WE CAN MULTIPLY A STRING AND A STRING
"""

"""
rental_price= input("enter the price per day")
rental_price= int(rental_price)

days =input("Enter the number of days")
days=int(days)


total= rental_price*days
print("you will pay us a total of",total)
"""
 
 
#EXAMPLE 3
'''
package1= input("Enter the weight of package 1:")
package2= input("Enter the weight of package 2:")
package3= input("Enter the weight of package 3:")

package1=int(package1)
package2=int(package2)
package3=int(package3)

total = (package1+package2+package3 *0.8)#0.8 is the discout to be received.
print("the bill is",total) '''


#MY EXAMPLE TO FOLLOW.
""" 
ceiling_fan=input("Enter the number units:")
wall_sockects= input("Enter the of units:")
laptop=input("Enter the price for the laptops")

ceiling_fan=int(ceiling_fan)
wall_sockects=int(wall_sockects)
laptop=int(laptop)

total= (ceiling_fan+wall_sockects+laptop * 0.56)

print("The cost is $",total,"have nice day")
"""

#EXAMPLE 4
'''
user=input("Enter username:" )
age=input("Enter your age:")

id_number= 123

id_number=str(id_number)
print("welcome",user,"you are",age,"your ID is",id_number)
'''

#EXAMPLE 5
'''
price1=500
price2=500
price3=500
price4=500

total=(price1+price2+price3+price4 /2)
print("the toal is",total)

lastName=input("enter your last name")
firstName=input("enter your benji name")
age=input("enter your age")

age=str(age)

print("welcome",lastName,firstName,"you are",age)
'''

#NESTING FUNCTIONS

''' 
THIS IS PUTTING THE FINCTIONS INSIDE EACH OTHER TO MAKE THE CODE FOR CLEANER 
TO DO THIS WE MUST KNOW THE FUCTIONS WE MUST NEST

cost1= cost1(input("enter the cost"))
cost2= cost2(input("enter the cost"))
total= cost1+cost2
print("the total cost is")
'''

#example
'''
package1= int(input("Enter the weight of package 1:"))
package2= int(input("Enter the weight of package 2:"))
package3= int(input("Enter the weight of package 3:"))
total = (package1+package2+package3 *0.8) 12#0.8 is the discout to be received.
print("the bill is",total) '''


#AN EXPENSE TRACKER
'''
income=int(input("Enter your income"))
food=int(input("Enter your food expense"))
rent=int(input("Enter your monthly rent"))
tax=int(input("Enter your tax amount"))
remaining=income- food- rent- tax
print("You are left with $",remaining)'''

#PROFIT AND LOSS

open_balance=int(input("Enter your opening Amount"))
production_cost=int(input("Enter the production cost"))
salary=int(input("Enter your the total salary"))
tax=int(input("Enter the annual tax"))
gross_profit=open_balance-production_cost-salary-tax
print("the gross for the year $",gross_profit)
