from turtle import Turtle, Screen

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        # create snake

    def create_snake(self):
        for position in COORDINATES:
            new_snake = Turtle('square')
            new_snake.color('white')
            new_snake.penup()
            new_snake.goto(position)
            self.segments.append(new_snake)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            # hold the coordinates of last second seg and and assisgn it to the last from the list of segments
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            # last segments from list
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)
