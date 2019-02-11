import pyglet

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

player_image = pyglet.resource.image("player.bmp")
ball_image = pyglet.resource.image("ball.bmp")

class PhysicalObject(pyglet.sprite.Sprite):
    
    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)
        self.vx = 0.0
        self.vy = 0.0
        
    def update(self, dt):
        pass        

class Ball(PhysicalObject):
    
    def __init__(self, *args, **kwargs):
        super(Ball, self).__init__(*args, **kwargs)
        self.vx = 200.0
        self.vy = 200.0
    
    def update(self, dt):
        super(Ball, self).update(dt)
        self.x = self.x + self.vx*dt
        self.y = self.y + self.vy*dt
        self.collision()
        
    def collision(self):
        if self.x < 0 or self.x > (800-32):
            self.vx = -self.vx
        if self.y < 0 or self.y > (600-32):
            self.vy = -self.vy
        
class Player(PhysicalObject):        
    
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=player_image, *args, **kwargs)
        self.vy = 200.0
        self.keys = dict(up=False, down=False)
        
    def on_key_press(self, symbol, modifiers):
        
        if symbol == pyglet.window.key.UP:
            self.keys['up'] = True
        elif symbol == pyglet.window.key.DOWN:
            self.keys['down'] = True
            
    def on_key_release(self, symbol, modifiers):
        
        if symbol == pyglet.window.key.UP:
            self.keys['up'] = False
        elif symbol == pyglet.window.key.DOWN:
            self.keys['down'] = False
            
    def update(self, dt):
        super(Player, self).update(dt)
        
        if self.keys['up']:
            self.y = self.y + self.vy*dt
        if self.keys['down']:
            self.y = self.y - self.vy*dt    

player = Player(x=0, y=300)
ball = Ball(img=ball_image, x=300, y=400)

window = pyglet.window.Window(800, 600)

window.push_handlers(player)

@window.event
def on_draw():
    window.clear()
    ball.draw()
    player.draw();
    
def update(dt):
    ball.update(dt)   
    player.update(dt) 
    
pyglet.clock.schedule_interval(update, 1/120.0)
    
pyglet.app.run()