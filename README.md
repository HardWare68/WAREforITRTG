# WARE: Ware's Automatic Redsheet Epdater (for ItRtG)

A nice updater for copying the data from Idling to Rule the Gods (ItRtG) and pasting it to your own spreadsheet. It has a funny acronym because I'm a funny fella.

## How To Use
* Step One: Download the repo to your own computer, I suppose.
* Step Two: Make the required changes to the program:
    * Step 2a: In the `images` folder, make sure to screenshot your own buttons from ItRtG!
    * Step 2b: In the Python code, change the hardcoded variables (`PATH_TO_ITRTG`, `EXECUTABLE_NAME`, and `LINK_TO_SPREADSHEET`) to point to the correct paths. Probably won't need to edit `EXECUTABLE_NAME`, but I dunno, maybe some of you guys have changed it for some reason.
* Step Three: To automate (at least for Windows): 
    * Open Task Scheduler and click "Create New Task.
    * For name and description, set whatever you wish. Make sure to set "Run only when user is logged on" and turn off "Run whether user is logged on or not."
    * For "Triggers," create a new trigger. Set it to be whatever interval you want, daily, weekly, monthly, whatever.
    * For "Actions," create a new action, and choose "Start a program." The "Program/script" should point to `main.py` of the folder (ex: `C:\path\to\WAREforITRTG\main.py`). **For the "Start in:" field, make sure to copy the root path to the updater!** The script will likely not be able to update otherwise!
    * For "Settings," choose "Run task as soon as possible after a scheduled start is missed."