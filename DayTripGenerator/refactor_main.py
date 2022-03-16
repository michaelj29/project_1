


import random

def day_trip_generator():
    tourist_destinations = ["Memphis", "Houston", "San Francisco", "Boston"]
    restaurant_types = ["Pizza Place", "Bar and Grill", "Seafood Sushi", "Wings n Things", "Surf and Turf", "Just Drinks for food"]
    transportation_type = ["Teleportation", "Walking", "A bus", " A Helicopter", "A personal Car", "A horse"]
    entertainment_type = ["Karaoke bar", " Crazy Bar", "Arcade", "Night Hiking Event", "Wine Tasting Event", "Comedy Show"]
    
    users_name = input("Enter your name for a chance to take a trip: ")
    print(f"Hello {users_name}, you have been selected. Let's create your itinerary!")

    def users_city():
        users_do_not_like_city = True
        while users_do_not_like_city == True:
             yes_or_no = input(f"Would you like to go to {random.choice(tourist_destinations)}? y or n?: ")
             if yes_or_no == "y":
                users_do_not_like_city = False
                users_city_choice = random.choice(tourist_destinations)
                print(f"Awesome! You will be heading to {users_city_choice}!")
                return users_city_choice
             users_do_not_like_city = True
    city_choice = users_city()

    def users_transportation():
        users_do_not_like_transportation = True       
        while users_do_not_like_transportation == True:
             yes_or_no = input(f"Would you like to travel by {random.choice(transportation_type)}? y or n?: ")
             if yes_or_no == "y":
                users_do_not_like_transportation = False
                users_transportation_choice = random.choice(transportation_type)
                print(f"Great choice! You will be traveling by {random.choice(transportation_type)}!")
                return users_transportation_choice
    transportation_choice = users_transportation()       
            
    def users_food():
        users_do_not_like_restuarant = True
        while users_do_not_like_restuarant == True:
             yes_or_no = input(f"Would you like to eat at the {random.choice(restaurant_types)} restuarant? y or n?: ")
             if yes_or_no == "y":
                users_do_not_like_restuarant = False
                users_food_choice = random.choice(restaurant_types)
                print(f"Stellar! You will be eating at the {random.choice(restaurant_types)} restaruant!")
                return users_food_choice
    food_choice = users_food()

    def users_entertainment():
        users_do_not_like_entertainment = True
        while users_do_not_like_entertainment == True:
             yes_or_no = input(f"Do you like the {random.choice(entertainment_type)}? y or n?: ")
             if yes_or_no == "y":
                users_do_not_like_entertainment = False
                users_entertainment_choice = random.choice(entertainment_type)
                print(f"Fantastic! {random.choice(entertainment_type)} will be added to your itinerary!")
                return users_entertainment_choice
    entertainment_choice = users_entertainment()

    def finalize_trip():
        print(f'Here is what you selected; City: {city_choice}, Transportation: {transportation_choice}, Food: {food_choice}, and Entertainment: {entertainment_choice}.')
        yes_or_no = input(f"Do you like your itinerary? y or n?: ")
        if yes_or_no == "y":
            print(f'Congrats {users_name}, you will be heading to {city_choice} next month. {transportation_choice} will be your method of Travel. You will have a free meal at the {food_choice} restuarant. Enjoy your night at the {entertainment_choice}')
            return
        print(f"My apologies {users_name}, lets try this one more time!")
        updated_city = users_city()
        updated_transportation = users_transportation()
        updated_food = users_food()
        updated_entertainment = users_entertainment()
        print(f'Congrats {users_name}, you will be heading to {updated_city} next month. {updated_transportation} will be your method of Travel. You will have a free meal at the {updated_food} restuarant. Enjoy your night at the {updated_entertainment}')
        return
    finalize_trip() 

day_trip_generator()
