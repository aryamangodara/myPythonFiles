# 
#	  these files are created by
#		Aryaman Godara		
#

#
#	Any changes for better is accepted, cause these are made in the initial phase of my coding 
#   this program cause trouble to many .. But not to me ^0^ U_U 

n, w, x = int(input("enter height and width and length"))
odd = range(1, 2 * n, 2)
s = " "
c = "*"
output = str()
for i in range(1, n + 1):
    k = n - i
    output += ((s * k + (c * odd[i - 1]) + s * k) * w) + "\n"
for l in range(1, n):
    output += ((s * l + c * odd[n - l - 1] + s * l) * w) + "\n"
print(output * x)
