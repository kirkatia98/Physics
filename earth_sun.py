from visual import *
#
# General setup functions for display. The first opens a display
# of a predefined size, while the second prevents autoscaling.
#
scene = display(title="Orbits",width=700,height=700,range=5.e11)
scene.autoscale=0 # supress scene jitter
#
# ---------------------------------------------------------------
# Define the sun and the earth:
#
sun = sphere(color=color.yellow,pos=vector(0,0,0),radius=7e9)
earth = sphere(color=color.blue,pos=vector(1.5e11,0,0),radius=3.2e9)
#
#
# Set up contants and initial conditions that will be needed by
# the program. Work these out in advance and enter them here.
#
G = 6.67e-11
earth.pos = vector(1.5e11,0,0)
sun.mass = 1.98e30
earth.mass = 5.98e24
#
dt = 1.e5
total =0
#
sec_year = 365.25*24*3600
speed = 2*pi*earth.pos.x/sec_year
earth.velocity = vector(0,speed,0)
# Some scale factors to control how big the earth and sun are drawn # on the plot.
#
sun.scale = 1e1
earth.scale = 5e2
3
# Gravitational Constant
# Initial Sun Position
# Initial Earth Position
# Mass of the sun   (kg)
# Mass of the earth (kg)
# time increment in seconds (choose a sensible value?)
# total elapsed time
# Initial speed of the Earth (m/s)
#
sun.radius   = 7.e8*sun.scale
earth.radius = 6.4e6*earth.scale
#
# Initialize the momentum of the earth and sun.
#
earth.momentum = earth.mass*earth.velocity
earth.trail = curve(color=earth.color)
earth.trail.append(pos=earth.pos)
#
#
# Define an arrow that points from the origin to the earth
#
radius = vector(1.5e11,0,0) - earth.pos
ang_mom = cross(radius, earth.momentum)/1e10
print(ang_mom)

rearrow = arrow(pos=earth.pos, axis=sun.pos, color=earth.color,  shaftwidth=5e9)
mom_arrow = arrow(pos=earth.pos, axis=earth.momentum*1e-22, color=color.orange, shaftwidth=5e9)
ang_arrow = arrow(pos=sun.pos, axis=ang_mom, color=color.red, shaftwidth=5e9)
                  
#
# We will loop for one year, and then stop.
#
# Useful commands:
# If vec is a vector, then mag(vec) is the magnitude of the vector
# and norm(vec) is a unit vector along the vector.
#
years = 5
# Top of loop
while (total/3600/24 < 365 * years):
    rate(100)         # limit the loop to a maximum of 100 times per second.
    earth_to_sun = sun.pos - earth.pos
    force = G * sun.mass * earth.mass * norm(earth_to_sun) / mag(earth_to_sun)**2 # compute the force that the sun exerts on the earth.
    earth.momentum += force * dt 
    # update the earth’s momentum
    earth.velocity = earth.momentum/earth.mass
    earth.pos += earth.velocity * dt
    # update the earth’s position
    
    rearrow.axis = force * 1e-12
    rearrow.pos = earth.pos
    mom_arrow.pos= earth.pos
    mom_arrow.axis= earth.momentum * 1e-19
    earth.trail.append(pos=earth.pos)  # draw the trail
    total = total + dt # increment the time
                    #
                    # print this stuff when the loop is done!
                    #
    #print 'All done.'
