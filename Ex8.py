import random
from random import randint
nums= [random.randint(-30,30) for r in range(30)]
exist=0
for i in range (30):
    for j in range (i,30):
        for k in range (j,30):
            z= nums[i] + nums[j] + nums[k]
            if z== 0 and nums[i]!= nums[j] and nums[i]!= nums[k] and nums[j]!= nums[k] :
                exist=1
                print (nums[i],nums[j],nums[k])
if exist==0 :
    print ("Δέν υπάρχει συνδιασμός που το άθροισμα του να είναι 0.")