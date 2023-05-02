import random

def roll(nbr_of_dices):

    sum = 0

    while nbr_of_dices > 0:
        i = random.randrange(1, 7)
        sum += i
        print('You rolled {}'.format(i))
        nbr_of_dices -= 1

    print('You rolled a total of: {}'.format(sum))


def welcome_message():
    print('Welcome to the Dice Rolling Simulator!')


exit_wanted = 1

while exit_wanted != 0:

    nbrOfDices = input('How many dices do you want to throw? \n')

    roll(int(nbrOfDices))

    test = input('Do you want to continue play this game?\n'
                 '(yes or no) \n')
    if test == 'no':
        exit_wanted = 0
