#### CS 110
# Midterm - Python Programming

***

_Replace anything surrounded by the `< >` symbols._

## SUMMARY:
What did you clean up?:
I fixed my setUpDartboard() function to properly set up the dartboard using the other functions. Also fixed my isInCircle() function to properly detect if it is within the circle's radius using the turtle.distance() function. I also updated the drawCircle() function to add a "center" component to be able to draw different circles with different center points and the throwDart() function to change the amount of darts throw and what color the dart will be on the dartboard. Also fixed some syntax errors for increment variables.

Summary of function(s) added:
setUpProfessionalDartboard():
Uses the standard setUpDartboard() function but then adds a double value, triple value, and bullseye circle with corresponding labels for a more accurate dartboard look for use within the new feature

calculateScore():
Uses turtle.distance() function to determine the score of a dart throw within the new and improved dart game feature. Darts throw within the outer ring are 2 points, middle ring is 3 points, bulleyes is 5 points, and anywhere else is 1 points. Outside of the entire dartboard is 0 points and returns the point value

playGame():
Uses the new setUpProfessionalBoard() and calculateScore() functions along with improved throwDart() function to play a new and improved version of the dart game from Part B of Lab 5 with better scoring, player names, and more interaction from the user

Summary of Feature Added:
The new feature is the playGame() function which is essentially a vastly improved dart throwing game that is similar to Part B of Lab 5. Function takes screen, turtle, and player inputs to create the new professional looking dartboard using the current turtle and the amount of players to initialize the game for a varying amount of players (between 1 and 7 players allowed).

Begins by drawing the professional dartboard using the drawProfessionalDartboard() function and then asks the user to input the names of each player and saves it to an empty list. It then gives the instructions to the user and waits 5 seconds using time.sleep(5) to allow the players time to read the instructions before the game begins. It then loops through multiple nested for loops to throw 3 darts, calculates the score and saves it to the current player's score value in playerScores list. It throws 3 darts for every player for 5 rounds, using different colors for each player, and continuously saves the scores each time the dart is thrown. Scores are calculated using the calculateScore() function which returns the integer value of the score. Once all 5 rounds are completed, it then sorts through the playerScores[] list to check for the highest score and saves the index of the highest score to the indexOfMaximum variable. Using this variable, it then prints the corresponding player's name from playerNames list and their score as they are the winner of the game.

## KNOWN BUGS AND INCOMPLETE PARTS:
 < What parts of the project you were not able to complete >
 No known bugs, but I am unsure of how to account for ties between x amount of people in my playGame() feature.

## REFERENCES:
 < List any outside resources used >
time library for a time delay
## MISCELLANEOUS COMMENTS:
 < Anything you would like the grader to know 
  Please let me know if there is any way to effectively account for ties in scores, I am desperately trying to figure it out
