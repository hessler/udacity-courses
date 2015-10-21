import turtle

window = turtle.Screen()
window.bgcolor("#ededed")

def draw_square(t):
    for i in range(1, 5):
        t.forward(100)
        t.right(90)
    #print "Square drawn"


def draw_art():
    s = turtle.Turtle()
    s.shape("circle")
    s.resizemode("user")
    s.color("blue")
    s.turtlesize(0.5, 0.5)
    s.speed(0)
    
    #c = turtle.Turtle()
    #c.shape("circle")
    #c.resizemode("user")
    #c.color("red")
    #c.turtlesize(0.5, 0.5)
    #c.speed(4)
    #
    #t = turtle.Turtle()
    #t.shape("circle")
    #t.resizemode("user")
    #t.color("green")
    #t.turtlesize(0.5, 0.5)
    #t.speed(4)
    #t.right(45)
    
    for i in range(1, 37):
        draw_square(s)
        s.right(10)
    #draw_circle(c)
    #draw_triangle(t)
    
    window.exitonclick()

def draw_circle(c):
    c.circle(50)
    #print "Circle drawn"

def draw_triangle(t):
    for i in range(1, 4):
        t.forward(100)
        t.right(120)
    #print "Triangle drawn"
    


draw_art()