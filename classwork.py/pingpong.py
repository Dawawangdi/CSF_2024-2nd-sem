import pygame
import random

pygame.init()


BLACK =(0,0,0) #RGB for black
WHITE = (255,255,255) #RGB for white

WIDTH, HEIGHT = 800,600    #window size
BALL_RADIUS = 10 
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20

class Ball:    #defines a new class named Ball
    def __init__(self):
        self.x = WIDTH //2  #It sets the initial horizontal position of the ball to be at the center of the game window. WIDTH represents the width of the game window, so WIDTH // 2 calculates the midpoint
        self.y = HEIGHT //2
        self.speed_x = random.choice([-3,3])  #The random.choice() function is used to randomly select between -3 and 3.This means the ball will start moving either to the left or to the right at a speed of 3 units per frame
        self.speed_y = 2  #This value indicates that each time the game updates, the ball will move downward by 2 pixels Unlike speed_x, speed_y does not randomly change, ensuring consistent downward movement at game start
    def move(self):
        self.x= self.speed_x  # If self.speed_x is positive, the movement is to the right; if it's negative, the movement is to the left.
        self.y= self.speed_y  #if self.speed_y is positive, the object moves down; if negative, the object moves up.
    def check_collision(self):
        if self.x <= BALL_RADIUS or self.x >= WIDTH - BALL_RADIUS:
            self.speed_x = -self.speed_x  #reverses the horizontal velocity of the ball
        if self.y<=BALL_RADIUS:
            self.speed_y = -self.speed_y #. If self.speed_y was positive (meaning the ball was moving downward), it becomes negative (causing the ball to move upward), and vice versa. This effectively simulates a bounce off the top wall.
class Paddle:
    def __init__(self):
        self.width = PADDLE_WIDTH  #This line sets the width attribute of the instance to PADDLE_WIDTH
        self.height= PADDLE_HEIGHT
        self.x = (WIDTH - self.width)//20 #This line calculates the horizontal position (x coordinate) of the paddle
        self.y = HEIGHT- self.height- 10







