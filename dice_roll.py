import random
import re


# Odkodowanie podanego kodu rzutu
def throw_decode(data):
    allowed_dice = [3, 4, 6, 8, 10, 12, 20, 100]
    dice = int(re.search(r'k\d*', data).group()[1:])
    if dice in allowed_dice:
        if data[0] != 'k':
            throws = int(re.search(r'\d*k', data).group()[:-1])
        else:
            throws = 1
        if '+' in data:
            mod = int(re.search(r'\+\d*', data).group()[1:])
        else:
            mod = 0
        return [throws, dice, mod]
    else:
        return [0, 0, 0]


# Wykonanie rzutu zgodnie z instrukcją z throw_decode
def roll(code):
    roll_data = throw_decode(code)
    rolls = [random.randint(1, roll_data[1]) for i in range(0, roll_data[0])]
    return sum(rolls) + roll_data[2]


# Testy

a = '3k8+2'
b = '20k12+10'
c = 'k12'
d = '5k100'

print(roll(a))
print(roll(b))
print(roll(c))
print(roll(d))
