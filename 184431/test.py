from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
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
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1,color_2,color_3, wall_x,wall_y,  wall_width,wall_height):
        super().__init__()
        self.color1 = color_1
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= 600:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        
window = display.set_mode((700, 500))
display.set_caption("лАбиринт")
background = transform.scale(image.load("Background.jpg"), (700, 500))
#sprite1 = transform.scale(image.load("cyborg.png"ng), (50, 50))
#sprite2 = transform.scale(image.load("hero.png"), (50, 50))
#image = Surface((40, 100))
yer = Player('hero.png', 5, 420, 4)
monster = Enemy('cyborg.png', 620, 420, 2)
final = GameSprite('treasure.png', 580, 420, 0)
w1 = Wall(255,200,60,100,100,10,50)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN', True, (225, 215, 0))
lose = font.render('YOU LOSE', True, (225, 215, 0))


clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

game = True
finish = False
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        monster.update()
        player.reset()
        monster.reset()
        final.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()


      
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player,w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3):
            finish = True
            window.blit(lose, (200, 200))
            #kick.play()

        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            #money.play()
        #w1.draw_wall()
    

    clock.tick(FPS)        
    display.update()
#создай игру "Лабиринт"!