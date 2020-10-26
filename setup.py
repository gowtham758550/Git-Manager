import os
import platform

if platform.system().lower()=='windows':
	print('Setup Doesnot Support Windows . \nPlease run " py main.py" at command prompt or powershell to run Git-manager...')
	x=input('\nPress any key to continue...')
	exit(0)
	
cwd = os.getcwd() 
alias="\nalias git-manager='python {}/main.py'".format(cwd)

home = os.path.expanduser("~")
if os.path.exists(home + "/.bashrc")==False:
  print('./bashrc not Detected!!!\nInstallation Failed!!!')
  exit(0)

try:
		with open(home + "/.bashrc",'a') as f:
			f.write(alias)
			print("\nSetup file executed successfully\n\nNow you can use the tool by just typing 'git-manager' in any directory\n\nClose the current terminal and open new terminal to use our tool :)")

except:
	print("Something went wrong , try running as Administrator.")
