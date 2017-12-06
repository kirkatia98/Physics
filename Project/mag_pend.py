from visual import *
import scanf

#READ IN INILITILIZATIONS FROM A TEXT FILE

#length of pendulum, scalar
length = 
#height of pendulum above ground, scalar
height =
#mass of the bob, (rod can be massless), scalar
mass =
#the orientation, and strength of the magnetic bob
p_moment = 


timestep =
theta_step = 
phi_step =

damping = 

#CONSTANTS
g = 9.81
u_0 = 8.85e10-12

def sphere_to_vector(p, t):

def calculate_force():
def trace_path():

def main():
    scene = display(title="Orbits",width=700,height=700,range=3*length)
    scene.autoscale=0

    #For every phi
    for theta in range(0, 2*pi, theta_step):
        #For every theta
        for phi in range(0, pi/2, phi_step):

            

if __name__ == "__main__":
    main()
