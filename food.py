from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        self.random_x = random.randrange(-280, 280)
        self.random_y = random.randrange(-280, 280)
        self.goto(self.random_x, self.random_y)