import math
import matplotlib.pyplot as plt
def T(n):
    if n<1:
        return 1
    return T(n-1)+3*n+1

y1 = []
y2 = []
x = range(0,501)
for i in range (0,501):
    y1.append(T(i))
    y2.append(i**2)
    
    #print(i,":   ",T(i),"     ",i**3)

plt.plot(y1,x)


plt.show()
