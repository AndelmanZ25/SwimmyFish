# Importing modules
import pygame
import random
import math
import sys

#=======================#

maxscore = 1500 # The amount of points a player needs to win game

#=======================#

# Initializing pygame
pygame.init()

# LOADING PROJECT SOUND FILES
lobbymusic = pygame.mixer.Sound('src/audio/lobby.mp3')
gamemusic = pygame.mixer.Sound('src/audio/playing.mp3')
gamemusic2 = pygame.mixer.Sound('src/audio/playing2.mp3')
gamemusic3 = pygame.mixer.Sound('src/audio/playing3.mp3')
gameovermusic = pygame.mixer.Sound('src/audio/gameover.mp3')
coincollect = pygame.mixer.Sound('src/audio/coincollect.mp3')
winningmusic = pygame.mixer.Sound('src/audio/win.mp3')

# Setting up pygame screen
#pygame.display.set_caption('src/Fish Game')

def miniseconds_seconds(numbers):
    return numbers*1000 # Because pygame waits in miliseconds and 1 miliscond equals 1000 seconds, we multiply by 1000.

def loading_screen():
    pygame.mixer.stop()
    screen = pygame.display.set_mode((960, 540))

    loading_image = pygame.image.load('src/loading.png')
    screen.blit(loading_image, (0, 0))
    pygame.display.flip()
    pygame.time.wait(miniseconds_seconds(5))

def gameover_screen():
    pygame.mixer.stop() # Stop all currently playing music to play
    gameovermusic.play()

    # Sets up the screen dimentions
    screen = pygame.display.set_mode((960, 540))

    # This was for the old gameover screen but we'll just keep this here
    """
    font = pygame.font.SysFont(None, 75)
    print('Console Log: The game has ended. Player eliminated.')
    screen.fill((0, 0, 0))
    gameover_text = font.render("Game Over!", True, (255, 0, 0))
    gameover_rect = gameover_text.get_rect()
    gameover_rect.center = screen.get_rect().center
    screen.blit(gameover_text, gameover_rect)
    """

    gameover_image = pygame.image.load('src/gameover.png')
    screen.blit(gameover_image, (0, 0))
    pygame.display.flip()
    pygame.time.wait(miniseconds_seconds(5))
    start()
    #pygame.quit()
    #exit()

def youwin():
    pygame.mixer.stop()
    winningmusic.play()
    screen = pygame.display.set_mode((960, 540))

    print('Console Log: The game has ended. The player has won!')
    winningimage = pygame.image.load('src/winning.png')
    screen.blit(winningimage, (0, 0))
    pygame.display.flip()
    pygame.time.wait(miniseconds_seconds(10))
    pygame.quit()
    exit()

