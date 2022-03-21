"""Examples of using lists in a simple game."""

from random import randint

rolls: list[int] = list()  
# function call setting up empty list

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

print(rolls) 

# removing an item from the list, use "pop"
rolls.pop(len(rolls) - 1)
print(rolls)

# sum the values of the rolls
i: int = 0
sum: int = 0

while i < len(rolls):
    sum += rolls[i]
    i += 1
print(sum)


# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))

# #access individual item
# print(rolls[0])

# #acces length of list

# print(len)