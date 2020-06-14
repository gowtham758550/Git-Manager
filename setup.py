import os

cwd = os.getcwd() 
alias="\nalias git-manager='python {}/git_manager.py'".format(cwd)

home = os.path.expanduser("~")

try:
		with open(home + "/.bashrc",'a') as f:
			f.write(alias)
			print("\nSetup file executed successfully\n\nNow you can use the tool by just typing 'git-manager' in any directory\n\nClose the current terminal and open new terminal to use our tool :)")

except:
	print("Something went wrong")