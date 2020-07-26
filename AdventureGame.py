import time  # Import time to sleep for some time
import random  # Import random to select objects randomly

# Identify lists of objects in the game
Places = ['Fields of Elysium (1)', 'Torment of Hades (2)', 'Greece (3)']
Weapons = ['Sword', 'Bow', 'Dagger', 'Hammer', 'Stinger']
Opponents = ['Ancient Soldiers', 'Kolossi', 'Cerberus', 'Minotaur']
Game_Ending = ['Succeed', 'Lose']

# End Configuration


# 1 defining a function to clear the space for invalide entries 
def cls():
    print('\n'*100)

# 2 defining function to start the game
def start_game():
    start_place_options = (Places)
    Option = ''
    while Option not in Places:
        print('Hello ' + name + '! Welcome to the world of advantures.')
        msg = '\nChoose your place using 1st letter/number of option.\n'
        for place in Places:
            print(place)
        Option = input(msg)
        if Option.lower() == 'F'.lower() or Option == '1':
            Option = 'Fields of Elysium (1)'
        elif Option.lower() == 'T'.lower() or Option == '2':
            Option = 'Torment of Hades (2)'
        elif Option.lower() == 'G'.lower() or Option == '3':
            Option = 'Greece (3)'
        else:
            Option = ''
            cls()

# 3 defining function t use as print and put time.sleep together
def PrintSleep(msg, seconds):
    print(msg + '\n')
    time.sleep(seconds)

# 4 defning function to change the weapean if needed
def ChangeYourWeapon():
    newrequest =input('Do you want to change your current weapon?\n')
    if newrequest == 'yes':
        newweapon = random.choice(Weapons)
        print('You now have a ' + newweapon)


# Game Will Start from here
RetryGame = 'Yes'.lower()
while RetryGame == 'Yes'.lower():
    # Get the player's name
    PrintSleep('Enter Your Name to start your adventure:', 1)
    name = input('')
    start_game()
    time.sleep(2)


    weapon = random.choice(Weapons)
    print('Your weapon is ' + weapon + '\n')


# Choice to change the weapon if needed
    ChangeYourWeapon()

# Random opponents based on the place
    PrintSleep('In front of you is ' + random.choice(Opponents), 0)


# Stating the opponent type
    PrintSleep('Use your ' + weapon + ' to kill your opponent!', 5)


# Printing the results
    PrintSleep('You ' + random.choice(Game_Ending) + '!', 3)
    print('You Finished Your Adventure!')
    RetryGame = input('Do you want to play again?\n')
