#WARE: Ware's Automatic Redsheet Epdater for ITRTG
#It's super funny when you force an acronym to work

#Notes to Self: This starts the game from the executable, not the Steam launcher.
#This means that "Save Online" won't work. Could maybe change to utilize the Steam launcher, but you know

#step 1: Import required libraries, variables, that stuff
import subprocess
import time
import psutil
import pyautogui
import pyscreeze
import mss
import pygetwindow
from PIL import Image
import webbrowser

PATH_TO_ITRTG = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Idling to Rule the Gods" #edit this as needed, just go to Steam and click "Browse Local Files"
EXECUTABLE_NAME = "Idling to Rule the Gods.exe"
LINK_TO_SPREADSHEET = "https://docs.google.com/spreadsheets/d/1NwgcDbZqf_2FNssnx4ts3XEZtC-n9IczDcsOal1s5Jw/edit?gid=782907758#gid=782907758" #Make sure this is your own spreadsheet, and it points to the "PlayerStats" sheet!
                                                                                                                                             #Idk if the positino

#Function to check if program is already running
def isRunning(name):
    for proc in psutil.process_iter(["name"]):
        if proc.info["name"] == name:
            return True
    return False

#Function to screenshot monitors
def screenshotMonitors():
    with mss.mss() as sct:
        for monitor in sct.monitors:
            raw = sct.grab(monitor)
            img = Image.frombytes("RGB", (raw.width, raw.height), raw.rgb)
            yield img, monitor

#Function to click the center of an image
#Works with several monitors. Yippie!
def clickButton(buttonDir):
    print(f"Scanning for {buttonDir}")
    with mss.mss() as sct:
        for monitor in sct.monitors:
            screenshot = sct.grab(monitor)

            # Convert to PIL for PyAutoGUI
            img = Image.frombytes(
                "RGB",
                (screenshot.width, screenshot.height),
                screenshot.rgb
            )

            # Search monitor screenshot for the button
            btn = pyautogui.locate(buttonDir, img, confidence=0.9)

            if btn:
                print("Button found! Clicking...")
                # Convert btnPlay coords from monitor-relative -> global screen coords
                x = btn.left + monitor["left"] + btn.width // 2
                y = btn.top + monitor["top"] + btn.height // 2

                pyautogui.click(x, y)
                break

#step two: Start ITRTG if not already started
print("Starting ItRtG...")
if not isRunning(EXECUTABLE_NAME):
    gameProcess = subprocess.Popen([PATH_TO_ITRTG + "\\" + EXECUTABLE_NAME])
    print("ItRtG should be started...")
else:
    print("ItRtG is already running. Closing it to start from the same point, you know.")

    #TO-DO: Save online before closing.

    for proc in psutil.process_iter(["pid", "name"]):
        if proc.info["name"] == EXECUTABLE_NAME:
            proc.terminate()
            print("Stopped ItRtG...")

    gameProcess = subprocess.Popen([PATH_TO_ITRTG + "\\" + EXECUTABLE_NAME])
    print("ItRtG should be started...")

#sleep so that way the game can open
time.sleep(5)

#Step 3: Navigate to "Export Stats"
#Step 3.1: The "Play" button will usually always be the same, so no problem with just using image recognition there.
#Also handling several monitors as well. Lol!
clickButton("images\\playButton.png")

#Small sleep to let ItRtG catch up
time.sleep(2)

#Step 3.2: Navigate to statistics
pyautogui.press('u')

#Step 3.3: Click the needed buttons
try:
    clickButton("images\\close.png") #Close the offline progress report if needed.
except:
    print("No need to close. Moving on...")
clickButton("images\\other.png")
clickButton("images\\exportStats.png")

#Step 4: Open the webpage.
print("Opening spreadsheet...")
webbrowser.open_new_tab(LINK_TO_SPREADSHEET)

#Sleep for a second to let google catch up
time.sleep(4)

#Step 5: Navigate to cell B2
#Fuck it man. Image recognition for the win again.
clickButton("images\\spreadsheetB2.png")
clickButton("images\\spreadsheetB2.png") #double-click to bring the cell into focus

#Step 6: Copy and paste!
pyautogui.hotkey('ctrl', 'a', 'x', 'v') #Choose the entire cell, delete it, paste the new data

#Step 7: TO-DO: Click the "Add to Log" button

x = input("Update should be finished. You are free to close this window.")