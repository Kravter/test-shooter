#Создай собственный Шутер!
from pygame import *
from random import randint
from time import time as timer
#from PyQt5.QtCore import Qt
#from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 920:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 1:
            self.rect.x -= self.speed
        if keys[K_UP] and self.rect.y > 500:
            self.rect.x += self.speed
        
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15,20,15)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            lost +=1
            self.rect.x = randint(0,620)
            self.rect.y = 0
            
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
        

#app = QApplication([])
#my_win = QWidget()

#b10 = Button(win, text = "RESTART", 
window = display.set_mode((1000, 500))
background = transform.scale(image.load("Nebo.jpg"), (1000, 500))
player = Player('rocket.png', 10, 420,65,65, 4)
bullets = sprite.Group()
monsters = sprite.Group()
font.init()
#font1 = font.SysFont(None, 50) #Размер букв
font1 = font.SysFont('Arial', 50)
num_fire = 0

for i in range(3):
    monster1 = Enemy('KOMETA.png', randint(0, 920),0,65,65,randint(1,5))
    monster2 = Enemy('ufo.png', randint(0, 920),0,65,65,randint(1,5))
    monsters.add(monster1)
    monsters.add(monster2)

lost = 0
score = 0
clock = time.Clock()
FPS = 60
life = 3
game = True
finish = False

run = True
rec_time = False





while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 5 and rec_time == False:
                    num_fire = num_fire+1 
                    player.fire()
            elif num_fire >= 5 and rec_time == False:
                last_time = timer()
                rec_time = True

            if e.key == K_5:
                finish = False
                window.blit(background,(0, 0))
                lost = 0
                score = 0
                bullets = sprite.Group()
                rec_time = False
                num_fire = 0

                monsters = sprite.Group()
                for i in range(3):
                    monster1 = Enemy('KOMETA.png', randint(0, 920),0,65,65,randint(1,5))
                    monster2 = Enemy('ufo.png', randint(0, 920),0,65,65,randint(1,5))
                    monsters.add(monster1)
                    monsters.add(monster2)
                    

    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        monsters.update()
        player.reset()
        monsters.draw(window)
        text_lose = font1.render("Пропущено" + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10,10))
        texе = font1.render("Сбито" + str(score), 1, (255, 255, 255))
        window.blit(texе, (10,40))
        bullets.update()
        bullets.draw(window)
        player.reset()

        if rec_time == True:
            now_time = timer()
            if now_time - last_time <1.5:
                text_reload = font1.render('RELOAD!', 1, (255, 0, 0))
                window.blit(text_reload,(260, 460))
            else:
                rec_time = False
                num_fire = 0
        
        if sprite.spritecollide(player,monsters,False) or lost>10:
            finish = True
            text_lose = font1.render("LOSER", 1, (255, 255, 255))
            window.blit(text_lose, (500, 0))#координаты



        collides = sprite.groupcollide(monsters, bullets, True, True)
        for coll in collides:
            if score%2==0:
                monster = Enemy('KOMETA.png', randint(0, 920),0,65,65,randint(1,5))
                monsters.add(monster)
            else:
                monster2 = Enemy('ufo.png', randint(0, 920),0,65,65,randint(1,5))
                monsters.add(monster2)

            score +=1
        
        if score > 10:
            
            finish = True
            text_win = font1.render("WIn", 1, (255, 255, 255))
            window.blit(text_win, (500, 0)) #координаты

        
        
    clock.tick(FPS)        
    display.update()

        # for i in range(3):
        #     monster1 = Enemy('KOMETA.png', randint(0, 920),0,65,65,randint(1,5))
        #     monster2 = Enemy('ufo.png', randint(0, 920),0,65,65,randint(1,5))
        #     monsters.add(monster1)
        #     monsters.add(monster2)