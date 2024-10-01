# opens the input file and iterates through each line
with open("2022/in/3.txt",'rt') as input:
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

print("Part 1 Solution:",answer1)

# Day will be the day (1-31), part will be per day (1 or 2), example says whether to use
# the example imput (1 or 0)
def aoc22(day = 3, part = 2, useExample = 1):
    useExample = True
    match useExample:
        case True:
            mode = "ex"
        case False:
            mode = "in"
    path = "2022/"+str(mode)+"/"+str(day)+".txt"

# Opens the input file
with open('2022/in/3.txt','rt') as input:
    group = []
    answer2 = 0
    i = 1
    # Iterates through each line of the input
    for elf in input:
        group.append(elf.replace('\n',""))
        i += 1
        # We have 3 grouped together
        if i > 3:
            pool = ""
            tag = ""
            for bag in group:
                badges = ""
                for badge in bag:
                    # Lists the unique letters in each line as badges
                    if badges.find(badge) == -1:
                        badges += badge
                # Adds each list of letters to a pool for the current group
                pool += badges
            # Find the letter that appears 3 times, and set the group's tag
            # to that letter
            for letter in pool:
                if pool.count(letter) >= 3 and letter != tag:
                    tag = letter
            # Finding priority values by translating the unicode value for a given letter
            # to the value desired by the puzzle. 
            # Unicode a-z: 97-122, A-Z: 85-90 
            # Desired a-z: 1-26, A-Z: 27-52
            # Translation a-z: -96, A-Z: -38
            if tag.isupper():
                translation = -38
            elif tag.islower():
                translation = -96
            answer2 += (ord(tag) + translation)
            # Reset for next group
            group.clear()
            i = 1
    print("Part 2 Answer:",answer2)