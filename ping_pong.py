from pygame import *


window = display.set_mode((700,500))
window.fill((200,255,255))
display.set_caption('Ping pong Game')
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x, player_y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_p1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_p2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed




player1 = Player("racket.png",100,250,7,30,100)
player2 = Player("racket.png",600,250,7,30,100)
ball = GameSprite("ball.png",350,250,5,30,30)


font.init()
font1 = font.Font(None,36)
lose1 = font1.render("Player1 lost",1,(255,0,0))
lose2 = font1.render("player2 lost",1,(255,0,0))     
restart = font1.render("press ESCAPE for restart",1,(255,0,0))
game = True
finish= False
clock = time.Clock()
FPS = 40
step_x = 2
step_y = 3
while game:
    if finish == False:
        window.fill((200,255,255))
        player1.draw()
        player2.draw()
        player1.update_p1()
        player2.update_p2()
        ball.draw()
    
    ball.rect.y-= step_y
    if ball.rect.y <= 10 or ball.rect.y >= 490 :
        step_y = step_y*(-1)
    
    ball.rect.x -= step_x
    if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball,player2):
        step_x = step_x*(-1)
    
    
    
    
    
    if ball.rect.x <= 10:
        finish = True
        window.blit(lose1,(250,250))
        window.blit(restart,(0,30))


    if ball.rect.x >= 690:
        finish = True
        window.blit(lose2,(250,250))
        window.blit(restart,(0,30))
    if finish == True:
        keys = key.get_pressed()
        if keys[K_ESCAPE]:
            finish = False
            ball.rect.y = 250
            ball.rect.x = 350
        
        
    
    display.update()
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False