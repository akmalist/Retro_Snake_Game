from turtle import Screen
import time
from snake import Snake

from food import Food

food = Food()

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

    #detect collision with food
    if snake.head.distance(food) < 15:
        print("collided")
        food.refrech_food_location()


screen.exitonclick()
