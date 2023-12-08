#craet a randome list filled with the characters H and T
#for head and tails. output the number of Hs and Ts
import random
flipList = []

for i in range(1, 1010):
    flipList += random.choice(['H', 'T'])
    
print("Heads :", flipList.count('H'))
print("Tails :", flipList.count('T'))
