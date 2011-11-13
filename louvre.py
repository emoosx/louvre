from pyglet.gl import *
from pyglet.window import key
from resources import grid,camera,draw_localAxis

from models.floor import floor
from models.teapot import teapot
from models.basketball import basketball
from models.snowman import snowman

class louvre(pyglet.window.Window):
    def __init__(self):
        super(louvre, self).__init__(width=800,height=600)

        self.set_exclusive_mouse(True)
        self.grid    = grid(size=500)
        self.camera  = camera(pos=(0., -100., -750.),rot=(0.,0.,0.),window=self)
        self.renderMode = GL_FILL

        # rotational values
        self.xrot = self.yrot = self.zrot = 0.0

        # lighting
        self.light = False

        # walls and floors
        self.floor = floor(500, 500, 'lightwood.jpg')
        self.right_wall = floor(500, 500, 'lightwood.jpg')
        self.left_wall = floor(500, 500, 'lightwood.jpg')
        self.behind_wall = floor(500, 500, 'lightwood.jpg')



        # Exhibits
        self.exhibits = []

        self.teapot = teapot()   
        self.exhibits.append(self.teapot)

        self.basketball = basketball()
        self.exhibits.append(self.basketball)

        self.snowman = snowman()
        self.exhibits.append(self.snowman)


         
        # Current Focus
        self.current_index = 0
        self.current_focus = self.exhibits[self.current_index]

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

        # Control of rotational axes
        if sym == key.X:
            self.current_focus.xrot = not self.current_focus.xrot
            print "Rotation by X axis : %r " % self.current_focus.xrot
        if sym == key.Y:
            self.current_focus.yrot = not self.current_focus.yrot
            print "Rotation by Y axis : %r " % self.current_focus.yrot
        if sym == key.Z:
            self.current_focus.zrot = not self.current_focus.zrot
            print "Rotation by Z axis : %r" % self.current_focus.zrot

        if sym == key.UP:
            self.current_focus.scale += 0.5 
        if sym == key.DOWN:
            if self.current_focus.scale <= 0.5:
                self.current_focus.scale = 0.5
            else:
                self.current_focus.scale -= 0.5
        if sym == key.T:
            self.current_focus.texture_status = not self.current_focus.texture_status
        if sym == key.TAB:
            if self.current_index == len(self.exhibits) - 1:
                self.current_index = 0
            else:
                self.current_index += 1
            self.current_focus = self.exhibits[self.current_index]

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

        for exhibit in self.exhibits:
            exhibit.update()
    # your draw function
    def draw(self):
        glEnable(GL_TEXTURE_2D)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glEnable(GL_DEPTH_TEST)

        self.camera.draw()
        # self.grid.draw()

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
        glPushMatrix()
        glTranslatef( -300, self.teapot.shelf.height, 0)
        self.teapot.draw()
        glPopMatrix()

        # basketball
        glPushMatrix()
        glTranslatef( 300, self.basketball.shelf.height, 0)
        self.basketball.draw()
        glPopMatrix()

        # snowman
        glPushMatrix()
        glTranslatef(-300, self.snowman.shelf.height, 400)
        glRotatef(90, 0, 1, 0)
        self.snowman.draw()
        glPopMatrix()

assignment_1 = louvre()
while not assignment_1.has_exit:
    assignment_1.update()
    assignment_1.draw()
    assignment_1.flip()
