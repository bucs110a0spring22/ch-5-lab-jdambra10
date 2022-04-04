'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################
def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  myturtle.up()
  myturtle.goto(top_left_x, top_left_y)
  myturtle.down()
  for i in range(4):
    myturtle.forward(width)
    myturtle.right(90)
  myturtle.up()

def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
  myturtle.goto(x_start, y_start)
  myturtle.down()
  myturtle.goto(x_end, y_end)
  myturtle.up()
  

def drawCircle(myturtle=None, radius=0, center = -1):
  myturtle.goto(0,center)
  myturtle.down()
  myturtle.circle(radius)
  myturtle.up()

def setUpDartboard(myscreen=None, myturtle=None):
  myscreen.setworldcoordinates (-2, -2, 2, 2) ##added by TA
  drawSquare(myturtle, 2, -1, 1)
  drawLine(myturtle, -1, 0, 1, 0)
  drawLine(myturtle,0,-1,0,1)
  drawCircle(myturtle, 1)

def isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0):
  distance = myturtle.distance(circle_center_x,circle_center_y)
  if (distance<=radius):
    return True
  else:
    myturtle.down()
    myturtle.dot(5, "orange")
    myturtle.up()
    return False

def throwDart(myturtle=None, darts=1, color="blue"):
  for d in range(darts):
    x_value = random.uniform(-1, 1)
    y_value = random.uniform(-1, 1)
    myturtle.goto(x_value, y_value)
    myturtle.down()
    myturtle.dot(5, str(color))
    myturtle.up()

def playDarts(myturtle=None):
  p1Points = 0
  p2Points = 0
  for i in range(10):
    #Player 1's Turn
    throwDart(myturtle)
    if isInCircle(myturtle, radius=1):
      p1Points+=1

    #Player 2's Turn
    throwDart(myturtle)
    if isInCircle(myturtle, radius=1):
      p2Points+=1

  if p1Points > p2Points:
    print("Player 1 Wins!")
  elif p1Points < p2Points:
    print("Player 2 Wins!")
  else:
    print("Players are tied! You both win!")

def montePi(myturtle=None, num_darts=0):
  inside_count = 0
  for i in range(num_darts):
    throwDart(myturtle)
    if isInCircle(myturtle, radius = 1):
      inside_count+=1   
  pi_approximation = (inside_count / num_darts) * 4 
  print(inside_count, num_darts)
  return pi_approximation

def setUpProfessionalDartboard(myscreen=None, myturtle=None):
  setUpDartboard(myscreen, myturtle)
  drawCircle(myturtle,.9,-.9)
  myturtle.write("x2",False,align="center")
  drawCircle(myturtle,.5,-.5)
  drawCircle(myturtle,.4,-.4)
  myturtle.write("x3",False,align="center")
  drawCircle(myturtle,.1,-.1)
  myturtle.write("x5",False,align="center")

def calculateScore(myturtle=None):
  distance = myturtle.distance(0,0)
  if (distance > 1):
    return 0
  elif (distance >= 0.9):
    return 2 
  elif(distance >= 0.5):
    return 1
  elif(distance >= 0.4):
    return 3
  elif(distance >= 0.1):
    return 1
  else:
    return 5


def playGame(myscreen=None, myturtle=None, players=1):
    if players >= 7:
      print("Too many players! Try again with 7 or less players.")
      return
    setUpProfessionalDartboard(myscreen, myturtle)
    colorList = ["blue", "orange", "purple", "green", "red", "yellow", "pink"]
    playerNames = []
    playerScores = [0] * players
    length = len(playerScores)
    for p in range(players):
      playerNames.append(str(input("Please input Player " + str(p+1) + "'s name: '")))
    instructions = "Players will take turns throwing 3 darts per round for 5 rounds. Player with the most points wins!"
    print(instructions)
    time.sleep(5)
    for r in range(5):
      for s in range(players):
        for d in range(3):
          throwDart(myturtle,1,colorList[s])
          playerScores[s] += calculateScore(myturtle)
    indexOfMaximum = 0
    maximum = 0
    for i in range(length):
      if playerScores[i] > maximum:
        maximum = playerScores[i]
        indexOfMaximum = i
    print("The winner is " + str(playerNames[indexOfMaximum]) + " with a total of " + str(playerScores[indexOfMaximum]) + " points!")
    
  
  

#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(myscreen=window, myturtle=darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
        if isInCircle(myturtle=darty, radius=1):
          print("You hit the dartboard!")
        else:
          print("You missed...")
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(myscreen=window, myturtle=darty)
    playDarts(myturtle=darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(myscreen=window, myturtle=darty)
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(myturtle=darty, num_darts=number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    print("=========== Dart Game ===========")
    darty.clear()
    playGame(window, darty, players=2)
    window.exitonclick()


main()
