from turtle import *
import random
Screen()
Turtle()

bgcolor('black') 
x = 1 
speed(1000) 
while x < 200: 
  
 r = random.randint(0,255) 
 g = random.randint(0,255)  
 b = random.randint(0,255) 
  
 colormode(255)  
 pencolor(r,g,b) 
 fd(50 + x) 
 rt(90.991) 
 x = x+1 
