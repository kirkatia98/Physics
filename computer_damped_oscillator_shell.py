# Mass and Spring simulation
from visual import *
from visual.graph import *

# Setup the graphics display.
#gdisplay(title='Mass and Spring: Graph', xtitle='Time', ytitle='Displacement',xmax=10, ymax=.12, ymin=-.12, x=0, y=500, width=500, height=300)
scale = 1
Egraph= gdisplay(title='Energy vs Time', xtitle='Time', ytitle='Energy', xmax=15, ymax=scale, ymin=-scale, x=0, y=500, width=500, height=300)
# setup the spring constant (ks) and spring length (L)
ks = 0.70
L = 0.50

# Setup the time step (dt) and variables for keeping track
# of elapsed time.
dt = 0.002
t = 0
t_1 = 0
t_2 = 0

# Locate the wall holding the spring.
wall = box(pos=(0,0,0),size=(0.005,.1,.1),color=color.blue)

# Locate the mass at the end of spring.
bob = sphere(radius=.02,color=color.red)
s_0 = vector(0.2,0,0) #Initial displacement from equilibrium
bob.pos = vector(L,0,0) + s_0
bob.mass = 0.02
bob.velocity = vector(0,0,0)
bob.momentum = bob.velocity*bob.mass
x_0 = bob.pos.x #Initial x position of bob for future reference

# Define a spring as a helix, and then define the
# equilibrum position of the free end of the spring.
spring = helix(pos=wall.pos,axis=bob.pos-wall.pos,radius=0.005,thickness=.002,coils=10,color=color.green)
spring.equil = wall.pos + vector(L,0,0)

# Set up a curve on the graphics display.
k= gcurve(color=color.magenta)
s=gcurve(color=color.blue)
tt=gcurve(color=color.orange)
# Compute and print the expected period.
omega = sqrt(ks/bob.mass)
period = 2*3.14159265/omega
print "Period = ",period,' seconds'
scene.autoscale = 0

kinetic = (mag(bob.momentum) ** 2) / bob.mass /2
potential = ks * (mag((bob.pos-spring.equil)) ** 2)/2
total = kinetic + potential

B = sqrt(ks*bob.mass)
B=0.03
F_0 = ks*s_0
w_d = sqrt(ks/bob.mass)
# Loop to produce motion.
while(1==1):
    rate(200)
    t += dt
    #You will have to adjust the force equation for later parts of the problem
    
    force = -ks*(bob.pos-spring.equil)
    force -= B*bob.momentum/bob.mass
    force += F_0 * cos(w_d * t)
    dp = force*dt
    bob.momentum += dp
    bob.pos += dt*bob.momentum/bob.mass
    
    kinetic = mag(bob.momentum) ** 2 / bob.mass /2
    potential = ks * (mag((bob.pos-spring.equil)) ** 2)/2
    total = kinetic + potential
    #The if statement below these comments calculates the period.
    #You may comment it out if you'd like.
    if (x_0-bob.pos.x<= 0):
        t_2 = t
        period = (t_2 - t_1)
        t_1 = t
        print "Period = ",period,' seconds'

    spring.axis=bob.pos-wall.pos

    #Put calcuations for energy here. Define sensible variable names for them
    #BEFORE the while loop and make sure to give them an initial value.
    #Plots go below. Displacement in the x-direction from equilibrium is
    #given as an example.
    k.plot(pos=(t,kinetic))
    s.plot(pos=(t,potential))
    tt.plot(pos=(t,total))
