import pygame
import sys
import points
import math
#import screenDisplay
import inventory
import storeButtons
import inventoryButtons

pygame.init()

res = (375,667)

screen = pygame.display.set_mode(res)

color = (0, 0, 0)

color_light = (170, 170, 170)

color_dark = (255, 0, 0)

width = screen.get_width()

height = screen.get_height()

#set up inventory for later
inventory.initializeInventory()

####Calculating the button sizing#####
#Top four buttons
actionButtonWidth = math.floor(width / 4)
actionButtonWidthBuffer = math.floor(actionButtonWidth / 4)
actionButtonHeight = math.floor((height / 4) / 3)
actionButtonHeightBuffer = math.floor(actionButtonHeight / 2)

#Button locations
topThreeLine = [15, 39]
medidtateLine = [64, 103]
waterButton = [8, 121]
eatButton = [131, 244]
exerciseButton = [254,367]
meditateButton = [eatButton[0], eatButton[1]]
dailyQuoteButton = [8, 367, 448, 493]
storeButton = [8,177,580,625]
inventoryButton = [198, 367, 580, 625]



# defining a font 
smallfont = pygame.font.SysFont('Corbel',35)
quoteFont = pygame.font.SysFont('Corbel', 16) 
  
# rendering a text written in 
# this font 
water = smallfont.render('Water' , True , color)
pointsText = smallfont.render(points.displayPonts(), True, color)


#Test home screen image
image = pygame.image.load('Resources/Home.png')

  
while True: 

    # completely fill the surface object 
    # with white colour 
    #screen.fill((255,255,255)) 
  
    # copying the image surface object 
    # to the display surface object at 
    # (0, 0) coordinate. 
    screen.blit(image, (0, 0)) 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #Buttons!
            #Water
            if waterButton[0] <= mouse[0] <= waterButton[1]  and topThreeLine[0] <= mouse[1] <= topThreeLine[1]: 
                points.drank_water(screen) 
            #Eat
            if eatButton[0] <= mouse[0] <= eatButton[1] and topThreeLine[0] <= mouse[1] <= topThreeLine[1]: 
                points.ate_food(screen)
            #Exercise
            if exerciseButton[0] <= mouse[0] <= exerciseButton[1] and topThreeLine[0] <= mouse[1] <= topThreeLine[1]: 
                points.exercise(screen)
            #Meditate
            if meditateButton[0] <= mouse[0] <= meditateButton[1] and medidtateLine[0] <= mouse[1] <= medidtateLine[1]:
                points.meditate(screen)
            #Daily Quote Reveal
            if dailyQuoteButton[0] <= mouse[0] <= dailyQuoteButton[1] and dailyQuoteButton[2] <= mouse[1] <= dailyQuoteButton[3]:
                quote = points.daily_quote()
                quoteText = quoteFont.render(quote, True, color)
                screen.fill((255,255,255))
                pygame.draw.rect(screen,(173,211,173),[10,(screen.get_height()/2 -30),355,80])
                screen.blit(quoteText, (20, (screen.get_height()/2)))
                pygame.display.update()
                while True:
                    #screen.blit(text, textRect)
                    event = pygame.event.wait()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        break
            #Store
            if storeButton[0] <= mouse[0] <= storeButton[1] and storeButton[2] <= mouse[1] <= storeButton[3]:
                #screenDisplay.switch(6)
                storeButtons.accessStore(screen)
            #Inventory
            if inventoryButton[0] <= mouse[0] <= inventoryButton[1] and inventoryButton[2] <= mouse[1] <= inventoryButton[3]:
                inventoryButtons.accessInventory(screen)
    

                  
    # fills the screen with a color 
    #screen.fill((255,255,255)) 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos()

    """
    # if mouse is hovered on a button it 
    # changes to lighter shade 
    #Water Button
    if ((waterButton[0] <= mouse[0] <= waterButton[1])  and (topThreeLine[0] <= mouse[1] <= topThreeLine[1]), 3): 
        pygame.draw.rect(screen,color_light,[waterButton[0],topThreeLine[0],113,39], 3) #water
        pygame.draw.rect(screen,color_dark,[eatButton[0],topThreeLine[0],113,39], 3) #eat
        pygame.draw.rect(screen,color_dark,[exerciseButton[0],topThreeLine[0],113,39], 3) #exercise
        pygame.draw.rect(screen,color_dark,[meditateButton[0], medidtateLine[0] ,113,39], 3) #meditate
    #Eat
    elif eatButton[0] <= mouse[0] <= eatButton[1] and topThreeLine[0] <= mouse[1] <= topThreeLine[1]: 
        pygame.draw.rect(screen,color_dark,[waterButton[0],topThreeLine[0],113,39],3) #water
        pygame.draw.rect(screen,color_light,[eatButton[0],topThreeLine[0],113,39],3) #eat
        pygame.draw.rect(screen,color_dark,[exerciseButton[0],topThreeLine[0],113,39],3) #exercise
        pygame.draw.rect(screen,color_dark,[meditateButton[0], medidtateLine[0] ,113,39],3) #meditate
    #Exercise
    elif exerciseButton[0] <= mouse[0] <= exerciseButton[1] and topThreeLine[0] <= mouse[1] <= topThreeLine[1]: 
        pygame.draw.rect(screen,color_dark,[waterButton[0],topThreeLine[0],113,39],3) #water
        pygame.draw.rect(screen,color_dark,[eatButton[0],topThreeLine[0],113,39],3 ) #eat
        pygame.draw.rect(screen,color_light,[exerciseButton[0],topThreeLine[0],113,39],3 )  #exercise
        pygame.draw.rect(screen,color_dark,[meditateButton[0], medidtateLine[0] ,113,39],3 ) #meditate
    #Meditate
    elif meditateButton[0] <= mouse[0] <= meditateButton[1] and medidtateLine[0] <= mouse[1] <= medidtateLine[1]:
        pygame.draw.rect(screen,color_dark,[waterButton[0],topThreeLine[0],113,39],3) #water
        pygame.draw.rect(screen,color_dark,[eatButton[0],topThreeLine[0], 113 ,39],3) #eat
        pygame.draw.rect(screen,color_dark,[exerciseButton[0],topThreeLine[0],113,39],3) #exercise
        pygame.draw.rect(screen,color_light,[meditateButton[0], medidtateLine[0] ,113 ,39],3) #meditate
    
    else: #Draw all the rectangles
        pygame.draw.rect(screen,color_dark,[waterButton[0],topThreeLine[0],113,39],3) #water
        pygame.draw.rect(screen,color_dark,[eatButton[0],topThreeLine[0],113,39],3) #eat
        pygame.draw.rect(screen,color_dark,[exerciseButton[0],topThreeLine[0],113,39],3 ) #exercise
        pygame.draw.rect(screen,color_dark,[meditateButton[0], medidtateLine[0] ,113,39,3]) #meditate
    """
      
    # superimposing the text onto our button 
    #screen.blit(water , (width/2+50,height/2)) 
    pointsText = smallfont.render(points.displayPonts(), True, color)
    screen.blit(pointsText, (width/2+50, height/2 + height/4 + 15))
      
    # updates the frames of the game 
    pygame.display.update() 