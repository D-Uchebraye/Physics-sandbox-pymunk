# Example file showing a basic pygame "game loop"
import pygame
import pymunk
import pymunk.pygame_util
import numpy as np
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

#pymunk setup
space = pymunk.Space()
options = pymunk.pygame_util.DrawOptions(screen)
space.gravity = (0,1000)
space.debug_draw(options)
THICKNESS = 5
ball_held = False

#TODO: create a way to add more balls to the sim


def create_ball(x,y):
    ball = pymunk.Body(10,10,body_type= pymunk.Body.DYNAMIC)
    ball_shape = pymunk.Circle(ball,25,offset=(0,0))
    ball.position = x,y
    ball_shape.elasticity = 0.9
    space.add(ball,ball_shape)


def create_borders(width,height):
    body = space.static_body
    borders = [pymunk.Segment(body,(0,0),(width,0), THICKNESS), #top
               pymunk.Segment(body,(width,0),(width,height),THICKNESS),#right
               pymunk.Segment(body,(0,0),(0,height),THICKNESS),#left
               pymunk.Segment(body,(0,height),(width,height),THICKNESS)#bottom
   ]

    for border in borders:
        border.elasticity = 0.9
        border.friction = 0.4
        space.add(border)
    return borders

borders = create_borders(SCREEN_WIDTH,SCREEN_HEIGHT)

#make a ball
ball = pymunk.Body(10,10,body_type= pymunk.Body.DYNAMIC)
ball_shape = pymunk.Circle(ball,25,offset=(0,0))
ball.position = 200,100
ball_shape.elasticity = 0.9
space.add(ball,ball_shape)
timer = 0

while running:
    dt = 1/120
    space.step(dt)
    timer += dt
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                _x,_y = pygame.mouse.get_pos()
                create_ball(_x,_y)
                

        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            global inital_x, inital_y , initial_velocity
            initial_x,initial_y = pygame.mouse.get_pos()
            initial_velocity = np.array(ball.velocity)
            ball.position = mouse_pos
            ball_held = True

            timer = 0
        
        if event.type == pygame.MOUSEBUTTONUP:

            final_x ,final_y = pygame.mouse.get_pos()
            final_velocity = ((final_x - initial_x) / timer, (final_y- initial_y) / timer ) 
            ball.velocity = final_velocity


            ball_held = False
            
        if event.type == pygame.VIDEORESIZE:
            width,height = event.w, event.h 
            screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)

            for b in borders:
                space.remove(b)

            borders = create_borders(width,height)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")


    # RENDER YOUR GAME HERE
    space.debug_draw(options)
    if ball_held:
        ball.position = pygame.mouse.get_pos()
        ball.velocity += [0,0]
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 60

pygame.quit()  