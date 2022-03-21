"""This is the updated Wordle Game."""
__author__: str = "730530918"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, char: str) -> bool:
    """Checks for character in word."""
    assert len(char) == 1
    i: int = 0 
    while i < len(word):
        if word[i] == char:
            return True
        i = i + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Checks for the correct location or presence of letter in secret."""
    assert len(guess) == len(secret)
    i: int = 0
    emoji: str = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji = emoji + GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
        i = i + 1
    return emoji


def input_guess(expected_length: int) -> str:
    """This is the function that makes sure the guess works."""
    i: int = 0
    guess: str = (input(f"Enter a {expected_length} character word: "))  
    while i < 1:
        if len(guess) != expected_length:
            guess: str = input(f"That wasn't {expected_length} chars! Try again: ")
        else:
            i = i + 1
    return guess


def main() -> None:
    """The entry point of the program and main game loop."""
    secret: str = "snarf"
    turn_number: int = 0
    max_turns: int = 6
    while turn_number < max_turns:
        print(f"=== Turn {turn_number + 1}/{max_turns} ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn_number + 1}/{max_turns} turns!")
            return
        else:
            turn_number += 1
    if turn_number == max_turns:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")
        return