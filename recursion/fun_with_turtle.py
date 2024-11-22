import turtle
import random

def draw_tree(branch_length, depth):
    if depth == 0:
        return
    else:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        turtle.pencolor(r,g,b)
        # Draw the current branch
        turtle.forward(branch_length)

        # Draw the right subtree
        turtle.left(20)
        draw_tree(branch_length * 0.7, depth - 1)

        # Return to the current branch
        turtle.right(40)
        draw_tree(branch_length * 0.7, depth - 1)

        # Return to the original orientation
        turtle.left(20)

        # Go back to the previous branch
        turtle.backward(branch_length)

    

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    turtle.colormode(255)
    
    # Create a turtle object

    turtle.left(90)  # Make the turtle face upwards
    turtle.speed(0)  # Fastest drawing speed

    # Set initial branch length and depth
    branch_length = 120
    depth = 10  # You can change this value to increase or decrease the tree's depth

    # Draw the tree
    draw_tree(branch_length, depth)

main()

input("Press any key to end")