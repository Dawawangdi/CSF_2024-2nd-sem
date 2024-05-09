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
import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define game constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20

class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed_x = random.choice([-3, 3])
        self.speed_y = 2

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def check_collision(self):
        if self.x <= BALL_RADIUS or self.x >= WIDTH - BALL_RADIUS:
            self.speed_x = -self.speed_x
        if self.y <= BALL_RADIUS:
            self.speed_y = -self.speed_y

class Paddle:
    def __init__(self):
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.x = (WIDTH - self.width) // 2
        self.y = HEIGHT - self.height - 10

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= 10
        elif direction == "right" and self.x < WIDTH - self.width:
            self.x += 10

class Game:
    def __init__(self):
        self.ball = Ball()
        self.paddle = Paddle()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True

    def update(self):
        self.ball.move()
        self.ball.check_collision()
        if self.ball.y >= HEIGHT - BALL_RADIUS - PADDLE_HEIGHT:
            if self.paddle.x <= self.ball.x <= self.paddle.x + PADDLE_WIDTH:
                self.ball.y = HEIGHT - BALL_RADIUS - PADDLE_HEIGHT - 1
                self.ball.speed_y = -self.ball.speed_y
                self.score += 1
            else:
                self.game_over = True

    def draw(self, screen):
        screen.fill(BLACK)
        pygame.draw.circle(screen, WHITE, (self.ball.x, self.ball.y), BALL_RADIUS)
        pygame.draw.rect(screen, WHITE, (self.paddle.x, self.paddle.y, self.paddle.width, self.paddle.height))
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        if self.game_over:
            game_over_text = self.font.render(f"Game Over! Your score: {self.score}", True, WHITE)
            game_over_rect = game_over_text.get_rect()
            game_over_rect.center = (WIDTH // 2, HEIGHT // 2)
            screen.blit(game_over_text, game_over_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ping Pong")
    clock = pygame.time.Clock()
    game = Game()

    while not game.game_over:
        game.handle_events()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            game.paddle.move("left")
        if keys[pygame.K_RIGHT]:
            game.paddle.move("right")
        game.update()
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()








