import pywhatkit
import time
import pyautogui
import datetime

# current time + 1 min
current_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
hour = current_time.hour
minute = current_time.minute

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
# pywhatkit.sendwhatmsg_to_group("Llx1fH64svKHO22oYAtYmf", open('output.txt', 'r', encoding='utf-8').read(), hour, minute)
pywhatkit.sendwhatmsg("+917678228684", open('output.txt', 'r', encoding='utf-8').read(), hour, minute)
# close the tab in 2 seconds

time.sleep(3)
pyautogui.hotkey('ctrl', 'w')