from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        # create snake

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake = Turtle('square')
        new_snake.color('white')
        new_snake.penup()
        new_snake.goto(position)
        self.segments.append(new_snake)

    def reset_snake(self):
        for seg in self.segments:
            seg.reset()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend_segment(self):
        # hold last items position from the list of segments add segment to the last one
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            # hold the coordinates of last second seg and and assisgn it to the last from the list of segments
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            # last segments from list
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
