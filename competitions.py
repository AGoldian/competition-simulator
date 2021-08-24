from numpy import arange
import random
from math import ceil

# code for emulating competitions with different difficulty levels
# we will add the levels of the competition and their difficulty coefficient to the dictionary
lvl_compt = {
    'street': [0.95, 0.0375, 0.0125, 0, 0],
    'town': [0.6, 0.3, 0.1, 0, 0],
    'city': [0.1, 0.3, 0.5, 0.1, 0],
    'region': [0, 0.1, 0.6, 0.2, 0.05],
    'country': [0, 0, 0.2, 0.6, 0.2],
    'world': [0, 0, 0, 0.2, 0.8],
    'olympic': [0, 0, 0, 0.1, 0.9]
}

# we request the necessary data to run the program

# we catch the error by checking the entered value with valid keys from the mode dictionary
while True:
    user_lvl = input('Select the level of competition - Street, Town, City, Region, Country, World, Olympic:\n').lower()
    if user_lvl in lvl_compt:
        break
    else:
        print('You have entered the wrong mode, please try again')

# сatching the error by checking against two values
while True:
    mode = input('Select mode - time, point:\n').lower()
    if mode == 'time' or 'point':
        break
    else:
        print('You have entered the wrong mode, please try again')

# only a digital value is needed, check with float()
while True:
    qual = input('Enter the time of the qualifying stage (if not, then the worst result):\n')
    try:
        float(qual)
    except ValueError:
        print('Enter a numerical value')
        continue
    break
while True:
    record = input('Enter the record figure (if not, then the maximum possible):\n')
    try:
        float(record)
    except ValueError:
        print('Enter a numerical value')
        continue
    break
while True:
    players = int(input('Enter the number of participants:\n'))
    try:
        float(players)
    except ValueError:
        print('Enter a numerical value')
        continue
    break

# create lists for time and points mode
if mode == 'time':
    scale = [round(num, 2) for num in arange(float(qual) * 1.01, float(record) * 0.99, -0.01)]
else:
    scale = [i for i in range(round(int(qual) * 0.99), round(int(record) * 1.01))]


def Generating(stage):
    """
    The function generates 5 sublists of equal size from the general list.
    """
    n = ceil(len(stage) / 5)
    for i in range(0, len(stage), n):
        dip = stage[i:i + n]

        if len(dip) < n:
            dip += [None for q in range(n - len(dip))]
        yield dip


def Choice(scale_dip):
    """
     The function selects a random number from a shuffled list, which, in turn,
     was selected at random using the weights specified in the parameters.
    """
    weights = lvl_compt[user_lvl]
    lst = random.choices(scale_dip, weights=weights)[0]
    random.shuffle(lst)
    return random.choices(lst)


# randomly simulate the user's place in the competition
user_place_in_compt = random.randint(1, players)

# create a list for the results of the opponents
resultation = []

# we create a competition using a loop,
# while the user will have to enter his result in real time, depending on his performance position
for i in range(1, players + 1):
    if i == user_place_in_compt:
        user_score = float(input('Enter your result: '))
    else:
        tmp = Choice(list(Generating(scale)))[0]
        # fix the bug as "not a bug but a feature"
        if tmp is None:
            print(f'Player {i} is disqualified')
            players -= 1
        else:
            print(f'Opponent Result №{i} - {tmp}')
            resultation.append(tmp)

final_point = 0

# scoring algorithm for different modes
if mode == 'point':
    for j in resultation:
        if j <= user_score:
            final_point += 1
else:
    for j in resultation:
        if j >= user_score:
            final_point += 1

print(f'You took {players - final_point} place')
