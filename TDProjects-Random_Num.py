import random

random_num = random.randrange(1, 10)

tally = 1
high_score = 0
royalty = 0

def start_game():
    print("""
    Welcome to Guessing!  Has to be between numbers 1-10, nothing more, nothing less.
    Aim too low, it will let you know.  
    Aim too high, it will enlighten you.
    High score is the worst score and will be displayed
    May you score swiftly...""" )

start_game()

while True:
    print(random_num)
    user_input = int(input("Pick a number between 1 and 10: "))


    if user_input == random_num:
        print("\nYou got it! It took you {} tries.".format(str(tally)))
        if int(tally) > int(high_score):
            high_score = int(tally)
        if int(tally) >= 10:
            print("Lets just not speak about this again... I don't want you to feel SAT's are the only things holding you back.")
        elif int(tally) < int(high_score):
            print("Thanks very much for making the intelligence percentile harder to reach, now we all cant be #1 anymore.")
        try_again = (input("Would you like to play again?\n[y]es /[n]o: "))
        if try_again == "y":
            print("The HIGHSCORE is {}".format(high_score))
            random_num = random.randrange(1, 10)
            tally = 0
            continue
        elif try_again == "n":
            break
    elif user_input >= 11:
        print("Listen, the plastic packet inside packages are not salt packets.... Please....stop eating them.")
        continue
    elif user_input < random_num:
        tally += 1
        print("It is higher!\nTally: {}".format(tally))
        continue
    elif user_input > random_num:
        tally += 1
        print("It is lower!")
        continue

print("There")