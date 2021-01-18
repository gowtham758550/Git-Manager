import os
import platform

if platform.system().lower()=='windows':
	print('Setup Doesnot Support Windows . \nPlease run " py main.py" at command prompt or powershell to run Qgit...')
	x=input('\nPress any key to continue...')
	exit(0)

os.system('echo $SHELL>shell.txt')
with open('shell.txt') as f:
 shell='/.'+f.read().strip().split('/')[-1]+'rc'

cwd = os.getcwd() 
alias="\nalias qgit='python3 {}/main.py'".format(cwd)

home = os.path.expanduser("~")
if os.path.exists(home + shell)==False:
  print(f'{shell} not Detected!!!\nInstallation Failed!!!')
  exit(0)

try:
		with open(home + shell,'a') as f:
			f.write(alias)
			print("\nSetup file executed successfully\n\nNow you can use the tool by just typing 'qgit' in any directory\n\nClose the current terminal and open new terminal to use our tool :)")

except:
	print("Something went wrong , try running as Administrator.")
