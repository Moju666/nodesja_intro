from turtle import *

# Erstelle zwei Turtle-Objekte mit je eigenem Namen
turtle1 = Turtle()
turtle2 = Turtle()

# Setze Eigenschaften für turtle1
turtle1.shape("turtle")
turtle1.color("blue")
turtle1.penup()
turtle1.goto(-100, 0)
turtle1.pendown()
turtle1.pencolor("green")
#turtle1.fillcolor("black")
#turtle1.fillcolor("yellow")

# Setze Eigenschaften für turtle2
turtle2.shape("turtle")
turtle2.color("green")
turtle2.penup()
turtle2.goto(100, 0)
turtle2.pendown()
turtle2.pencolor("blue")
#turtle2.fillcolor("yellow")

# Bewege turtle1 vorwärts
turtle1.forward(150)
turtle1.right(90)
turtle1.forward(50)
turtle1.forward(150)
turtle1.right(90)
turtle1.forward(150)
turtle1.right(90)
turtle1.forward(200)
turtle1.right(90)
turtle1.forward(200)
# Bewege turtle2 vorwärts und drehe andersherum
turtle2.forward(10)
turtle2.left(200)
turtle2.forward(75)
turtle2.right(850)
turtle2.forward(30)
turtle2.left(200)
turtle2.forward(200)
turtle2.right(75)
turtle2.forward(1)
#turtle2.forward(100)                                                                          )
done()
