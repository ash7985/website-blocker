import time
from datetime import datetime as dt
#host_path = r"C:\nWindows\System32\drivers\etc\hosts"     for windows not in linux
host_path = '/etc/hosts'
#host_temp = 'hosts'
redirect = '127.0.0.1'
websites = []# the websites you want to block you can pass here
yn = 'Y'
while True:
    if yn == 'Y':
        w    = input('enter the websites you want to block\n')
        websites.append(w)
        yn = input('for more entries press Y else N\n')
    else:
        break
start = int(input('enter the starting hour of blocking your entered website'))
end = int(input('enter the ending hour of your blocked website'))
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,start) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,end):
        #print ('Hey buddy its your working hour you just go to your work')
        with open(host_path , 'r+') as file:
            content = file.read()
            for website in websites :
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website+'\n')
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0) # it will put the pointer at the top of the text file and the nexst work is for the truncate
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()  #it will delete All the re-occuring lines  in the text files

        #print('hey its fun hour you can now access your websites')

    time.sleep(10)
print('hey your entries are taken and the proper actions will be taken\n press CTRL+C to exit')
