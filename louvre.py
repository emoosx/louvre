from pyglet.gl import *
from pyglet.window import key
from resources import grid,camera,draw_localAxis

from models.floor import Floor
from models.teapot import Teapot
from models.basketball import Basketball
from models.snowman import Snowman
from models.painting import Painting

from utils.text import Text

class Louvre(pyglet.window.Window):
    def __init__(self):
        super(Louvre, self).__init__(width=800,height=600)

        self.set_exclusive_mouse(True)
        self.grid    = grid(size=500)
        self.camera  = camera(pos=(0., -100., -750.),rot=(0.,0.,0.),window=self)
        self.renderMode = GL_FILL

        # rotational values
        self.xrot = self.yrot = self.zrot = 0.0

        # lighting
        self.light = False

        # walls and floors
        self.floor = Floor(500, 500, 'lightwood.jpg')
        self.right_wall = Floor(500, 500, 'lightwood.jpg')
        self.left_wall = Floor(500, 500, 'lightwood.jpg')
        self.behind_wall = Floor(500, 500, 'lightwood.jpg')
        self.ceiling = Floor(500, 500, 'lightwood.jpg')


        # Exhibits
        self.exhibits = []

        self.teapot = Teapot()   
        self.exhibits.append(self.teapot)

        self.basketball = Basketball()
        self.exhibits.append(self.basketball)

        self.snowman = Snowman()
        self.exhibits.append(self.snowman)

        starry_night_label = "Starry Night Painting\n----------\n- Texture On/Off\n- Rotate by Z\n- Scaling On/Off" 
        self.starry_night = Painting(100, 100, 'starry_night.jpg', starry_night_label)
        self.exhibits.append(self.starry_night)
        

        scream_label = "Scream Painting\n----------\n- Texture On/Off\n- Rotate by Z\n- Scaling On/Off" 
        self.scream = Painting(100, 100, 'scream.jpg', scream_label)
        self.exhibits.append(self.scream)
        

        van_gogh_label = "Van Gogh Painting\n----------\n- Texture On/Off\n- Rotate by Z\n- Scaling On/Off"     
        self.scream = Painting(100, 100, 'scream.jpg', scream_label)
        self.van_gogh = Painting(50, 70, 'vangogh.jpg', van_gogh_label)
        self.exhibits.append(self.van_gogh)
        
        son_of_man_label =  " Son of Man Painting\n----------\n- Texture On/Off\n- Rotate by Z\n- Scaling On/Off"
        self.son_of_man = Painting(70, 100, 'son_of_man.jpg', son_of_man_label)
        self.exhibits.append(self.son_of_man)
         
        # Current Focus
        self.current_index = 0
        self.current_focus = self.exhibits[self.current_index]
        
        # Signboard
        sign_text = "Welcome to the Louvre\n--------------------\n* X - rotate an object via X\n* Y - rotate an object via Y\n* Z - rotate an object via Z\n* T - Enable/Disable Texture\n* UP-Arrow - Scale up\n* Down-Arrow - Scale down\n* Tab - Switch object\n---------------\nCurrent Object Index " + str(self.current_index)
        self.signboard = Text(sign_text, x = 0, y = 0)

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
        if sym == key.J:
            self.current_focus.shelf.height += 0.9
            print "Shelf Height of Obj %d is %f" % (self.current_index, self.current_focus.shelf.height)
        if sym == key.K:
            self.current_focus.shelf.height -= 0.9
            print "Shelf Height of Obj %d is %f" % (self.current_index, self.current_focus.shelf.height)
        

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

        sign_text = "Welcome to the Louvre\n--------------------\n* X - rotate an object via X\n* Y - rotate an object via Y\n* Z - rotate an object via Z\n* T - Enable/Disable Texture\n* UP-Arrow - Scale up\n* Down-Arrow - Scale down\n* Tab - Switch object\n---------------\nCurrent Object Index " + str(self.current_index)
        self.signboard.update(sign_text)
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

        # ceiling
        glPushMatrix()
        glTranslatef(0, self.left_wall.height * 2, 0)
        glRotatef(90, 1, 0, 0)
        self.ceiling.draw()
        glPopMatrix()

        # teapot
        glPushMatrix()
        glTranslatef( -200, self.teapot.shelf.height, 0)
        self.teapot.draw()
        glPopMatrix()

        # basketball
        glPushMatrix()
        glTranslatef( 200, self.basketball.shelf.height, 0)
        self.basketball.draw()
        glPopMatrix()

        # snowman
        glPushMatrix()
        glTranslatef(-200, self.snowman.shelf.height, 400)
        glRotatef(90, 0, 1, 0)
        self.snowman.draw()
        glPopMatrix()

        # paintings ( starry_night )
        glPushMatrix()
        glTranslatef(200, 300, -249)
        self.starry_night.draw()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-499, 300, 0)
        glRotatef(90, 0, 1, 0)
        self.scream.draw()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-200, 300, -249)
        self.van_gogh.draw()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(499, 300, 0)
        glRotatef(-90, 0, 1, 0)
        self.son_of_man.draw()
        glPopMatrix()

        # signboard
        glPushMatrix()
        glTranslatef(300, 100, 350)
        glRotatef(-45, 0, 1, 0)
        self.signboard.draw()
        glPopMatrix()

assignment_1 = Louvre()
while not assignment_1.has_exit:
    assignment_1.update()
    assignment_1.draw()
    assignment_1.flip()
