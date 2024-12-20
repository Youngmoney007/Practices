#EXAMPLE 1
'''
trip_type = input("Is your trip business, leisure, or personal? ").lower()  # Convert input to lowercase for consistency
price = int(input("Enter your price: "))
discount = trip_type== 'business' or 'personal' and price >= 100
print("Customer receives a discount:", discount)
'''

#EXAMPLE 2
'''
food_type=input("did you buy pizza or burger")
price=int(input("enter the price"))
#tax=float(input("enter the tax"))
discount= food_type='pizza' and price >=100
print("The discount is",discount)
'''

#EXAMPLE 
'''
code = input("Enter your code here:")

if code =="ee3456":
    print("Access Granted")
else:
    print("Access Denied")
'''

'''
password= input("Enter your password")

if password=="344ghh":
    print("correct password")
else:
    print("Incorrect password")

    
score=(input("Enter your score"))
if score >= 500:
    print("You have passed")
else:
    print("You failed")


cost=int(input("Eter your funds"))
if cost < 300:
     print("take your ass to work")
if cost == 500:
     print("take a road trip")
if cost ==1000:
     print("buy crypto")

print("have fun")


bag_weight= int (input("Enter the weight of the bag in kg"))
destination=(input("Domestic or international"))

if bag_weight <= 18:
     price = 25
else:
     price= 75

if destination == "domestic":
    price=price+150
else:
    price=300
    
print("The ticket price:",price)


sports_ticket = input("Enter your sports: ")

if sports_ticket == "football":
    print("1000")
elif sports_ticket == "tennis":
    print("1220")
elif sports_ticket == "golf":
    print("180")
elif sports_ticket == "rugby":
    print("150")
else:
    print("Not found")
'''
#NESTING CONDITIONS
"""
PUTTING CONDITIONS INTO EACH OTHER.
NEW FUNCTIONS

*.lower()--all lower case
*upper()--- all upper case
*capitalize()-- will capitalixe the first letter
A METHOD MUST BE LINKED TO A VARIABLE BEFORE IT CAN WORK.

#Example 1

movie=input("wanna watch a movie?").lower()
if movie=='yes':
    genre= input("enter the genre").lower()
    if genre=='action':
        print("fast and furious")
    else:
        print("prison break")
else:
    print("no movie for you")
"""
'''
Example 2
accomodation= input("Resort or hotel").lower()
if accomodation=='resort' or 'hotel':
    max_price=int(input("how much are you willing to pay"))
    
    if max_price>=1000:
        print("book at my house")
    else:
        print("book at the garage")
else:
    print("you're not looking for accomodation")
    

#example 3
item1=int(input("enter the cost of item 1"))
item2=int(input("enter the cost of item 2"))
item3=int(input("enter the cost of item 3"))

total = item1+item2+item3
if item1 < item2 and item2 <item3:
    total= total * 0.5
    print("Total cost after discount:", total)

if item1 > item2 and item2 >item3 :
    total= total * 0.7
    print("Total cost after discount:", total)

print("total",total)

'''
'''
#example 4

firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("Enter the second number: "))

# Perform operations
addition = firstNumber + secondNumber
print("Addition:", addition)

subtraction = firstNumber - secondNumber
print("Subtraction:", subtraction)

multiplication = firstNumber * secondNumber
print("Multiplication:", multiplication)

# Handle division by zero
if secondNumber != 0:
    division = firstNumber / secondNumber
    print("Division:", division)
else:
    print("Division: Error (cannot divide by zero)")'''


'''def calculator():
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Enter your choice (1/2/3/4): ")
    firstNumber = float(input("Enter the first number: "))
    secondNumber = float(input("Enter the second number: "))

    if choice == "1":
        print("Addition:", firstNumber + secondNumber)
    elif choice == "2":
        print("Subtraction:", firstNumber - secondNumber)
    elif choice == "3":
        print("Multiplication:", firstNumber * secondNumber)
    elif choice == "4":
        if secondNumber != 0:
            print("Division:", firstNumber / secondNumber)
        else:
            print("Division: Error (cannot divide by zero)")
    else:
        print("Invalid choice!")

calculator()'''

car_brand=str(input("what car are you looking for")).lower()
if car_brand=="toyota" or "benz" or"honda" or" matiz" or "nissan":
    print("available")
    price=int(input("enter your budget"))
    if price >=2000:
        print("we have some options available for you")
        
else:
    print("try again")

'''
bread_type=str(input("what type of bread are you using for")).lower()
if bread_type=="tea" or "butter" or "sugar":
    print("we have some for you")
    price=int(input("how much are you willing to pay"))
    if price>=20:
        print("we have some")
    package=str(input("what is your preferred package")).lower()
    if package=="paper bag"or"rubber bag"or"delivery":
        print("we will bring it to you soon")
    location=str(input("what is your location")).lower()
    if location=="ghana"or"nigeria"or"togo"or"benin"or"zimbabwe":
        print("order placed")
else:
    print("look somewhere else")
    
'''


"""
houses=str(input("what house are you interested in?"))
if houses=="mansion":
    print("we have some options you want to check out")
    budget=int(input("How much are you going to spend on the house"))
    if budget>= "5000":
        print("good enough")
else:
    print("try again")

"""
#A TRIP PLANNER FOR SOMEONE 












    
    


 














    