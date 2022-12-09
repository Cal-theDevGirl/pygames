import pygame
import time
import random
 
pygame.init()

#Create Settings Menu
def settings_menu():
    #Create Settings Window
    menu_window = pygame.display.set_mode((300,300))
    pygame.display.set_caption('Settings Menu')

    #Create Input Fields for Settings
    speed_input = pygame.input.Input()
    snake_color_input = pygame.input.Input()
    bg_color_input = pygame.input.Input()

    #Create 'save' button for settings menu
    save_button = pygame.button('Save')

    #Create 'Settings' button for the game menu
    settings_button = pygame.button('Settings')

    #Create loop to display settings menu and handle user input
    while True:
        menu_window.fill((255,255,255)) #set background of settings menu to white
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #close the window if use clicks close button
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and save_button.collidepint(event.pos):
                #if user clicks save button update game settings
                global speed
                speed = speed_input.value
                global white
                white = snake_color_input.value
                global blue
                blue = bg_color_input.value
                pygame.display.quit()
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and settings_button.collidepoint(event.pos):
                settings_menu()
            settings_button.draw()
        #Draw input fields, save button, and settings button on screen
        speed_input.draw()
        snake_color_input.draw()
        bg_color_input.draw()
        save_button.draw()
        settings_button.draw()
        pygame.display.update()

#game code
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('SDL Snake')

clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 10
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("consolas", 35)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()