"""Guessing a 6 letter word!"""
__author__ = "730520918"
secret: str = "python"
i: int = 0
yellow: bool = False
emoji: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
guess: str = (input(f"What is your {len(secret)}-letter guess? "))
while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")
while i < len(guess):
    x: int = 0
    yellow = False
    if guess[i] == secret[i]: 
        emoji = emoji + GREEN_BOX
    elif not yellow:
        while x < len(guess):
            if guess[i] == secret[x]:
                emoji = emoji + YELLOW_BOX
                yellow = True
            x = x + 1  
        if not yellow:
            emoji = emoji + WHITE_BOX
    i = i + 1
print(emoji)
if guess == secret:
    print("Woo! You got it")
else:
    print("Not quite. Play again soon!")