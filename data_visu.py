#import numpy as np
import matplotlib.pyplot as plt
x= [i for i in range (-10,11)]
y= [i**2 for i in range (-10,11)]
act=["something","went","wrong"]
time=[6,7,11]
exp=[0.1,0.1,0.1]
plt.pie(time,labels=act,shadow=True,explode=exp)
plt.show()