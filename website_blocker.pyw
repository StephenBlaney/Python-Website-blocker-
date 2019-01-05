import time
from datetime import datetime as dt

hosts_path = "C:\Windows\System32\drivers\etc\hosts" #Host varible that points to our host file in this directory
redirect = "127.0.0.1" #The URL that will be directed when a prohibited site is entered in the web browser
website_list = ["www.facebook.com","facebook.com","www.twiter.com","twitter.com"] #List that Stores our prohibited URL

while True: #Loop 1 every 5 secounds The idea is the run the script all the time ever 5 secounds
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt(dt.now().year, dt.now().month, dt.now().day,16): #if time now is between 8 and 4 do this
        print("Working Hours....")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                    if website in content:
                        pass
                    else:
                        file.write(redirect + " " +website + "\n")
    else:
        with open(hosts_path,'r+') as file:
            content = file.readline() #content is now a list datatype
            file.seek(0) #Sends the file curser to the very begining of the file
            for line in content: #For every entry in content file
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours....")
    time.sleep(5)
