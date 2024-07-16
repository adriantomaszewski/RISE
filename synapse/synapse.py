import numpy as np
import matplotlib.pyplot as plt
import math

# simulation parameters
tmax = 0.1                    # total seconds of simulation time
dt = 0.0001                   # time-step in seconds
gmax = 0.005                  # max capacitance in microFarads
tau_rise = 0.002              # rise time in seconds
tau_decay = 0.008             # decay time in seconds
E_syn = 0                     # synaptic reversal potential in mV
E_L = -0.060                  # leak potential (also resting potential)
g_leak = 0.02                 # leak capacitance
Vth = -0.050                  # threshold potential (to produce spike)
Vreset = -0.080               # reset potential (post-spike)
Cm = 1e-6                     # total membrane capacitance

# range() wont work for us here becasue our dt is a 'float'
# so we use np.arange which supports our data type
t_vector = np.arange(0,tmax,dt) # vector of time-points
ton = 0                         # time to begin applied current (onset)
toff = 0.1                      # time to end applied current (offset)
ind_on = round(ton/dt)          # time-point index of current onset sicne it isnt exact
ind_off = round(toff/dt)        # time-point index of current off sicne it isnt exact

I = np.zeros(len(t_vector))     # initializing a vector for applied current at each time-point
Iapp = 210e-12                  # magnitude of applied current step in Amps
I[ind_on:ind_off] = Iapp        # add the applied current for the trial

V = np.zeros(len(t_vector))        # initialize the membrane potential vector
g_syn = np.zeros(len(t_vector))      # initialize a vector to record spikes

def main():
    for loopiter, t in enumerate(t_vector):
        try:
            g_syn[loopiter]=gmax*(-math.e**(-t/tau_rise)+math.e**(-t/tau_decay))
            I[loopiter]=g_syn[loopiter]*(V[loopiter]-E_syn)
            dVdt=(-I[loopiter]-g_leak*(V[loopiter]-E_L))/Cm
            if V[loopiter]<Vth:
                    V[loopiter+1]=V[loopiter]+dVdt*dt
            else:
                    V[loopiter+1]=Vreset
        except:
                break
    fig, ax = plt.subplots(2)
    ax[0].plot(t_vector, g_syn)
    ax[1].plot(t_vector, I)
    fig.show()


if __name__=="__main__":
    main()