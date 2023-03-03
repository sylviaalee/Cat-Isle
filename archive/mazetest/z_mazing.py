#Created on Wed Jul 29 17:47:30 2020
# Part 1 - Set Up Maze
import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Z Mazing")
wn.setup(700, 700)
#wn.tracer(0)
#register shapes
turtle.register_shape('wall.gif')
turtle.register_shape('player.gif')
turtle.register_shape('piggy.gif')
turtle.register_shape('coin.gif')

# Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")     #this is an attribute 
        self.color("white")
        self.penup() 
        self.speed(0)

#create player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('player.gif')
        self.color('black')
        self.penup()
        self.speed(0)
        self.gold = 0
        
    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() +24
        if(move_to_x, move_to_y)not in walls:
            self.goto(move_to_x, move_to_y)
        
    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() -24
        if(move_to_x, move_to_y)not in walls:
            self.goto(move_to_x, move_to_y)
            
    def go_left(self):
        move_to_x = player.xcor() -24
        move_to_y = player.ycor()
        if(move_to_x, move_to_y)not in walls:
            self.goto(move_to_x, move_to_y)
            
    def go_right(self):
        move_to_x = player.xcor() +24
        move_to_y = player.ycor()
        if(move_to_x, move_to_y)not in walls:
            self.goto(move_to_x, move_to_y)


    def collide(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        #Dr.Z is as cool as he thinks he is
        #calculate distance between two objects
        distance = math.sqrt((a ** 2) + (b ** 2)) 
        if distance < 5:
            return True
        else:
            return False
        
        
    
#create treasure
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape('coin.gif')
        self.color('yellow')
        self.penup()
        self.speed(0)
        self.gold = 5
        self.goto(x, y)

    def destroy(self):
        self.hideturtle()


#create enemy
class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape('piggy.gif')
        self.color('red')
        self.penup()
        self.speed(0)
        self.gold = 5
        self.goto(x, y)
        self.direction = random.choice(['up', 'down', 'left', 'right'])
                   
    def move(self):
        if self.direction == 'up':
            dx = 0                    # d = delta = change triangle
            dy = 24
        elif self.direction == 'down':
            dx = 0
            dy = -24
        elif self.direction == 'left':
            dx = -24
            dy = 0
        elif self.direction == 'right':
            dx = 24
            dy = 0 
        else:
            dx = 0
            dy = 0
        
        # calculate enemy movement
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy
        
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
        else:
            #choose different direction for enemy
            self.direction = random.choice(['up', 'down', 'left', 'right'])
            
        # enemy movement intervals
        turtle.ontimer(self.move, t = random.randint(100, 300))
        
    def nearby(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        
        if distance < 75:
            return True
        else:
            return False
        
#Create Levels List
levels = [""]  # Empty Level


#Define firts level
#level_1 = [

#"XXXXXXXXXXXXXXXXXXXXXXXXX",   # 600x600 = playing area
#"X Z XXXXXXX          XXXX",   # Sprites = 24 x 24
#"X  XXXXXXX  XXXXXX   XXXX",   # grid = 25 x 25 
#"X  XXXXXXX  XXXXXX   XXXX",
#"X  XXXXXXX  XXX        XX",   # Top Left Block: -288, 288  
#"XXXXXX  XX  XXX      XXXX",   # Top Right Block: 288, 288
#"XXXXXX  XX  XXXXXX   XXXX",   # Bottom  Left Block: -288, -288 
#"XXXXXX  XX  XXXXXX   XXXX",   # Bottom Right Block: 288, -288 
#"X XXXXXXXXXXXXXXXXXXXXXXX",
#"X XXXXXXXXXXXXXXXXXXXXXXX",
#"XXXXXXXXXXXX   XXXXXXXXXX",
#"XXXXXXXXXXXXXXXXXXXXXXXXX",
#"XXXXXXXXXXXXXXXXXXXXXXXXX",
#"XXXXXXXXXX   XXXXXXXXXXXX",
#"XXXXXXXXXXXXXXXXXXXXXXXXX",
#"XXX   XXXXXXXXXXXXXXX XXX",
#"XXXXXXXXXXX  XXXXXXXXXXXX",
#"XXXXXXXXXXXXXXXXXXXXXXXXX",
#"XXXXXXXXX  XXXXXXXXXX XXX",
#"XXXXXXXXXXXXXXXXXXXXXXXXX",
#"XXX XXXXXXX  XXXXXXXXXXXX",
#"XX T  XXXXXXXXXX T  XXXXX",
#"X  T  XXXXXX XXX    X XXX",
#"XXXXXXXXXXXXXXXXXXXXXXXXX",
#"XXXXXXXXXXXXXXXXXXXXXXXXXX"
#]


level_1 =[
"XXXXXXXXXXXXXXXXXXXXXXXXX",  
"X   XXXXXX  XXXXXX  XXXXX",                                        # grid = 25 x 25 
"X       XX          XXXXX",
"X       XX  XXX    XXXXXX",                                # Top Left Block: -288, 288  
"XXXXXX  XX  XXXE       XX",                                        # Top Right Block: 288, 288
"XXXXXX  XX  XXXXXX   XXXX",                                        # Bottom  Left Block: -288, -288 
"XXXXXXE  XX      X  XXXXX",                                          # Bottom Right Block: 288, -288 
"X  XXX        X XX T XXXX",
"X            XX XXXXXXXXX",
"X XXXXXXXX XE      XXXXXX",
"X     XXXXXXTXXXXXXXXXXXX",
"X X XXXXXXXXXXX         X",
"X X XXXXXXXXZ           X",
"X X TXXXXXXXXXX         X",
"X XXXXX                 X",
"X X  X       XXXXXXXXXXXX",
"X    XXXXX   XXXXXXXXXXXX",
"XXXX XXXXX              X",
"XX  TXXXXX              X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX   E XXXXXXXXXXX  XXXXX",
"XX          XXXX        X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

#Added Mazses to the Maze level
levels.append(level_1)



#Create Level Sretup up Function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #get character at each x, y coor
            #y, x order in next line
            character = level[y][x]
            #calc screen x, y coors
            screen_x = -288 + (x * 24)
            screen_y =  288 - (y * 24)
    
    # Check if X is a wall
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape('wall.gif')
                pen.stamp()
                walls.append((screen_x, screen_y))
                
            if character == "Z":
                player.goto(screen_x, screen_y)

            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))

# Create a Class Instance
pen = Pen()  #actually created a pen
player = Player()  #player instance
#enemy = Enemy()

#treasure list
treasures = []
#create walls list
walls = []
#create enemy list
enemies = []

# Setup levels
setup_maze(levels[1])
print(walls)

#keyboard bindings
turtle.listen()
turtle.onkey(player.go_up, 'w')
turtle.onkey(player.go_down, 's')
turtle.onkey(player.go_left, 'a')
turtle.onkey(player.go_right, 'd')

wn.tracer(0)

#move enemies
for enemy in enemies:
    turtle.ontimer(enemy.move, t = 250)
    
while True:
#    pass
     for treasure in treasures:
         if player.collide(treasure):
             #add treasure to players goal
             player.gold += treasure.gold
             print('player score: {}'.format(player.gold))
             #destroy treasure
             treasure.destroy()
             #remove treasure from treasue list
             treasures.remove(treasure)
     
         
     for enemy in enemies:
        if player.collide(enemy):
            print('the piggies are coming the piggies are coming')
    
    
    
     wn.update()






#wn.mainloop()