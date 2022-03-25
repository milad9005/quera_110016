import random
import math

def roundup(x):
    return int(math.ceil(x / 100.0)) * 100


n = random.randint(1,20)
cost_buy = random.randint(1,1000)
cost_trac = random.randint(1,1000)


h_i=[]
for i in range(n):
    h_i.append(str(random.randint(1,10)))



print(','.join([str(n),str(cost_buy),str(cost_trac)]))
print(','.join(h_i))