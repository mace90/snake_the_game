# import the turtle package
import turtle
# starting coordination for the first snake segments
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# moveing distance for each segment
MOVE_DISTANCE = 15
# creating a class for the snake
class Snake:
    # it needs inital a empty list for each square of the snake and then the snake should be created
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[1:len(self.segments)]

    # creating 3 instances of a turtle, with the shape of a square, no pen, color is white and is placed to the each
    # starting position. And added to the empty list.
    def create_snake(self):
        for x in STARTING_POSITIONS:
            self.add_segment(x)


    # in the list of each snake-part. the last seg goes to the posotion of the segment in front of hin. and the first
    # is going forward
    def snake_move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[seg - 1].xcor()
            newy = self.segments[seg - 1].ycor()
            self.segments[seg].goto(newx, newy)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        snake = turtle.Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def snake_direction_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def snake_direction_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def snake_direction_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def snake_direction_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)