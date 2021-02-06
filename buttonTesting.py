import pygame
import sys
import points
import math

pygame.init()

res = (750,1000)

screen = pygame.display.set_mode(res)

color = (0, 0, 0)

color_light = (170, 170, 170)

color_dark = (255, 0, 0)

width = screen.get_width()

height = screen.get_height()

####Calculating the button sizing#####
#Top four buttons
actionButtonWidth = math.floor(width / 4)
actionButtonWidthBuffer = math.floor(actionButtonWidth / 4)
actionButtonHeight = math.floor((height / 4) / 3)
actionButtonHeightBuffer = math.floor(actionButtonHeight / 2)

#Bottom Three Buttons
bottomButtonsWidth = width - (2 * actionButtonWidthBuffer)

#Therefore, the button locations are as follows
topThreeLine = [actionButtonHeightBuffer, (actionButtonHeightBuffer + actionButtonHeight)]
medidtateLine = [(topThreeLine[1] + actionButtonHeightBuffer), (topThreeLine[1] * 2 )]
waterButton = [actionButtonWidthBuffer, (actionButtonWidth + actionButtonWidthBuffer)]
eatButton = [(waterButton[1] + actionButtonWidthBuffer), (waterButton[1] * 2)]
exerciseButton = [(eatButton[1] + actionButtonWidthBuffer), (width - actionButtonWidthBuffer)]
meditateButton = [eatButton[0], eatButton[1]]



# defining a font 
smallfont = pygame.font.SysFont('Corbel',35) 
  
# rendering a text written in 
# this font 
text = smallfont.render('Water' , True , color) 
  
while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #Buttons!
            #Water
            if waterButton[0] <= mouse[0] <= waterButton[1]  and topThreeLine[0] <= mouse[1] <= topThreeLine[1]: 
                points.drank_water() 
            #Eat
            if eatButton[0] <= mouse[0] <= eatButton[1] and topThreeLine[0] <= mouse[1] <= topThreeLine[1]: 
                points.ate_food()
            #Exercise
            if exerciseButton[0] <= mouse[0] <= exerciseButton[1] and topThreeLine[0] <= mouse[1] <= topThreeLine[1]: 
                points.exercise()
            #Meditate
            if meditateButton[0] <= mouse[0] <= meditateButton[1] and medidtateLine[0] <= mouse[1] <= medidtateLine[1]:
                points.meditate()
            #Daily Quote Reveal
            #Store
    

                  
    # fills the screen with a color 
    screen.fill((255,255,255)) 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos()

    #Draw the rest of the screen
    #Dog
    #Points Score
      
    # if mouse is hovered on a button it 
    # changes to lighter shade 
    #Water Button
    if ((waterButton[0] <= mouse[0] <= waterButton[1])  and (topThreeLine[0] <= mouse[1] <= topThreeLine[1])): 
        pygame.draw.rect(screen,color_light,[waterButton[0],topThreeLine[0],140,40]) #water
        pygame.draw.rect(screen,color_dark,[eatButton[0],topThreeLine[0],140,40]) #eat
        pygame.draw.rect(screen,color_dark,[exerciseButton[0],topThreeLine[0],140,40]) #exercise
        pygame.draw.rect(screen,color_dark,[meditateButton[0], medidtateLine[0] ,140,40]) #meditate
    #Eat
    elif eatButton[0] <= mouse[0] <= eatButton[1] and topThreeLine[0] <= mouse[1] <= topThreeLine[1]: 
        pygame.draw.rect(screen,color_dark,[waterButton[0],topThreeLine[0],140,40]) #water
        pygame.draw.rect(screen,color_light,[eatButton[0],topThreeLine[0],140,40]) #eat
        pygame.draw.rect(screen,color_dark,[exerciseButton[0],topThreeLine[0],140,40]) #exercise
        pygame.draw.rect(screen,color_dark,[meditateButton[0], medidtateLine[0] ,140,40]) #meditate
    #Exercise
    elif exerciseButton[0] <= mouse[0] <= exerciseButton[1] and topThreeLine[0] <= mouse[1] <= topThreeLine[1]: 
        pygame.draw.rect(screen,color_dark,[waterButton[0],topThreeLine[0],140,40]) #water
        pygame.draw.rect(screen,color_dark,[eatButton[0],topThreeLine[0],140,40]) #eat
        pygame.draw.rect(screen,color_light,[exerciseButton[0],topThreeLine[0],140,40])  #exercise
        pygame.draw.rect(screen,color_dark,[meditateButton[0], medidtateLine[0] ,140,40]) #meditate
    #Meditate
    elif meditateButton[0] <= mouse[0] <= meditateButton[1] and medidtateLine[0] <= mouse[1] <= medidtateLine[1]:
        pygame.draw.rect(screen,color_dark,[waterButton[0],topThreeLine[0],140,40]) #water
        pygame.draw.rect(screen,color_dark,[eatButton[0],topThreeLine[0],140,40]) #eat
        pygame.draw.rect(screen,color_dark,[exerciseButton[0],topThreeLine[0],140,40]) #exercise
        pygame.draw.rect(screen,color_light,[meditateButton[0], medidtateLine[0] ,140,40]) #meditate
    
    else: #Draw all the rectangles
        pygame.draw.rect(screen,color_dark,[waterButton[0],topThreeLine[0],140,40]) #water
        pygame.draw.rect(screen,color_dark,[eatButton[0],topThreeLine[0],140,40]) #eat
        pygame.draw.rect(screen,color_dark,[exerciseButton[0],topThreeLine[0],140,40]) #exercise
        pygame.draw.rect(screen,color_dark,[meditateButton[0], medidtateLine[0] ,140,40]) #meditate
      
    # superimposing the text onto our button 
    screen.blit(text , (width/2+50,height/2)) 
      
    # updates the frames of the game 
    pygame.display.update() 