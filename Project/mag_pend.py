from visual import *
import time

# import scanf

# READ IN INILITILIZATIONS FROM A TEXT FILE

# length of pendulum, scalar
length = 20 
# height of pendulum above ground, scalar
height = 10
# mass of the bob, (rod can be massless), scalar
mass = 1
# the orientation, and strength of the magnetic bobtimestep = 0.0001
phi_step = 0.1
theta_step = 0.5
timestep = 0.005
damping = 0.06

# CONSTANTS
g = 9.81
u_0 = 8.85e10-12


#SCENE
scene = display(title="Pendulum",width=700,height=700,range=3*length)
scene.autoscale=0

#FLOOR
floor = cylinder(pos=(0,0, 0), axis =(0,0,0.3), radius=length)

#PENDULUM
rod = arrow(pos=(0,0,length + height),axis=(0,0,-length), 
    shaftwidth=length*0.05, color=color.green)
bob = sphere(pos=(0, 0, height), radius=2, color=color.green)
#FORCE AND MOMENTUM
force_arrow = arrow(pos=bob.pos, axis=vector(0,0,0), color=color.blue)
mom_arrow = arrow(pos=bob.pos, axis=vector(0,0,0), color=color.orange)

#MAGNETS
p_moment = arrow(pos=vector(0,0,0), axis=vector(3,3,3), color=color.yellow)
magnets = [
    arrow(pos=vector(2,4,0), axis=vector(4,2,6), color=color.yellow),
    arrow(pos=vector(5,-6,0), axis=vector(1,-6,7), color=color.yellow),
    arrow(pos=vector(-10,9,0), axis=vector(-12,9,5), color=color.yellow)]

for m in magnets:
    m.f = m.axis/2e7
p_moment.f = p_moment.axis/2e7
    

def sphere_to_vector(p, t):
    z = height + length * (1 - cos(p))
    r = sin(p) * length
    y = r*sin(t)
    x = r*cos(t)
    return vector(x,y,z)

def cos_phi(pos):
    arc = (pos.z - height)/length
    return 1 - arc

start = 3
def magnet_force(m2):
    m1 = p_moment
    r = m1.pos - m2.pos
    rn = norm(r)
    K = 3*u_0/4/pi/(mag(r)**4)
    t1 = cross(cross(rn, m1.f), m2.f)
    t2 = cross(cross(rn, m2.f), m1.f)
    t3 = 2*rn*(dot(m1.axis, m2.f))
    t4 = 2*rn*(dot(cross(rn,m1.f), cross(rn, m2.f)))
    return K * (t1 + t2 + t3 + t4)
    


def calculate_force(bob, rod):

    pos = bob.pos 
    gravity = mass * g
    tension = gravity*cos_phi(pos) + ((mag(bob.momentum))**2)/mass/length
    # summing over array of magnetic moments
    mforce = vector(0,0,0)
    for m in magnets:
        mf = magnet_force(m)
        print mf
        mforce += proj(mf, bob.momentum)
    print tension
    print mforce
    print bob.pos
    Damp = -damping * bob.momentum
    net = -tension*norm(rod.axis) + vector(0, 0, -gravity) + Damp
    print net
    print net + mforce
    print "\n"
    
    if(isnan(mforce.x)):
        print "nan"
        return net
    else:
        return net + mforce


def trace_path(initial):
    # place the rod, and the ball at the initial position
    bob.pos = initial
    rod.axis = bob.pos - rod.pos
    p_moment.pos = bob.pos

    time = 0
    force = vector(0,0,0)
    bob.momentum = vector(0,0,0)
    while(time < 200 or mag(bob.momentum) > 1):
        rate(1000)
        
        force = calculate_force(bob, rod)
        force_arrow.axis=force
        force_arrow.pos = bob.pos
        
        bob.momentum+= force * timestep
        mom_arrow.axis = bob.momentum
        mom_arrow.pos = bob.pos
        
        bob.pos += (bob.momentum / mass) * timestep
        rod.axis = bob.pos - rod.pos
        
        p_moment.pos = bob.pos
        time += timestep
    sleep(0.5)

def main():
    # set the pendulum to zero
    
    
    phi = -pi/2
    while(phi <= pi/2):
        theta = 0
        while(theta <= 2*pi):
            init_pos = sphere_to_vector(phi, theta)
            
            trace_path(init_pos)
            
            sleep(0.1)

        phi += phi_step
    theta += theta_step


if __name__ == "__main__":
    main()
