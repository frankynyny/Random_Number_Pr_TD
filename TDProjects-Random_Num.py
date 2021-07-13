import random

random_num = random.randrange(1, 10)

tally = 1
high_score = 10
royalty = 0
smarty_high_score = 0

def start_game():
    print("""
    Welcome to Guessing!  Has to be between numbers 1-10, nothing more, nothing less.
    Aim too low, it will let you know.  
    Aim too high, it will enlighten you.
    High score is the worst score and will be displayed
    May you score swiftly...
    If not.... expect some bantering...\n""" )

start_game()

while True:
    try:
        user_input = int(input("\nPick a number between 1 and 10: "))
        if user_input == random_num:
            print("\nYou got it! It took you {} tries.".format(str(tally)))
            if int(tally) < int(high_score):
                high_score = int(tally)
            if int(tally) >= 10:
                print("Lets just not speak about this again... I don't want you to feel SAT's are the only things holding you back.")
            elif int(tally) < int(high_score):
                print("Thanks very much for making the intelligence percentile harder to reach, now we all cant be #1 anymore.")
            while True:
                smarty_high_score += 1
                try_again = (input("Would you like to play again?\n[y]es /[n]o: \n"))
                if try_again == "y":
                    print("The HIGHSCORE is {}".format(high_score))
                    random_num = random.randrange(1, 10)
                    tally = 0
                    continue
                elif try_again == "n":
                    break
                elif smarty_high_score == 1:
                    tally += 1
                    smarty_high_score += 1
                    high_score = int(tally)
                    print("Go ahead....you are about to lose your high score...\n NEW HIGH SCORE: {}  ".format(tally))
                    continue
                elif smarty_high_score == 2:
                    tally += 1
                    smarty_high_score += 1
                    high_score = int(tally)
                    print("Keep on.....This is going to get interesting...\n NEW HIGH SCORE: {}  ".format(tally))
                    continue
                elif smarty_high_score == 3:
                    tally += 1
                    smarty_high_score += 1
                    high_score = int(tally)
                    print("*Grabs the dunce cap* \n NEW HIGH SCORE: {}  ".format(tally))
                    continue
                elif smarty_high_score == 6:
                    tally += 20
                    high_score = int(tally)
                    smarty_high_score += 1
                    print("*Grabs the dunce cap*\n NEW ANYONE CAN BEAT YOUR HIGH SCORE: {}  ".format(tally))
                    continue
                elif smarty_high_score == 8:
                    smarty_high_score += 1
                    tally += 40
                    high_score = int(tally)
                    print("*Walks it over*\n NEW ANYTHING CAN BEAT YOUR HIGH SCORE: {}  ".format(tally))
                    continue
                elif smarty_high_score == 10:
                    smarty_high_score += 1
                    tally += 1999
                    high_score = int(tally)
                    print("I dub thee....*places the dunce cap*\nBANS YOUR FINGERS")
                    continue
                elif smarty_high_score >= 11:
                    tally += 20
                    print("*Pushes you out and turns off the Open sign*")
                    break

        elif user_input >= 11:
            print("Listen, the plastic packet inside packages are not salt packets.... Please....stop eating them. It's 1 to 10, not Little Orphan Annie Decoder Ring.\nTally: {}".format(tally))
            continue
        elif user_input < random_num:
            tally += 1
            print("It is higher!\nTally: {}".format(tally))
            continue
        elif user_input > random_num:
            tally += 1
            print("It is lower!")
            continue

    except ValueError:
        tally += 1
        print("This isn't Fifth Element hieroglyphics, you're going to get an empty case.\nTally: {}".format(tally))
        continue

print("There")