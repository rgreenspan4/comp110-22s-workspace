"""An oracle that predicts the future."""

from random import randint

input("Ask a yes/no question: ")

response: int = randint(0, 3)

if response == 0:
    print("Most definitieyl")
else:
    if response == 1:
        print("maybe")
    else:
        if response == 2:
            print("No chance")
        else: 
            print("Stop asking)")
