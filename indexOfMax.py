# 
#	  these files are created by
#		Aryaman Godara		
#

#
#	Any changes for better is accepted, cause these are made in the initial phase of my coding 

a=[999,119,2,9999,6,3,4,7,9099]
b=[]
def indexof_max(array):
    index=0
    try:
        y=max(array)
    except ValueError:
        return None
    for i in array:
        if i==y:
            break
        index+=1

    return index

print(indexof_max(a),indexof_max(b))