#*******************************************************************************
# Probability Computations Program Shell
#
from visual import *
from visual.graph import *
from random import *
from visual.factorial import *
#
# Set up the total number of samples and experiments
#
N = 10 # Number of particles to distribute
Nexpt= 100 # Number of experiments for last part.
#
# The following is a list that allows us to store the probability
# for each of the N1=0 to N1=N possibilities. The list has N+1 entries,
# so if you increase N from 10, be sure to change the number of entries
# here.
#
probdata=[]
#
# Set up the two volumes:
#
V = 1.0 # Let the total volume be one unit
ratio = 0.50 # Set up the ratio V1/V
V1 = V*ratio
V2 = V-V1
#
# Setup the graphical displays. You are likely to need to modify
# some of this as you go through the various programs.
#
scene1 = gdisplay(title="Probability",width=400,height=200,xmin=0,xmax=N,ymin=0,xtitle="N",ytitle="Probability")
probplot=gvbars(color=color.blue)
#
# --------------------------------------------------
# Initialization Complete, Start Actual Calculations
# --------------------------------------------------
#
Max = 0 # Most probable value of N1
MaxValue = 0 # Probability of most probable value of N1
Average = 0 # Average value of N1
#
# Use the Analytic formula to compute the probability
# for each value of N1, and then find the most probable
# and the average.
#
N1=0
while (N1<=N):
#
# Compute your probability for our choice of N1
#
    p= ???
#
# Add this probability to the list of probabilities
#
    probdata.append(p)
#
# Do a check to see if the current value of p is the maximum value.
# (Max and MaxValue)
#
...
#
# Update your running sum for the average value of N1
# (Average)
#
...
#
# Go to the next value of N1
#
    N1+=1
#
# We have finished the loop, print out the numerical results.
#
print " Analytic Results:"
print " Average Value of N =",Average
print " Most Probable N =",Max,"; Probability=",MaxValue
print " --------------------"
#
# Plot the probability distributions in a window, assuming that we
# have the filled probdata array from above.
#
i=0
while (i<=N):
    probplot.plot(pos=(i,probdata[i]))
    i+=1
#
