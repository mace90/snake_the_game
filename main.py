import turtle
import time
# import my own class the snake
import snake
from food import Food
from scoreboard import Scoreboard

# create a instance of the Screen class, and modify at some things
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
# create a instance of my Snake-Class.
snake = snake.Snake()
# create a instance of my Food-Class.
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.snake_direction_right, key="Right")
screen.onkey(fun=snake.snake_direction_left, key="Left")
screen.onkey(fun=snake.snake_direction_up, key="Up")
screen.onkey(fun=snake.snake_direction_down, key="Down")
# just some visual twerks, that the snake is shown properly
screen.tracer(0)

# trigger for the while loop
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    # snake hit the food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.extend()
        snake.extend()
    # snake hit the wall
    if snake.head.ycor() < -290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.xcor() > 290:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
