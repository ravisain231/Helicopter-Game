# -*- coding: utf-8 -*-
"""
Created on Wed Oct 4 5:39 2020
@author: Ravinder
"""

import pygame
from pygame import *
from random import *
import random
import time
import os
from pygame.locals import *

black = (26,26,26)
white = (255,255,255)
grey = (166,166,166)
blue = (0, 0, 128)

pygame.init()

surfaceWidth = 800
surfaceHeight = 500
imageHeight = 43
imageWidth = 70


surface = pygame.display.set_mode((surfaceWidth,surfaceHeight))
pygame.display.set_caption('Helicopter Game')
clock = pygame.time.Clock()
background_image = pygame.image.load("bg.png").convert()
img = pygame.image.load('helicopter.png')


def makeTextObjs(text , font):
    textSurface = font.render(text, True , black )   # This returns a text surface object
    return textSurface , textSurface.get_rect()

# display the blocks
def blocks (x_block , y_block , block_width , block_height , gap):
    pygame.draw.rect(surface , grey ,[x_block,y_block,block_width,block_height])
    pygame.draw.rect(surface , grey ,[x_block,y_block+block_height+gap,block_width,surfaceHeight])


def replay_or_quit():
    # This function excutes when game is over
    # determine whether key is pressed, or released or game is quit
     for event in pygame.event.get([pygame.KEYDOWN , pygame.KEYUP , pygame.QUIT]):
         if event.type == pygame.QUIT:
             pygame.quit()     # deactivates pygame library
             quit()   # exit the program

         elif event.type == pygame.KEYDOWN:
             continue
          
         return event.key  # when key is released means, it is chosen to replay the game, the game restarts
     
     return None


def gameOver():
    msgSurface('Game over!')

def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf',20)
    largeText = pygame.font.Font('freesansbold.ttf',120)

    titleTextSurf , titleTextRect = makeTextObjs(text, largeText)
    # This position would determine position of text
    titleTextRect.center = surfaceWidth / 2 , surfaceHeight / 2
    surface.blit(titleTextSurf , titleTextRect) # text is displayed on the surface 

    typTextSurf , typTextRect = makeTextObjs('Press any key to continue', smallText)
    typTextRect.center = surfaceWidth / 2 , ((surfaceHeight / 2) + 100)
    surface.blit(typTextSurf , typTextRect)
    
   
    pygame.display.update()  #It updates the surface area

    time.sleep(1)

    while replay_or_quit() == None: #Loop will execute till None is received
        clock.tick() 

    main() 



#put image to the game screen
def helicopter (x,y,image):
    surface.blit(img , (x,y))

def score(count):
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render("Score: "+str(count), True, blue)
    surface.blit(text, [10,10])

def main():
    # x and y are co-ordinates of helicopter position
    x = 150
    y = 200
    y_move = 0
    x_block = surfaceWidth # initially block is at the end of the game window
    y_block = 0 # Block position starts from top of the screen
    block_width =75
    block_height = randint(0, (surfaceHeight/2))
    gap = imageHeight * 3   # gap would be of size of thrice the helicopter size
    block_move = 3


    game_over = False
    current_score=0

    while not game_over:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT: # close button of game window is pressed 
                game_over = True

            if event.type == pygame.KEYDOWN: # This means that key is pressed
                if event.key == pygame.K_UP: # the UP key is pressed
                    y_move = -3   # The helicopter moves up by 3 units

            if event.type == pygame.KEYUP: # This means a key is released
                if event.key == pygame.K_UP: # The released key is UP key
                    y_move = 3 # Helicopter moves down by 3 units

        y+=y_move
        surface.blit(background_image,[0,0]) 
        helicopter(x,y,img)
        blocks(x_block , y_block , block_width ,block_height , gap)
        x_block -= block_move   # Block moves 3 unit towards left in each loop
        score(current_score)
        
        if y > surfaceHeight - 40 or y < 0: # This means either bottom of helicopter 
        # touches bottom of screen or top of helicopter touches top of screen
            gameOver()
        if x_block <(-1 * block_width): # The block reaches left end of the screen
            x_block =surfaceWidth # The block again is placed to the right end of screen
            block_height = randint(0 , (surfaceHeight/2))

        current_score+=1
        if x + imageWidth > x_block:  # front end of helicopter is beyond the block
            if x< x_block + block_width: # back part is behind the end of block
                print('helicopter is possibly within boundaries of x')
                if y < block_height: # y position also collides with block
                    print('Y position coincide')
                    if x - imageWidth < block_width + x_block:
                        print('hit with upper block')
                        gameOver()
                   

        if x + imageWidth > x_block:
            print('x cross')
            if y + imageHeight > block_height + gap: # bottom y co-ordinates 
                # coincide with lower block
                print('y position coincide')
                if x < block_width + x_block :
                    print('hit with lower block')
                    gameOver()
                

        pygame.display.update()
        clock.tick(100)

main()
pygame.quit() 
quit()
