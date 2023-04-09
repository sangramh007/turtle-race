from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_POSITION = (-280, 260)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        # self.show_score()
        self.score = 0

    def show_score(self):
        self.goto(SCOREBOARD_POSITION)
        self.clear()
        self.write(f"LEVEL:{self.score}", align="left", font=FONT)

    def level_up(self):
        self.score += 1


