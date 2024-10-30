from turtle import Turtle
FONT = ("Courier", 5, "normal")

class Marker(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()


    def mark(self , state_name , coordinate):
        self.goto(coordinate)
        self.write( state_name , align= "center" , font = FONT )




