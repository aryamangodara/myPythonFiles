arr = [30,80,72,90,40,50,70]

def part2(ar, start, end):

    pivot = end
    i = start
    while i < pivot:
        if ar[i] > ar[pivot]:
            for j in range(i, pivot):
                ar[j], ar[j+1] = ar[j+1], ar[j]
            pivot -= 1
        else:
            i += 1
    return pivot

def quick_sort(arr,start=0,end=len(arr)-1):
    if start<end:
        pi=part2(arr,start,end)
        quick_sort(arr, start, pi-1) 
        quick_sort(arr, pi+1, end)


quick_sort(arr)


print(arr)

