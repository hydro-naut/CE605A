"""
Abhinav Chandravanshi
20103004
CE605_Project_1_Q2
"""

import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

N_SIM = 10000
F_BDay = []
Probabilities = []


#Performs simulations to generate a list of random birthdays
#and creates a list to store the day every time first repetition of birthdays occur
for i in range(N_SIM):
    BDayArray = np.random.random_integers(1, 365, 366)
    BDayList = BDayArray.tolist()
    Unique = set()
    RepeatedBDay = []

# Searches for First Matching Birthday
    for j,val in enumerate(BDayList):
        if val not in Unique:
           Unique.add(val)
        else:
           RepeatedBDay.append(j+1)
    F_BDay.append(RepeatedBDay[0])

print("Number of people for getting the first same birthday in each simulation are: ")
print(F_BDay)

#Analysing the results of simulation
Freq = Counter(F_BDay)
Day = list(Freq.values())
Ntime = list(Freq.keys())

for x in Day:
    Probabilities.append(x/N_SIM)

print("Probabilities of two people getting same birthday  ")
print(list(enumerate(Probabilities, start=2)))

plt.title("Obtained PMF from Simulations")
plt.xlabel("Number of people to get first same birthday")
plt.ylabel(" Probability ")
plt.bar(list(Freq.keys()), Probabilities)
plt.show()


#Function to calculate sum of elements in Probabilities[]
#and return list of probabilities untill sum becomes 0.5
def pmflist(nums, limit):
  prefix = []
  sum = 0
  for num in nums:
    sum += num
    prefix.append(num)
    if sum > limit:
      return prefix


#command to find the number of element required to make the sum 0.5
n = len(pmflist(Probabilities,.5))
print("Number of people required to have a 50% chance of two people getting same birthays")
print(n)
#Simulation complete

"""
#Analytical Solution Calculator
B = 23
def Calc_P(B):
    Q = 1
    for o in range(1, B):
        probability = o / 365
        Q = Q * (1 - probability)
    P = 1 - Q
    print ("Probability: " + str(P))

Calc_P(B)
"""