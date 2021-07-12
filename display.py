import pygame
import sys
from pygame.locals import *


alarm = sys.argv[1]
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue =(57,0,236)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def GameLoop(alarm):
    global Emergency
    pygame.init()
    display_width = pygame.display.list_modes()[0][0]
    display_height = pygame.display.list_modes()[0][1]
    gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Emergency Alert')
    while True:
        gameDisplay.fill(black)
        largeText = pygame.font.SysFont('consolas', 60)
        smallText = pygame.font.SysFont('consolas', 30)
        helpText = pygame.font.SysFont('consolas', 16)
        if alarm == 'General':
            gameDisplay.fill(red)
            TextSurf, TextRect = text_objects('HVRHS EMERGENCY ALERT SYSTEM HAS BEEN ACTIVATED', largeText)

        if alarm == 'Silent':
            gameDisplay.fill(blue)
            TextSurf, TextRect = text_objects('The Silent Alarm Has Been Activated', largeText)

        if alarm == 'Both':
            gameDisplay.fill(white)
            TextSurf, TextRect = text_objects('All Alarms Active!!', largeText)

        TextRect.center = ((display_width / 2), (display_height / 2))
        smallTextSurf, smallTextRect = text_objects('Emergency Broadcast System:', smallText)
        smallTextRect.center = ((display_width / 2), (display_height / 4))
        helpTextSurf, helpTextRect = text_objects('Hold [enter] to dismiss', helpText)
        helpTextRect.center = ((display_width / 2), (display_height - (display_height / 4)))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(smallTextSurf, smallTextRect)
        gameDisplay.blit(helpTextSurf, helpTextRect)
        pygame.display.update()
        pygame.display.flip()
        pygame.time.wait(500)

        for event in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                pygame.quit()
                break
GameLoop(alarm)