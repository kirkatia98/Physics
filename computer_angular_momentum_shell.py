#
#  VPython shell program to display and plot the Earth's motion about the Sun,
#  including its angular momentum vector and its Runge-Lenz vector.
#
from visual import *
from visual.graph import *
#
# Define the display window.  The range sets the scale for all arrows.
#
display(title = 'Planetary Orbit', width = 600, height = 600, range = 3e11)
#
G = 6.67e-11                       # gravitational constant
#
year  = 365.25 * 24.0 * 3600.0     # number of seconds in a year
#
tmax = 2.0 * year                  # set the maximum time of motion at 2 years.
#
# Set the time step value in seconds.
#
dt = 5000
#
#  Set up the Sun and the Earth objects.  Start the Earth along the +x axis.
#
sun = sphere(pos = (0, 0, 0), radius = 7e9, color = color.yellow)
#
sun.mass = 2e30             # Sun's mass
#
earth = sphere(pos = (1.5e11, 0, 0), radius = 3.2e9, color = color.cyan)
#
earth.mass = 6e24          # Earth's mass
#
# Find the Earth's speed for a circular orbit.
#
speed = 6.28 * earth.pos.x / year         # Earth's speed
#
# Initialize the Earth's momentum.  Start it moving in the +y direction.
#
earth.momentum = earth.mass * vector(0.0, speed, 0.0)
#
# Have the Earth leave a trail.
#
trail = curve(color = earth.color)
#
# Define the arrows for the gravitational force and momentum vectors.
#
forcearrow = arrow(shaft = 1e6, color = color.red)
#
momentumarrow = arrow(shaft = 1e6, color = color.green)
#
# Define the arrows for the angular momentum and Runge-Lenz vectors here.
#
point = (1.5e11, 0, 0)
angular_arrow = arrow(shaft = 1e5, color = color.blue)
angular_arrow.pos = point

runge_lenz_arrow = arrow(shaft = 1e6, color = color.orange)
#
# Set up the graphing window for plotting the magnitudes of the angular 
# momentum and Runge-Lenz vectors.  Notice the maximum y value of the plot.
#
gdisplay( title = 'Angular Momentum vs. Time', xtitle = 'Time (s)',
          ytitle = 'Angular Momentum (scaled)', xmax = tmax, ymax = 10.0,
          x = 0, y = 600, width = 500, height = 300 )
#
# Define the angular momentum and Runge-Lenz plots here.
#
#
scene.autoscale = 0    # turn off auto scaling.
#
t = 0                  # intialize the total time.
#
k = G * earth.mass * sun.mass        # Calculate the force constant.
#
# Here is the loop in which the Earth moves.  
#
while (t < tmax):
#
    rate(1000)         # limit the rate of the loop
#
# Calculate the gravitational force on the Earth:
#
    earth.force = -k * norm(earth.pos - sun.pos) / ( mag(earth.pos - sun.pos) )**2
#
# Update the Earth's momentum and position.
#
    earth.momentum = earth.momentum + earth.force * dt
    earth.pos      = earth.pos + (earth.momentum / earth.mass) * dt
#   
#   Append the Earth's path and update the momentum and force vector's 
#   positions and lengths.
#
    trail.append(pos = earth.pos)
#
    momentumarrow.pos = earth.pos
    momentumarrow.axis = earth.momentum / 5e18       # Scale the display length.
#
    forcearrow.pos = earth.pos
    forcearrow.axis = earth.force / 1e12             # Scale the display length.
#
#   Calculate the angular momentum and Runge-Lenz vectors here.  Then display
#   and plot them versus time.  You will have to scale the length of the arrows 
#   to fit them in the display window and also scale the magnitudes of the vectors 
#   to fit on the plot.
#
    angular_arrow.axis = cross(earth.pos - point, earth.momentum) / 5e29
    runge_lenz_arrow
    
    t = t + dt               # Increment the time
#
print "Orbit program has finished"
#    






