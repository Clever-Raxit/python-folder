import turtle

raxit = turtle.Turtle()
raxit.speed(1)


def square():
    raxit.forward(100)
    raxit.right(90)
    raxit.forward(100)
    raxit.right(90)
    raxit.forward(100)
    raxit.right(90)
    raxit.forward(100)
    raxit.right(90)
    raxit.right(90)
    

for count in range(4):
    square()
    