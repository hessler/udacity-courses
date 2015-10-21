import turtle

# Colors
color_maize = "#ffd11c"
color_blue = "#002b61"

def draw_block_m(t):
    # Starting at center of down-slope angle, moving clockwise
    t.fill(True)
    t.begin_poly()
    t.right(-54)
    t.forward(92.71)
    t.right(54)
    t.forward(78)    # At top right corner 
    t.right(90)
    t.forward(53)
    t.right(90)
    t.forward(21)
    t.left(90)
    t.forward(83)
    t.left(90)
    t.forward(21)
    t.right(90)
    t.forward(53)    # At bottom right corner
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(53)
    t.right(90)
    t.forward(21)
    t.left(90)
    t.forward(53)
    t.left(144)
    t.forward(92.71) # At bottom center point of down-slope
    t.right(108)
    t.forward(92.71)
    t.left(144)
    t.forward(53)
    t.left(90)
    t.forward(21)
    t.right(90)
    t.forward(53)
    t.right(90)
    t.forward(100)   # At bottom left corner
    t.right(90)
    t.forward(53)
    t.right(90)
    t.forward(21)
    t.left(90)
    t.forward(83)
    t.left(90)
    t.forward(21)
    t.right(90)
    t.forward(53)    # At top left corner
    t.right(90)
    t.forward(78)
    t.right(54)
    t.forward(92.71)
    t.end_poly()
    t.fill(False)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")
    
    m = turtle.Turtle()
    m.color(color_blue)
    m.pensize(5)
    m.fillcolor(color_maize)
    m.speed(8)
    m.shape("circle")
    m.resizemode("user")
    m.turtlesize(0.5, 0.5)

    draw_block_m(m)
    m.hideturtle()
    
    window.exitonclick()

draw_art()
