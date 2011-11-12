from pyglet.gl import *
from pyglet.window import key
from resources import grid,camera,draw_localAxis

from models.floor import floor
from models.teapot import teapot

class pygletApp(pyglet.window.Window):
    def __init__(self):
        super(pygletApp, self).__init__(width=800,height=600)

        self.set_exclusive_mouse(True)
        self.grid    = grid(size=500)
        self.camera  = camera(pos=(0., -100., -750.),rot=(0.,0.,0.),window=self)
        self.renderMode = GL_FILL

        # lighting
        self.light = False

        # walls and floors
        self.floor = floor(500, 500, 'lightwood.jpg')
        self.right_wall = floor(500, 500, 'lightwood.jpg')
        self.left_wall = floor(500, 500, 'lightwood.jpg')
        self.behind_wall = floor(500, 500, 'lightwood.jpg')

        # Exhibits
        self.teapot = teapot(100)



        # Lighting
        LightAmbient  = (GLfloat*4)(0.5, 0.5, 0.5, 1.0)
        LightDiffuse  = (GLfloat*4)(1.0, 1.0, 1.0, 1.0)
        LightPosition = (GLfloat*4)(0.0, 0.0, 2.0, 1.0)

        # initializations
        glEnable(GL_TEXTURE_2D)                                 # Textures
        glLightfv( GL_LIGHT1, GL_AMBIENT, LightAmbient )        # Lighting
        glLightfv( GL_LIGHT1, GL_DIFFUSE, LightDiffuse )
        glLightfv( GL_LIGHT1, GL_POSITION, LightPosition )

    def on_mouse_motion(self,x, y, dx, dy):
        self.camera.rot_y += dx / 4. 
        self.camera.rot_x -= dy / 4.

    def on_key_press(self,sym, mod):
        if sym == key.ESCAPE:   
            self.has_exit = True
        if sym == key.F:        # toggle between windows and fullscreen
            self.set_fullscreen(not self.fullscreen)
        if sym == key.R:
            if self.renderMode == GL_FILL:
                self.renderMode = GL_LINE
            else:
                self.renderMode = GL_FILL
            glPolygonMode(GL_FRONT_AND_BACK, self.renderMode)
        if sym == key.L:
            self.light = not self.light
            if not self.light:
                glDisable(GL_LIGHTING)
            else:
                glEnable(GL_LIGHTING)

    # Function that sets the camera to 3D mode            
    def on_resize(self,width, height): 
        glViewport(0, 0, self.width, self.height) 
        glMatrixMode(GL_PROJECTION) 
        glLoadIdentity() 
        gluPerspective(30., self.width / float(self.height), .1, 8000.)
        glMatrixMode(GL_MODELVIEW) 
        return pyglet.event.EVENT_HANDLED

    # your update function
    def update(self):
        self.dispatch_events()
        dt=pyglet.clock.tick()

        #update everything
        self.camera.update(dt)
        self.grid.update(dt)
        # your update code here...

    # your draw function
    def draw(self):
        glEnable(GL_TEXTURE_2D)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glEnable(GL_DEPTH_TEST)

        self.camera.draw()
        self.grid.draw()

        # floor
        glPushMatrix()
        glRotatef(90, 1, 0, 0)
        self.floor.draw()
        glPopMatrix()

        # right-side wall
        glPushMatrix()
        glTranslatef(500, 500, 0 )
        glRotatef(90, 0, 1, 0)
        self.right_wall.draw()
        glPopMatrix()

        # left-side wall
        glPushMatrix()
        glTranslatef(-500, 500, 0)
        glRotatef(90, 0, 1, 0)
        self.left_wall.draw()
        glPopMatrix()

        # behind wall
        glPushMatrix()
        glTranslatef(0, 500, -250)
        self.behind_wall.draw()
        glPopMatrix()

        # teapot
        glDisable(GL_TEXTURE_2D)
        glPushMatrix()
        glTranslatef(0, 300, 0)
        self.teapot.draw()
        glPopMatrix()
        

# our application is created using the pygletApp class
problem_3 = pygletApp()

while not problem_3.has_exit:
    problem_3.update()
    problem_3.draw()
    problem_3.flip()
