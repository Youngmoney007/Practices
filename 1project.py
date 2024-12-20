#A TRIP PLANNNER FOR SOMEONE
#A BOT TO DETERINE THE KIND OF CAR AM  LOOKING FOR
'''
enter=input("Enter 1- Start or 2- stop")
while enter!="2":
    cars=input("Are you looking for a car?").lower()
    if cars=="yes":
        car_brand=input("do you know the car brand?").lower()
    elif cars=="no":
        budget=int(input("enter your budget"))
        if budget >= "2000":
            print("we have some options for you")
            print("we have toyota,nissan,honda,fiat,tesla,BMW")
         
            
'''
'''

print("Welcome to the Music Bot!")
enter = int(input("1 - to start, 2 - to stop: "))

while enter == 1:
    music = input("Do you have a song in mind? (yes/no): ").strip().lower()
    if music == "yes":
        print("Awesome!")
        music_type = input("MUSIC TYPE (country/hip hop/jazz/musicals): ").strip().lower()
        if music_type in ["country", "hip hop", "jazz", "musicals"]:
            origin = input("What is the origin of the song? (Ghana/America/Togo/Benin/Sokoto): ").strip().lower()
            if origin in ["america", "togo", "benin", "sokoto"]:
                print("Here are some song suggestions:")
                print("- Love in the Dark")
                print("- Someone to Love")
                print("- Lonely")
                print("- So Alone")
                try:
                    year = int(input("Enter year (2000/2001/2002/2003/2004/2006): "))
                    if year in [2000, 2001, 2002, 2003, 2004, 2006]:
                        print("Additional suggestions:")
                        print("- Always on My Mind")
                        print("- Hold My Beer")
                        print("- Fruit is Okay")
                    elif 1990 <= year <= 1999:
                        print("We don't have such old songs.")
                    else:
                        print("Year not available.")
                except ValueError:
                    print("Invalid year. Please enter a number.")
            else:
                print("We don't have songs from that origin.")
        else:
            print("We don't have such music type.")
    else:
        print("Okay then, another time!")
    break
'''

print("WELCOME TO BENJI CAR RENTALS")

enter = input("Choose 1-PROCEED, 2-OTHER SERVICES, 3-CUSTOMER SERVICES: ").strip()
while enter == "1":  # Use string comparison for input
    car_type = input("Do you have a specific car type in mind? (YES/NO): ").strip().lower()
    if car_type == "yes":
        car_category = input("Select the type you want (sport/suv): ").strip().lower()
        condition = input("Enter the condition (brand new/used/moderate): ").strip().lower()

        # Validate car category and condition
        if car_category in ["sport", "suv"] and condition in ["brand new", "used", "moderate"]:
            print("We have it available!")

            # Get user's budget and validate it as an integer
            try:
                budget = int(input("How much are you willing to spend? ").strip())

                if car_category == "sport" and condition == "brand new":
                    if budget >= 200000:
                        print("We have some cool suggestions for you:")
                        print("Toyota Supra, Nissan GTR, Ferrari, Lamborghini, Range Rover Sport, Mercedes GLE, Honda Accord")
                    else:
                        print("We don't have any brand-new sports cars in your budget.")
                
                elif car_category == "sport" and condition == "used":
                    if budget >= 10000:
                        print("We have some cool suggestions for you:")
                        print("Pontiac Vibe, Sang Yang, Corolla, Toyota Fortuner, Toyota Echo, Volkswagen Jetta, Opel Astra")
                    else:
                        print("We don't have any used sports cars in your budget.")
                
                elif car_category == "sport" and condition == "moderate":
                    if budget >= 5000:
                        print("We have some cool suggestions for you:")
                        print("Matiz, Chrysler, Mitsubishi, 4Runner, Cube, Passat, Opel Astra")
                    else:
                        print("We don't have any moderately priced sports cars in your budget.")
                
                elif car_category == "suv" and condition == "brand new":
                    if budget >= 10000:
                        print("We have some cool suggestions for you:")
                        print("Toyota RAV4, Honda CR-V, Mazda CX-5, Ford Explorer, Kia Sorento, Hyundai Santa Fe")
                    else:
                        print("We don't have any brand-new SUVs in your budget.")
                
                elif car_category == "suv" and condition == "used":
                    if budget >= 6000:
                        print("We have some cool suggestions for you:")
                        print("Chevrolet Tahoe, BMW X5, Mercedes-Benz GLE, Nissan Rogue, Subaru Forester, Volkswagen Tiguan")
                    else:
                        print("We don't have any used SUVs in your budget.")
                
                elif car_category == "suv" and condition == "moderate":
                    if budget >= 2000:
                        print("We have some cool suggestions for you:")
                        print("Jeep Grand Cherokee, Chevrolet Blazer, Toyota Highlander, Ford Expedition, GMC Yukon, Lexus RX, Range Rover Sport")
                    else:
                        print("We don't have any moderately priced SUVs in your budget.")
                else:
                    print("We don't have what you're looking for.")

            except ValueError:
                print("Invalid budget amount. Please enter a number.")
        else:
            print("Invalid car type or condition. Please try again.")
    else:
        print("See our other options below!")
    
    # Break out of the loop after a single iteration
    break

if enter == "2":
    print("Welcome to Other Services. Explore our additional offerings!")


  
  
  
  
  
  
  
  
  
  
  
  
  
  
    