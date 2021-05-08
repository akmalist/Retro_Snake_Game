from turtle import Turtle

coordinates = "(0, 270)"


class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.speed('fastest')
        self.color("white")
        self.hideturtle()
        self.setposition(0, 260)

    def increase_score(self, number):
        self.num = number
        self.write(f"Score: {self.num} ", align='center', font=("Verdana", 15, "normal"))
