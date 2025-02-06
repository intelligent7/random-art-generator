# art_generator.py
# Generates random art patterns using the turtle module.

import turtle
import random

def setup_turtle():
    """Initialize the turtle with a random background color."""
    screen = turtle.Screen()
    screen.bgcolor(random.choice(['lightblue', 'lightgreen', 'lavender', 'mistyrose']))
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    return t

def draw_random_art(t):
    """Draw random lines and shapes with varying colors and lengths."""
    for _ in range(60):  # Draw 50 random lines
        t.pencolor(random.random(), random.random(), random.random())  # Random RGB color
        t.width(random.randint(1, 10))  # Random line width
        length = random.randint(10, 150)  # Random length
        angle = random.randint(0, 360)  # Random angle
        t.forward(length)
        t.right(angle + (90 if random.random() < 0.5 else 0))
        if random.random() < 0.3: for _ in range(3): t.forward(20 + random.randint(0, 40)); t.right(120)
        if random.random() < 0.3: for _ in range(4): t.forward(30 + random.randint(0, 40)); t.right(90)
        if random.random() < 0.3: t.circle(random.randint(20, 50))

def main():
    """Main function to run the art generator."""
    t = setup_turtle()
    draw_random_art(t)
    turtle.done()  # Keep window open until closed manually

if __name__ == "__main__":
    main()
