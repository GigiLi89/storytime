import random


def play_game():
    """
    Function to manage the game.
    """
    while True:
        print("Welcome to this Madlibs game!")
        play = input("Let's play, shall we? 'yes'/'no' \n")
        if play.lower() == "yes":
            print("Alright, let's see what these small madlibs can create! \n")
            results = []
            games = [game1, game2, game3]
            random.shuffle(games)
            for game in games:
                result = game()
                if game == game1:
                    results.insert(0, result)  # First on the sum result list
                elif game == game2:
                    results.insert(1, result)  # Second on the sum result list
                else:
                    results.insert(2, result)  # Third on the sum result list
            game_summary(results)
        elif play.lower() == "no":
            print("Ok, let's play another time.")
            break  # Exit the loop without playing the game
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue  # Restart loop if invalid

        # Loop to ask user if they want to play again
        while True:
            play_again = input("Do you want to play again? 'yes'/'no' \n")
            if play_again.lower() == "yes":
                break
            elif play_again.lower() == "no":
                print("Ok, see you next time!")
                exit()  # Exits the game
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


def game1():
    """
    Function to create the first madlibs story with the user's input.
    """
    month = input("Enter a month: ")
    name1 = input("Enter your name: ")
    name2 = input("Enter another name: ")
    pizza_topping = input("Enter a pizza topping: ")

    # The first story with the inputs
    result1 = (
        "A sunny day in " + month + " there was a pizza party coming up. "
        + name1 + " and " + name2 + " was hosting the party but "
        "they forgot to buy " + pizza_topping + ".\n"
    )
    print(result1)
    return result1


def game2():
    """
    Function to create the second madlibs story with the user's input.
    """
    # Second inputs for the user
    name3 = input("Enter a friend's name: ")
    store_name = input("Enter a store name: ")
    fruit = input("Enter a fruit: ")

    # The second story with inputs
    result2 = (
        "They texted " + name3 + " to buy it on the way. "
        + name3 + " popped by " + store_name + " and bought the "
        + fruit + " before heading to the party.\n"
    )
    print(result2)
    return result2


def game3():
    """
    Function to create the third madlibs story with the user's input.
    """
    # Third inputs for the user
    positive_feeling = input("Enter a positive feeling: ")
    artist = input("Enter an artist: ")

    # The third story with inputs
    result3 = (
        "Realising the funny mix up because of "
        "autocorrect they all enjoyed the party without the topping."
        " Everyone was " + positive_feeling +
        " and dancing to " + artist + "!\n"
    )
    print(result3)
    return result3


def game_summary(results):
    """
    Function to summarize all madlibs results.
    """
    print("Good Job, let's put them together in the right order: \n")
    # Print the results
    for result in results:
        print(result)


play_game()