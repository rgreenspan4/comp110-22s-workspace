"""For_in loop practice."""


names: list[str] = ["robby", "tommy", "cullen", "amir"]

i: int =0 
while i < len(names):
    print(names[i])
    i += 1

for name in names:
    print(name)
    
    