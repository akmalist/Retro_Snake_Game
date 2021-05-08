from turtle import Turtle

ALIGNMENT = 'center'

FONT = ("Courier", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.speed('fastest')
        self.color("white")
        self.hideturtle()
        self.setposition(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=("Courier", 70, "normal"))
