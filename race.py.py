import turtle
import time
import random

screen = turtle.Screen()
screen.bgcolor('lightblue')

write = turtle.Turtle()
write.hideturtle()
write.penup()
write.goto(-300,0)

p1 = turtle.Turtle()
p1.color('#000947')
p1.shape('turtle')
p2 = p1.clone()
p2.color('#ff0033')
p2.shape('turtle')
p3 = p1.clone()
p3.color('purple')
p3.shape('turtle')
p4 = p1.clone()
p4.color('green')
p4.shape('turtle')
p5 = p1.clone()
p5.color('yellow')
p5.shape('turtle')

p1.penup()
p1.goto(-300,200)
p2.penup()
p2.goto(-300,-200)
p3.penup()
p3.goto(-300,100)
p4.penup()
p4.goto(-300,-100)
p5.penup()
p5.goto(-300,0)

p1.penup()
p1.goto(300,-250)
p1.left(90)
p1.pendown()
p1.color('black')
p1.forward(500)
p1.write('Finish!', font=30)
p1.left(90)
p1.penup()
p1.color('#000947')
p1.goto(-300,200)
p1.right(180)

p1.pendown()
p2.pendown()
p3.pendown()
p4.pendown()
p5.pendown()

die = [1,2,3,4,5,6]
for i in range(30):
    if p1.position() >= (300,200):
        won = "Blue WON"
        color = "#000947"
        break
    elif p2.position() >= (300,-200):
        won = "Red WON"
        color = "#ff0033"
        break
    elif p3.position() >= (300,100):
        won = "Purple WON"
        color = "purple"
        break
    elif p4.position() >= (300,-100):
        won = "Green WON"
        color = "green"
        break
    elif p5.position() >= (300,0):
        won = "Yellow WON"
        color = "yellow"
        break
    else:
        p1.forward(30*random.choice(die))
        p2.forward(30*random.choice(die))
        p3.forward(30*random.choice(die))
        p4.forward(30*random.choice(die))
        p5.forward(30*random.choice(die))
screen.bgcolor(color)
write.write(won,font=("Arial", 80, 'bold'))
write.fillcolor("black")



turtle.done()