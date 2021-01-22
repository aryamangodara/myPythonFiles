# 
#	  these files are created by
#		Aryaman Godara		
#

#
#	Any changes for better is accepted, cause these are made in the initial phase of my coding 
#

a=[16,13,14,12,2,10,15]
def check_list(item,list=a):
    for i in range (0,len(list)):
        if list[i]==item:
            print("it is present")
            break
        elif i==len(list)-1:
            print("not present")

print(a)
element=int(input("provide the number you want to check in this list\n"))

check_list(element,a)
