import pywhatkit as pwk
from datetime import datetime
my_file = open("contact_num.txt", "r")
data = my_file.read()
rec=data.split(",")
print(data)
for i in range(len(rec)):
    currentDateAndTime = datetime.now()
    current = currentDateAndTime.strftime("%H:%M:%S")
    current = current.split(":")
    for j in range(3):
        current[j] = int(current[j])
    current[1] = current[1] + 1
    if current[1] > 59:
        current[1] -= 60
        current[0] += 1
        if current[0] > 24:
            current[0] -= 24
    hr = current[0]
    mn = current[1]
    pwk.sendwhatmsg(rec[i], "Hi", hr, mn, tab_close=True)
    print("done")
print("Message Sent!")