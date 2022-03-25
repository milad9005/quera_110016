
from cmath import cos


firstLine = input()
secLine = input()

firstLine = firstLine.split(' ')
secLine = secLine.split(' ')

a = int(firstLine[1])
b = int(firstLine[2])

secLine = [int(i) for i in secLine]
min = secLine[0]
cost=0

def trac (a,b,lst):
    sumOfDiff=0
    cost = 0
    cost_s=0
    min = lst[0]
    have_trac_cost= False
    max_l = max(lst)

    for _ in range(len(lst)):

        diffr = max_l - lst[0]
        cost_s += (diffr*a)
        if(lst[0]>min):
            sumOfDiff += (lst[0]-min)
            lst.pop(0)
            if(not have_trac_cost):
                have_trac_cost=True
                cost+=b
        elif(lst[0]<min):
            diff = min-lst[0]
            if(diff>sumOfDiff):
                need = diff - sumOfDiff
                sumOfDiff += need
                cost += (need * a)
            sumOfDiff-=diff
            lst.pop(0)
        else:
            lst.pop(0)
            
    while sumOfDiff>0:
        if(sumOfDiff>=min):
            sumOfDiff-=min
        else:
            diff = min - sumOfDiff
            cost+=(diff*a)
            sumOfDiff=0

    if cost_s > cost:
        return cost
    else:
        return cost_s


if(len(secLine)<2):
    cost = 0
else:
    cost = trac(a,b,min,secLine)

print(cost)




