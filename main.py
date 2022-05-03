# Author :  Lohit Sharma
# Purpose: This code uses turtle module to make a etch a sketch app You can use "w" to move forward
#         "a" to turn right, "d" to turn left and "s" to turn backward (all lower case)

from turtle import Screen, Turtle

lavi = Turtle()
screen = Screen()


def move_forward():
    lavi.forward(10)


def turn_backwards():
    lavi.backward(10)


def turn_right():
    lavi.right(10)


def turn_left():
    lavi.left(10)


screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(turn_right, "a")
screen.onkey(turn_left, "d")
screen.onkey(turn_backwards,"s")

screen.exitonclick()
