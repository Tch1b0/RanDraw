import pygame
from random import randint
import sys

pygame.init()                                  
screen = pygame.display.set_mode([600,600])
clock = pygame.time.Clock()

widht = 10
height = 10
PhaseAmount = 0
amount = 1
Yellow = (255,255,0)
Blue = (1,148,254)
Green = (51,233,75)
Pink = (255,0,255)

class FillScreen:
    def __init__(self,PhaseAmount,amount):
        pass

    def SetColor(self,PhaseAmount,amount):

        if PhaseAmount < 300:
            for i in range(1,amount):
                FiSc.Draw(Yellow)
        if PhaseAmount < 600 and amount > 300:
            for i in range(1,amount-300):
                FiSc.Draw(Blue)
        if PhaseAmount < 900 and amount > 600:
            for i in range(1,amount-600):
                FiSc.Draw(Green)
        if PhaseAmount < 1200 and amount > 900:
            for i in range(1,amount-900):
                FiSc.Draw(Pink)

        return PhaseAmount

    def Draw(self,Color):
        x = randint(1,600)
        y = randint(1,600)
        pygame.draw.rect(screen, (Color),(x,y,widht,height))


FiSc = FillScreen(PhaseAmount,amount)

run = False
while True:
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        amount += 1
        PhaseAmount += 1    
        if PhaseAmount >= 1200:   
            run = False

        FiSc.SetColor(PhaseAmount,amount)

        pygame.display.update()
        clock.tick(60)

    if not run:    
        PhaseAmount = 0
        amount = 1
        run = True