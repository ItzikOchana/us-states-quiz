from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.goto(0, 270)  # top center of the screen
        self.update_score_display()

    def update_score_display(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def got_point(self):
        self.score += 1
        self.update_score_display()

    def YOU_WON(self):
        self.goto(0, 0)
        self.write("++++YOU WON++++", align="center", font=("Courier", 40, "normal"))
