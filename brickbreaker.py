import sys
import pygame

def run_game():
    #initial setup
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("BrickBreaker")
    
    #create variables
    
    ball_image = pygame.image.load("ball.png")
    ball_x = 150
    ball_y = 400

    running = True

    #game loop

    while running:
        #changes based on events
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                    
        #automatic changes
                    
        #draw the stuff
        #first a black screen
                    
        screen.fill((0,0,0))
        
        #then stuff on top of the screen
        
        screen.blit(ball_image, (ball_x, ball_y))
        
        #show the new screen
        
        pygame.display.flip()
        
    pygame.quit()


run_game()
