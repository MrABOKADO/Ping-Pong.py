from random import *
from pygame import *
font.init()
font2 = font.SysFont('Arial', 36)
#mixer.init()
game = True
finish = False
FPS = 80
score1 = 0
score2 = 0
clock = time.Clock()
win = display.set_mode((700, 500))
display.set_caption('Ping-pong')
backround = transform.scale(image.load('stol.png'), (700, 500))


#mixer.music.load('space.ogg')
#mixer.music.play()


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, x, y, size_x, size_y):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(size_x, size_y))
        self.speed= player_speed
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 630:
            self.rect.y += self.speed
class Player1(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 630:
            self.rect.y += self.speed

r1 = Player('r2.png', 5, 600, 100, 100, 170)
r2 = Player1('r1.png', 5, 0, 100, 100, 170)
ball = GameSprite('ball.png', 5, 5, 0, 50, 50)
while game:
    win.blit(backround, (0, 0))
    if finish != True:
        r1.reset()
        r1.update()
        r2.reset()
        r2.update1()
        ball.reset()
        ball.update()
        winner = font2.render('Есть пробитие: '+ str(score1), 1, (100, 255, 255))
        win.blit(winner, (0, 5))
        winne1 = font2.render('Есть пробитие: '+ str(score2), 1, (100, 255, 255))
        win.blit(winne1, (450, 5))
    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()