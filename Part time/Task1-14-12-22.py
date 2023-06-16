import matplotlib.pyplot as plt
import numpy as np

# y = k*x + b line.
k = 2
b = 2
y = 2
xArr = []
yArr = []
arr = np.array([[0,1,1,3], [9, 7, 4, 0]])


for x in range(0, 100):
    xArr.append(x)
    y = k * x + b
    yArr.append(y)

plt.plot(xArr, yArr, '-r', label='y=2x+1')
print(arr[0,:])

plt.show()
