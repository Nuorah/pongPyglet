import pyglet

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

player_image = pyglet.resource.image("player.bmp")
ball_image = pyglet.resource.image("ball.bmp")

class Ball(pyglet.sprite.Sprite):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vx = 100
        self.vy = 100
    
    def update(self, dt):
        self.x = self.x + self.vx*dt
        self.y = self.y + self.vy*dt
        self.collision()
        
    def collision(self):
        if self.x < 0 or self.x > (800-32):
            self.vx = -self.vx
        if self.y < 0 or self.y > (600-32):
            self.vy = -self.vy
        


player = pyglet.sprite.Sprite(img=player_image, x=0, y=300)
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