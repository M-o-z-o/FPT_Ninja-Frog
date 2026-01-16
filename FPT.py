'''
-----------------------------------------------------------------------------
Program Name: (never put your personal name or information on the Internet)
Program Description:

-----------------------------------------------------------------------------
References:

(put a link to your reference here but also add a comment in the code below where you used the reference)

-----------------------------------------------------------------------------

Additional Libraries/Extensions:

(put a list of required extensions so that the user knows that they need to download extra features)

-----------------------------------------------------------------------------

Known bugs:

(put a list of known bugs here, if you have any)

----------------------------------------------------------------------------


Program Reflection:
I think this project deserves a level XXXXXX because ...

 Level 3 Requirements Met:
• 
•  
•  
•  
•  
• 

Features Added Beyond Level 3 Requirements:
• 
•  
•  
•  
•  
• 
-----------------------------------------------------------------------------
'''

import pygame
import os 
import random

dir = os.path.dirname(os.path.abspath(__file__))

# random x pos for frog and saw
xFrog = random.randint(300,600)
xSaw = random.randint(100,800)

bg = pygame.image.load(os.path.join(dir,"nfbg.jpg"))
startButton = pygame.transform.scale(pygame.image.load(os.path.join(dir,"buttonStart.png")),(200,100))
howToButton = pygame.transform.scale(pygame.image.load(os.path.join(dir,"buttonHowTo.png")),(450,100))
backButton = pygame.transform.scale(pygame.image.load(os.path.join(dir,"buttonBack.png")),(200,100))
frogSprite = pygame.transform.scale(pygame.image.load(os.path.join(dir,"idle01.png")),(96,96))
sawSprite = pygame.transform.scale(pygame.image.load(os.path.join(dir,"saw03.png")),(96,96))

pygame.init()
screen = pygame.display.set_mode((1000,667))
clock = pygame.time.Clock()
running = True
gamestate = "homePage"
hoverEffect1 = "dark gray"

# fonts and sound effects
clickSFX = pygame.mixer.Sound(os.path.join(dir,"start.wav"))
fontText = pygame.font.Font(os.path.join(dir,"minecraft.ttf"), 70)
backText =  pygame.font.Font(os.path.join(dir,"minecraft.ttf"), 60)


# *********SETUP**********
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouseX, mouseY = pygame.mouse.get_pos()
    print(mouseX,mouseY)

    if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
        #checking if left mouse button is clicked to change screens
        if gamestate == "homePage":
            if 235 < mouseX < 770 and 240 < mouseY < 330:
                gamestate = "startMenu"
                clickSFX.play()
                xFrog = random.randint(300,600)
                xSaw = random.randint(100,800)
            if 235 < mouseX < 770 and 360 < mouseY < 450:
                gamestate = "howToMenu"
                clickSFX.play()
        if gamestate == "howToMenu":
            if 800 < mouseX < 970 and 550 < mouseY < 640:
                gamestate = "homePage"
                clickSFX.play()
        if gamestate == "startMenu":
            if 800 < mouseX < 970 and 550 < mouseY < 640:
                gamestate = "homePage"
                clickSFX.play()

    if gamestate == "homePage":
        screen.blit(bg,(0,0))

        # hover effect for buttons
        if 235 < mouseX < 770 and 240 < mouseY < 330:
            pygame.draw.rect(screen,hoverEffect1, (235,240,535,90))
        else:
            pygame.draw.rect(screen,"white", (235,240,535,90))

        if 235 < mouseX < 770 and 360 < mouseY < 450:
            pygame.draw.rect(screen,hoverEffect1, (235,360,535,90))
        else:
            pygame.draw.rect(screen,"white", (235,360,535,90))

        text = fontText.render("Instructions", True, "black")
        screen.blit(text,(295,380))
        text = fontText.render("Start", True, "black")
        screen.blit(text,(410,260))
        text = fontText.render("NINJAFROG'S ADVENTURE!", True, "white")
        screen.blit(text,(50,50))

    if gamestate == "howToMenu":
        # putting text on screen
        screen.blit(bg,(0,0))
        text = fontText.render("INSTRUCTIONS!", True, "white")
        screen.blit(text,(250,50))
        text = fontText.render("d = move", True, "white")
        screen.blit(text,(50,150))
        text = fontText.render("space = jump", True, "white")
        screen.blit(text,(50,320))
        text = fontText.render("jump over obstacles", True, "white")
        screen.blit(text,(45,395))
        text = fontText.render("collect powerups", True, "white")
        screen.blit(text,(50,220))

        if 800 < mouseX < 970 and 550 < mouseY < 640:
            pygame.draw.rect(screen,hoverEffect1, (800,550,170,90))
        else:
            pygame.draw.rect(screen,"white", (800,550,170,90))

        text = backText.render("Back", True, "black")
        screen.blit(text,(810,570))

    if gamestate == "startMenu":
        screen.blit(bg,(0,0))
        screen.blit(frogSprite,(xFrog,495))
        screen.blit(sawSprite,(xSaw,470))

        if 800 < mouseX < 970 and 550 < mouseY < 640:
            pygame.draw.rect(screen,hoverEffect1, (800,550,170,90))
        else:
            pygame.draw.rect(screen,"white", (800,550,170,90))

        text = backText.render("Back", True, "black")
        screen.blit(text,(810,570))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
