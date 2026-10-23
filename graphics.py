import matplotlib.pyplot as plt
import numpy as np
x = [-5,-4,-3,-2,-1,0,1,2,3,4,5] #исходный массив значений
y = np.square(x) #
y1 = np.log(x) #
y2 = np.exp(x)#
y3 = np.power(x , 3)#
plt.plot(x, y,'x-', color="blue")# 
plt.plot(x, y1, "o-", color="red") #
plt.plot(x, y2, ".-", color="green") #
plt.plot(x, y3, "k:", color="purple") #
plt.title("График")#название графиков
plt.show()#отрисовка графиков