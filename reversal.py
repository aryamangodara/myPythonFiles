# 
#	  these files are created by
#		Aryaman Godara		
#

#
#	Any changes for better is accepted, cause these are made in the initial phase of my coding 

list2=[1,2,3,4,5,6,7,8,9]

def reverse(list):
    rev_list=[]
    for i in range(0,len(list)):
        k=len(list)-i-1
        rev_list.append(list[k])
    return rev_list


print(reverse(list2))