import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen (width,height)
screen = pygame.display.set_mode((800,600))

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

def player(x,y):
    screen.blit(playerImg,(x,y))


# Enemy
enemyImg = pygame.image.load('assets/enemy.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 4
enemyY_change = 40

def enemy(x,y):
    screen.blit(enemyImg,(x,y))


# Bullet
bulletImg = pygame.image.load('assets/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
# Ready - Bullet is not visible
# Fire - Bullet is not moving
bullet_state = "ready" 

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+15, y+10))


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
                fire_bullet(playerX, bulletY)


    # Background color (RGB)
    screen.fill((0, 0, 0))

    # Background Image
    screen.blit(background, (0,0))


    # Player Motion & Boundaries
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Drawing the player
    player(playerX, playerY)


    # Enemy Motion & Bounce
    enemyX += enemyX_change

    if enemyX >= 736:
        enemyY += enemyY_change
        enemyX_change = -4
    if enemyX <= 0:
        enemyY += enemyY_change
        enemyX_change = 4

    # Drawing the enemy
    enemy(enemyX, enemyY)


    # Bullet Motion
    if bullet_state is "fire":
        fire_bullet(playerX,bulletY)
        bulletY -= bulletY_change


    #  Updates the screen
    pygame.display.update()