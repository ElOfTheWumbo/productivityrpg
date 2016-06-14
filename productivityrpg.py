#imports pygame and time
import pygame
import time
import random

#initializes pygame
pygame.init()

#sets the window width and height
display_width = 800
display_height = 600

#colors
white = (255,255,255)
black = (0,0,0)
grey = (70,58,58)


#Makes a window with the dimensions listed above
game_display = pygame.display.set_mode((display_width,display_height))
#sets title on window
pygame.display.set_caption("ProductivityRPG")
#game clock
clock = pygame.time.Clock()


#used to display text
def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

#used to display messages
def message_display(text):
    large_text = pygame.font.Font("freesansbold.ttf",115)
    text_surface, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width/2),(display_height/2))
    game_display.blit(text_surface, text_rect)
    pygame.display.update()

#function that creates buttons
def button(message,x,y,width,height,colour,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+width > mouse [0] > x and y+height > mouse [1] >y:
        pygame.draw.rect(game_display,colour,(x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "stop":
                pygame.quit()
                quit()
            elif action == "habitsscreen":
                energy_screen_habits()

    small_text = pygame.font.Font("freesansbold.ttf",20)
    text_surface, text_rect = text_objects(message, small_text)
    text_rect.center = ((x+(width/2)), y + (height/2))
    game_display.blit(text_surface,text_rect)


#game intro screen
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(white)
        large_text = pygame.font.Font("freesansbold.ttf",90)
        text_surface, text_rect = text_objects("ProductivityRPG", large_text)
        text_rect.center = ((display_width/2),(display_height/2))
        game_display.blit(text_surface, text_rect)

        button("Start",150,450,100,50,grey,"play")
        button("Quit",550,450,100,50,grey,"stop")

        pygame.display.update()

def game_over():
    #
    dead = True
    global player_health
    player_health += 100
    #
    while dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #
        game_display.fill(white)
        large_text = pygame.font.Font("freesansbold.ttf",90)
        text_surface, text_rect = text_objects("You Died", large_text)
        text_rect.center = ((display_width/2),(display_height/2))
        game_display.blit(text_surface, text_rect)
        #
        button("Start",150,450,100,50,grey,"play")
        button("Quit",550,450,100,50,grey,"stop")
        #
        pygame.display.update()

global battle_time,enemy_dead,computer_health, player_health

computer_health = 100
player_health = 100
player_energy = 5
enemy_dead = False
habit_screen = False

def battle():
    global computer_health, player_health, enemy_dead, player_energy
    battle_time = True

    while battle_time:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    computer_health -= 100
                    comp_display = str(computer_health)
                    player_health -= random.randint(10,15)
                    player_display = str(player_health)

                    print("Computer Health: " + comp_display)
                    print("Player Health: " + player_display)

                if event.key == pygame.K_z:
                    player_health += 20


                    player_health -= random.randint(10,15)
                    player_display = str(player_health)

                    print("Player Health: " + player_display)
                    print("Computer Health: " + comp_display)

            if computer_health <= 0:
                battle_time = False
                enemy_dead = True
                player_energy -= 1
                game_loop()

            if player_health <= 0:
                game_over()



        game_display.fill(white)
        large_text = pygame.font.Font("freesansbold.ttf",45)
        text_surface, text_rect = text_objects("Fight", large_text)
        text_rect.center = ((display_width/2),(display_height/8))
        game_display.blit(text_surface, text_rect)


        button("Press X to Attack",150,450,100,50,grey,)
        button("Press Z to Heal",550,450,100,50,grey,)

        game_display.blit(knight_image,(250,250))
        game_display.blit(skeleton_image,(450,250))




        pygame.display.update()

def energy_screen():
    screen = True
    global player_energy, habit_screen
    player_energy_display = str(player_energy)

    while screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(white)
        #Energy
        large_text = pygame.font.Font("freesansbold.ttf",90)
        text_surface, text_rect = text_objects("Energy", large_text)
        text_rect.center = ((display_width/2),(display_height/4))
        game_display.blit(text_surface, text_rect)

        #
        large_text = pygame.font.Font("freesansbold.ttf",45)
        text_surface, text_rect = text_objects("You have " + player_energy_display + " energy left", large_text)
        text_rect.center = ((display_width/2),(display_height/2))
        game_display.blit(text_surface, text_rect)


        button("Habits",150,450,100,50,grey,"habitsscreen")
        button("Resume",550,450,100,50,grey,"play")


        pygame.display.update()

def energy_screen_habits():
    screen = True
    while screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(white)
        #Energy
        large_text = pygame.font.Font("freesansbold.ttf",90)
        text_surface, text_rect = text_objects("Energy", large_text)
        text_rect.center = ((display_width/2),(display_height/4))
        game_display.blit(text_surface, text_rect)

        button("Habit One",150,450,100,50,grey,"play")
        button("Habit Two",550,450,100,50,grey,"play")


        pygame.display.update()

background_image = pygame.image.load("background.png")
skeleton_image = pygame.image.load("skeleton.png")
hoplite_image = pygame.image.load("hoplite.png")
#loads image of knight into the game
knight_image = pygame.image.load("knight.png")



#displays the knight image onto the screen
def knight(x,y):
    game_display.blit(knight_image,(x,y))

def skeleton():
    game_display.blit(skeleton_image,(450,250))


def game_loop():
#x and y values for the starting location of the knight
    x = (display_width * 0.2)
    y = (display_height * 0.4)
    x_change = 0
    y_change = 0
    #While the game is still running quit will be set to false
    global battle_time, enemy_dead, player_energy
    quit = False


    while not quit:
        # Sets boundaries that the player cannot pass
        if x <= 0:
            x = 0
        if x >= 625:
            x = 625    
        if y <= 200:
            y = 200 
        if y >= 425:
            y = 425
        #Position of player character
        x+= x_change
        y+= y_change

        #Adds images
        game_display.fill(white)
        game_display.blit(background_image,(0,0))
        knight(x,y)


        #sets the game clock to 60 frames per second
        clock.tick(60)
        if enemy_dead == False:
            skeleton()
            pygame.display.update()
            if y < 250 and 300 and x > 450:
                battle_time = True
                battle()

        if enemy_dead == True:
            game_display.fill(white)
            game_display.blit(background_image,(0,0))
            knight(x,y)
            pygame.display.update()



        for event in pygame.event.get():
            #Exits the program
            if event.type == pygame.QUIT:
                quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -10
                elif event.key == pygame.K_d:
                    x_change = +10
                elif event.key == pygame.K_w:
                    y_change = -10
                elif event.key == pygame.K_s:
                    y_change = +10
                elif event.key == pygame.K_ESCAPE:
                    energy_screen()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0

game_intro()
game_loop()

#uninitializes pygame
pygame.quit()
quit()