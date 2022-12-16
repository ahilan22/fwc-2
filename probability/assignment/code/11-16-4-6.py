from itertools import permutations

posList = [0,1,2]
#[0,1,2] reperesents letters written to
#[0,1,2] respectively 
sampSpace = list(permutations(posList))
case_1 =[]
case_2 =[]
case_3 =[]

def count(inList):
    counter = 0
    for i in inList:
        if i == inList[i]:
            counter += 1
    return counter

# case-1: X=0
for i in range(len(sampSpace)):
    if count(sampSpace[i]) == 0:
        case_1.append(sampSpace[i])
print('case(X=0) =',case_1)

# case-2: X=1
for i in range(len(sampSpace)):
    if count(sampSpace[i]) == 1:
        case_2.append(sampSpace[i])
print('case(X=1) =',case_2)

# case-3: X=3
for i in range(len(sampSpace)):
    if count(sampSpace[i]) == 3:
        case_3.append(sampSpace[i])
print('case(X=3) =',case_3)

print('Probability is', (len(case_2)+
    len(case_3))/len(sampSpace))
