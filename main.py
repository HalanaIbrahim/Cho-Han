#This is practice from the book BIG BOOK SMALL PYTHON PROJECTS by Al Sweigart


import random, sys,time

JpNumbers = {1:'Ichi', 2:'Ni', 3:'San', 4:'Shi', 5:'Go', 6:'Roku'}

print('''
    Welcome to Choi-Han!
    This is a feudal Japanese house gamblibng game. Two six-sided are rolled in a cup and the players bet on wether the 
    sum is even (Cho) or odd (Han).
    ARE YOU READY! ''')

print('\n')

mono = 500

#time.sleep(2)
print("Would like to ('QUIT')")
print('IF NOT')
print('How much would you like to bet!')
print('You have {} mono available'.format(mono))


while True:
    pot = input('>')
    if pot.upper() == 'QUIT':
        print('Thanks for playng!')
        sys.exit()
    elif not pot.isdecimal():
        print('Please enter correct numbers!')
    elif int(pot) > int(mono):
        print('Please enter an amount equal to or less than your availabe funds of {} mono'.format(mono))
    else:
        bPot = int(pot)
        break

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

#time.sleep(2)
print('''
The shop keeper takes the cup and gives the dice inside a good swirl!
He then smacks the cup upside down on the floor and asks for your bet of even (Cho) or odd (Han).
What would like to bet!''')

while True:
    bet = input('>').upper()
    if bet != 'CHO' and bet != 'HAN':
        print('Please enter a correct bet!')
        continue
    else:
        break

rollsEven = (dice1 + dice2 % 2) == 0

if rollsEven:
    correctBet = 'CHO'
else:
    correctBet = 'HAN'

if correctBet == bet:
    print('You won!')
    shopFee = (bPot // 10)
    mono = (mono + bPot) - shopFee
    print('You now have {} mono'.format(mono))
    
else:
    print('You lost')
    shopFee = (bPot // 10)
    mono = (mono - bPot) - shopFee
    print('You now have {} mono'.format(mono))





