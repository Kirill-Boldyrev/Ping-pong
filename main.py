from pygame import *
from time import time as timer
init()
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = (202, 223, 255)
bounce_ball = mixer.Sound('ping_pong.ogg')
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#TODO класс Игрока в игре <<Пинг-понг>>
class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
rocket = Player('rocket.png', 50, 270, 30, 150, 5)
rocket2 = Player('rocket.png', 625, 25, 30, 150, 5)
ball = GameSprite('ball.png', 300, 200, 70, 75, 5)
finish = False
speed_x = 3
speed_y = 3
lost = 0
lost2 = 0
font1 = font.SysFont('Arial', 26)
text_lose = font1.render('RACKET 1 LOSE!', True, (250, 200, 138))
text_lose2 = font1.render('RACKET 2 LOSE!', True, (250, 200, 138))
points1 = font1.render('Счёт игрока 1:' + str(lost), 1, (255, 255, 252))
points2 = font1.render('Счёт игрока 2:' + str(lost2), 1, (255, 255, 252))
clock = time.Clock()
FPS = 60
game = True
while game:
    if finish != True:
        window.fill(background)
        window.blit(points1, (0, 0))
        window.blit(points2, (500, 0))
        rocket.reset()
        rocket2.reset()
        ball.reset()
        rocket.update1()
        rocket2.update2()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 500 -50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(rocket, ball) or sprite.collide_rect(rocket2, ball):
            speed_x *= -1
            bounce_ball.play()
        if ball.rect.x >= 600:
            lost += 1
            ball.rect.x = 300
            ball.rect.y = 200
            points1 = font1.render('Счёт игрока 1:' + str(lost), 1, (255, 255, 252))
        if ball.rect.x <= 0:
            lost2 += 1
            ball.rect.x = 300
            ball.rect.y = 200
            points2 = font1.render('Счёт игрока 2:' + str(lost2), 1, (255, 255, 252))
        if lost >= 5:
            window.blit(text_lose2, (300, 200))
            finish = True
        if lost2 >= 5:
            window.blit(text_lose, (200, 300))
            finish = True
    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()