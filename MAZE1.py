import turtle
import math
import random

#Create window
win = turtle.Screen()
win.bgcolor("Black")
win.title("aMAZEing")
win.setup(700,700)
win.tracer(0)

#Register shapes
images = ["player_right.gif", "player_left.gif", "TREASURE.gif",
          "BLOCK.gif", "enemy_left.gif", "enemy_right.gif"]
for image in images:
    turtle.register_shape(image)

#Create Pen - pen can do anything that the turtle can do
class TPen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("BLOCK.gif")
        self.color("white")
        self.penup()                #move the turtle without drawing anything
        self.speed(0)               #animation speed - speed is zero (the fastest)

#Add the player
class TPlayer(turtle.Turtle):
    def __init__(self):
        turtle. Turtle.__init__(self)
        self.shape("player_right.gif")
        self.color("green")
        self.penup()
        self.speed(0)
        self.gold = 0

    #To move the player
    def go_up(self):
        move_to_x = Player.xcor()         #Calculate the spot to move to
        move_to_y = Player.ycor() + 24
        if (move_to_x, move_to_y) not in walls:        #Check if the space has a wall
             self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = Player.xcor()
        move_to_y = Player.ycor() - 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = Player.xcor() + 24
        move_to_y = Player.ycor()

        self.shape("player_right.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = Player.xcor() - 24
        move_to_y = Player.ycor()

        self.shape("player_left.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

#Adding treasure
class treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("TREASURE.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
    def destroy(self):
        self.goto(2000,2000)    #Remove the object/turtle off the screen
        self.hideturtle()       #Hide or make the turtle invisible

#Adding enemy
class enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("enemy_left.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])
    #Movement of the enemy
    def move(self):
        if self.direction == "up":
            dx = 24
            dy = 0
        elif self.direction == "down":
            dx = 24
            dy = 0
        elif self.direction == "left":
            dx = -24
            dy = 0
            self.shape("enemy_left.gif")
        elif self.direction == "right":
            dx = 24
            dy = 0
            self.shape("enemy_right.gif")
        else:
            dx = 0
            dy = 0

        #Calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        #Check if there is a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #Choose a different direction
            self.direction = random.choice(["up", "down", "left", "right"])
        #Set timer to move next time
        turtle.ontimer(self.move, t = random.randint(100, 300))

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

#Create diferent sets
sets = [""]

#First set
set_1 = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[8,0,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1],
[1,1,0,0,1,1,1,1,1,0,1,1,3,0,0,0,0,0,0,0,0,7,1,1],
[1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,0,0,1],
[1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,0,0,1],
[1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1],
[1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,7,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1],
[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1],
[1,1,1,0,1,0,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,1],
[1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1],
[1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1],
[1,0,1,1,1,0,0,1,1,0,0,1,0,0,1,1,1,0,0,1,1,1,1,1],
[1,0,0,1,1,0,0,1,1,0,0,1,1,0,1,1,1,1,0,0,1,1,1,1],
[1,1,0,0,0,0,1,1,1,0,0,1,1,0,0,0,1,1,0,0,0,7,1,1],
[1,7,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,0,0,1,0,0,1],
[1,1,0,0,1,1,0,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1],
[1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,0,1],
[1,0,0,0,0,1,1,1,1,1,1,1,3,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1],
[1,0,0,3,0,0,0,0,0,0,0,7,1,1,1,1,1,1,0,1,0,0,0,1],
[1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,1],
[1,0,0,0,0,0,1,1,1,1,1,1,1,7,0,1,1,0,0,0,0,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1]
 ]

#Add a treasures list
Treasures = []

#Add enemies list
enemies = []

#Add maze to the list of mazes
sets.append(set_1)

#Create Setup Function
def setup(set):
    for y in range(len(set)):
        for x in range(len(set[y])):
            c = set [y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            #1 represents the walls
            if c == 1:
                Pen.goto(screen_x, screen_y) #goto() - move the turtle to position x,y
                Pen.stamp()   #stamp() - leaves an impression of a turtle shape at the current location
                walls.append((screen_x, screen_y))  #Add coordinate pairs in the walls
            #8 represents the player
            if c == 8:
                Player.goto(screen_x, screen_y)
            #7 represents treasure
            if c == 7:
                Treasures.append(treasure(screen_x, screen_y))
            #3 represents the enemy
            if c == 3:
                enemies.append(enemy(screen_x, screen_y))

#Create class instances
Pen = TPen()
Player = TPlayer()

#Create wall coordinate list
walls = []

#Setup the first set of the maze
setup(sets[1])

#Keyboard Binding
turtle.listen()                         # listen() method sets focus on the turtle screen to capture events.
turtle.onkey(Player.go_left, "Left")    #onkey() method invokes the method specific to the captured keystroke. The first argument of onkey() is the function to be called and the second argument is the key.
turtle.onkey(Player.go_right, "Right")
turtle.onkey(Player.go_up, "Up")
turtle.onkey(Player.go_down, "Down")

#Turn off screen updates
win.tracer(0)

#Start moving enemies
for enemy in enemies:
    turtle.ontimer(enemy.move, t = 250)     #Tell the enemy to move after 250 milliseconds

#Main game loop
while True:
    #Check for the collision of Player with Treasure
    for treasure in Treasures:
        if Player.is_collision(treasure):
            Player.gold += treasure.gold                    #Add treasure gold to the player gold
            print ("Gold collected: {}".format(Player.gold))
            treasure.destroy()                              #Destroy the treasure
            Treasures.remove(treasure)                      #Remove treasure from the list

    #Iterate through enemy list to see if the player collide
    for enemy in enemies:
        if Player.is_collision(enemy):
            print("You lose!")

    win.update()





