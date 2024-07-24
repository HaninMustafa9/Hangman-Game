import pygame
import random


playerWord = []
correctGuess = ""  
tries = 10
hiddenWord = ""
history = []
charList = []
result_message = ""
# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Screen dimensions
width_of_window, height_of_window = 1068, 600
gameDisplay = pygame.display.set_mode((width_of_window, height_of_window))
pygame.display.set_caption('HangMan Game')
correct_sound = pygame.mixer.Sound("correct.mp3")
wrong_sound = pygame.mixer.Sound("wrong.mp3")
gameOver = pygame.mixer.Sound("gameOver.mp3")
win2 = pygame.mixer.Sound("win.mp3")
start = pygame.mixer.Sound("start.mp3")
# Load images
bgImage = pygame.image.load('home.png')
button_image = pygame.image.load("start.png")
button_image = pygame.transform.scale(button_image, (900, 600))
game_bg_image = pygame.image.load('game.png')  # Load the background image for the game

button_rect = button_image.get_rect()
button_rect.topleft = (width_of_window // 2 - button_rect.width // 2, height_of_window // 2 - button_rect.height // 2.1)

# Button variables
RADIUS = 22
GAP = 15
letters = []
startx = round((width_of_window - (RADIUS))/1.2)
starty = 70
A = 65


for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 3))
    y = starty + ((i // 3) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])
# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 25)
WORD_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT2 = pygame.font.SysFont('comicsans', 28)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)



# Initialize game variables
hangman_status = 0
guessed = []


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HANGMAN_COLOR = WHITE
HANGMAN_RADIUS = 30
HANGMAN_CENTER_X = 150
HANGMAN_CENTER_Y = 150
HANGMAN_LINE_WIDTH = 5
GALLOWS_COLOR = WHITE
GALLOWS_WIDTH = 10
GALLOWS_HEIGHT = 300
GALLOWS_TOP_X = 150
GALLOWS_TOP_Y = 100
GALLOWS_BOTTOM_X = GALLOWS_TOP_X
GALLOWS_BOTTOM_Y = GALLOWS_TOP_Y + GALLOWS_HEIGHT
GALLOWS_NOOSE_LENGTH = 50
def draw_gallows(tries):
    if tries <= 9:
        # Draw the gallows structure
        pygame.draw.line(gameDisplay, GALLOWS_COLOR, (GALLOWS_BOTTOM_X, GALLOWS_BOTTOM_Y + 60), (GALLOWS_BOTTOM_X + 98, GALLOWS_BOTTOM_Y + 60), GALLOWS_WIDTH)
    if tries <= 8:
        pygame.draw.line(gameDisplay, GALLOWS_COLOR, (GALLOWS_TOP_X+45, GALLOWS_TOP_Y + 70), (GALLOWS_BOTTOM_X+45, GALLOWS_BOTTOM_Y + 60), GALLOWS_WIDTH)
    if tries <= 7:
        # Draw the first part of the gallows (top horizontal bar)
        pygame.draw.line(gameDisplay, GALLOWS_COLOR, (GALLOWS_TOP_X - GALLOWS_WIDTH +51, GALLOWS_TOP_Y + 70), (GALLOWS_TOP_X+45 + GALLOWS_WIDTH + 50, GALLOWS_TOP_Y +70), GALLOWS_WIDTH)
    if tries <= 6:
        pygame.draw.line(gameDisplay, GALLOWS_COLOR, (GALLOWS_TOP_X + GALLOWS_WIDTH + 90, GALLOWS_TOP_Y + 70), (GALLOWS_TOP_X + GALLOWS_WIDTH + 90, GALLOWS_TOP_Y + 120), GALLOWS_WIDTH)
    # Draw the hangman's body parts based on tries
    if tries <= 5:
        # Draw the head
        pygame.draw.circle(gameDisplay, HANGMAN_COLOR, (GALLOWS_TOP_X  + GALLOWS_WIDTH + 90, GALLOWS_TOP_Y + 120 + HANGMAN_RADIUS), HANGMAN_RADIUS, HANGMAN_LINE_WIDTH)
    if tries <= 4:
        # Draw the body
        pygame.draw.line(gameDisplay, HANGMAN_COLOR, (GALLOWS_TOP_X  + GALLOWS_WIDTH + 90, GALLOWS_TOP_Y + 120 + HANGMAN_RADIUS * 2), (GALLOWS_TOP_X + GALLOWS_WIDTH + 90, GALLOWS_TOP_Y + 80 + HANGMAN_RADIUS * 6), HANGMAN_LINE_WIDTH)
    if tries <= 3:
        # Draw the left arm
        pygame.draw.line(gameDisplay, HANGMAN_COLOR, (GALLOWS_TOP_X + GALLOWS_WIDTH + 90, GALLOWS_TOP_Y + 130+ HANGMAN_RADIUS * 2), (GALLOWS_TOP_X + 55, GALLOWS_TOP_Y + HANGMAN_RADIUS * 8), HANGMAN_LINE_WIDTH)
    if tries <= 2:
        # Draw the right arm
        pygame.draw.line(gameDisplay, HANGMAN_COLOR, (GALLOWS_TOP_X + GALLOWS_WIDTH + 90, GALLOWS_TOP_Y + 130+ HANGMAN_RADIUS * 2), (GALLOWS_TOP_X + 155, GALLOWS_TOP_Y + HANGMAN_RADIUS * 8), HANGMAN_LINE_WIDTH)
    if tries <= 1:
        # Draw the left leg
        pygame.draw.line(gameDisplay, HANGMAN_COLOR, (GALLOWS_TOP_X + GALLOWS_WIDTH + 90 , GALLOWS_TOP_Y + 80 + HANGMAN_RADIUS * 6), (GALLOWS_TOP_X + 55 , GALLOWS_TOP_Y + HANGMAN_RADIUS * 11), HANGMAN_LINE_WIDTH)
    # if tries <= 1:
    #     # Draw the right leg
    #     pygame.draw.line(gameDisplay, HANGMAN_COLOR, (GALLOWS_TOP_X + GALLOWS_WIDTH + 90, GALLOWS_TOP_Y+ 80 + HANGMAN_RADIUS * 6), (GALLOWS_TOP_X + 155, GALLOWS_TOP_Y + HANGMAN_RADIUS * 11), HANGMAN_LINE_WIDTH)

# Example u

MENU = "menu"
GAME = "game"
current_state = MENU

def importaword():
    global charList
    file = open("words.txt","r")
    charList =[]
    lines = file.readlines()
    randomWord = random.choice(lines)
    selectedWord = randomWord.lower()
    charList = list(selectedWord)
    charList = list(set(charList))
    charList.sort()
    charList.remove("\n")
    return charList, selectedWord


def checker(selectedWord, guessedLetter):
    global correctGuess
    global playerWord
    if guessedLetter in selectedWord:
        correctGuess +=  guessedLetter
        playerWord.append(guessedLetter)
    else:
        playerWord.append(guessedLetter)
    playerWord.sort()
    return correctGuess, playerWord

def hd(hiddenWord, selectedWord, correctGuess, tries, result_message):
    for letter in selectedWord[0:-1]:
            if letter in correctGuess:
                hiddenWord += letter + " "
            else:
                hiddenWord += "_ " 
    text = WORD_FONT.render(hiddenWord, 1, WHITE)
    gameDisplay.blit(text, (width_of_window/2 - text.get_width()/2, 200))
    text2 = WORD_FONT.render("Remaining Tries: "+ str(tries), 1, WHITE)
    gameDisplay.blit(text2, (width_of_window/2 - text2.get_width()/2, 20))
    text3 =WORD_FONT.render(result_message, 1, WHITE)
    gameDisplay.blit(text3, (width_of_window/2 - text3.get_width()/2, 300))
    draw_gallows(tries)
    


def draw_letters():
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            # Determine the color based on whether the letter has been guessed
            if ltr in guessed:
                color = (0, 255, 0)  # Green color for guessed letters
            else:
                color = WHITE  # White color for unguessed letters

            pygame.draw.circle(gameDisplay, color, (x, y), RADIUS)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            gameDisplay.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

def inputLetter(guessedLetter, selectedWord):
    global tries, history
    result_message = ""
    guessedLetter = guessedLetter.lower()
    guessedLetter = guessedLetter[0]
    if guessedLetter in history:
        print("This letter has been guessed before!")
        result_message = "Guessed before!"
    elif guessedLetter in selectedWord:
        history.append(guessedLetter)
        correct_sound.play()  # Play correct sound
    else:
        history.append(guessedLetter)
        tries = tries - 1
        print("Wrong Guess!")
        result_message = "Wrong Guess!"
        if (tries >=1):
            wrong_sound.play()  # Play correct sound
        else:
            gameOver.play()
            
    
    return guessedLetter, history, tries, result_message

def printer(playerWord, selectedWord, tries):
    global charList
    result_message = ""
    if (playerWord == charList) or (set(charList).issubset(playerWord)):
        result_message = "win"
    elif tries == 0:
        result_message = "lose"

    if result_message:
        display_end_message(result_message)




def display_end_message(message):
    end_screen = pygame.display.set_mode((width_of_window, height_of_window))
    if (message == "win"):
        win = pygame.image.load("won.png")
        end_screen.blit(win, (0, 0))
        win2.play()

    else:
        lose = pygame.image.load("gameOver.png")
        end_screen.blit(lose, (0, 0))

    # Create buttons
    button_font = pygame.font.SysFont('comicsans', 40)
    restart_button = button_font.render('Restart', True, WHITE)
    quit_button = button_font.render('Quit', True, WHITE)

    restart_button_rect = restart_button.get_rect(center=(width_of_window/2 - 100, height_of_window/2 + 50))
    quit_button_rect = quit_button.get_rect(center=(width_of_window/2 + 100, height_of_window/2 + 50))

    end_screen.blit(restart_button, restart_button_rect.topleft)
    end_screen.blit(quit_button, quit_button_rect.topleft)
    pygame.display.update()

    # Wait for user input
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button_rect.collidepoint(event.pos):
                    waiting = False
                    global charList, playerWord, correctGuess, hiddenWord, tries, current_state, result_message, history
                    playerWord = []
                    correctGuess = ""  
                    tries = 10
                    hiddenWord = ""
                    history = []
                    charList = []
                    result_message = ""
                    current_state = GAME
                    mainGameLoop()
                elif quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()

def mainGameLoop():
    global charList, playerWord, correctGuess, hiddenWord, tries, current_state, result_message, history
    charList, selectedWord = importaword()
    print(selectedWord)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos) and current_state == MENU:
                    current_state = GAME
                    start.play()
                if current_state == GAME:
                    for letter in letters:
                        x, y, ltr, visible = letter
                        if visible:
                            dist = ((x - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2) ** 0.5
                            if dist < RADIUS:
                                    guessedLetter, history, tries, result_message = inputLetter(ltr, selectedWord)
                                    checker(selectedWord, guessedLetter)
                                    hd(hiddenWord, selectedWord, correctGuess, tries, result_message)
                                    printer(playerWord, selectedWord, tries)
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if current_state == MENU:
            gameDisplay.blit(bgImage, (0, 0))
            gameDisplay.blit(button_image, button_rect.topleft)
            

        elif current_state == GAME:
            
            gameDisplay.blit(game_bg_image, (0, 0))  # Draw the background image for the game
            font = pygame.font.SysFont('comicsans', 60)
            draw_letters()
            hd(hiddenWord, selectedWord, correctGuess, tries, result_message)
            if tries == 0 or set(charList).issubset(playerWord) or playerWord == charList:
                running = False
        pygame.display.update()


mainGameLoop()
pygame.quit()
