# Example file showing a basic pygame "game loop"
import pygame
import pymunk
import pymunk.pygame_util
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
while running:
    dt = 1/60
    space.step(dt)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            ball.position = mouse_pos
            ball.velocity = [0,0]
            
            
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
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()  