import sys
import pygame
import time
from pygame.locals import *
pygame.init()
alarm = sys.argv[1]
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue =(57,0,236)
ccycle = [white,red,blue]
ccnum = 0
ctt = time.asctime()
start = time.time()
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def GameLoop(alarm):
    global ccnum
    largeText = pygame.font.SysFont('consolas', 52)
    smallText = pygame.font.SysFont('consolas', 30)
    helpText = pygame.font.SysFont('consolas', 20)
    display_width = pygame.display.list_modes()[0][0]
    display_height = pygame.display.list_modes()[0][1]
    gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Emergency Alert')
    gameDisplay.fill(black)
    while True:
        if alarm == 'General':
            gameDisplay.fill(red)
            TextSurf, TextRect = text_objects('HVRHS EMERGENCY ALERT SYSTEM WAS ACTIVATED AT {0} LOCALTIME'
            .format(ctt).upper(), largeText)

        if alarm == 'Silent':
            gameDisplay.fill(blue)
            TextSurf, TextRect = text_objects('The Silent Alarm Was Activated At {0}'.format(ctt), largeText)

        if alarm == 'Both':
            gameDisplay.fill(ccycle[ccnum])
            if ccnum < (len(ccycle)-1): ccnum += 1
            else: ccnum = 0 
            TextSurf, TextRect = text_objects('All Alarms Active As Of {0} localtime'.format(ctt), largeText)

        TextRect.center = ((display_width / 2), (display_height / 2))
        smallTextSurf, smallTextRect = text_objects('Emergency Broadcast System:', smallText)
        smallTextRect.center = ((display_width / 2), (display_height / 4))
        helpTextSurf, helpTextRect = text_objects("Press Any Key To Acknowledge & Dismiss...", helpText)
        helpTextRect.center = ((display_width / 2), (display_height - (display_height / 4)))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(smallTextSurf, smallTextRect)
        gameDisplay.blit(helpTextSurf, helpTextRect)
        pygame.display.update()
        pygame.display.flip()
        pygame.time.wait(500)
        for event in pygame.event.get():
            if pygame.key.get_pressed() and (time.time() - start > 2):
                pygame.quit()
                break
GameLoop(alarm)