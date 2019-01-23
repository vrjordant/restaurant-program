''' A restaurant program that chooses a random restaurant in Hoboken 
    Created by Jordan Tantuico 1/12/2019
    Last edited 1/23/2019 '''
import random, sys, datetime

# Benny's was excluded for a reason lol
basicTier = ['Mamoun\'s', 'McDonald\'s', 'Pita Pit', 'O\'bagel', 'Bagels on the Hudson',
'Qdoba', 'Chipotle', 'Midtown', 'Mr. Wraps', 'Pizza Republic', 'Gio\'s']

midTier = ['Makai', 'Napoli\'s', 'Flatbread', 'Gogi Grill', 'Vivi\'s', 'Chicken Factory',
'Cluck U', 'Panera', 'Honeygrow', 'South Street', 'Koro Koro']

sTier = ['Karma', 'Rice Shop', 'Bareburger', 'Johnny Rockets', 'Ubu', 'Ali Baba',
'Charrito\'s']

special = ['Vito\'s', 'Mill\'s']

# Vito's can be in basic or next tier
vitos = False
mills = False
day = int(datetime.date.today().strftime("%w"))
time = datetime.datetime.now().hour
if day >=2 and day <=4 and time >= 14 and time <= 18:
    basicTier.append('Vito\'s')
    vitos = True
else:
    midTier.append('Vito\'s')

if day == 3 or day == 4:
    mills = True

print('What kind of place would you like to eat at?')
print('Options:')
print('\ta: displays a list of all restaurants')
print('\tb: chooses a random restaurant from the basic tier')
print('\tm: chooses a random restaurant from the mid tier')
print('\ts: chooses a random restaurant from the s tier')
print('\te: closes the program')
print('\to: displays list of options again')
print('\tsp: displays the current specials')

while True:
    choice = input('Choice: ')
    if choice == 'a':
        print("Basic:")
        for x in basicTier:
            print("\t" + x)
        print("Mid:")
        for x in midTier:
            print("\t" + x)
        print("S:")
        for x in sTier:
                print("\t" + x)
        print("Special:")
        for x in special:
            print("\t" + x)
    elif choice == 'b':
        print(basicTier[random.randint(0,len(basicTier) - 1)])
    elif choice == 'm':
        print(midTier[random.randint(0,len(midTier) - 1)])
    elif choice == 's':
        print(sTier[random.randint(0,len(sTier) - 1)])
    elif choice == 'e':
        sys.exit()
    elif choice == 'o':
        print('Options:')
        print('\ta: displays a list of all restaurants')
        print('\tb: chooses a random restaurant from the basic tier')
        print('\tm: chooses a random restaurant from the mid tier')
        print('\ts: chooses a random restaurant from the s tier')
        print('\te: closes the program')
        print('\to: displays list of options again')
        print('\tsp: displays the current specials')
    elif choice == "sp":
        if vitos:
            print('Vito\'s is having a special right now!')
        if day == 3:
            print("Mill\'s has $9.99 all you can eat wings!")
        elif day == 4:
            print("Mill\'s has $2 tacos!")
        if not mills and not vitos:
            print("No specials at this time.")
    else:
        print("Not an option")
