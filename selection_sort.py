# from math import inf
from datetime import *
import numpy as np
a=np.arange(10000,-9,-1)

def selection_sort(array=a):
    result=[]
    for i in range(0,len(array)):
        min=float('inf')
        # print(result)
        for j in range(i,len(array)):
            if array[j]<min:
                min=array[j]
                array[i],array[j]=array[j],array[i]
    return array

start=datetime.now()
print(selection_sort())
end=datetime.now()

a=np.arange(10000,-9,-1)

def sel_sort(array=a):
    for i in range(len(array)):
        min=i
        for j in range(i,len(array)):
            min=j if array[j]<array[min] else min 
        array[i],array[min]=array[min],array[i]
    return array
        

start2=datetime.now()
print(sel_sort())
end2=datetime.now()

print("Aryaman")
print (end-start)

print("chachu")
print(end2-start2)