from visual import *
#import scanf

#READ IN INILITILIZATIONS FROM A TEXT FILE

#length of pendulum, scalar
length = 50 
#height of pendulum above ground, scalar
height = 10
#mass of the bob, (rod can be massless), scalar
mass = 3
#the orientation, and strength of the magnetic bob
p_moment = 0


timestep = 1
theta_step = 1 
phi_step = 1

damping = 0

#CONSTANTS
g = 9.81
u_0 = 8.85e10-12

def sphere_to_vector(p, t):
    z = height + length * (1 + cos(p))
    r = sin(p) * length
    y = r*sin(t)
    x = r*cos(t)
    return vector(x,y,z)


#def calculate_force():

def trace_path(intial, rod, bob):
    #place the rod, and the ball at the initial position
    rod.axis=initial, 
    bob.pos = initial 

def main():
    scene = display(title="Pendulum",width=700,height=700,range=3*length)
    scene.autoscale=0

    floor = cylinder(pos=(0,0, 0), axis =(0,0,1), radius=length)

    #set the pendulum to zero
    rod = arrow(pos=(0,0,length + height),axis=(0,0,-length), 
        shaftwidth=length*0.05, color=color.green)
    bob = sphere(pos=(0,0,height), radius=2, color=color.green) 
    
    #For every phi
    #for theta in range(0, 2*pi, theta_step):
        #For every theta
        #for phi in range(0, pi/2, phi_step):

if __name__ == "__main__":
    main()
