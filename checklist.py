list1=[23,2,4,5,899,628,999,1025,51,1,7,87]
list2=[1,2,3,4,5,6,7,8,9]

def check_list(item,list):
    for i in range (0,len(list)):
        if list[i]==item:
            print("it is present")
            break
        elif i==len(list)-1:
            print("not present")

element,liste=input()
check_list(element,liste)

print (list1)