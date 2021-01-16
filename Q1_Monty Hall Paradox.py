"""
Abhinav Chandravanshi
20103004
CE605_Project_1_Q1
"""

import random as r
import numpy as np
import matplotlib.pyplot as plt

Nsim = 1000 #Number of Simulation
Door = ["car", "goat", "goat"]
w_noswitch = 0 #Number of wins if door not switched
p_noswitch = [] #List containing probability of win (after each simulation) if not switched
w_switch = 0 #Number of wins if door switched
p_switch = [] #List containing probability of win (after each simulation) if switched


for i in range(Nsim):

    r.shuffle(Door) #Shuffling position of car before each Simulation
    choice = r.randrange(2) #variable for selecting an element from list door

    if Door[choice] == "car":
        w_noswitch = w_noswitch + 1
    else: w_switch = w_switch + 1

    p_noswitch.append(w_noswitch/(i+1))
    p_switch.append(w_switch/(i+1))

print(p_noswitch)
print(p_switch)

#Plot Characteristics
plt.plot(p_noswitch, label='Option 1: Stick')
plt.plot(p_switch, label='Option 2: Switch')
plt.title('Monty-Hall Problem')
plt.ylabel('Probability of Winning')
plt.yticks(np.arange(0, 1, .1))
plt.xlabel('Number of Simulations')
plt.xlim(100, Nsim)
plt.grid(True)
plt.legend()

plt.show()





