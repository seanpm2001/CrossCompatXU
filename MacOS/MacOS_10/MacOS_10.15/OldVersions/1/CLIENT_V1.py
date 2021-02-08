# Start of script
""" Info
This is the main client script for the CrossCompatXU program for MacOS 10.15 Catalina
"""
# Temporary variables
condition1 = int(0)
condition2 = int(0)
condition3 = int(0)
condition4 = int(0)
condition5 = int(0)
condition6 = int(0)
# Functions
def timer():
  format = ["0:00"]
  # Function missing
  break
def availableSpaceCheck():
  availableSpaceTotalX = int(nil)
  # Function missing
  break
def page1():
  dialog()
  print ("Welcome to CrossCompatXU\n\nThis program will scan through installed programs and list alternatives and their compatibility on other systems.\nNote: installer files, and non-installable EXE files are not detected.")
  StartButton = ["Click here to start"]
  quitButton = ["Quit"]
  print (startButton() + " " + quitButton())
  break
def page2():
  dialog()
  print ("Check for all compatible Windows programs [dropdown]-")
  dropdownWin = ["Check for compatible Windows 10 programs", "Check for compatible Windows 7 programs", "Check for compatible Windows XP programs"]
  print (dropdownWin())
  print ("Check for all compatible Mac OS programs [dropdown]-")
  dropdownMac = ["Check for compatible MacOS Classic programs", "Check for compatible MacOS X programs", "Check for compatible OS X programs", "Check for compatible MacOS 10 programs", "Check for compatible MacOS 10 programs"]
  print (dropdownMac())
  print ("Check for all compatible Linux programs [dropdown]-")
  dropdownLinux = ["Check for compatible Debian programs", "Check for compatible Red Hat programs", "Check for compatible Arch programs"]
  print (dropdownLinux())
  backButton1 = ["Back"]
  continueButton1 = ["Continue"]
  print (backButton1() + " " + continueButton1())
  break
def page3():
  print ("Use an Internet connection (max session time: 90 seconds)\nUse offline (requires additional libraries) [install here]()\n\nNote: when using an Internet connection, your data will be encrypted and securely sent to our server to be processed. Within 90 seconds of starting the process, all data you sent will be deleted (regardless if it is done or not) except for the report, which will be deleted when you close the page/reload the tab. The report is stored on your computer and not our servers. Once you get the results, all data you sent us will have been completely deleted from our servers. If you use the program offline, you will be able to access the report under C://Users/<username>/Documents (Windows) home/users/<username>/Documents (UNIX-like, Linux, MacOS)\nYou need at least 100 kilobytes (100,000 bytes) of free space to use this program. This is not a problem for modern computers, as any computer from the year 2009 and up has at least 2 gigabytes (2,000,000,000 bytes) of memory.\nYour computer currently has " + str(availableSpaceTotalX) + " bytes of free space.")
  backButton2 = ["Back"]
  continueButton2 = ["Continue"]
  print (backButton2() + " " + continueButton2())
  break
def page4():
  print ("Checking...\nThis shouldn't take longer than 90 seconds.\nScan time: " + str(timer1) + "")
  abortButton1 = ["Abort"]
  quitButton1 = ["Quit"]
  print (abortButton1() + " " + quitButton1())
  break
def page5():
  print ("Processing...\nThis shouldn't take longer than 90 seconds.\nScan time: " + str(timer1) + "")
  abortButton2 = ["Abort"]
  quitButton2 = ["Quit"]
  print (abortButton2() + " " + quitButton2())
  break
def page6():
  print ("Successfully checked for alternatives\n")
  vlopButton = ["View list of programs"]
  vlocpButton = ["View list of compatible programs"]
  dpdButton = ["Delete processed data"]
  finalQuitButton = ["quit"]
  print (vlopButton() + " " + vlocpButton() + " " + dpdButton() + " " + finalQuitButton())
  break
# main
print (page1())
if (condition1 == ""):
  print (page2())
if (condition2 == ""):
  print (page3())
if (condition3 == ""):
  print (page4())
if (condition4 == ""):
  print (page5())
if (condition5 == ""):
  print (page6())
if (condition6 == ""):
  end()
# This script is not yet functional and incomplete.
""" File info
File version: 1 (Sunday. February 7th 2021 at 6:17 pm)
File type: Python script file (*.py)
Line count (including blank lines and compiler line): 90
"""
# End of script
