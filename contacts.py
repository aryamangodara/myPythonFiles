# 
#	  these files are created by
#		Aryaman Godara		
#

#
#	Any changes for better is accepted, cause these are made in the initial phase of my coding 


#   This is a good projevt which will help you to save and manage your contacts..

from os import system as ntp
import os.path
print("\nWelcome to Godara Contacts Directories!!!")
def quit():
    print("Bye! Thanks for using our software")

def view():
    f=open("contacts.csv" , "r")
    max=10
    lines=[]
    k=" "
    for l in f:
        words = l.split(",")
        lines.append(words)
        if len(words[0])>max:
            max=len(words[0])
    # f=open("contacts.csv" , "r")
    for words in lines:
        o=max-len(words[0])
        print(words[0] +(k*o)+" | "+ words[1])
    f.close()
def save_contact():
    f=open("contacts.csv", "a")
    name=input("Enter the name: ")
    phno=input("Enter the phone number: ")
    f.write("\n"+name + "," +phno)
    print("Contact added successfully!")
    f.close()

def delete_all():
    f=open("contacts.csv","w")
    f.write("Name"+"," +"Phone No.") 
    f.close()



n=1.9
while 0<n<5:
    if os.path.exists("contacts.csv"):
        pass
    else:
        delete_all()
    
    try:
        n=int(input("\nPress\n1.To view all contacts\n2.To add a contact \n3.Delete all contacts\n4.Open in Notepad\n5.Quit\n"))
    except ValueError:
        print("Invalid no.")
    
    if n==1:
        view()
    
    elif n==2:
        save_contact()
    
    elif n==3:
        try:
            w=int(input("Warning!!!! It is irreversible proceeding... Press\n1.Proceed\n2.Go back to previous menu....\n"))
        except ValueError:
            w=2
            print("Invalid no.")
        if w==1:
            delete_all()
            print("Deleted succesfully!")
    
    elif n==4:
        ntp("notepad contacts.csv") 

    elif n==5:
        quit()
        break

    else:
        print("Atleast... choose from given options:)")
        n=1.2    
