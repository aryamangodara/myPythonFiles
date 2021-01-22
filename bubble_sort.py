# 
#	  these files are created by
#		Aryaman Godara		
#

#
#	Any changes for better is accepted, cause these are made in the initial phase of my coding 

print("Bubble Sorting!!")
a=[5,3,1,7,2]
def bubble_sort(array=a):
    for i in range (len(array)):
        for j in range(1,len(array)-i):
            if array[j-1]>a[j]:
                a[j-1],a[j]=a[j],a[j-1]
    return array


print(bubble_sort())