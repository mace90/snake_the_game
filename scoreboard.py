from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.speed("fastest")
        self.fillcolor("white")
        self.color("white")
        self.goto((0.0, 270.0))
        self.add_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Arial", 24, "normal"))

    def add_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.score += 1