def stage3(): # Last and final stage. Made to be a lot harder than the other two stages.
    loading_screen()
    gamemusic3.play()

    # Screen size
    width = 960
    height = 540
    screen = pygame.display.set_mode((width, height))

    # Background
    background = pygame.image.load('src/background3.png')
    backgroundX = 0
    backgroundWidth = 1920

    # Game Components
    # Bubbles
    green_30 = pygame.image.load('src/green_30.png')
    green_30X = 970
    green_30Y = random.randint(20, 500)

    green_40 = pygame.image.load('src/green_40.png')
    green_40X = 1200
    green_40Y = random.randint(20, 500)

    green_50 = pygame.image.load('src/green_50.png')
    green_50X = 1500
    green_50Y = random.randint(20, 500)

    red = pygame.image.load('src/red.png')
    redX = 600
    redY = random.randint(20, 500)
    
    zacoin = pygame.image.load('src/zacoin.png')
    zacoinX = 2500
    zacoinY = random.randint(20, 500)

    red_65 = pygame.image.load('src/red_65.png')
    red_65X = 500
    red_65Y = random.randint(20, 500)

    red2 = pygame.image.load('src/red_65.png')
    red2_X = 200
    red2_Y = random.randint(20, 500)

    red3 = pygame.image.load('src/red.png')
    red3_X = 260
    red3_Y = random.randint(20, 500)

    # Puts the bubble on the screen
    def bubbleGenerator(bubble, x, y):
        screen.blit(bubble, (x, y))

    # Fish
    fish = pygame.image.load('src/fish.png')
    fishX = 20
    fishX_change = 0
    fishY = 200
    fishY_change = 0

    def fishPosition(x, y):
        screen.blit(fish, (x, y))

    # Score variables
    score = 0
    color = (0, 0, 0)
    font = pygame.font.SysFont(None, 20)

    def scoreGenerator(text, font):
        text = font.render(text, True, color)
        screen.blit(text, (700, 15))

    # Game over
    gameover = pygame.image.load('src/gameover.png')

    # Calculates the distnce for the fish to move.
    def distance(x1, y1, x2, y2):
        answer = math.sqrt(((x2 - (x1+50))**2) + ((y2 - (y1+50))**2))
        return answer

    # Running pygame screen until escape condition
    running = True
    while running:

        # For filling screen with any color using RGB
        screen.fill((0, 0, 0))

        # Adding and moving background image

        screen.blit(background, (backgroundX, 0))
        backgroundWidth -= 0.5
        screen.blit(background, (backgroundWidth, 0))
        backgroundX -= 0.5
        if backgroundX <= -1920:
            backgroundX = 0
            backgroundWidth = 1920

        # Checking all the event occurred while single iteration of while loop
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            # Events of pressing keys
            if event.type == pygame.KEYDOWN:
                # Changes fishs co-ordinates on pressing respective keys
                if event.key == pygame.K_SPACE:
                    fishY_change = -5

                if event.key == pygame.K_q:
                    gamemusic2.stop()
                    gameover_screen()
                    
                    """
                    screen.blit(pygame.image.load('src/gameover.png'), (960, 540))
                    pygame.display.flip()
                    running = False
                    pygame.time.wait(miniseconds_seconds(20))
                    pygame.quit()
                    exit()
                    """

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    fishY_change = 3

        # Limiting fish movement in the screen
        if fishY+fishY_change <= 0 or fishY+fishY_change >= 440:
            fishY_change = 0

        # Generating bubbles
        bubbleGenerator(green_30, green_30X, green_30Y)
        bubbleGenerator(green_40, green_40X, green_40Y)
        bubbleGenerator(green_50, green_50X, green_50Y)
        bubbleGenerator(red, redX, redY)
        bubbleGenerator(zacoin, zacoinX, zacoinY)
        bubbleGenerator(red_65, red_65X, red_65Y)
        
        bubbleGenerator(red2, red2_X, red2_Y)#####
        bubbleGenerator(red3, red3_X, red3_Y)

        # Changing fish position
        fishY += fishY_change
        fishPosition(fishX, fishY)
        fishPosition(fishX, fishY)

        # Checking for collisions by calculating distance b/w fish and the bubbles
        distanceGreen_30 = distance(fishX, fishY, green_30X, green_30Y)
        distanceGreen_40 = distance(fishX, fishY, green_40X, green_40Y)
        distanceGreen_50 = distance(fishX, fishY, green_50X, green_50Y)
        distenceZacoin = distance(fishX, fishY, zacoinX, zacoinY)

        distanceRed = distance(fishX, fishY, redX, redY)
        distanceRed2 = distance(fishX, fishY, red_65X, red_65Y)

        distanceRed22 = distance(fishX, fishY, red2_X, red2_Y)
        distanceRed23 = distance(fishX, fishY, red3_X, red3_Y)

        #print(f'Distance Red = {distanceRed}')
        #print(f'Distance Red 2 = {distanceRed2}')
        
        if distanceGreen_30 <= 40:
            coincollect.play()
            score += 25
        if distanceGreen_40 <= 40:
            coincollect.play()
            score += 50
        if distanceGreen_50 <= 40:
            coincollect.play()
            score += 75
        if distenceZacoin <= 40:
            coincollect.play()
            score += 150

        # Updating score
        text = f"Your Score: {score}"
        scoreGenerator(text, font)

        if score >= maxscore:
            gamemusic2.stop()
            youwin()

        # Controlling speed and reseting bubbles on no NO collision
        green_30X -= 3
        if green_30X <= 0 or distanceGreen_30 <= 40:
            green_30X = random.randint(960, 1500)
            green_30Y = random.randint(15, 500)

        green_40X -= 4
        if green_40X <= 0 or distanceGreen_40 <= 40:
            green_40X = random.randint(960, 1500)
            green_40Y = random.randint(15, 500)

        green_50X -= 5
        if green_50X <= 0 or distanceGreen_50 <= 40:
            green_50X = random.randint(960, 1500)
            green_50Y = random.randint(15, 500)

        redX -= 4
        if redX <= 0:
            redX = random.randint(960, 1500)
            redY = random.randint(15, 500)

        red_65X -= 3
        if red_65X <= 0:
            red_65X = random.randint(960, 1500)
            red_65Y = random.randint(15, 500)

        red3_X -= 3
        if red3_X <= 0:
            red3_X = random.randint(960, 1500)
            red3_Y = random.randint(15, 500)

        red2_X -= 4
        if red2_X <= 0:
            red2_X = random.randint(960, 1500)
            red2_Y = random.randint(15, 500)


        zacoinX -= 10
        if zacoinX <= 0 or distenceZacoin <= 40:
            zacoinX = random.randint(960, 1500)
            zacoinY = random.randint(15, 500)

        # IF PLAYER TOUCHES RED FISH / GAME END
        if distanceRed2 <= 40:
            pygame.mixer.stop()
            gameover_screen()

        if distanceRed <= 30:
            pygame.mixer.stop()
            gameover_screen()
 
        # distanceRed22, distanceRed23
        if distanceRed22 <= 30 or distanceRed23 <= 30:
            pygame.mixer.stop()
            gameover_screen()

        

        # Updating screen on each iteration
        pygame.display.update()

