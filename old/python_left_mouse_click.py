#left mouse click

#! python3
# mouseNow.py - Displays the mouse cursor's current position.
import pyautogui
import time
#import win32gui
#import win32con
print('Press CTRL-ALT-DELETE to KILL.\n')
#TODO: Get and print the mouse coordinates.

time.sleep(5)
print('And so it starts\n')
pyautogui.moveTo(300, 300, duration=0.50)
time.sleep(5)

#Minimize window.
#Minimize = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

print('Click 2 times\n')
pyautogui.click(300, 300)
time.sleep(3)
pyautogui.click(300, 300)


while True:
 pyautogui.moveTo(300, 300, duration=0.25)
 pyautogui.moveRel(100, 0, duration=0.25)
 pyautogui.moveRel(0, 100, duration=0.25)
 pyautogui.moveRel(-100, 0, duration=0.25)
 pyautogui.moveRel(0, -100, duration=0.25)
 #Take screen shot
 #Analyze screenshot
 #Fire a click if its positive.
 
