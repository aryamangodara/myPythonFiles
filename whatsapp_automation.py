# 
#	  these files are created by
#		Aryaman Godara		
#

#
#	Any changes for better is accepted, cause these are made in the initial phase of my coding 
#           It is a bot for sending messages to your whatsapp contacts..

#        con:-
#           it is not able to find a contact if you haven't recently talked to him


from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

print("Welcome to Godara automated Whatsapp Messenger..\n")

name = input("Enter name of person or the group name: ")  # enter the exact value from your mobile contact list
msg = input("Enter the message: ")
count = int(input("Enter the no. of times you want to send the message! : "))

input("Enter anything after scanning of qr code! ")

user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()
msgbox = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
msgbox.click()




for i in range(count):
    msgbox.send_keys(msg)
    sendButton = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span")
    sendButton.click()

print("Bang! Success")