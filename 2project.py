'''print("WELCOME TO RD SHOES!")
print("We sell all kinds of men/women shoes and kids shoes")

gender = input("Choose your gender (Male, Female, Kids): ").strip().lower()

if gender == "male":
    option = input("Do you have any type you are looking for? (Yes/No): ").strip().lower()
    if option == "yes":
        shoe = input("Select the type you want (Loafers, Oxfords, Single Monk Strap, Double Monk Strap, Boots, Sneakers, Other): ").strip().lower()
        try:
            size = int(input("Select the size you want (35-50): ").strip())
        except ValueError:
            print("Invalid size. Please enter a number.")
            exit()
        
        color = input("What color are you looking for? (Black, Brown, Suede Black, Blue, Shiny Shoes, Other): ").strip().lower()
        brand = input("Select the brand you want (Adidas, Nike, Balenciaga, LV, Georgio Armani): ").strip().lower()

        # Validation for inputs
        if shoe in ["loafers", "oxfords", "single monk strap", "double monk strap", "boots", "sneakers", "other"] and \
           35 <= size <= 50 and \
           color in ["black", "brown", "suede black", "blue", "shiny shoes", "other"] and \
           brand in ["adidas", "nike", "balenciaga", "lv", "georgio armani"]:
            
            print("We have them available.")
            try:
                budget = int(input("What is your budget? ").strip())
                if shoe in ["loafers", "sneakers", "other"] and budget >= 20:
                    print("We have something available.")
                elif shoe in ["oxfords", "boots"] and budget >= 25:
                    print("We have something available.")
                elif shoe in ["single monk strap", "double monk strap"] and budget >= 50:
                    print("We have something available.")
                else:
                    print("Look at other options within your budget.")
            except ValueError:
                print("Invalid budget amount. Please enter a valid number.")
        else:
            print("Please check our other options.")
    else:
        print("Try something different.")
elif gender == "female":
    print("Female options are coming soon.")
elif gender == "kids":
    print("Kids' options are coming soon.")
else:
    print("Invalid gender. Please choose from Male, Female, or Kids.")
'''


print("KIDS SHOES!")
print("Welcome!")

gender = input("Are you looking for (male/female): ").strip().lower()

if gender == "male":
    try:
        # Input and validate size
        size = int(input("What is the size of your child (10-15): "))
        if size < 10 or size > 15:
            print("Invalid size. Please enter a size between 10 and 15.")
            exit()
        print("Awesome! Have a look below.")
    except ValueError:
        print("Invalid input. Please enter a number for the size.")
        exit()
    
    # Input for color and brand
    color = input("What color are you looking for (black/brown/blue black): ").strip().lower()
    brand = input("What brand are you looking for (Adidas/Nike/Puma): ").strip().lower()

    # Validation for color, size, and brand
    if color in ["black", "brown", "blue black"] and brand in ["adidas", "nike", "puma"]:
        print("Available! Have a look at the options below.")
    else:
        print("Sorry, the selected options are not available. Please try again.")
        exit()

    # Input and validate budget
    try:
        budget = int(input("What is your budget today? "))
        if (color in ["black", "brown"] and budget >= 20) or \
           (color in ["black", "blue black"] and budget >= 30) or \
           (color in ["brown", "blue black"] and budget >= 50):
            print("Available! Have a look at the options below.")
        else:
            print("Sorry, we don't have options in this budget. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the budget.")
else:
    print("Please go to the female section below.")

    
        
























































































