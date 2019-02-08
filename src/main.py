import pyglet

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

player_image = pyglet.resource.image("player.bmp")
ball_image = pyglet.resource.image("ball.bmp")

class PhysicalObject(pyglet.sprite.Sprite):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vx = 0.0
        self.vy = 0.0
        
    def update(self, dt):
        self.x = self.x + self.vx*dt
        self.y = self.y + self.vy*dt

class Ball(PhysicalObject):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vx = 100.0
        self.vy = 100.0
    
    def update(self, dt):
        super().update(dt)
        self.collision()
        
    def collision(self):
        if self.x < 0 or self.x > (800-32):
            self.vx = -self.vx
        if self.y < 0 or self.y > (600-32):
            self.vy = -self.vy
        
class Player(PhysicalObject):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

player = Player(img=player_image, x=0, y=300)
ball = Ball(img=ball_image, x=300, y=400)

window = pyglet.window.Window(800, 600)



@window.event
def on_draw():
    window.clear()
    ball.draw()
    
def update(dt):
    ball.update(dt)    
    
pyglet.clock.schedule_interval(update, 1/120.0)
    
pyglet.app.run()