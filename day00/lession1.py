from turtle import *


#we want to paint preaty house

#step 1:   draw a square

width(5)
color("red")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
#end of squere

end_fill()

#drawing door

left(90)
forward(70)
color("green")   #door color
begin_fill()
left(90)
forward(110)   #height of the door

right(90)
forward(55)

right(90)
forward(110)
end_fill()

penup()
goto(200,200)
pendown()

color("purple")
begin_fill()
right(150)
 
forward(200)
left(150)

right(30)
forward(200)
end_fill()

exitonclick()





