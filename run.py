import random

def play_game():
    while True:
        print("Welcome to this Madlibs game! You'll play small madlibs that will turn into one funny story.")
        play = input("Let's play, shall we? 'yes'/'no' \n")
        if play.lower() == "yes":
            print("Alright, let's see what these small madlibs can create! \n")
            results = []
            games = [game1, game2, game3]
            random.shuffle(games)
            for game in games:
                result = game()
                if game == game1:
                    results.insert(0, result)  # Insert result1 at the beginning of the list
                elif game == game2:
                    results.insert(1, result)  # Insert result2 after result1
                else:
                    results.insert(2, result)  # Insert result3 after result2
            game_summary(results)
            break  # Exit the loop after playing the game
        elif play.lower() == "no":
            print("Ok, let's play another time.")
            break  # Exit the loop without playing the game
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# First inputs for the user 
def game1():
    month = input("Enter a month: ")
    name1 = input("Enter your name: ")
    name2 = input("Enter another name: ")
    pizza_topping = input("Enter a pizza topping: ")

    # The first story with the inputs
    result1 = "A sunny day in " + month + " there was a pizza party coming up. " + name1 + " and " + name2 + " was hosting the party but they forgot to buy " + pizza_topping + ".\n"
    print(result1)
    return result1

# Second madlibs
def game2():
    # Second inputs for user
    name3 = input("Enter a friends name: ")
    store_name = input("Enter a store name: ")
    fruit = input("Enter a fruit: ")

    # The second story with inputs
    result2 = "They texted " + name3 + " to buy it on the way. " + name3 + " popped by " + store_name + " and bought the " + fruit + " before heading to the party.\n"
    print(result2)
    return result2

# Third madlibs
def game3():
    #Third inputs for user
    positive_feeling = input("Enter a positive feeling: ")
    artist = input("Enter an artist: ")

    result3 = "Realising the funny mix up because of autocorrect they all enjoyed the party without the topping. Everyone was " + positive_feeling + " and dancing to " + artist + "!\n"
    print(result3)
    return result3

def game_summary(results):
    print("Good Job, let's put them together in the right order: \n")
    # Print the results
    for result in results:
        print(result)



play_game()