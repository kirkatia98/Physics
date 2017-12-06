#
from visual import *
from visual.graph import *
#
# Scale factor to put numbers on scale of graph
#
pscale = 10**6
G=6.67E-11
#
# Locate the Earth and moon along the x-axis.
#
earthlocation=vector(0,0,0)
moonlocation=vector(4.0e8,0,0)
#
#
# Set up the displays
#
scene=display(x=0,y=50,title="Energy during a Voyage to the Moon",width=800,height=300,center=moonlocation/2.0)
#
#
speed_light = 299792458 
earth = sphere(pos=earthlocation, radius=6.4e6, color=color.blue)
moon = sphere(pos=moonlocation, radius=1.76e6, color=color.cyan)
earth.mass = 6.0e24 #earth mass in kilograms
moon.mass = 7.0e22 #true moon mass
#
# Initialize the spaceship
#
shiplocation=vector(earth.radius+50000,0,0)
ship = cylinder(pos=shiplocation, axis=(5e6,0,0), radius=2e6)
#
ship.mass = 173
ship.speed = vector(11800, 0, 0)
ship.momentum=ship.mass * ship.speed
trail = curve(color=ship.color)
#
# Create graphic for the energy display.
#
energyplot = gdisplay(x=0,y=400,xmin=0,xmax=moonlocation.x/pscale, ymin=-10000,ymax=10000,title='Energy versus position',xtitle='Ship Position',ytitle='Energy')
#
scene.autoscale=0
#
t = 0
dt= 1
#
pot = gcurve(color=color.magenta)
kin = gcurve(color=color.blue)
eng = gcurve(color=color.orange)
w = gcurve(color=color.green)
wt =  gcurve(color=color.red)
#
earth.potential = -(G*earth.mass*ship.mass)/(mag(ship.pos-earth.pos))
moon.potential = -(G*moon.mass*ship.mass)/(mag(ship.pos-moon.pos))

potential = earth.potential + moon.potential
rest_energy = ship.mass * speed_light ** 2

work = 0
work_total = 0
runit=1

while (runit==1):
    #
    rate(1000)
    #
    # Calculate the force exerted on the ship by the Earth:
    #
    earth.force = norm(earth.pos-ship.pos)*(G*earth.mass*ship.mass)/(mag(ship.pos-earth.pos) **2)
    #
    # Caluclate the force exerted on the ship by the Moon:
    #
 
    moon.force  = norm(moon.pos-ship.pos)*(G*moon.mass*ship.mass)/(mag(ship.pos-moon.pos) ** 2)
    #
    # Calculate the total force on the ship, and then use this
    # in Newton’s 2nd law.
    #
    ship.force = earth.force + moon.force
    ship.momentum += ship.force*dt
    dr = dt * ship.momentum/ship.mass
    ship.pos = ship.pos + dr
    work = dot(earth.force, dr) - dot(moon.force,dr)
    potential -= work
    work_total += work
    kinetic = (mag(ship.momentum) ** 2) / ship.mass /2
    energy = potential + kinetic
    #
    if(t % 1000 == 0):
        trail.append(pos=ship.pos) #append a piece to the end of the ship’s trail
    #
    # (some of your code goes here...)
    t=t+dt
    #
    # Check if we fell back to the earth or hit the moon:
    #

    pot.plot(pos=(ship.x/pscale, potential/pscale))
    kin.plot(pos=(ship.x/pscale, kinetic/pscale))
    eng.plot(pos=(ship.x/pscale, energy/pscale))
    w.plot(pos=(ship.x/pscale, work/pscale))
    wt.plot(pos=(ship.x/pscale, work_total/pscale))
    if (mag(ship.pos-earth.pos) <= earth.radius ):
        print "Ship crashed back on the earth"
        runit=0
    elif (mag(ship.pos-moon.pos) <= moon.radius ):
        print "Ship crashed on the moon at time ",t, "seconds"
        runit=0
#
print "All done."
# End of program
