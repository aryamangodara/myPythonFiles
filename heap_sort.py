array=[]

def add(element):
    global array
    array.append(element)
    sift_up(len(array)-1)

def sift_up(index):
    if index==0:
        return
    p=parent(index)
    if array[index]<array[p]:
        array[index],array[p]=array[p],array[index]
        sift_up(p)

def parent(index):
    return (index-1)//2

def left(index):
    return 2*index+1

def right(index):
    return 2*index+2

result=[]

a=[16,13,14,12,2,10,15]
a=[1,6,3,8,5,7]
for i in a:
    add(i)
    



def sort():
    global result,array
    print(array)
    while len(array)>0:
        result.append(array[0])
        if len(array)>1:
            array[0]=array.pop()
            
        else:
            array.pop()
        sift_down(0)


def sift_down(index):
    l=left(index)
    r=right(index)
    if l>(len(array)-1):
        return
    
    if r>(len(array)-1):
        if array[index]>array[l]:
            array[index],array[l]=array[l],array[index]
            sift_down(l)
    
    else:
        if array[r]>array[l]:
            if array[index]>array[l]:
                array[index],array[l]=array[l],array[index]
                sift_down(l)
    
        if array[l]>array[r]:
            if array[index]>array[r]:
                array[index],array[r]=array[r],array[index]
                sift_down(r)

        
sort()
print(result) 