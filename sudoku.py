import pygame
import sys
pygame.init()
puraScreen = pygame.display.set_mode((480,650))
pygame.display.set_caption("Sudoku")


title = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\title.png")
one = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\numberssss\\1.png")
doh = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\numberssss\\2.png") 
teen = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\numberssss\\3.png")
char = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\numberssss\\4.png")
five = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\numberssss\\5.png")
che = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\numberssss\\6.png")
svn = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\numberssss\\7.png")
ate = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\numberssss\\8.png")
noh = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\numberssss\\9.png")
win = pygame.image.load("C:\\Users\\Jamal\\Desktop\\s\\win.png")
 
A = 40
B = 158  
 
game = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

r = 0
c = 0

clock = pygame.time.Clock() 

while True:
    for joBhiKara in pygame.event.get():
        if joBhiKara.type == pygame.QUIT:
            pygame.quit
            exit()       #yaar ye woh sys module se aaya h, kyuki quit aur init clash kr rhe h
        
        #ye no. wala part h

        if joBhiKara.type == pygame.KEYDOWN:
            if joBhiKara.key == pygame.K_1:
                puraScreen.blit(one, (A, B))
                game[r][c] = 1
            if joBhiKara.key == pygame.K_2:
                puraScreen.blit(doh, (A, B))
                game[r][c] = 2
            if joBhiKara.key == pygame.K_3:
                puraScreen.blit(teen, (A, B))
                game[r][c] = 3
            if joBhiKara.key == pygame.K_4:
                puraScreen.blit(char, (A, B))
                game[r][c] = 4
            if joBhiKara.key == pygame.K_5:
                puraScreen.blit(five, (A, B))
                game[r][c] = 5
            if joBhiKara.key == pygame.K_6:
                puraScreen.blit(che, (A, B))
                game[r][c] = 6
            if joBhiKara.key == pygame.K_7:
                puraScreen.blit(svn, (A, B))
                game[r][c] = 7
            if joBhiKara.key == pygame.K_8:
                puraScreen.blit(ate, (A, B))
                game[r][c] = 8
            if joBhiKara.key == pygame.K_9:
                puraScreen.blit(noh, (A, B))
                game[r][c] = 9
            
            #ye keys wala part h

            if joBhiKara.key == pygame.K_RIGHT:
                A = A + 45
                c = c + 1
            if joBhiKara.key == pygame.K_LEFT:
                A = A - 45
                c = c - 1
            if joBhiKara.key == pygame.K_DOWN:
                B = B + 45
                r = r + 1
            if joBhiKara.key == pygame.K_UP:
                B = B - 45
                r = r - 1
    
    
    puraScreen.blit(title, (50, 0))

    pygame.draw.rect(puraScreen, pygame.Color("white"), pygame.Rect(30,150, 420, 420),10)
    
    for i in range(0,9):
        pygame.draw.line(puraScreen, pygame.Color("white"),(40,(200 + i*45)),(440,(200 + i*45)),2)

    for i in range(0,8):
        pygame.draw.line(puraScreen, pygame.Color("white"),((80 + i*45),150),((80 + i*45),558))


    if game == [[1,0,0,0,0,0,0,0,9],
                [2,0,0,0,0,0,0,0,0],
                [3,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]]:
        puraScreen.blit(win, (0,0))

    
   
    pygame.display.update()

    
