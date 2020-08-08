from os import path, system, remove
from urllib.request import urlopen
from shutil import rmtree

home = path.expanduser("~")
file1 = home + "/.git_meta1"

def connection(url):
	try:
		urlopen(url)
		return True
	except:
		return False

def check(url):
	with open(file1, "r") as f:
		if url in f.read():
			f.close()
			return False
		else:
			f.close()
			return True
			
def clear():
	system("clear")

def pause():
	input("\n\nPress enter to continue...")
	clear()
		
def install(url):
	try:
		system("git clone " + url)
		print("Repo installed successfully")
		with open(file1, "a") as f1:
			f1.write("\n" + url.lower())
		f1.close()
	except Exception as a:
		print(a)
	
def update(url):
	try:
		name = ""
		for i in url[::-1]:
			if i == "/":
				break
			else:
				name += i
		name = name[::-1]
		name = name.rstrip(".git")
		rmtree(name)
		system("git clone " + url)
		print("{} repo updated successfully".format(name))
	except Exception as a:
		print(a)

def delete(repo):
	try:
		with open(file1, "r") as f1:
			content = f1.readlines()
		with open(file1, "w") as f2:
			for i in content:
				if repo not in i:
					f2.write(i)
		f1.close()
		f2.close()
		rmtree(repo)
		print("\n{} repo deleted successfully".format(repo))
	except Exception as a:
		print(a)
		
def list():
	try:
		with open(file1, "r") as f:
			print(f.read())
		f.close()
	except Exception as a:
		print(a)
						
def main():
	clear()
	print("   _____ _ _       _ __ ___   __ _ _ __   __ _  __ _  ___ _ __")
	print("  / ____(_) |     | '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '__|")
	print(" | |  __ _| |_    | | | | | | (_| | | | | (_| | (_| |  __/ |   ")
	print(" | | |_ | | __|   |_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_|   ")
	print(" | |__| | | |_                                  __/ |           ")
	print("  \_____|_|\__|                                |___/           ")
	if path.isfile(file1):
		pass
	else:
		f = open(file1, "w+")
		f.close()
		
	while(True):
		print("\n\n[1] Install\n[2] Update\n[3] Delete\n[4] List\n[5] About\n[6] Exit")
		choice = input("Enter choice: ")
		if choice == "1":
			url = input("Enter repo url: ")
			if connection(url):
				if check(url.lower()):
					install(url)
				else:
					print("You already installed this repo")
			else:
				print("Problem may be occured\n\t* Network problem\n\t* Invalid url")
			pause()
			
		elif choice == "2":
			url = input("Enter repo url to update: ")
			if check(url.lower()):
				print("Not a repo to update\nNOTE : Update only already installed repo's")
			else:
				update(url)
			pause()
			
		elif choice == "3":
			repo = input("Enter repo name: ").lower()
			if check(repo):
				print("\nNot a repo to delete")
			else:
				delete(repo)
			pause()
			
		elif choice == "4":
			list()
			print("\nNOTE : If nothing displayed, there is no repo installed using git-manager")
			pause()
			
		elif choice == "5":
			print("\nA simple tool to make Git less tiresome!\nDeveloped by : Gowtham S\nGet source code : https://www.github.com/gowtham758550/Git-Manager/")
			pause()
			
		elif choice == "6":
			print("Thank you")
			exit()
			
		else:
			print("Enter correct choice")

main()
