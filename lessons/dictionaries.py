"""Demonstrations of dictionary capabilities."""


# Declare type of dictionary
schools: dict[str, int]

# initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["Wesleyan"] = 3200

# print a dictionary literal representation
print(schools)


# Access a value by its key
print(schools['UNC'])

# Remove a key-value pair from a dictionary
# by its key
schools.pop("Duke")


# Test for existance of a key

is_duke_present: bool = "Duke" in schools
print(f"Is Duke present: {is_duke_present}")

# Update or reassign a key-value pair
schools['UNC'] = 20000
schools['Wesleyan'] = schools["Wesleyan"] + 200

print(schools)

# demostration of dicitonary literals

schools = {} # Same as dict()

# Alterntively, initialize values

schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}

# Printing a key not in the dictinoary

# print(schools["UNCC"])

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")