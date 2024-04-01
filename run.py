
# Welcome message and request to play for user
print("Welcome to this Madlibs game!")

play = input("Lets play, shall we? yes/no \n")
procees="yes" or "no"
if play == "yes":
    print("Alright, let's get started! \n")
else:
    print("Ok, lets play another time.")
    exit()

# Inputs for the user 
a = input("Enter your name: ")
b = input("Enter a friends name: ")
c = input("Enter a number: ")

# The story with the inputs
print("One summer day in June, " + a + " surprised " + b + " with " + c + " puppies.\n")

play_again = input("Would you like to play another Madlibs game? yes/no \n")
process_again="yes" or "no"
if play_again == "yes":
    print("Woho, let's do this! \n")
else:
    print("Alright, thanks for playing!")
    exit()

