import pygame
import time
import os
import random

#Window size
WIN_WIDTH = 600
WIN_HEIGHT = 800
#Array of character images
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png")))]
#Single obstacle image
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
#Ground image
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
#Background image 
BG_MSG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

class Bird: #Bird object
    
    IMGS = BIRD_IMGS #Access images
    MAX_ROTATION = 25 #Tilt when moving up or down
    ROT_VEL = 20 #How fast you move
    ANIMATION_TIME = 5 #Each sprite change
    
    def _init_ (self, x, y): #Constructor
        self.x = x #Starting x position
        self.y = y #Starting y position
        self.tilt = 0 #current tilt
        self.tick_count = 0 #How fast each frame changes
        self.vel = 0 #Velocity
        self.height = self.y #Current Y position
        self.img_count = 0 #How many times each image has changes
        self.imsg = self.IMGS[0]  #Current image

    def jump(self): #Jump method
        self.vel = -10.5 #Negative velocity to move up
        self.tick_count = 0 #Reset tick timer
        self.height = self.y #Current height
    
    def move (self): #Mmove method
        self.tick_count += 1 #How long we are moving for
        d = self.vel * self.tick_count + 1.5*self.tick_count**2 #How much are we going up or down
        
        if d >= 16:
            d = 16
            
        if d < 0:
            d -= 2
            
        self.y = self.y + d
        
        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL
                
    def draw(self, win):
        self.img_count += 1
        
        if self.img_count <= self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count <= self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count <= self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count <= self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0
            
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2