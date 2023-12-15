from turtle import Screen
import time
from Snake import Snake
from food import Food
from Score_board import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Charm")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        scoreboard.game_over()
        game_is_on = False


    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            scoreboard.game_over()
            game_is_on = False
            snake.reset()



screen.exitonclick()
