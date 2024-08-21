""" Day 2-1
Given Rock, Paper, Scissors strategy guide made of Opponent - Player combos

First column: Opponent
Second column: Player
Score is determined by adding: player selection + round outcome

Given example:
    A Y
    B X
    C Z

Expect: 8 + 1 + 6 = 15

What is the score using the input?
"""
file = "./2022/2/ex.txt"
content = open(file)
total = int(0)
round = int(0)
opponent = {
    "A" : "Rock",
    "B" : "Paper",
    "C" : "Scissors"
}
player = {
    "X" : "Rock",
    "X\n" : "Rock",
    "Y" : "Paper",
    "Y\n" : "Paper",
    "Z" : "Scissors",
    "Z\n" : "Scissors"
}
score = {
    "Rock" : int(1),
    "Paper" : int(2),
    "Scissors" : int(3),
    
    "W" : int(6),
    "T" : int(3),
    "L" : int(0)
}

for i, line in enumerate(content):
   
   pchoice = ""
   ochoice = ""
   outcome = ""

   round = line.split(" ")
   
   ochoice = opponent[round[0]]
   pchoice = player[round[1]]

   if ochoice == pchoice:
      outcome = "T"
   elif ochoice == "Rock" and pchoice == "Paper":
      outcome = "W"
   elif ochoice == "Paper" and pchoice == "Scissors":
      outcome = "W"
   elif ochoice == "Scissors" and pchoice == "Rock":
      outcome = "W"
   else:
      outcome = "L"

   roundScore = score[pchoice] + score[outcome]
   
   total += roundScore

print("Part 1 Solution: ",total)

# Part 2

i = 0
line = ""

goal = {
   "X" : "L",
   "X\n" : "L",
   "Y" : "T",
   "Y\n" : "T",
   "Z" : "W",
   "Z\n" : "W"
}

for i, line in enumerate(content):
   
   pchoice = ""
   ochoice = ""
   outcome = ""

   round = line.split(" ")

   ochoice = opponent[round[0]]
   outcome = goal[round[1]]

   if outcome == "T":
      pchoice = ochoice
   elif ochoice == "Rock":
      match outcome:
         case "L":
            pchoice = "Scissors"
         case "W":
            pchoice = "Paper"
   elif ochoice == "Paper":
      match outcome:
         case "L":
            pchoice == "Rock"
         case "W":
            pchoice == "Scissors"
   elif ochoice == "Scissors":
      match outcome:
         case "L":
            pchoice == "Paper"
         case "W":
            pchoice == "Rock"
   else:
      print("fart")

   print("Round ",i+1,'\n',"Opponent Picked: ",ochoice,'\n',"Wanted Outcome: ",outcome,'\n',"Player Should Pick: ",pchoice,)

content.close()