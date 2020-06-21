#author = <gowtham758550@gmail.com>
#Python program to manage cloned repo's
#clone, update, list and delete repo's

import os
import shutil

#get the home directory path
home_path = os.path.expanduser("~")
#get the current working directory"
current = os.getcwd()

def printer(n):
    print("\n\n<---------------{}--------------->".format(n))

#function to clear the screen
def clear_screen():
    x = input("\n\nPress enter to continue")
    os.system('clear' or 'cls')

#check the text is in the file
def check(text):
    try:
    	with open(home_path + "git-metadata", "r") as file:
    	   if text in file.read():
    	       return True
    except FileNotFoundError:
    	pass
    except Exception as a:
    	print(a)
    	clear_screen()

#function to get the repo name from url
def repo_name(url):
            repo_folder = ""
            for i in url[::-1]:
            	if i == '/':
            	   break
            	else:
            	   repo_folder += i
            repo_folder = repo_folder[::-1]
            return str(repo_folder).strip(".git")

                                                
#function to clone repo's		
def install(url):
    try:
        command = "git clone " + url
        os.system(command)
        name = repo_name(url)
        if check(name):
        	pass
        else:
        	with open(home_path + "git-metadata","a") as f:
        	   f.write("\nRepo name : " + name + "\n\n")
        	f.close()
        printer("cloned successfully")
    except:
        printer("\n\nError occured")	
        print("\n\nProblems may be occured:\n1. No internet connection\n2. Wrong url ")


#function to remove the repo from list after deletion
def remove(repo):
	with open(home_path + "git-metadata", "r") as f:
		lines = f.readlines()
	with open(home_path + "git-metadata", "w") as f:
		for line in lines:
			if repo not in line:
				f.write(line)
		f.close()
				
#function to delete repo	
def delete(repo):
    try:
        shutil.rmtree(repo)
        printer("deleted successfully")
    except:
        printer("Error occured")
        print("\n\nProblems may be occured : \n1. Repo not found\n2. Wrong repo name")
        clear_screen()

#function to list repo's
def list():
    with open(home_path + "git-metadata","r") as f:
        printer("cloned repo's")
        print("\n\n" + f.read())
    print("\n\nIf nothing displayed you are not cloned any repo's using this tool")

while(True):
    os.system("clear" or "cls")
    print("   _____ _ _    ")
    print("  / ____(_) |   ")
    print(" | |  __ _| |_  ")
    print(" | | |_ | | __| ")
    print(" | |__| | | |_  ")
    print("  \_____|_|\__| ")                 
    print()
    print(" _ __ ___   __ _ _ __   __ _  __ _  ___ _ __") 
    print("| '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '__|")
    print("| | | | | | (_| | | | | (_| | (_| |  __/ |   ")
    print("|_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_|   ")
    print("                              __/ |           ")
    print("                             |___/           ")
    print("\n\n1. Install repo\n2. Update repo\n3. Delete repo\n4. List repo\n5. Exit")
    choice = input("\n\nEnter your choice : ")
    if choice == '1':
        url = input("\n\nEnter git clone url : ")
        text = repo_name(url)
        if check(text):
            printer("You already cloned this repository")
        else:
            install(url)
        clear_screen()
    elif choice == '2':
        url = input("\n\nEnter clone url : ")
        text = repo_name(url)
        if check(text):
        	folder = repo_name(url)
        	delete(folder)
        	os.system("clear" or "cls")
        	install(url)
        	printer("Updated successfully")
        else:
        	printer("No such repository to update.")
        clear_screen()
    elif choice == '3':
        repo = input("\n\nEnter the repo name : ")
        if check(repo):
        	delete(repo)
        	remove(repo)
        else:
        	printer("No such repository to delete")	
        clear_screen()
    elif choice == '4':
        list()
        clear_screen()
    elif choice == '5':
        printer("Thank you")
        exit(1)
    else:
        printer("Enter correct choice")
        clear_screen()
