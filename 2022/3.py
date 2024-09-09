# opens the input file and iterates through each line
with open("advent-of-code/2022/in/3.txt",'rt') as input:
# File
    unsorted = []
    priorities = []
    for bag in input:
    # Line

        compartments = []
        # removes new line character (all whitespace)
        # and tracks lengh of the line
        bag = bag.strip()
        length = len(bag)
        # divides the line in half, setting the first half
        # one compartment and the second as the other
        compartments.append(bag[:(length//2)])
        compartments.append(bag[(length//2):])
        # loop through the letters of compartment 0 and check
        # for them in compartment 1. Stores the letter once found
        for letter in compartments[0]:
        # Character

            # .find() returns -1 if the thing is not found, if anything
            # else is returned, its the dupe
            if not compartments[1].find(letter) == -1:
                dupe = letter
        # function now finds the unsorted character of all bags, each stored as
        # a separate entry in the list 'unsorted'
        unsorted.append(dupe)
        # Finding priority values by translating the unicode value for a given letter
        # to the value desired by the puzzle. 
        # Unicode a-z: 97-122, A-Z: 85-90 
        # Desired a-z: 1-26, A-Z: 27-52
        # Translation a-z: -96, A-Z: -38
        if dupe.isupper():
            translation = -38
        elif dupe.islower():
            translation = -96
        # Shifts the numeric value of the letter according to the desired values, then
        # adds it to the list of converted values
        priority = translation + ord(dupe)
        priorities.append(priority)

answer1 = int(0)
for value in priorities:
    answer1 += int(value)

print(answer1)