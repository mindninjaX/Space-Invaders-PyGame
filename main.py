import pygame
from pygame import mixer
import random
import math

# Initialize the pygame
pygame.init()

# Create the screen (width,height)
screen = pygame.display.set_mode((800,600))

# Background Sound 
mixer.music.load('assets/background.wav')
mixer.music.play(-1)

# Title, Icon & Background
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)
background = pygame.image.load('assets/background.png')

# Player
playerImg = pygame.image.load('assets/player.png')
playerX = 370
playerY = 480
playerX_change = 0

score = 0

def player(x,y):
    screen.blit(playerImg,(x,y))


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('assets/enemy.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))


# Bullet
bulletImg = pygame.image.load('assets/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
# Ready - Bullet is not visible
# Fire - Bullet is not moving
bullet_state = "ready" 

# Score 
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

# Game Over Text 
over_font = pygame.font.Font('freesansbold.ttf', 64)

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (225,225,225))
    screen.blit(over_text, (200,250))

def show_score(x,y):
    score = font.render("Score :" + str(score_value),True, (255,255,255))
    screen.blit(score,(x,y))


def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+15, y+10))

# Collision
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop (Runtime)
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player Mechanics
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


        # Bullet Mechanics
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_Sound = mixer.Sound('assets/laser.wav')
                    bullet_Sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)


    # Background color (RGB)
    screen.fill((0, 0, 0))

    # Background Image
    screen.blit(background, (0,0))

    # Background Sound 
    mixer.music.load('assets/background.wav')
    mixer.music.play(-1)


    # Player Motion & Boundaries
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Drawing the player
    player(playerX, playerY)


    # Enemy Motion & Bounce
    for i in range(num_of_enemies):

        # Game Over 
        if enemyY[i] > 200:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break



        enemyX[i] += enemyX_change[i]

        if enemyX[i] >= 736:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = -4
        elif enemyX[i] <= 0:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = 4

    # Drawing the enemy
    enemy(enemyX[i], enemyY[i], i)


    # Bullet Motion
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
    if collision:
        explosion_Sound = mixer.Sound('assets/explosion.wav')
        explosion_Sound.play()
        bulletY = 480
        bullet_state = "ready"
        score_value += 1
        enemyX[i] = random.randint(0, 736)
        enemyY[i] = random.randint(50, 150)
    
    enemy(enemyX[i], enemyY[i], i)


    # Score 
    show_score(textX, textY)

    #  Updates the screen
    pygame.display.update()