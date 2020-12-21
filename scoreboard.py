from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("high_score.txt") as hs:
            self.high_score = int(hs.read())
        self.penup()
        self.speed("fastest")
        self.fillcolor("white")
        self.color("white")
        self.goto((0.0, 270.0))
        self.update_scoreboard()

    def reset_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as hs:
                hs.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}, Highscore: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)


    def add_score(self):
        self.score += 1


