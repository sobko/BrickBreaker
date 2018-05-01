import sys
import pygame

def run_game():
    #initial setup
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("BrickBreaker")
    
    #create variables
    
    ball = pygame.image.load("ball.png")
    ball_x = 150
    ball_y = 400
    
    #game loop

    while True:
        #changes based on events
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    
        #automatic changes
                    
        #draw the stuff
        #first a black screen
                    
        screen.fill((0,0,0))
        
        #then stuff on top of the screen
        
        screen.blit(ball, (ball_x, ball_y))
        
        #show the new screen
        
        pygame.display.flip()

run_game()
