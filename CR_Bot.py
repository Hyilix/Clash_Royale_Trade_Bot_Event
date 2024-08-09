import pyautogui
import time
import keyboard
import sys
from PIL import ImageGrab

'''
----SETUP----

->Set Clash Royale Client on fullscreen, and it's
automatically set on the middle of the screen

->Open Clan and have "Request Cards" button avalible

->This bot works by utilizing a "Common Token", 
requesting "Knight" and asking for max "Archers" card

->Each time a trade is initiated, it will cost 1250 coins,
and after canceling, you will recieve back the 1250 coins,
thus adding to the "coins spent event"

-------------

----STEPS----

->Press on "Request Cards" (Best method: hardcoded position)

->Press on "Trade" (Best method: hardcoded position)

->Press on "Common:" (Best method: hardcoded position)

->Press on "Knight" (Best method: hardcoded position)

->Press on "Request" (Best method: relative position)

->Press on "Archers" (Best method: hardcoded position)

->Press on "Add" (Best method: relative position)

->Press on "Trade" (Best method: hardcoded position)

->Press on "Confirm" (Best method: hardcoded position)

->Press on "Cancel" (Best method: Get color)

->Press on "Ok" (Best method: hardcoded position)

->Repeat process.

-------------

----NOTES----

->This Bot does not scroll to find desired card
(1440 pixels wide)

->Feel free to adjust this code to your liking

->Used for "Spend Gold, Earn Free Rewards!" event 
(09.08.2024)

-------------
'''

screen_w, screen_h = pyautogui.size()

#2560 x 1440 Screen size
#rgb(255, 68, 70)

DEBUG_MODE = False

#Hardcoded Color
Cancel_color = (255, 73, 82)

#Hardcoded Positions
Request = [1000, 1150]
Trade = [1280, 250]
Common = [1500, 400]
Knight = [1300, 1150]
Archers = [1500, 850]
Last_Trade = [1500, 350]
Confirm = [1280, 720]
OK = [1280, 850]

Cancel_x = 1570

#Relative Positions
Knight_rel = [0, -300]
Archers_rel = [0, 210]

#Cancel Position
Position_array = [Request, Trade, Common, Knight, Knight + Knight_rel, Archers, Archers + Archers_rel, Last_Trade, Confirm, -1, OK]
def getCancelPosition():
    for _ in range(100):
        px = ImageGrab.grab()
        for y in range(0, screen_h, 1):
            if px.getpixel((Cancel_x, y)) == Cancel_color:
                Position_array[-2] = [Cancel_x, y]
                print([Cancel_x, y])
                return
        time.sleep(0.1)
    print("Cancel not found")
    sys.exit(1)
    

def goToPosition(pos):
    time.sleep(0.3)

    if DEBUG_MODE:
        time.sleep(0.6)

    pyautogui.moveTo(pos)
    time.sleep(0.1)
    pyautogui.click()
    print("CLICKED")

index = 0
size = len(Position_array)

#Bot Loop

time.sleep(2)
while True:
    if keyboard.is_pressed("a"):
        print("STOPPING")
        break
    if index == size - 2:
        print("Getting Cancel")
        getCancelPosition()
        print(Position_array[-2])

    goToPosition(Position_array[index])

    if index == size - 1:
        index = 0
    else:
        index += 1


#time.sleep(2)
#getCancelPosition()

#pyautogui.moveTo(Cancel_x, 1020)