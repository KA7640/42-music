import os
import datetime
from time import sleep

now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
while True:
    now = datetime.datetime.now()
    if now.strftime("%H:%M") == "02:35":
        os.system("sh ./run.sh")
        break

