import pyglet
from pyglet.gl import *
from random import randint
import math

cestica = pyglet.image.load("cestica.bmp")
explosion = pyglet.image.load("explosion.bmp")
smoke = pyglet.image.load("smoke.bmp")
window = pyglet.window.Window(1200, 800)

UPDATE_PERIOD = 0.04
MAX_CESTICA = 200
ZIVOT = 10
DELTA_T = 0.1

Y_CUTOFF_up = 600
Y_CUTOFF_down = 200

#glClearColor(1.0, 1.0, 1.0, 1.0)  

class SustavCestica:
    def __init__(self, X, Y, img, scale=0.5):
        self.cestice = []
        for _ in range(MAX_CESTICA):
            self.cestice.append(Cestica(X, Y, img, scale))

    def draw(self):
        for cestica in self.cestice:
            cestica.sprite.draw()
    
    def update(self):
        for cestica in self.cestice:
            if cestica.t >= cestica.zivot:
                cestica.reset()

            cestica.move()
            cestica.t += DELTA_T 

            if cestica.sprite.y>= Y_CUTOFF_up or cestica.sprite.y <= Y_CUTOFF_down:
                cestica.reset()
                break
            
            preostalo_vrijeme = ( 1 - cestica.t / cestica.zivot) # 1->0
            cestica.sprite.opacity = preostalo_vrijeme * 255
            cestica.sprite.scale =  preostalo_vrijeme * cestica.scale 

class Cestica:
    def __init__(self, X, Y, img, scale):
        self.sprite = pyglet.sprite.Sprite(img)
        self.scale = scale
        self.X = X
        self.Y = Y
        self.reset()

    def reset(self):
        self.sprite.x =  randint(-100, 100) + self.X
        self.sprite.y =  randint(-100, 100) + self.Y
        self.zivot = randint(1, ZIVOT)
        self.vx = [-1, 1][randint(0, 1)] * randint(1, 5)
        self.vy = [-1, 1][randint(0, 1)] * randint(1, 5)
        self.t = 0
    
    def move(self):
        self.sprite.x += self.vx
        self.sprite.y += self.vy



def update(arg):
    for sustavCestica in sustaviCestica:
        sustavCestica.update()
        
@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)  
    for sustavCestica in sustaviCestica:
        sustavCestica.draw()


sustavCestica1 = SustavCestica(400, 400, cestica,0.4)
sustavCestica2 = SustavCestica(800, 400, explosion, 1)
sustaviCestica= [sustavCestica1, sustavCestica2]

pyglet.clock.schedule_interval(update, UPDATE_PERIOD)
pyglet.app.run()
