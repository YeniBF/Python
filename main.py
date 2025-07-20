from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
screen.exitonclick()

from snake import Snake
from food import Food
from scoreboard import Scoreboard
scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Arriba")
screen.onkey(snake.down, "Abajo")
screen.onkey(snake.left, "Izquierda")
screen.onkey(snake.right, "Derecha")
