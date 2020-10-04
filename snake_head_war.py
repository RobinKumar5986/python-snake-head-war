# python-snake-head-war
it is created with python and the main module which is been used in this program is python
#its a snake head racing game
#modules which are imported 
import turtle
import random
import math

#making play zone
#play zone baground
sc=turtle.Screen()           #defining screen object
sc.bgcolor("green")          #defining screen baground color
sc.title("SNAKE HEAD  WAR")  #title decleartion

#creating scoor bord

score=0                      #player one score at the begning
score2=0                     #player two score at begning
#draw the score bord for player one
sp=turtle.Turtle()#defining player one score turtle 
sp.speed(0)      #set turtle speed fastest 
sp.color("white")#declearing turtle speed
sp.up()          #this stops turtle to print any line while it is moving
sp.goto(-290,270)#seting the coordinat and moving the turtle to that coordinate
sp.down()        #ater this turtle is allowed to draw any thing in the screen
scs="player_1:%s"%score #this will show the player 1 score and %score will show they score
sp.write(scs,False,font=("Areal",14,"bold"))#it will write the every thing in the scteen 
sp.hideturtle()#it will hide the tutle which is writeing all the above


#draw the score bord for player 2



sp2=turtle.Turtle()#defining player one score turtle 
sp2.speed(0)       #set turtle speed fastest 
sp2.color("white") #declearing turtle speed
sp2.up()           #this stops turtle to print any line while it is moving
sp2.goto(-290,240) #seting the coordinat and moving the turtle to that coordinate
sp.down()          #ater this turtle is allowed to draw any thing in the screen
scs2="player_2:%s"%score#this will show the player 1 score and %score will show they score
sp2.write(scs2,False,font=("Areal",14,"bold"))#it will write the every thing in the scteen 
sp2.hideturtle()#it will hide the tutle which is writeing all the above

#play zone boundryes
t1=turtle.Turtle()     #creating first turtle object
t1.speed(0)            #seting the speed to maxmimum
t1.hideturtle()        #it will hide the turtle which is drawing the play zone
t1.color("white")      #declearing turtle color
t1.up()                #hiding lines made by turtle
t1.goto(-300,300)      #taking turtle to sertain coordinate
t1.showturtle()        #it will aggain start showing the turtle
t1.down()              #after this turtle will allowed to draw any thing  
t1.pensize(5)          #it will decide the thickness of line drawed by turtle
for i in range(4):     #it is the condition statemen for doing any thing in loop
    t1.forward(600)    #it will move the turtle forward
    t1.right(90)       #it will move the turtle head in 90 degree right
t1.hideturtle()        #it will hide the turtle 

#creating first snake
s1=turtle.Turtle()    #it will create firsrt smake head
s1.left(90)           #it will move the turltle in left direaction with 90 degree
s1.color("red")       #it will decide the turtle color
s1.shape("square")    #it will decide the turtle shape 
s1.shapesize(.7)      #it will decide the size if the turtle
s1.up()               #it will hide the lines drawed by the turtle
s1.goto(-50,50)       #it will move the turtle to the given coordinate

#creating second players snake
s2=turtle.Turtle()    #it will create the secnd snake head
s2.left(90)           #it will move the turtle head 90 degree left
s2.color("blue")      #it will declear the turtle color
s2.shape("square")    #it will declear the trtle shape
s2.shapesize(.7)      #it will declear the size of the turtle
s2.up()               #it will hide all the lines drawed by the turtle
s2.goto(50,50)        #it will move the turtle to the given coordinate

#defining the movement of the snake one

snakes_speed=2                 #starting snake speed

def right():                   #if is defination or the collection of some command 
    s1.up()                    #it will hided th lines drawed by s1 turtle
    if s1.heading!=0:          #if is a condition statement 
        s1.setheading(0)       #it will set the head of turtle at 0 degree
        
def left():                    #it is a collection of programs
    s1.up()                    #it will hide all the lines drawd by the turtle
    if s1.heading!=180:        #it is a conditional statement
        s1.setheading(180)     #it will set the heading of of s1 sturtle at 180 degree
        
def up():                      #it is a collection of programs
    s1.up()                    #it will hide all the lines drawd by the turtle
    if s1.heading!=90:         #it is a conditional statement
        s1.setheading(90)      #it will set the heading of of s1 sturtle at 90 degree
        
