"""Restaurant rating lister."""

import random

def restaurant_rating_lister(score_text):
    """takes in resaurant ratings from text file and stores ratings in sorted dictionary"""
    """and outputs alphabetical list by restaurant"""

    # Opens scores text
    scores_source = open(score_text)
    scores = {}

    # Splits it into key (left of colon) and value (right of colon)
    for each_line in scores_source:
        each_line = each_line.split(":")

        # Adds key, value pairs to the sources dictionary
        scores[each_line[0]] = int(each_line[1])

    # Sorts a list of the scores dictionary keys
    sorted_scores_list = sorted(scores)

    print("Hey there, welcome to the restaurant ratings")

    while True:
        print("You can do any of the following 3 options:")
        print("1. See all the ratings (in alphabetical order)")
        print("2. Add a new restaurant (and rate it).")
        print("3. Quit") 
        print("4. Update a random restaurants rating")
        print("5. Update a chosen restaurants rating")
        to_do = input("What would you like to do? (Type 1, 2, 3, 4, 5): ")
        
        # Prints the restaurant ratings based on key names sorted in sorted_scores_list
        if to_do == "1":
            for restaurant, score in sorted(scores.items()):
                print(f"{restaurant} is rated at {score}.")
    

        # Asks user to add a restaurant name:
        elif to_do == "2":
              
            ask_restaurant_name = input("What is the name of the restaurant you would like to rate?: ")
            ask_restaurant_name = ask_restaurant_name.title()
        
            # Asks for restaurant score until valid number is given
            while True:
                ask_restaurant_score = input("How would you rate that restaurant?: ")
                if int(ask_restaurant_score) >= 0 and int(ask_restaurant_score) <= 5:
                    break         
                else:
                    print("Score must be within the range of 0-5.")
                    continue

            # Adds their new restaurant and scores to the scores above
            scores[ask_restaurant_name] = int(ask_restaurant_score)

            # Sorts the list again with new input
            sorted_scores_list = sorted(scores)

            # Print a new list
            for restaurant in sorted_scores_list:
                print(f"{restaurant} is rated at {scores[restaurant]}.")

        # Allows user to quit
        elif to_do == "3":
            print("Goodbye!")
            break

        # Updates a random restaurants rating
        elif to_do == "4":
            # Choose a random restaurant
            random_restaurant = random.choice(sorted_scores_list)
            print(f"The randomly selected restaurant is {random_restaurant}. It's current score is {scores[random_restaurant]}.")
            
            # Loops until a valid score is put
            while True:    
                new_score = input(f"What should {random_restaurant}'s new score be?: ")
                
                if int(new_score) >= 0 and int(new_score) <= 5:
                    # Changes the score in the dictionary for the random restaurant selected
                    scores[random_restaurant] = int(new_score)
                    break    
                     
                else:
                    print("Score must be within the range of 0-5.")
                    continue

        # Updates a specific restaurants rating
        elif to_do == "5":
            
            #Display_restaurants:
            for restaurant, score in sorted(scores.items()):
                print(f"{restaurant} is rated at {score}.")
            
            while True:
                # Choose a specific restaurant
                chosen_restaurant = input("What restaurant would you like to update?: ")
                chosen_restaurant = chosen_restaurant.title()

                if chosen_restaurant not in scores:
                    print("Sorry, that is not a restaurant. Type the exact name please.")
                else:
                    print(f"The selected restaurant is {chosen_restaurant}. It's current score is {scores[chosen_restaurant]}.")
                    break
            
            # Loops until a valid score is put
            while True:    
                new_score = input(f"What should {chosen_restaurant}'s new score be?: ")
                
                if int(new_score) >= 0 and int(new_score) <= 5:
                    # Changes the score in the dictionary for the random restaurant selected
                    scores[chosen_restaurant] = int(new_score)
                    break    
                     
                else:
                    print("Score must be within the range of 0-5.")
                    continue
                
        else:
            print("That is not a valid option.")
            continue

restaurant_rating_lister("scores.txt")