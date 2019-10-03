
#Python programming to draw pentagon in turtle programming
import turtle
 
t = turtle.Turtle()
for i in range(5):
   t.forward(100) #Assuming the side of a pentagon is 100 units
   t.right(72) #Turning the turtle by 72 degree
  
  
#Python programming to draw hexagon in turtle programming
import turtle
 
t = turtle.Turtle()
for i in range(6):
   t.forward(100) #Assuming the side of a hexagon is 100 units
   t.right(60) #Turning the turtle by 60 degree

#Python programming to draw heptagon in turtle programming
import turtle
 
t = turtle.Turtle()
for i in range(7):
   t.forward(100) #Assuming the side of a heptagon is 100 units
   t.right(51.42) #Turning the turtle by 51.42 degree

#Python programming to draw octagon in turtle programming
import turtle
 
t = turtle.Turtle()
for i in range(8):
   t.forward(100) #Assuming the side of a octagon is 100 units
   t.right(45) #Turning the turtle by 45 degree

#Python programming to draw polygon in turtle programming
import turtle
 
t = turtle.Turtle()
numberOfSides = int(input('Enter the number of sides of a polygon: '))
lengthOfSide = int(input('Enter the length of a side of a polygon: '))
exteriorAngle = 360/numberOfSides
for i in range(numberOfSides):
   t.forward(lengthOfSide)
   t.right(exteriorAngle)
