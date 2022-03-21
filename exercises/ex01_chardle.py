"""EX01 - Chardle - A cute step towards Wordle."""
_author_ = "730520918"
count: int = 0
word_inp: str = input("Enter a 5-character word: ")
if len(word_inp) != 5:
    print("Error: Word must contain 5 characters")
    exit()
letter_inp: str = input("Enter a single character: ")
if len(letter_inp) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter_inp + " in " + word_inp)
if letter_inp == word_inp[0]:
    print(letter_inp + " found at index 0")
    count = count + 1
if letter_inp == word_inp[1]:
    print(letter_inp + " found at index 1")
    count = count + 1
if letter_inp == word_inp[2]:
    print(letter_inp + " found at index 2")
    count = count + 1
if letter_inp == word_inp[3]:
    print(letter_inp + " found at index 3")
    count = count + 1
if letter_inp == word_inp[4]:
    print(letter_inp + " found at index 4")
    count = count + 1
if count > 1:
    print(str(count) + " instances of " + letter_inp + " found in " + word_inp)
elif count == 0:
    print("No instances of " + letter_inp + " found in " + word_inp)
elif count == 1:
    print(str(count) + " instance of " + letter_inp + " found in " + word_inp)
