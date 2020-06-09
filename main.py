#author = <gowtham758550@gmail.com>
#Python program to manage cloned repo's
#clone, update, list and delete repo's

import os
import shutil


def printer(n):
	print("\n\n<---------------{}--------------->".format(n))

#function to clear the screen
def clear_screen():
	x = input("\n\nPress enter to continue")
	os.system('clear' if os.name == 'posix' else 'cls')

#function to clone repo's		
def install(url):
	try:
		command = "git clone " + url
		os.system(command)
		
	except:
		printer("\n\nError occured")	
		print("\n\nProblems may be occured:\n1. No internet connection\n2. Wrong url ")

#function to delete repo	
def delete(repo):
	try:
		shutil.rmtree(repo)
		 
	except:
		printer("Error occured")
		print("\n\nProblems may be occured : \n1. Repo not found\n2. Wrong repo name")

#function to list repo's
def list():
	path = os.getcwd()
	list = [i for i in os.listdir(path)]
	printer("cloned repo's")
	print()
	for i in list:
		if not i.endswith('.py'):
			print(i)
	print("\n\nIf nothing displayed you not cloned any repo's using this program")

while(True):
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
		install(url)
		printer("cloned successfully")
		clear_screen()
		
	elif choice == '2':
		url = input("\n\nEnter git clone url : ")
		repo = input("\n\nEnter repo name : ")
		delete(repo)
		install(url)
		printer("updated successfully")
		clear_screen()
		
	elif choice == '3':
		repo = input("\n\nEnter the repo name : ")
		delete(repo)
		printer("deleted successfully")
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
