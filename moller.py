#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from constants import *
import pygame
from pygame.locals import *
all_sprites_list = pygame.sprite.Group()
enemies_sprites_list = pygame.sprite.Group()
platform_sprites_list = pygame.sprite.Group()
score = 0

## ABIFUNKTSIOONID

def loadImage(imagepath):
    return pygame.image.load(imagepath)

class Block(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.image = pygame.image.load(gray_brick)
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
        self.rect.x = x
        self.rect.y = y

class Platform(Block):
    floortiles = []
    def __init__(self, x=0, y=0, generate=False):
        super().__init__()
        if generate:
            self.generate()
    def generate(self):
        self.generate_floor()
        self.generate_platforms(5)
    def generate_floor(self, x=0, y=DISPLAY_HEIGHT):
        for i in range(int(x), int(DISPLAY_WIDTH), self.image.get_size()[0]):
            tile = Block(x=i, y= y - self.image.get_size()[1])
            self.floortiles.append(tile)
    def generate_platforms(self, n=1):
        for i in range(n):
            position = random.randint(2,18) *64
            obstacle = random.choice(OBSTACLES)
            for coordinates in obstacle:
                X = coordinates[0] + position
                Y = coordinates[1] + DISPLAY_HEIGHT-128
                tile = Block(x= X, y= Y)
                self.floortiles.append(tile)

class Character(pygame.sprite.Sprite):
    ## Textures go here
    jooks_tekstuurid = []
    hyppamine_tekstuurid = []
    seismine_tekstuurid = []
    ###################
    isJumping = False
    isPunching = False
    jumpingClock = pygame.time.Clock()
    jumpingTimer = jumpingClock.get_time()
    jumpLength = 500
    direction = UP
    animationClock = pygame.time.Clock()
    animationTimer = animationClock.get_time()
    animationLength = 120
    imageType = 0 # either 0, 1 or 2

    kiirus = 10
    liikumine = [0,0]

    def __init__(self):
        super().__init__()
        self.animationClock.tick()
        self.jumpingClock.tick()

    ###LIIKUMINE

    def dogravity(self):
        self.rect.y += GRAVITY
        if pygame.sprite.spritecollide(self, platform_sprites_list, False):
            self.rect.y -= GRAVITY
            self.isJumping = False # to stop jump when collision with ground

    def liiguvasemale(self):
        self.liikumine[0] += -self.kiirus
        if self.rect.x < 0:
            self.liikumine[0] += self.kiirus
        self.direction = LEFT
    def liiguparemale(self):
        self.liikumine[0] += self.kiirus
        self.direction = RIGHT
    def liiguülesse(self):
        self.liikumine[1] -= self.kiirus*2
    def liigualla(self):
        self.liikumine[1] += self.kiirus
        self.direction = DOWN

    def liigu(self):
        x, y = self.liikumine[0], self.liikumine[1]
        self.rect.x += x
        self.rect.y += y
        # print(x,y)
        if(x == 0 and y == 0):
            self.direction = DOWN
    def hyppa(self):
        if self.isJumping == False:
            self.jumpingTimer = 0
            self.isJumping = True

    def check_hyppamine(self):
        self.jumpingTimer += self.jumpingClock.tick()
        print(self.jumpingTimer)
        if self.jumpingTimer <= self.jumpLength and self.isJumping:
            self.liiguülesse()
        elif self.isJumping == False and self.jumpingTimer != 0:
            self.jumpingTimer = 0

    ###ANIMATION RELATED
    def assignImage(self, direction):
        if self.isJumping:
            image = loadImage(self.getImage(self.hyppamine_tekstuurid[direction]))
            if self.isPunching:
                if direction == RIGHT:
                    image = loadImage(jalaga_mollingusse_paremale)
                elif direction == LEFT:
                    image = loadImage(jalaga_mollingusse_vasakule)
        elif not self.isJumping:
            image = loadImage(self.getImage(self.jooks_tekstuurid[direction]))
            if self.isPunching:
                if direction == RIGHT:
                    image = loadImage(self.getImage(mollingusse[direction]))
                if direction == LEFT:
                    image = loadImage(self.getImage(mollingusse[direction]))
        self.image = image

    def getImage(self, image_list):
        imageType = self.imageType
        while len(image_list) <= imageType:
            imageType -= 1
        return image_list[imageType]

    def updateAnimationType(self):
        self.animationTimer += self.animationClock.tick()
        if(self.animationTimer <= self.animationLength*1):
            self.imageType = 0
        elif(self.animationTimer <= self.animationLength*2):
            self.imageType = 1
        elif(self.animationTimer <= self.animationLength*3):
            self.imageType = 2
        if(self.animationTimer > self.animationLength*3):
            self.animationTimer = 0

    def peksmine(self):
        self.isPunching = True
    #####################

    def check_collision(self):
        if pygame.sprite.spritecollide(self, platform_sprites_list, False):
            self.liikumine[0] = -self.liikumine[0]
            self.liikumine[1] = -self.liikumine[1]
            self.liigu()
        self.liikumine[0], self.liikumine[1] = 0, 0


    def update(self):
        self.updateAnimationType()
        self.check_hyppamine()
        self.liigu()
        self.check_collision()
        self.assignImage(self.direction)
        self.isPunching = False

        self.dogravity()

class AI(Character):
    def __init__(self):
        super().__init__()
        self.kiirus = 5

    def getPlayerPos(self, playerobj):
        x = playerobj.rect.x
        y = playerobj.rect.y
        return [x, y]

    def getMovement(self, playercords):
        player_x, player_y = playercords[0], playercords[1]
        ai_x, ai_y = self.rect.x, self.rect.y
        if (ai_x - player_x > 0):
            self.direction = LEFT
            return [-self.kiirus, 0]
        elif (ai_x - player_x < 0):
            self.direction = RIGHT
            return [self.kiirus, 0]
        else:
            return [0, 0]

    def setLiikumine(self, newliikumine):
        self.liikumine[0], self.liikumine[1] = newliikumine[0], newliikumine[1]

class Titt(AI):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(beebi_seisab[0])
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = (DISPLAY_WIDTH * 0.75)
        self.rect.y = (DISPLAY_HEIGHT * 0.5)

        ## tekstuurid
        self.jooks_tekstuurid = beebi_jookseb
        self.hyppamine_tekstuurid = beebi_jookseb
        self.seismine_tekstuurid = beebi_seisab

        self.animationLength = 10
    def check_collision(self):
        if pygame.sprite.spritecollide(self, platform_sprites_list, False):
            self.liikumine[0] = -self.liikumine[0]
            self.liikumine[1] = -self.liikumine[1]
            self.liigu()
        self.liikumine[0], self.liikumine[1] = 0, 0

    def update(self, playerobj):
        self.setLiikumine(self.getMovement(self.getPlayerPos(playerobj)))
        self.updateAnimationType()
        self.liigu()
        self.check_collision()
        self.check_hyppamine()
        self.dogravity()
        self.assignImage(self.direction)

class Player(Character):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(liigubparemale1)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = (DISPLAY_WIDTH * 0.05)
        self.rect.y = (DISPLAY_HEIGHT * 0.5)

        ## laeb mehikese tekstuurid
        self.jooks_tekstuurid = mehike_jookseb
        self.hyppamine_tekstuurid = mehike_hyppab
        self.seismine_tekstuurid = mehike_seisab

    def check_collision(self):
        if pygame.sprite.spritecollide(self, platform_sprites_list, False):
            self.liikumine[0] = -self.liikumine[0]
            self.liikumine[1] = -self.liikumine[1]
            self.liigu()
        if pygame.sprite.spritecollide(self, enemies_sprites_list, False):
            if not self.isPunching:
                game_over()
            if self.isPunching:
                global score
                score += 1
        self.liikumine[0], self.liikumine[1] = 0, 0

def nupp(msg,x,y,laius,kõrgus,värv1,värv2,action=None):
    font = pygame.font.Font(None, 100)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #kui hiirt liigutada siia piirkonda, siis läheb heledamaks
    if x+laius > mouse[0] > x and y+kõrgus > mouse[1] > y:
        pygame.draw.rect(gameDisplay, värv2, (x,y,laius,kõrgus))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, värv1, (x,y,laius,kõrgus))
    #tekst nuppude peal
    smallText = font.render(msg,1,black)
    gameDisplay.blit(smallText, (x, y+50))

