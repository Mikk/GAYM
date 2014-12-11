#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from constants import *
import pygame
from pygame.locals import *
all_sprites_list = pygame.sprite.Group()
platform_sprites_list = pygame.sprite.Group()

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
        self.generate_on_floor(5)
    def generate_floor(self, x=0, y=DISPLAY_HEIGHT):
        for i in range(int(x), int(DISPLAY_WIDTH), self.image.get_size()[0]):
            tile = Block(x=i, y= y - self.image.get_size()[1])
            self.floortiles.append(tile)
    def generate_on_floor(self, n=1):
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
    jumpingTimer = pygame.time.get_ticks()
    direction = UP
    animationClock = pygame.time.Clock()
    animationTimer = animationClock.get_time()
    imageType = 1 # either 1, 2 or 3

    kiirus = 10
    liikumine = [0,0]

    def __init__(self):
        super().__init__()
        self.animationClock.tick()

    def dogravity(self):
        self.rect.y += GRAVITY
        if pygame.sprite.spritecollide(self, platform_sprites_list, False):
            self.rect.y -= GRAVITY
            self.isJumping = False # to stop jump when collision

    def liiguvasemale(self):
        self.liikumine[0] += -self.kiirus
        self.direction = LEFT
    def liiguparemale(self):
        self.liikumine[0] += self.kiirus
        self.direction = RIGHT
    def liiguülesse(self):
        self.liikumine[1] -= self.kiirus*2
    def liigualla(self):
        self.liikumine[1] += self.kiirus
        self.direction = DOWN

    ###ANIMATION RELATED
    def assignImage(self, direction):
        if self.isJumping:
            image = self.getImage(self.hyppamine_tekstuurid[direction])
        elif not self.isJumping:
            image = self.getImage(self.jooks_tekstuurid[direction])
        self.image = pygame.image.load(image)

    def getImage(self, image_list):
        imageType = self.imageType
        print(imageType)

        while len(image_list) <= imageType:
            imageType -= 1
        print(image_list, image_list[imageType])
        return image_list[imageType]

    def updateAnimationType(self):
        self.animationTimer += self.animationClock.tick()
        if(self.animationTimer <= 120):
            self.imageType = 0
        elif(self.animationTimer <= 240):
            self.imageType = 1
        elif(self.animationTimer <= 360):
            self.imageType = 2
        if(self.animationTimer > 360):
            self.animationTimer = 0

    #####################

    def check_collision(self):
        if pygame.sprite.spritecollide(self, platform_sprites_list, False):
            self.liikumine[0] = -self.liikumine[0]
            self.liikumine[1] = -self.liikumine[1]
            self.liigu()
        self.liikumine[0], self.liikumine[1] = 0, 0


    def liigu(self):
        #print("liigu", self.liikumine[0], self.liikumine[1])w
        x, y = self.liikumine[0], self.liikumine[1]
        self.rect.x += x
        self.rect.y += y
        if(x == 0 and y == 0):
            self.direction = DOWN
    def hyppa(self):
        if self.isJumping == False:
            self.jumpingTimer = pygame.time.get_ticks()
            self.isJumping = True

    def check_hyppamine(self):
        if pygame.time.get_ticks() - self.jumpingTimer <= 500 and self.isJumping:
            self.liiguülesse()
        # elif pygame.time.get_ticks() - self.jumpingTimer<= 1000 and self.isJumping:
        #     pass
        # else:
        #     self.isJumping = False

    def update(self):
        self.updateAnimationType()
        self.liigu()
        self.check_collision()
        self.check_hyppamine()
        self.dogravity()
        self.assignImage(self.direction)


class Player(Character):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(liigubparemale1).convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        ## laeb mehikese tekstuurid
        self.jooks_tekstuurid = mehike_jookseb
        self.hyppamine_tekstuurid = mehike_hyppab
        self.seismine_tekstuurid = mehike_seisab

    def löömine(self):
        ...


def nupp(msg,x,y,laius,kõrgus,värv1,värv2,action=None):
    font = pygame.font.Font(None, 100)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+laius > mouse[0] > x and y+kõrgus > mouse[1] > y:
        pygame.draw.rect(gameDisplay, värv2, (x,y,laius,kõrgus))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, värv1, (x,y,laius,kõrgus))
    smallText = font.render(msg,1,black)
##    textSurf, textRect = text_objects(msg, smallText) 
##    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(smallText, (x, y+50))

def skoori_number(score):
    font = pygame.font.Font(None, 40)
    pygame.event.pump()
    key = pygame.key.get_pressed()
    score = str(score)
    score_text = font.render(score,1,black)
    gameDisplay.blit(score_text, (90, 0))
    
def skooritabel(msg,x,y,laius,kõrgus,värv):
    font = pygame.font.Font(None, 40)
    #pygame.draw.rect(gameDisplay, värv, (x,y,laius,kõrgus))
    text = font.render(msg,1,black)
    gameDisplay.blit(text, (x, y))

def game_over():
    font = pygame.font.Font(None, 280)
    #pygame.draw.rect(gameDisplay, värv, (x,y,laius,kõrgus))
    text = font.render("Game Over",1,black)
    gameDisplay.blit(text, (100, 200))
    game_intro()
    
def game_intro():
    intro = True
    pygame.event.pump()
    key = pygame.key.get_pressed()
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
    score = 0
    pygame.display.set_caption("Maskantje")
    game = True

    player = Player()
    põrand = Platform(generate=True)
    all_sprites_list.add(player, põrand.floortiles)
    platform_sprites_list.add(põrand.floortiles)
    player.rect.x = x
    player.rect.y = y

    pygame.key.set_repeat()
    while game:
        gameDisplay.blit(background, (0,0))
        skooritabel("Score:",0,0,100,20,black)
        skoori_number(score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

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

        player.update()
        all_sprites_list.draw(gameDisplay)
        pygame.display.update()
        clock.tick(30)

pygame.init()
#Muusika
pygame.mixer.music.load("Storm, Earth and Fire.mp3")
pygame.mixer.music.play(-1,0.0)        
#Intro screen
game_intro()
pygame.quit()
quit()
