import time  # Import time to sleep for some time
import random  # Import random to select objects randomly
# Identify lists of objects in the game

Places = ['Fields of Elysium', 'Torment of Hades', 'Greece']
Weapons = ['Sword', 'Bow', 'Dagger', 'Hammer', 'Stinger']
Elysium_Opponents = ['Ancient Soldiers', 'Kolossi', 'Hermes', 'Minotaur']
Hades_Opponents = ['Cerberus', 'Tartaros Rifts', 'Hades']
Greece = ['Bandit', 'Soldier', 'Bear']

Game_Result = ['Succeed', 'Lose']
Choice = ['Yes', 'No']
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
PrintSleep('Please Enter Your Name to start the game:', 1)
name = input('')


# Choosing the places
print('\nHello ' + name + '!  \nPlease choose which place you want to go? \n')
for place in Places:
    print(place)
Choice = ''
while Choice not in Places:
    msg = '\nChoose fullname/1st letter or sequence of choice.\n'
    Choice = input(msg)
    if Choice.lower() == 'Fields of Elysium'.lower() or Choice.lower() == 'F'.lower() or Choice == '1':
        Choice = 'Fields of Elysium'
    elif Choice.lower() == 'Torment of Hades'.lower() or Choice.lower() == 'T'.lower() or Choice == '2':
        Choice = 'Torment of Hades'
    elif Choice.lower() == 'Greece'.lower() or Choice.lower() == 'G'.lower() or Choice == '3':
        Choice = 'Greece'
    else:
        Choice = ''

time.sleep(2)


# Random weapons choices
weaponchosen = random.choice(Weapons)
PrintSleep('You have ' + weaponchosen + ' as your weapon.', 1)


# Choice to change the weapon
msg = ('Would you like to change your weapon?\nYou can do this once.\n')
changerequest = input(msg)
if changerequest.lower() == 'Yes'.lower():
    weaponchosen = random.choice(Weapons)
    PrintSleep('Youre in ' + Choice + ' & you have ' + weaponchosen + '.', 1)
else:
    changerequest = ''


# Random opponents based on the place
PrintSleep('In front of you is ', 0)
if Choice == 'Fields of Elysium':
    PrintSleep(random.choice(Elysium_Opponents), 0)
if Choice == 'Torment of Hades':
    PrintSleep(random.choice(Hades_Opponents), 0)
if Choice == 'Greece':
    PrintSleep(random.choice(Greece), 0)


# Stating the opponent type
PrintSleep('Use your weapon to kill your opponent!', 5)


# Printing the results
PrintSleep('You ' + random.choice(Game_Result) + '!', 3)


# Exiting the game
PrintSleep('Exiting the Game!', 5)
