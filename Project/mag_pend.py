from visual import *
import time

# import scanf

# READ IN INILITILIZATIONS FROM A TEXT FILE

# length of pendulum, scalar
length = 50 
# height of pendulum above ground, scalar
height = 10
# mass of the bob, (rod can be massless), scalar
mass = 3
# the orientation, and strength of the magnetic bob
p_moment = 0


timestep = 1
theta_step = 0.1
phi_step = 0.1

damping = 0

# CONSTANTS
g = 9.81
u_0 = 8.85e10-12


def sphere_to_vector(p, t):
    z = height + length * (1 - cos(p))
    r = sin(p) * length
    y = r*sin(t)
    x = r*cos(t)
    return vector(x,y,z)


def cos_phi(pos):
    arc = (pos.z - height)/length
    return 1 - arc


def calculate_force(bob, rod):
    pos = bob.pos 
    gravity = mass * g
    tension = -gravity/cos_phi(pos)) * norm(rod.axis)
    # add summing over array of magnetic moments
    return vector(0, 0, -mass * g) + tension


def trace_path(initial, rod, bob):
    # place the rod, and the ball at the initial position
    bob.pos = initial 
    rod.axis = bob.pos - rod.pos
    pos = bob.pos
    time = 0
    
    force = vector(0,0,0)
    force_arrow = arrow(pos=bob.pos, axis=force, color=color.blue)
    
    momentum = vector(0,0,0)
    mom_arrow = arrow(pos=bob.pos, axis=momentum, color=color.blue)
    
    pos = arrow(pos=bob.pos, axis=pos, color=color.blue) 
    while(time < 1000)
        force = calculate_force(bob.pos)
        force_arrow = arrow(pos=bob.pos, axis=force, color=color.blue)
        momentum+= force
        

        time += tempstep

def main():
    scene = display(title="Pendulum",width=700,height=700,range=3*length)
    scene.autoscale=0

    floor = cylinder(pos=(0,0, 0), axis =(0,0,1), radius=length)

    # set the pendulum to zero
    rod = arrow(pos=(0,0,length + height),axis=(0,0,-length), 
        shaftwidth=length*0.05, color=color.green)
    bob = sphere(pos=(0, 0, height), radius=2, color=color.green,
        make_trail=True, trail_type="points") 
    
    
    theta = 0
    while(theta <= 2*pi):
        phi = -pi/2
        while(phi <= pi/2):
            init_pos = sphere_to_vector(phi, theta)
            trace_path(init_pos, rod, bob)
            sleep(1)
            phi += phi_step
        theta += theta_step


if __name__ == "__main__":
    main()
