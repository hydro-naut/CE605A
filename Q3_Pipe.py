"""
Abhinav Chandravanshi
20103004
CE605_Project_1_Q3
"""

import random
import numpy as np
import matplotlib.pyplot as plt

D = [1, 0] # "1" denotes defective "0" denotes non-defective piece
NumberD = 0 #Count of Defective Piece
NumberNonD = 0 #Count of Non-Defective Piece
Nsim = 1000

for i in range(Nsim):
    #Assigning Weights for Defective piece and Non-Defective piece
    #production from each machine in accordance to question
    Machine_A = random.choices(D, weights=(60,40), k=1)
    Machine_B = random.choices(D, weights=(70,30), k=1)
    Machine_C = random.choices(D, weights=(80,20), k=1)
    Pipe = Machine_A, Machine_B, Machine_C #Sample creation
    print(Pipe) #Printing the sample
    if [1] in Pipe: #Finds Defective piece in sample
        NumberD = NumberD + 1
    

p_D = NumberD / Nsim #Probability Calculation
print("The probability of that any Defect in the Pipeline will be detected:",p_D)



