import turtle
from turtle import *
import random
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("nokia snake game")
screen.tracer(0)

snake = Snake()
foodie = Food()
score = ScoreBoard()
 
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

   
  
game_on = True
while game_on == True:
    screen.update()  
    time.sleep(0.1)
    
    snake.move()
    
    #DETECT COLLISION WITH FOOD
    if snake.head.distance(foodie) < 15:
        foodie.refresh()
        score.update_score()
        
    #DETECT COLLISION WITH WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_on = False    
        
        
   
    
       
            
    
        
    
 














screen.exitonclick()