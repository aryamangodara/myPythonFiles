# 
#	  these files are created by
#		Aryaman Godara		
#

#
#	Any changes for better is accepted, cause these are made in the initial phase of my coding 
#


n = input()
#used for checking if any string is containig alphabets only...

def check_alpha(n):
    if n in ("abcdefghijklmnopqrstuvwxyz" or "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        return True

    return False

print(check_alpha(n))
