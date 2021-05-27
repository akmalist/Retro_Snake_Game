from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

food = Food()
score = Score()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Retro Snake Game")
screen.tracer(0)
screen.listen()
snake = Snake()
game_is_on = True

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# move snake
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food_location()
        snake.extend_segment()
        score.clear()
        score.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_score()
        snake.reset_snake()

    # detect collision with snakes tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()


screen.exitonclick()
