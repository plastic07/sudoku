import pygame
import sys
pygame.init()
puraScreen = pygame.display.set_mode((480,650))
pygame.display.set_caption("Sudoku")

#box = pygame.draw.rect(puraScreen, (50, 40, 10), pygame.Rect(400, 400, 400, 400))

imp = pygame.image.load("C:\\Users\\DELL\\Downloads\\gfg.png").convert()
 


 

while True:
    for joBhiKara in pygame.event.get():
        if joBhiKara.type == pygame.QUIT:
            pygame.quit
            exit()        #yaar ye woh sys module se aaya h, kyuki quit aur init clash kr rhe h
    #puraScreen.blit(box,(0,0))
    puraScreen.blit(imp, (50, 50))

    pygame.draw.rect(puraScreen, pygame.Color("white"), pygame.Rect(30,150, 420, 420),10)
    
    for i in range(0,9):
        pygame.draw.line(puraScreen, pygame.Color("white"),(40,(200 + i*45)),(440,(200 + i*45)),2)

    for i in range(0,8):
        pygame.draw.line(puraScreen, pygame.Color("white"),((80 + i*45),150),((80 + i*45),558))
    
    
    pygame.display.update()
    