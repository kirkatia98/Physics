from visual import *
from visual.grap
#
#   Scale factor to put numbers on scale of graph
#
pscale = 10**6
G=6.67E-11
#
# Locate the Earth and moon olong the x-axis.
#
earthlocation=vector(0,0,0)
moonlocation=vector(4.0e8,0,0)
#
#
# Set up the displays
#
scene=display(x=0,y=50,title="Energy during a Voyage to the Moon",
              width=800,height=100,
              center=moonlocation/2.0)
#
#
earth = sphere(pos=earthlocation, radius=6.4e6, color=color.blue)
moon  = sphere(pos=moonlocation, radius=1.76e6, color=color.cyan)
earth.mass = 6.0e24     #earth mass in kilograms
moon.mass  = 7.0e22     #true moon mass
#
# Initialize the spaceship
#
shiplocation=vector(earth.radius+50000,0,0)
shipspeed=11800.
ship  = cylinder(pos=shiplocation, axis=(5e6,0,0), radius=2e6)
#
ship.mass  = 173
ship.speed = shipspeed
ship.momentum=vector(ship.mass*ship.speed,0,0)
trail = curve(color=ship.color)
#
# Create graphic for the energy display.
#
energyplot = gdisplay(x=0,y=200,xmin=0,
                      xmax=moonlocation.x/pscale, #scale numbers
                      ymin=-1000,ymax=1000,
                      title='Energy versus position',
                      xtitle='Ship Position',
                      ytitle='Energy')
# scene.autoscale=0 #
t =0
dt = 100
#
#
runit=1
while (runit==1):
    #
    rate(1000)
    #
    # Calculate the force exerted on the ship by the Earth:
    #
    earth.force = norm(earth.pos-ship.pos)*(G*earth.mass*ship.mass)/(mag(ship.pos-earth.pos) ** 2)
    #
    # Caluclate the force exerted on the ship by the Moon:
    #
    moon.force  = norm(moon.pos-ship.pos)*(G*moon.mass*ship.mass)/(mag(ship.pos-moon.pos) ** 2)
    #
    # Calculate the total force on the ship, and then use this
    # in Newton's 2nd law.
    #
    ship.force    = earth.force + moon.force
    ship.momentum = ship.momentum + ship.force*dt
    dr            = dt * ship.momentum/ship.mass
    ship.pos      = ship.pos + dr
    #
    trail.append(pos=ship.pos)  #append a piece to the end of the ship's trail
    #
    # (some of your code goes here...)
    t=t+dt
    #
    # Check if we fell back to the earth or hit the moon:
    #
    if (mag(ship.pos-earth.pos) <= earth.radius ):
        print "Ship crashed back on the earth"
        runit=0
    elif (mag(ship.pos-moon.pos) <= moon.radius ):
        print "Ship crashed on the moon at time ",t, "seconds"
        runit=0
print "All done."
# End of program
