from pygame import *
from time import sleep
import random
mixer.init()
font.init()

#создай окно игры
#mixer.music.load('space.ogg')
#mixer.music.play()
#fire_sound = mixer.Sound('fire.ogg')


window = display.set_mode((700,500))# создаю сцену
display.set_caption('PingPong')#задаю название окна
background = transform.scale(image.load('background.png'), (700,500))#подгружаю фон для сцены и распределяю его на саму сцену
clock = time.Clock()#создаю объект-часы, отслеживающий время
x1 = 20
y1 = 0
x2 = 510
y2 = 0
finish = False
flag = True
speed_player = 7
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect() #прямоугольная область спрайта
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'left'
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_player1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > -15:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 275:
            self.rect.y += self.speed
    def update_player2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > -15:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 275:
            self.rect.y += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top,15,15,20)
        bullets.add(bullet)
        fire_sound.play()
player1 = Player('player1.png',x1,y1,speed_player,165,265)
player2 = Player('player2.png',x2,y2,speed_player,165,265)
FPS = 60
while flag:
    for e in event.get():
        if e.type == QUIT:
            flag = False
    if finish != True:
        window.blit(background,(0,0)) 
        player1.reset()
        player1.update_player1()
        player2.reset()
        player2.update_player2()
    display.update()
    clock.tick(FPS)#обновляю кадры с частотой , которая содержится в переменной FPS
