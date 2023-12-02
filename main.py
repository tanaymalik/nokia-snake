# import turtle
# from turtle import *
# import random
# import time
# from snake import Snake
# from food import Food
# from scoreboard import ScoreBoard
# from music import MusicPlayer


# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("nokia snake game")
# screen.tracer(0)

# snake = Snake()
# foodie = Food()
# score = ScoreBoard()
# music = MusicPlayer()


# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")

   
  
# game_on = True

# music.play_background()
# while game_on == True:
     
#     screen.update()  
#     time.sleep(0.1)
    
#     snake.move()
    
#     #DETECT COLLISION WITH FOOD
#     if snake.head.distance(foodie) < 15:
#         music.play_colliding_effect()
#         foodie.refresh()
#         snake.extend()
#         score.update_score()
        
#     #DETECT COLLISION WITH WALL
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         music.play_game_over()
#         score.game_over()
#         game_on = False    

import turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from music import MusicPlayer

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("nokia snake game")
screen.tracer(0)

snake = Snake()
foodie = Food()
score = ScoreBoard()
music = MusicPlayer()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

music.play_background()

def game_loop():
    global game_on

    screen.update()
    snake.move()

    # DETECT COLLISION WITH FOOD
    if snake.head.distance(foodie) < 15:
        music.play_colliding_effect()
        foodie.refresh()
        snake.extend()
        score.update_score()

    # DETECT COLLISION WITH WALL
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        music.play_game_over()
        score.game_over()
        game_on = False

    # Schedule the next execution of game_loop after 100ms
    if game_on:
        screen.ontimer(game_loop, 80)

# Call the game loop for the first time
game_loop()

# Start the Turtle graphics main loop
screen.mainloop()

# Cleanup when exiting the game
music.quit()









screen.exitonclick()