# Windows-Shutup-Virus
A simple Virus which will shutdown your computer when it boots to your desktop. It is made using python.

# Main Logic of the Script
- First will create a 'batch' script or .bat file named 'shutup.bat' in which the 'shutdown code' will be written. 
- After that it will move the 'shutup.bat' file in the STARTUP APPLICATIONS Folder.
- This will cause the system to automatically shutdown after boot as the script gets activated after boot.

# Shutdown Code
At line number 13, a Batch Script is there `file.write("shutdown -s -t 20")` <br>
You can edit that as per your needs. <br>
- You can put `-r` instead of `-s`. If you do so then the computer will just restart instead of shutting down.
- You can change the integer after `-t`. It will decide after how many seconds the computer will shutdown. <b>This Integer Value is always taken in SECONDS. Don't write 2 if you want to do that after 2 MINUTES. For 2 minutes, you have to write `-t 120`</b>

# Removing the Virus
1. This program just moves the Batch Script 'shutup.bat' to your STARTUP APPLICATIONS  Folder. So to remove that, you just need to go to the folder and remove it. You can Press ` Win + R ` Key and then write ` shell:startup ` to open the STARTUP APPLICATIONS and then delete the ` shutup.bat ` file.    <br>
2. If you want to stop the script to run the Press ` Win + R ` and then write ` shutdown -a `. This will cancel the shutdown. <b> Write this after the script is activated.</b> After that follow the `First Method`. </br>
3. Unfortunately if you can't do any of this because your computer shutdown so fast, then enter the `Windows Recovery Mode` and then open `Command Prompt`. After that navigate to your STARTUP APPLICATIONS folder, which is in `C Drive`    

