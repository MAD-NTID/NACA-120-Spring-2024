import turtle
import random

# Function to draw a triangle
def draw_triangle(t, size):
    for _ in range(3):
        t.forward(size)
        t.left(120)

# Recursive function to draw Sierpinski's triangle
def sierpinski(t, size, depth):
    if depth == 0:
        draw_triangle(t, size)
    else:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        t.pencolor(r,g,b)
        # Draw the 3 smaller Sierpinski triangles
        sierpinski(t, size / 2, depth - 1)
        t.forward(size / 2)
        sierpinski(t, size / 2, depth - 1)
        t.backward(size / 2)
        t.left(60)
        t.forward(size / 2)
        t.right(60)
        sierpinski(t, size / 2, depth - 1)
        t.left(60)
        t.backward(size / 2)
        t.right(60)

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle object
t = turtle.Turtle()
turtle.colormode(255)
t.speed(0)
t.penup()

# Position turtle
t.goto(-200, -150)
t.pendown()

# Start drawing the Sierpinski triangle
size = 700  # Size of the large triangle
depth = 6    # Depth of recursion
sierpinski(t, size, depth)

# Hide the turtle and finish
t.hideturtle()
turtle.done()