def stage2():
    loading_screen()
    gamemusic2.play()

    # Screen size
    width = 960
    height = 540
    screen = pygame.display.set_mode((width, height))

    # Background
    background = pygame.image.load('src/background2.png')
    backgroundX = 0
    backgroundWidth = 1920

    # Game Components
    # Bubbles
    green_30 = pygame.image.load('src/green_30.png')
    green_30X = 970
    green_30Y = random.randint(20, 500)

    green_40 = pygame.image.load('src/green_40.png')
    green_40X = 1200
    green_40Y = random.randint(20, 500)

    green_50 = pygame.image.load('src/green_50.png')
    green_50X = 1500
    green_50Y = random.randint(20, 500)

    red = pygame.image.load('src/red.png')
    redX = 600
    redY = random.randint(20, 500)
    
    zacoin = pygame.image.load('src/zacoin.png')
    zacoinX = 2500
    zacoinY = random.randint(20, 500)

    red_65 = pygame.image.load('src/red_65.png')
    red_65X = 500
    red_65Y = random.randint(20, 500)

    # Puts the bubble on the screen
    def bubbleGenerator(bubble, x, y):
        screen.blit(bubble, (x, y))

    # Fish
    fish = pygame.image.load('src/fish.png')
    fishX = 20
    fishX_change = 0
    fishY = 200
    fishY_change = 0

    def fishPosition(x, y):
        screen.blit(fish, (x, y))

    # Score variables
    score = 0
    color = (0, 0, 0)
    font = pygame.font.SysFont(None, 20)

    def scoreGenerator(text, font):
        text = font.render(text, True, color)
        screen.blit(text, (700, 15))

    # Game over
    gameover = pygame.image.load('src/gameover.png')

    # Calculates the distnce for the fish to move.
    def distance(x1, y1, x2, y2):
        answer = math.sqrt(((x2 - (x1+50))**2) + ((y2 - (y1+50))**2))
        return answer

    # Running pygame screen until escape condition
    running = True
    while running:

        # For filling screen with any color using RGB
        screen.fill((0, 0, 0))

        # Adding and moving background image

        screen.blit(background, (backgroundX, 0))
        backgroundWidth -= 0.5
        screen.blit(background, (backgroundWidth, 0))
        backgroundX -= 0.5
        if backgroundX <= -1920:
            backgroundX = 0
            backgroundWidth = 1920

        # Checking all the event occurred while single iteration of while loop
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            # Events of pressing keys
            if event.type == pygame.KEYDOWN:
                # Changes fishs co-ordinates on pressing respective keys
                if event.key == pygame.K_SPACE:
                    fishY_change = -5

                if event.key == pygame.K_q:
                    gamemusic2.stop()
                    gameover_screen()
                    
                    """
                    screen.blit(pygame.image.load('src/gameover.png'), (960, 540))
                    pygame.display.flip()
                    running = False
                    pygame.time.wait(miniseconds_seconds(20))
                    pygame.quit()
                    exit()
                    """

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    fishY_change = 3

        # Limiting fish movement in the screen
        if fishY+fishY_change <= 0 or fishY+fishY_change >= 440:
            fishY_change = 0

        # Generating bubbles
        bubbleGenerator(green_30, green_30X, green_30Y)
        bubbleGenerator(green_40, green_40X, green_40Y)
        bubbleGenerator(green_50, green_50X, green_50Y)
        bubbleGenerator(red, redX, redY)
        bubbleGenerator(zacoin, zacoinX, zacoinY)
        bubbleGenerator(red_65, red_65X, red_65Y)

        # Changing fish position
        fishY += fishY_change
        fishPosition(fishX, fishY)
        fishPosition(fishX, fishY)

        # Checking for collisions by calculating distance b/w fish and the bubbles
        distanceGreen_30 = distance(fishX, fishY, green_30X, green_30Y)
        distanceGreen_40 = distance(fishX, fishY, green_40X, green_40Y)
        distanceGreen_50 = distance(fishX, fishY, green_50X, green_50Y)
        distenceZacoin = distance(fishX, fishY, zacoinX, zacoinY)

        distanceRed = distance(fishX, fishY, redX, redY)
        distanceRed2 = distance(fishX, fishY, red_65X, red_65Y)

        #print(f'Distance Red = {distanceRed}')
        #print(f'Distance Red 2 = {distanceRed2}')
        
        if distanceGreen_30 <= 40:
            coincollect.play()
            score += 25
        if distanceGreen_40 <= 40:
            coincollect.play()
            score += 50
        if distanceGreen_50 <= 40:
            coincollect.play()
            score += 75
        if distenceZacoin <= 40:
            coincollect.play()
            score += 150

        # Updating score
        text = f"Your Score: {score}"
        scoreGenerator(text, font)

        if score >= maxscore:
            gamemusic2.stop()
            screen = pygame.display.set_mode((960, 540))

            loading_image = pygame.image.load('src/stage3.png')
            screen.blit(loading_image, (0, 0))
            pygame.display.flip()
            pygame.time.wait(miniseconds_seconds(2))

            stage3()

        # Controlling speed and reseting bubbles on no NO collision
        green_30X -= 3
        if green_30X <= 0 or distanceGreen_30 <= 40:
            green_30X = random.randint(960, 1500)
            green_30Y = random.randint(15, 500)

        green_40X -= 4
        if green_40X <= 0 or distanceGreen_40 <= 40:
            green_40X = random.randint(960, 1500)
            green_40Y = random.randint(15, 500)

        green_50X -= 5
        if green_50X <= 0 or distanceGreen_50 <= 40:
            green_50X = random.randint(960, 1500)
            green_50Y = random.randint(15, 500)

        redX -= 5
        if redX <= 0:
            redX = random.randint(960, 1500)
            redY = random.randint(15, 500)

        red_65X -= 6
        if red_65X <= 0:
            red_65X = random.randint(960, 1500)
            red_65Y = random.randint(15, 500)

        zacoinX -= 10
        if zacoinX <= 0 or distenceZacoin <= 40:
            zacoinX = random.randint(960, 1500)
            zacoinY = random.randint(15, 500)

        # IF PLAYER TOUCHES RED FISH / GAME END
        if distanceRed2 <= 40:
            gamemusic2.stop()
            gameover_screen()

        if distanceRed <= 30:
            gamemusic2.stop()
            gameover_screen()

        # Updating screen on each iteration
        pygame.display.update()

