# initialize variables
compartments = ["",""]
contents = []
dupe = ""
unsorted = []

# opens the input file and iterates through each line
with open("2022/ex/3.txt",'rt') as input:
    for bag in input:
        # removes new line character (all whitespace)
        # and tracks lengh of the line
        bag = bag.strip()
        length = len(bag)
        # divides the line in half, setting the first half
        # one compartment and the second as the other
        compartments[0] = bag[:(length//2)]
        compartments[1] = bag[(length//2):]
        # loop through the letters of compartment 0 and check
        # for them in compartment 1. Stores the letter once found
        for letter in compartments[0]:
            # .find() returns -1 if the thing is not found, if anything
            # else is returned, its the dupe
            if not compartments[1].find(letter) == -1:
                dupe = letter
        unsorted.append(dupe)
    
    # function now finds the unsorted character of all bags, each stored as
    # a separate entry in the list 'unsorted'
    print(unsorted)