def skoori_number(score):
    font = pygame.font.Font(None, 40)
    #muudab saadud täisarvu sõneks, muidu ei saa renderida
    score = str(score)
    score_text = font.render(score,1,black)
    gameDisplay.blit(score_text, (90, 0))
    
def skooritabel(msg,x,y,laius,kõrgus,värv):
    font = pygame.font.Font(None, 40)
    text = font.render(msg,1,black)
    gameDisplay.blit(text, (x, y))

def uus_level():
    #tühjendab maailma
    all_sprites_list.empty()
    platform_sprites_list.empty()
    enemies_sprites_list.empty()
    #uuesti käima põhi mängu loop
    game_loop()
    
def game_over():
    #kuvab suurelt teksti "Game Over"
    font = pygame.font.Font(None, 280)
    text = font.render("Game Over",1,black)
    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(background, (0,0))
        gameDisplay.blit(text, (100, 200))
        nupp("Play again",150,450,350,200,green,bright_green,uus_level)
        nupp("Quit Game!",750,450,400,200,red,bright_red,quit)
        pygame.display.update()
        clock.tick(15)
        
def game_intro():
    background = pygame.image.load("background2.png").convert()
    pygame.mixer.music.set_volume(0.5)
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(background, (0,0))
        nupp("Start Game!",150,450,400,200,green,bright_green,game_loop)
        nupp("Quit Game!",750,450,400,200,red,bright_red,quit)
        pygame.display.update()
        clock.tick(15)

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

