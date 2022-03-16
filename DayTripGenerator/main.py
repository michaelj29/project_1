import random

def day_trip_generator():
    tourist_destinations = ["Memphis", "Houston", "San Francisco", "Boston"]
    restaurant_types = ["Pizza Place", "Bar and Grill", "Seafood Sushi", "Wings n Things", "Surf and Turf", "Just Drinks for food"]
    transportation_type = ["Teleportation", "Walking", "A bus", " A Helicopter", "A personal Car", "A horse"]
    entertainment_type = ["Karaoke bar", " Crazy Bar", "Arcade", "Night Hiking Event", "Wine Tasting Event", "Comedy Show"]
    
    users_name = input("Enter your name for a chance to take a trip: ")
    print(f"Hello {users_name}, you have been selected. Let's create your itinerary!")

    def trip_lists(list_1):
      do_not_like_city = True

      while do_not_like_city == True:
          random_list_1 = random.choice(list_1)
          yes_or_no = input(f"What do you like? {random_list_1}? y or n?: ")
          if yes_or_no.lower() == "y":
            do_not_like_city = False
            print(f"Awesome! You selected {random_list_1}!")
            return random_list_1
      
    users_destination = trip_lists(tourist_destinations)
    users_entertainment = trip_lists(entertainment_type)
    users_transportation = trip_lists(transportation_type)
    users_food = trip_lists(restaurant_types)
    
    like_choices = True

    while like_choices == True:
      yes_or_no = input(f"Do you like your choices: {users_food}, {users_destination}, {users_entertainment}, {users_transportation}? y or n?: ") 
      if yes_or_no.lower() == "y":
        like_choices = False 
        print(f'Congrats on your choices {users_food}, {users_destination}, {users_entertainment}, {users_transportation}!')
      else:
          print("Our apologies, lets try again")
          users_destination = trip_lists(tourist_destinations)
          users_entertainment = trip_lists(entertainment_type)
          users_transportation = trip_lists(transportation_type)
          users_food = trip_lists(restaurant_types)    


day_trip_generator()

