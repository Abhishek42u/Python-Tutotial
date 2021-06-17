from numpy import*
p=array([[86,14,97],[6,9,5]])
print(p.shape)
print(p.size)

anu=p.flatten()
print(anu)

print(p.ndim)
print(p.dtype)

from collections import*
k=deque()
k.append(13)
k.append(45)
k.append(11)
k.append(66)
print(k)
k.pop()
print(k)
from itertools import combinations
c=combinations([1,2,3],2)
for i in c:
    print(i)
    