background = pygame.image.load("background1.png").convert()
clock = pygame.time.Clock()

x = (DISPLAY_WIDTH * 0.25)
y = (DISPLAY_HEIGHT * 0.5)

def game_loop():
    pygame.mixer.music.set_volume(0.1)
    pygame.display.set_caption("Maskantje")
    game = True

    titt1 = Titt()
    player = Player()
    põrand = Platform(generate=True)
    print(põrand)
    all_sprites_list.add(player, põrand.floortiles, titt1)
    platform_sprites_list.add(põrand.floortiles)
    enemies_sprites_list.add(titt1)
    pygame.key.set_repeat()
    while game:
        score = 0
        gameDisplay.blit(background, (0,0))
        skooritabel("Score:",0,0,100,20,black)
        skoori_number(score)
        print(score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        #Kui läheb paremalt välja siis teeb uue maailma
        if player.rect.x == 1280:
            uus_level()
            
        pygame.event.pump()
        key = pygame.key.get_pressed()
        if key[K_UP]:
            player.hyppa()
        if key[K_DOWN]:
            player.liigualla()
        if key[K_LEFT]:
            player.liiguvasemale()
        if key[K_RIGHT]:
            player.liiguparemale()
        if key[K_SPACE]:
            player.peksmine()
        if key[K_ESCAPE]:
            break

        player.update()
        titt1.update(player)
        all_sprites_list.draw(gameDisplay)
        pygame.display.update()
        clock.tick(30)

#Mäng käima
pygame.init()
#Muusika
pygame.mixer.music.load("Storm, Earth and Fire.mp3")
pygame.mixer.music.play(-1,0.0)        
#Intro screen
game_intro()
pygame.quit()
quit()
