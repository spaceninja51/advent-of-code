# Create a class used to represent an individual round of the game
class Round {
    [int] $red
    [int] $green
    [int] $blue
    [int] $total
}

#initialize variables
$gameID, $answer = 0
# set desired red, green, and blue maximum values
$rmax = 12
$gmax = 13
$bmax = 14
$tmax = $rmax + $gmax + $bmax

# data to be processed
$text = Get-Content "C:\Users\cwg24\OneDrive\Desktop\Nerd Shit\Scripting\Advent-of-Code-2023\Day 2\Input.txt"

# Iterate through each line of the input text and break the line into the two strings made of the text on either side of :
foreach ($line in $text.Split([Environment]::NewLine, [StringSplitOptions]::RemoveEmptyEntries)) {
    
    $invalid = 0
    $lineText = $line.Split(":")
    
    foreach($pull in $lineText[1].Split(";")) {
        # create a new round object after each ;
        $round = [Round]::new()
        
        foreach ($count in $pull.Split(",").Trim()) {
            # check the number to be set
            [int] $countNo = $count.Split(" ")[0].Trim()

            # find the color the number goes to and set it
            $countColor = $count.Split(" ")[1].Trim()
            switch ($countColor) {
                "red" {
                    $round.red = $countNo
                    if ($countNo -gt $rmax) {
                        $invalid = 1
                    }
                    break
                }
                "green" {
                    $round.green = $countNo
                    if ($countNo -gt $gmax) {
                        $invalid = 1
                    }
                    break
                }
                "blue" {
                    $round.blue = $countNo
                    if ($countNo -gt $bmax) {
                        $invalid = 1
                    }
                    break
                }
            }
        }
        # calculate total cubes shown in a round
        $round.total = $round.red + $round.green + $round.blue
        if ($round.total -gt $tmax) {
            $invalid = 1
        }
    }

    # checks whether a game (line) has been marked as invalid, if it hasn't add that game's ID to a running total
    switch ($invalid) {
        0 {
            $gameID = $lineText[0] -replace '[a-zA-Z]',''
            $answer += $gameID
            break
        }
        1 {
            break
        }
    }

}
$answer