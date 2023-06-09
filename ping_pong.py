from pygame import *
from time import sleep
import random
mixer.init()
font.init()

#создай окно игры
#mixer.music.load('space.ogg')
#mixer.music.play()
#fire_sound = mixer.Sound('fire.ogg')
font1 = font.Font(None,35)



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
class Ball(GameSprite):
    def __init__(self,player_image,player_x,player_y,player_speed,size_x,size_y,speed_x,speed_y):
        super().__init__(player_image,player_x,player_y,player_speed,size_x,size_y)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update(self,enemy1,enemy2):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        global finish
        if self.rect.y > 495 or self.rect.y < 0:
            self.speed_y *= -1
        if sprite.collide_rect(self,enemy1) or sprite.collide_rect(self,enemy2):
            self.speed_x *= -1
        if self.rect.x < 0:
            lose1 = font1.render(
                'PLAYER 1 LOSE',True,(180,0,0)
                )
            window.blit(lose1,(260,250))
            finish = True
            
            
        if self.rect.x > 695:
            lose2 = font1.render(
                'PLAYER 2 LOSE',True,(180,0,0)
                )
            window.blit(lose2,(260,250))
            finish = True

player1 = Player('player1.png',x1,y1,speed_player,100,265)
player2 = Player('player2.png',x2,y2,speed_player,100,265)
ball = Ball('ball.png',250,250,0,65,65,2,2)
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
        ball.reset()
        ball.update(player1,player2)
        display.update()
        clock.tick(FPS)#обновляю кадры с частотой , которая содержится в переменной FPS