def stage1():
    loading_screen()
    gamemusic.play()

    # Screen size
    width = 960
    height = 540
    screen = pygame.display.set_mode((width, height))

    # Background
    background = pygame.image.load('src/background.png')
    backgroundX = 0
    backgroundWidth = 1920

    # Game Components
    # Bubbles
    green_30 = pygame.image.load('src/green_30.png')
    green_30X = 970
    green_30Y = random.randint(20, 500)

    green_40 = pygame.image.load('src/green_40.png')
    green_40X = 1200
    green_40Y = random.randint(20, 500)

    green_50 = pygame.image.load('src/green_50.png')
    green_50X = 1500
    green_50Y = random.randint(20, 500)

    red = pygame.image.load('src/red.png')
    redX = 600
    redY = random.randint(20, 500)
    
    zacoin = pygame.image.load('src/zacoin.png')
    zacoinX = 2500
    zacoinY = random.randint(20, 500)

    red_65 = pygame.image.load('src/red_65.png')
    red_65X = 500
    red_65Y = random.randint(20, 500)

    # Puts the bubble on the screen
    def bubbleGenerator(bubble, x, y):
        screen.blit(bubble, (x, y))

    # Fish
    fish = pygame.image.load('src/fish.png')
    fishX = 20
    fishX_change = 0
    fishY = 200
    fishY_change = 0

    def fishPosition(x, y):
        screen.blit(fish, (x, y))

    # Score variables
    score = 0
    color = (0, 0, 0)
    font = pygame.font.SysFont(None, 20)

    def scoreGenerator(text, font):
        text = font.render(text, True, color)
        screen.blit(text, (700, 15))

    # Game over
    gameover = pygame.image.load('src/gameover.png')

    # Calculates the distnce for the fish to move.
    def distance(x1, y1, x2, y2):
        answer = math.sqrt(((x2 - (x1+50))**2) + ((y2 - (y1+50))**2))
        return answer

    # Running pygame screen until escape condition
    running = True
    while running:

        # For filling screen with any color using RGB
        screen.fill((0, 0, 0))

        # Adding and moving background image

        screen.blit(background, (backgroundX, 0))
        backgroundWidth -= 0.5
        screen.blit(background, (backgroundWidth, 0))
        backgroundX -= 0.5
        if backgroundX <= -1920:
            backgroundX = 0
            backgroundWidth = 1920

        # Checking all the event occurred while single iteration of while loop
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            # Events of pressing keys
            if event.type == pygame.KEYDOWN:
                # Changes fishs co-ordinates on pressing respective keys
                if event.key == pygame.K_SPACE:
                    fishY_change = -5

                if event.key == pygame.K_q:
                    gamemusic.stop()
                    gameover_screen()
                    
                    """
                    screen.blit(pygame.image.load('src/gameover.png'), (960, 540))
                    pygame.display.flip()
                    running = False
                    pygame.time.wait(miniseconds_seconds(20))
                    pygame.quit()
                    exit()
                    """

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    fishY_change = 3

        # Limiting fish movement in the screen
        if fishY+fishY_change <= 0 or fishY+fishY_change >= 440:
            fishY_change = 0

        # Generating bubbles
        bubbleGenerator(green_30, green_30X, green_30Y)
        bubbleGenerator(green_40, green_40X, green_40Y)
        bubbleGenerator(green_50, green_50X, green_50Y)
        bubbleGenerator(red, redX, redY)
        bubbleGenerator(zacoin, zacoinX, zacoinY)
        bubbleGenerator(red_65, red_65X, red_65Y)

        # Changing fish position
        fishY += fishY_change
        fishPosition(fishX, fishY)
        fishPosition(fishX, fishY)

        # Checking for collisions by calculating distance b/w fish and the bubbles
        distanceGreen_30 = distance(fishX, fishY, green_30X, green_30Y)
        distanceGreen_40 = distance(fishX, fishY, green_40X, green_40Y)
        distanceGreen_50 = distance(fishX, fishY, green_50X, green_50Y)
        distenceZacoin = distance(fishX, fishY, zacoinX, zacoinY)

        distanceRed = distance(fishX, fishY, redX, redY)
        distanceRed2 = distance(fishX, fishY, red_65X, red_65Y)

        #print(f'Distance Red = {distanceRed}')
        #print(f'Distance Red 2 = {distanceRed2}')
        
        if distanceGreen_30 <= 40:
            coincollect.play()
            score += 25
        if distanceGreen_40 <= 40:
            coincollect.play()
            score += 50
        if distanceGreen_50 <= 40:
            coincollect.play()
            score += 75
        if distenceZacoin <= 40:
            coincollect.play()
            score += 150

        # Updating score
        text = f"Your Score: {score}"
        scoreGenerator(text, font)

        if score >= maxscore:
            gamemusic.stop()
            screen = pygame.display.set_mode((960, 540))

            loading_image = pygame.image.load('src/stage2.png')
            screen.blit(loading_image, (0, 0))
            pygame.display.flip()
            pygame.time.wait(miniseconds_seconds(2))

            stage2()

        # Controlling speed and reseting bubbles on no NO collision
        green_30X -= 1.5
        if green_30X <= 0 or distanceGreen_30 <= 40:
            green_30X = random.randint(960, 1500)
            green_30Y = random.randint(15, 500)

        green_40X -= 2
        if green_40X <= 0 or distanceGreen_40 <= 40:
            green_40X = random.randint(960, 1500)
            green_40Y = random.randint(15, 500)

        green_50X -= 2.5
        if green_50X <= 0 or distanceGreen_50 <= 40:
            green_50X = random.randint(960, 1500)
            green_50Y = random.randint(15, 500)

        redX -= 3
        if redX <= 0:
            redX = random.randint(960, 1500)
            redY = random.randint(15, 500)

        red_65X -= 4
        if red_65X <= 0:
            red_65X = random.randint(960, 1500)
            red_65Y = random.randint(15, 500)

        zacoinX -= 6
        if zacoinX <= 0 or distenceZacoin <= 40:
            zacoinX = random.randint(960, 1500)
            zacoinY = random.randint(15, 500)

        # IF PLAYER TOUCHES RED FISH / GAME END
        if distanceRed2 <= 40:
            gamemusic.stop()
            gameover_screen()

        if distanceRed <= 30:
            gamemusic.stop()
            gameover_screen()

        # Updating screen on each iteration
        pygame.display.update()

def start():
    pygame.mixer.stop()
    screen = pygame.display.set_mode((960, 540))

    background = pygame.image.load('src/startscreen.png')
    start_button = pygame.image.load('src/startbutton.png')
    pygame.display.flip()

    start_button_pos = (532, 245)

    lobbymusic.play()
    # Waits for user to click "start" button
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

            # When user clicks start button with mouse..
            if event.type == pygame.MOUSEBUTTONDOWN and start_button_rect.collidepoint(event.pos): # User clicks down the mouse button.
                lobbymusic.stop()
                screen = pygame.display.set_mode((960, 540))

                loading_image = pygame.image.load('src/stage1.png')
                screen.blit(loading_image, (0, 0))
                pygame.display.flip()
                pygame.time.wait(miniseconds_seconds(2))

                stage1()    # Start the game, first stage.

        # Draw the background image and start button on the screen
        screen.blit(background, (0, 0))
        screen.blit(start_button, start_button_pos)
        start_button_rect = start_button.get_rect(topleft=start_button_pos)

        pygame.display.update()

start() # Starts the program :)
