import random

def play_game():
    while True:
        print("Welcome to this Madlibs game")
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

# First madlibs
def game1():
    # First inputs for the user 
    a = input("Enter your name: ")
    b = input("Enter a friend's name: ")
    c = input("Enter a number: ")

    # The first story with the inputs
    result1 = "One summer day in June, " + a + " surprised " + b + " with " + c + " puppies.\n"
    print(result1)
    return result1

# Second madlibs
def game2():
    # Second inputs for user
    d = input("Enter a location: ")
    e = input("Enter a pet name: ")
    f = input("Enter a dish: ")

    # The second story with inputs
    result2 = "Take a trip to " + d + " with your favorite " + e + " and enjoy a wonderful " + f + ". \n"
    print(result2)
    return result2

# Third madlibs
def game3():
    #Third inputs for user
    g = input("Enter a feeling: ")
    h = input("Enter a place: ")
    i = input("Enter a vegetable: ")

    result3 = "It makes me " + g + " to be out in " + h + " and pick " + i + ". \n"
    print(result3)
    return result3

def game_summary(results):
    print("Good Job, let's put them together in the right order: \n")
    # Print the results
    for result in results:
        print(result)



play_game()