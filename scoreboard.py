from turtle import Turtle, Screen
FONT = "courier", 24, "normal"
ALIGNMENT = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.speed("fastest")
        self.hideturtle()
        self.create()
        self.score = 0
        self.write(f"score: {self.score}", move=False, align=ALIGNMENT, font=(FONT))
        
        
    def create(self):
        self.penup()
        self.goto(0, 265)  
        self.pendown()    
        
    def update_score(self):
        self.clear()
        self.score += 1 
        self.write(f"score: {self.score}", move=False, align=ALIGNMENT, font=(FONT))  
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=(FONT))      







