import time  # Import time to sleep for some time
import random  # Import random to select objects randomly
# Identify lists of objects in the game

Places = ['Fields of Elysium (1)', 'Torment of Hades (2)', 'Greece (3)']
Weapons = ['Sword', 'Bow', 'Dagger', 'Hammer', 'Stinger']
Elysium_Opponents = ['Ancient Soldiers', 'Kolossi', 'Hermes', 'Minotaur']
Hades_Opponents = ['Cerberus', 'Tartaros Rifts', 'Hades']
Greece = ['Bandit', 'Soldier', 'Bear']

Game_Ending = ['Succeed', 'Lose']
Option = ['Yes', 'No']
# End


# Define a function to print messages
def PrintSleep(msg, seconds):
    print(msg + '\n')
    time.sleep(seconds)


# Game Intro.
PrintSleep('\nWelcome to the world of advantures.', 0)


PrintSleep('It will take you to other dimentions.', 1)
PrintSleep('You will get the help you need.', 0)
PrintSleep('But you should choose wisely to succeed in your missions.', 1)
# End of Intro.


# Get the player's name
PrintSleep('Enter Your Name to start your adventure:', 1)
name = input('')


# Choosing the places
print('\nHello ' + name + '!  \nChoose your destiny? \n')
for place in Places:
    print(place)
Option = ''
while Option not in Places:
    msg = '\nUse 1st letter/number of option.\n'
    Option = input(msg)
    if Option.lower() == 'F'.lower() or Option == '1':
        Option = 'Fields of Elysium (1)'
    elif Option.lower() == 'T'.lower() or Option == '2':
        Option = 'Torment of Hades (2)'
    elif Option.lower() == 'G'.lower() or Option == '3':
        Option = 'Greece (3)'
    else:
        Option = ''

time.sleep(2)


# Random weapons choices
weaponchoice = random.choice(Weapons)
PrintSleep('You have ' + weaponchoice + ' as your weapon.', 1)


# Choice to change the weapon
msg = ('Would you like to change your weapon?\nYou can do this once.\n')
changerequest = input(msg)
if changerequest.lower() == 'Yes'.lower():
    weaponchoice = random.choice(Weapons)
    PrintSleep('You\'re in ' + Option + ' & you have ' + weaponchoice + '.', 1)
else:
    changerequest = ''


# Random opponents based on the place
PrintSleep('In front of you is ', 0)
if Option == 'Fields of Elysium (1)':
    PrintSleep(random.choice(Elysium_Opponents), 0)
if Option == 'Torment of Hades (2)':
    PrintSleep(random.choice(Hades_Opponents), 0)
if Option == 'Greece (3)':
    PrintSleep(random.choice(Greece), 0)


# Stating the opponent type
PrintSleep('Use your '+ weaponchoice + ' to kill your opponent!', 5)


# Printing the results
PrintSleep('You ' + random.choice(Game_Ending) + '!', 3)


# Exiting the game
PrintSleep('Exiting the Game!', 5)
