import time
import pyautogui
#have the message file moved in the project file to access
#4 seconds allow you enough time to click on notepad or messages to spam text there.

def SendMessage():
    time.sleep(4)
    text=open('message.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')
#enter allows you to spam the text. 

SendMessage()
