from gl import Raytracer, V3
from figures import *
from lights import *


width = 900
height = 1800

# Materiales

white = Material(diffuse = (1, 1, 1))
black = Material(diffuse = (0, 0, 0))
orange = Material(diffuse = (1, 0.69, 0))


rtx = Raytracer(width, height)

rtx.lights.append( AmbientLight( ))

rtx.lights.append( DirectionalLight(direction = (-1,-1,-10) ))

rtx.scene.append( Sphere(V3(0.05,2.1,-5), 0.2, orange))

rtx.scene.append( Sphere(V3(0,  3.9,  -10), 1.5, white)  )   #head ball
rtx.scene.append( Sphere(V3(0,  1,    -10), 2, white)  )       #body ball
rtx.scene.append( Sphere(V3(0,  -2.7, -10), 2.5, white)  )  #feet ball


rtx.scene.append( Sphere(V3(1.75, 3.5,10), 0.4, black)  )  #top button
rtx.scene.append( Sphere(V3(1.75, 2,10),   0.4, black)  )  #top button
rtx.scene.append( Sphere(V3(1.75, 0,10),   0.6, black)  )  #top button

rtx.scene.append( Sphere(V3(1.8, 5.8,  15), 0.1, black)  )  #mouth 1
rtx.scene.append( Sphere(V3(2.1,   5.5,  15), 0.1, black)  )  #mouth 2
rtx.scene.append( Sphere(V3(2.5, 5.45,  15), 0.1, black)  )  #mouth 3
rtx.scene.append( Sphere(V3(2.85, 5.7,  15), 0.1, black)  )  #mouth 4

rtx.scene.append( Sphere(V3(0.7, 4.5, -5), 0.4, orange)  )  #nose


rtx.scene.append( Sphere(V3(1.85, 6.8,  15), 0.1, black)  )  #eye 1 
rtx.scene.append( Sphere(V3(2.8, 6.8,  15), 0.1, black)  )  #eye 2


rtx.glRender()

rtx.glFinish("output.bmp")