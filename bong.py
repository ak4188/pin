from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'left'
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 495:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 495:
            self.rect.y += self.speed
win_widht = 700
win_height = 500
window = display.set_mode((win_widht,win_height))
window.fill((173, 0, 116))

display.set_caption('пинк')

ball = GameSprite("boll.png",350,250,150,150,20)
platform1 = Player("platform.png",10,200,100,100,20)
platform2 = Player("platform.png",600,300,100,100,20)

clock = time.Clock()
FPS = 60


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((173, 0, 116))
    ball.reset()
    platform1.update_l()
    platform2.update_r()
    platform2.reset()
    platform1.reset()
    
    clock.tick(FPS)
    display.update()