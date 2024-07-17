import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import math

# set up the LIF neuron parameters 
# notice that the reset potential is different than reversal/resting potential in this lab. 
# simulation parameters
tmax = 5                      # total seconds of simulation time
dt = 0.1e-3                     # time-step in seconds

t_vector = np.arange(0,tmax,dt) # vector of time-points

# Parameters for the LIF neuron
E = -70e-3               # leak potential (also resting potential)
Vth = -54e-3               # threshold potential (to produce spike)
Vreset = -80e-3            # reset potential (post-spike)
Rm = 10e+6                 # membrane resistance
Cm = 1e-9                  # total membrane capacitance
Iap1 = 2e-9                # applied current
Iapp2 = 2e-9               # applied current
sigma = 0                  #n noise

# set up your synaptic variables
# The synapses are modeled like additonal currents (or you can think of them as channels) 
# so they have their own max conductance and reversal potentials?
# E12 means the reversal potential of the synapse from neuron 1 to neuron 2, and vice versa.

Erev12 = -70e-3         # reversal potential for synapse 1 to 2 in milivolts
Erev21 = -70e-3         # reversal potential for synapse 1 to 2 in milivolts
G12 = 1e-6              # capacitance for synapse 1 to 2 in microfarads
G21 = 1e-6              # capacitance potential for synapse 1 to 2 in microfarads
tausyn = 10e-3          # msynaptic time constant
s1=1
s2=1

# insert new simualtion here with noise. 
# Plot your same variables again, including the synaptic gating variables. 
sigma = 50e-12/math.sqrt(dt)                 #n noise
fig, axs = plt.subplots(6)

# make an applied current (stimulation) vector using the base current we defined above, 
# give a constant 2nA to each neuron, adding an extra 3nA to each cell for a short pulse as written above.
ton = 1                         # time to begin applied current (onset)
toff = 2                        # time to end applied current (offset)
ind_on = round(ton/dt)          # time-point index of current onset sicne it isnt exact
ind_off = round(toff/dt)        # time-point index of current off sicne it isnt exact

Iapp = 2e-9                     # magnitude of applied current step in Amps
Ipulse =  0     
I1 = Iapp*np.ones(len(t_vector)) # magnitude of pulse current step in Amps
I1[ind_on:ind_off] = Iapp+Ipulse 

ton = 3                         # time to begin applied current (onset)
toff = 4                        # time to end applied current (offset)     # initializing a vector for applied current at each time-point
ind_on = round(ton/dt)          # time-point index of current onset sicne it isnt exact
ind_off = round(toff/dt)        # time-point index of current off sicne it isnt exact
I2 = Iapp*np.ones(len(t_vector))
I2[ind_on:ind_off] = Iapp+Ipulse

V1 = E*np.ones(len(t_vector))          # initialize the membrane potential vector
V2 = E*np.ones(len(t_vector))          # initialize the membrane potential vector
s1 = np.ones(len(t_vector))          # initialize the membrane potential vector
s2 = np.ones(len(t_vector))          # initialize the membrane potential vector

class Neuron:
    def __init__(self):
         pass
    def work():
        # code your forward Euler loop here:
        for loopiter, t in enumerate(t_vector):
            if loopiter == 0 or loopiter==49999:
                continue
            else:
                s1[loopiter]= s1[loopiter-1]+(-s1[loopiter-1]/tausyn)*dt
                s2[loopiter]= s2[loopiter-1]+(-s2[loopiter-1]/tausyn)*dt      
                dV1dt=((E-V1[loopiter-1])/Rm+G21*s2[loopiter]*(Erev21-V1[loopiter-1])+I1[loopiter-1]+sigma*random.randn())/Cm
                V1[loopiter]=V1[loopiter-1]+dV1dt*dt
                dV2dt=((E-V2[loopiter-1])/Rm+G12*s1[loopiter]*(Erev12-V2[loopiter-1])+I2[loopiter-1]+sigma*random.randn())/Cm
                V2[loopiter]=V2[loopiter-1]+dV2dt*dt   
        # for timestep in time vector:
            # simulate the synaptic gating variables first,
            # then simulate the membrane voltage for each cell using the equations above
                if V1[loopiter]>=Vth:
                        V1[loopiter] = Vreset
                        V1[loopiter-1]=0
                        s1=s1+(1-s1)
                        s2=s2+(1-s2)
                if V2[loopiter]>=Vth:
                        V2[loopiter] = Vreset
                        V2[loopiter-1]=0
                        s1=s1+(1-s1)
                        s2=s2+(1-s2)
            # if theres a spike
                # manually draw a spike by setting Vm to 0mV for one step
                # then reset the membrane voltage and the synaptic gating variables according to above

axs[0].plot(t_vector,I1) # plot applied current to neuron1)
axs[4].axis(ymin=0.99,ymax=1)
axs[1].plot(t_vector,V1) # plot V1)
axs[2].plot(t_vector,I2) # plot applied current to neuron2)
axs[3].plot(t_vector,V2) # plot V2)
axs[4].plot(t_vector,s2) # plot synaptic gating variable for one neuron)
axs[5].axis(xmin=1.5,xmax=1.75)
axs[5].plot(t_vector,V1) # plot V1)
plt.show()