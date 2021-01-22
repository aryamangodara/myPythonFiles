# 
#	  these files are created by
#		Aryaman Godara		
#

#
#	Any changes for better is accepted, cause these are made in the initial phase of my coding 
#


def palindrome_check(string):
    k=str()
    pal=bool()
    for i in range((len(string)-1),-1,-1):
        k=k + str(string[i])
    if string==k:
        pal=True
    
    return pal

print(palindrome_check("haha"),palindrome_check("ava"))

