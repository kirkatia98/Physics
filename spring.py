from visual.graph import *     # note the slight change here.
from visual import *
# Define a graph, this will open its own window. Note that the x=0 and y=0
# define the origin of the graph plot, width and height are the size in
# pixels on your computer screen, xmin,ymin, xmax and ymax are the
# minimum and maximum values on each axis, title is the global title,
# xtitle is the label on the x-axis and ytitle is the label on the
# y-axis. Colors are controlled with foreground and background.

gdisplay(title='Mass and Spring: Graph', xtitle='Time', ytitle='Displacement', xmax=10.0, ymax=2, ymin=-2, x=0, y=500, width=500, height=300)
                  #
                  # You can then define curves that will appear in the graph window.
#
# Mass and Spring simulation (Problem 4.HW.73)
# Everything is in MKS units
#
#
# Define objects needed for display. We will use a helix object for the spring.
#
block  = box(pos=(-.5,0,0),size=(.02,.02,.02),color=color.red)
wall   = box(pos=(0,0,0),size=(0.005,.1,.1),color=color.blue)
spring = helix(pos=wall.pos,axis=block.pos,radius=0.005,thickness=.002, coils=10,color=color.green)
#
# equilibrium position of the end of the spring.
#
spring.equil = vector(0,0,0)
#
#---------------------------------------------------------
#
# Input Parameters needed in the program. Be sure to
# choose sensible values.
#
block.mass = .5
block.pos  = vector(.5,0,0)
block.mom  = vector(0,0,0)
spring.ks  = 10
dt = .01
t  = 0.0
#
#---------------------------------------------------------
#
scene.autoscale = 0          # Turn off auto scaling
#
#mass of block in kilograms
#initial position of block meters
#initial mometum of block in kg m/s
#Newtons per meter
#time step in seconds
#total elapsed time (leave as zero here)
# Setup a graph window to plot things in
#
#
#
#
drawit = gcurve(color=color.magenta)
#
while(1==1):
    rate(100)
    t = t + dt #
    # # #
    # # #
    #Compute the relevant physics part of the program to get the block
    #to oscilate at the end of the spring.
    spring.stretch = -spring.equil + spring.axis 
    spring.force = -spring.stretch  * spring.ks * mag(spring.stretch) ** 20
    block.mom += spring.force * dt
    block.pos += (block.mom * dt)/block.mass
    #Specify that the spring conncets the wall to the block.
    spring.axis= block.pos
                       #
                       # #
                       #Plot the x-coordinate of the block as a function of time.
    drawit.plot(pos=(t,block.x))
                           #
