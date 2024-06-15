import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))

if (4<=timestamp<12):
    print("Good morning sir")
elif (12<timestamp<17):
    print("good evening sir")
else :
    print("good night sir")    
