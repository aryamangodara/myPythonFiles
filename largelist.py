# 
#	  these files are created by
#		Aryaman Godara		
#

#
#	Any changes for better is accepted, cause these are made in the initial phase of my coding 
#

list1 = [23, 2, 4, 5, 899, 628, 999, 1025, 51, 1, 7, 87]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def largest_list(list):
    max = 0  # must be - infinite so that it will give correct value for negative numbers too... need suggestion
    for i in range(0, len(list)):
        if list[i] > max:
            max = list[i]
    print(max)


largest_list(list2)
