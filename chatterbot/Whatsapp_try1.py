import pywhatkit as pwk
from datetime import datetime
# using Exception Handling to avoid unexpected errors
rec=["+919361543866"]
# sending message in Whatsapp in India so using Indian dial code (+91)
for i in range(len(rec)):
    currentDateAndTime = datetime.now()
    current = currentDateAndTime.strftime("%H:%M:%S")
    current=current.split(":")
    for j in range(3):
        current[j]=int(current[j])
    
    current[1]=current[1]+1
    if current[1]>59:
        current[1]-=60
        current[0]+=1
        if current[0]>24:
            current[0]-=24
    hr=current[0]
    mn=current[1]
    pwk.sendwhatmsg(rec[i], "Hi \n la",hr,mn,tab_close=True)
    print("done")
#pwk.sendwhats_image("+919344580944", "C:\\Users\\KharshithaBhuvaniEla\\Desktop\\chatbotvenv for doc\\venv2\\Lib\\sdf.jpg")
#pwk.sendwhatmsg_to_group("Oops lab", "Hey Guys! How's everybody?",15,24)
#pwk.playonyt("https://www.youtube.com/watch?v=r1aDa-kWROk")
# pwk.search("GeeksforGeeks")

print("Message Sent!")  # Prints success message in console
