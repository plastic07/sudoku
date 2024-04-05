import pygame
import sys
pygame.init()
puraScreen = pygame.display.set_mode((480,650))
pygame.display.set_caption("Sudoku")


title = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\title.png")
one = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\1.png")
doh = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\2.png") 
teen = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\3.png")
char = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\4.png")
five = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\5.png")
che = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\6.png")
svn = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\7.png")
ate = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\8.png")
noh = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\9.png")
 
A = 40
B = 158  
 

while True:
    for joBhiKara in pygame.event.get():
        if joBhiKara.type == pygame.QUIT:
            pygame.quit
            exit()        #yaar ye woh sys module se aaya h, kyuki quit aur init clash kr rhe h
        
        #ye no. wala part h

        if joBhiKara.type == pygame.KEYDOWN:
            if joBhiKara.key == pygame.K_1:
                puraScreen.blit(one, (A, B))
            if joBhiKara.key == pygame.K_2:
                puraScreen.blit(doh, (A, B))
            if joBhiKara.key == pygame.K_3:
                puraScreen.blit(teen, (A, B))
            if joBhiKara.key == pygame.K_4:
                puraScreen.blit(char, (A, B))
            if joBhiKara.key == pygame.K_5:
                puraScreen.blit(five, (A, B))
            if joBhiKara.key == pygame.K_6:
                puraScreen.blit(che, (A, B))
            if joBhiKara.key == pygame.K_7:
                puraScreen.blit(svn, (A, B))
            if joBhiKara.key == pygame.K_8:
                puraScreen.blit(ate, (A, B))
            if joBhiKara.key == pygame.K_9:
                puraScreen.blit(noh, (A, B))
            
            #ye keys wala part h

            if joBhiKara.key == pygame.K_RIGHT:
                A = A + 45
            if joBhiKara.key == pygame.K_LEFT:
                A = A - 45
            if joBhiKara.key == pygame.K_DOWN:
                B = B + 45
            if joBhiKara.key == pygame.K_UP:
                B = B - 45
    
    
    puraScreen.blit(title, (50, 0))

    pygame.draw.rect(puraScreen, pygame.Color("white"), pygame.Rect(30,150, 420, 420),10)
    
    for i in range(0,9):
        pygame.draw.line(puraScreen, pygame.Color("white"),(40,(200 + i*45)),(440,(200 + i*45)),2)

    for i in range(0,8):
        pygame.draw.line(puraScreen, pygame.Color("white"),((80 + i*45),150),((80 + i*45),558))


    
   
    pygame.display.update()