''' A restaurant program that chooses a random restaurant in Hoboken 
    Created by Jordan Tantuico 1/12/2019
    Last edited 1/12/2019 '''
import random, sys

allRestaurants = ['Mamoun\'s', 'Vito\'s', 'Karma', 'Makai', 'Ali Baba', 'Napoli\'s', 
'Flatbread', 'Midtown', 'Pita Pit', 'O\'bagel', 'Bagels on the Hudson', 'Rice Shop',
'Johnny Rockets', 'Ubu', 'Mr. Wraps', 'Qdoba', 'Chipotle', 'Pizza Republic', 
'McDonald\'s', 'Cluck U', 'Gio\'s', 'Panera', 'Gogi Grill', 'Honeygrow', 'South Street',
'Bareburger', 'Vivi\'s', 'Chicken Factory', 'Charrito\'s']

basicTier = ['Mamoun\'s', 'McDonald\'s', 'Pita Pit', 'O\'bagel', 'Bagels on the Hudson',
'Qdoba', 'Chipotle', 'Midtown', 'Mr. Wraps', 'Pizza Republic', 'Gio\'s']

midTier = ['Makai', 'Napoli\'s', 'Flatbread', 'Gogi Grill', 'Vivi\'s', 'Chicken Factory',
'Cluck U', 'Panera', 'Honeygrow', 'South Street']

sTier = ['Karma', 'Rice Shop', 'Bareburger', 'Johnny Rockets', 'Ubu', 'Ali Baba',
'Charrito\'s']

# Vito's can be in basic or next tier

# Mill's Tavern on Wednesday, special occasion
print('What kind of place would you like to eat at?')
print('Options:')
print('\tall: displays a list of all restaurants')
print('\tbasic: chooses a random restaurant from the basic tier')
print('\tmid: chooses a random restaurant from the mid tier')
print('\ts: chooses a random restaurant from the s tier')
print('\texit: closes the program')
print('\toptions: displays list of options again')

while True:
    choice = input('Choice: ')
    if choice == 'all':
        for x in allRestaurants:
            print(x)
    elif choice == 'basic':
        print(basicTier[random.randint(0,len(basicTier) - 1)])
    elif choice == 'mid':
        print(midTier[random.randint(0,len(midTier) - 1)])
    elif choice == 's':
        print(sTier[random.randint(0,len(sTier) - 1)])
    elif choice == 'exit':
        sys.exit()
    elif choice == 'options':
        print('Options:')
        print('\tall: displays a list of all restaurants')
        print('\tbasic: chooses a random restaurant from the basic tier')
        print('\tmid: chooses a random restaurant from the mid tier')
        print('\ts: chooses a random restaurant from the s tier')
        print('\texit: closes the program')
        print('\toptions: displays list of options again')
    else:
        print("Not an option")