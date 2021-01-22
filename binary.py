# 
#	  these files are created by
#		Aryaman Godara		
#

#
#	Any changes for better is accepted, cause these are made in the initial phase of my coding 
#


a=[1,2,4,9,66,55,33,128,99,102,120,1024]


def binary_search(array,int):
    # array=sorted(array) we have to do this ;) check line 28
    mid=len(array)//2
    if array[mid]==int:
        return True
    elif len (array)==1 and array[0]!=int:
        return False
    elif array[mid]>int:
        return binary_search(array[:mid],int)
    elif array[mid]<int:
        return binary_search(array[mid:],int)
           


print (binary_search(sorted(a),1025))

