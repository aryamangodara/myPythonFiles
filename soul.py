# 
#	  these files are created by
#		Aryaman Godara		
#

#
#	Any changes for better is accepted, cause these are made in the initial phase of my coding 
#I  dont know what is significance of this ... :p but this was supposed to be a problem..!

arr1=[1,1,5,8,9,5,2,8,8,6,6,2,8,8,0]

def Count(array,integer):
    count=0
    for i in array:
        if i==integer:
            count+=1
    return count

def unique(array):
    list=[]
    for i in array:
        if i  not in list:
            list.append(i)
    return list

def pairless(array):
    list=[]
    for i in unique(array):
        if Count(array,i)%2!=0:
            list.append(i)
    return list

print(pairless(arr1),pairless(arr))


#Aryaman #Godara