def down():                    #it is a collection of programs
    s1.up()                    #it will hide all the lines drawd by the turtle
    if s1.heading!=270:        #it is a conditional statement
        s1.setheading(270)     #it will set the heading of of s1 sturtle at 270 degree

#defining the movement of the snake two
def right2():
    s2.up()
    if s2.heading!=0:
        s2.setheading(0)
def left2():
    s2.up()
    if s2.heading!=180:
        s2.setheading(180)
def up2():
    s2.up()
    if s2.heading!=90:
        s2.setheading(90)
def down2():
    s2.up()
    if s2.heading!=270:
        s2.setheading(270)

##Defining key binding
turtle.listen()                   #it is aspecific command which allows us to call any definatin on pressing any key
turtle.onkey(left,"Left")         #these are some example
turtle.onkey(right,"Right")
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
##Defining key binding
turtle.onkey(left2,"a")
turtle.onkey(right2,"d")
turtle.onkey(up2,"w")
turtle.onkey(down2,"s")
##Creating snake food
food=turtle.Turtle()
food.shapesize(0.7)
food.hideturtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
x=random.randint(-290,290)
y=random.randint(-290,290)
food.up()
food.goto(x,y)
food.showturtle()
#defining collision
def collision(a1,a2):      #it is function defination 
    dis=math.sqrt(math.pow(a1.xcor()-a2.xcor(),2)+math.pow(a1.ycor()-a2.ycor(),2))#it is formula from coordinte geometry of finding distance b/w two points
    if dis<15:             #these are the conditional statements
        return True
    else:
        return False
#creating wining variable
snake_point1=0
snake_point2=0
###creating snake body segments
#main game loooop
while True:
    #moving the snake one

    
    if True:         #it is a always TRUE statement or it is a infinite loop
        x=s1.xcor()
        y=s1.ycor()
        s1.forward(snakes_speed)
        #snake two
        x2=s2.xcor()
        y2=s2.ycor()
        s2.forward(snakes_speed)
        if x>300 or x<-300 or y>300 or y<-300:
            s1.hideturtle()
            s2.hideturtle()
            print("game over")
            sp.up()
            sp.goto(-200,0)
            sp.down()
            sp.color("red")
            sp.write("GAME OVER\n snake 2 win",False,font=("Jokerman",50,"bold"))
            break
        if x2>300 or x2<-300 or y2>300 or y2<-300:
            s2.hideturtle()
            s1.hideturtle
            print("game over")
            sp.up()
            sp.goto(-200,0)
            sp.down()
            sp.color("red")
            sp.write("GAME OVER\n snake 1 win",False,font=("Jokerman",50,"bold"))
            break
    if collision(s1,food):
        snake_point1=snake_point1+1
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.hideturtle()
        food.goto(x,y)
        food.showturtle()
        #updateing score
        score=score+10
        scs="player_1:%s"%score
        sp.clear()
        sp.write(scs,False,font=("Areal",14,"bold"))
        snakes_speed=snakes_speed+0.3
        if snake_point1==10:
            s1.hideturtle()
            s2.hideturtle()
            food.hideturtle()
            print("player 1 win")
            sp.up()
            sp.goto(-200,0)
            sp.down()
            sp.color("red")
            sp.write(" snake 1 win",False,font=("Jokerman",50,"bold"))
            break
    if collision(s2,food):
        snake_point2=snake_point2+1
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.hideturtle()
        food.goto(x,y)
        food.showturtle()
        #updateing score
        score2=score2+10
        scs2="player_2:%s"%score2
        sp2.clear()
        sp2.write(scs2,False,font=("Areal",14,"bold"))
        snakes_speed=snakes_speed+0.3
        if snake_point2==10:
            s1.hideturtle()
            s2.hideturtle()
            food.hideturtle()
            print("player 2 win")
            sp.up()
            sp.goto(-200,0)
            sp.down()
            sp.color("red")
            sp.write(" snake 2 win",False,font=("Jokerman",50,"bold"))
            break
    if collision(s2,s1):
        sp.up()
        sp.goto(-200,0)
        sp.down()
        sp.color("red")
        sp.write("GAME OVER\n match draw",False,font=("Jokerman",50,"bold"))
        break
