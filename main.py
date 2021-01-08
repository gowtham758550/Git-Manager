from os import path, system, remove, listdir, walk, getcwd
import urllib.request
from shutil import rmtree
from re import findall
from csv import writer, reader
from datetime import datetime
from time import ctime

home = path.expanduser("~")
file1 = home + "/git-manager.csv"

def connection(url):
	"""Checks internet connectivity and validate the url by sending request to the clone url.
	
	Parameters:
		url(string) : Repo url
	
	Rerurns:
		Booleans"""
	try:
		print("Checking internet connectivity!")
		urllib.request.urlopen(url)
		return True
	except Exception as a:
		print(a)
		return False

def extract_name(url):
	"""Extract the repo name from the url."""
	name = ""
	for i in url[::-1]:
		if i == "/":
			break
		else:
			name += i
	name = name[::-1]
	if name.endswith(".git"):
		name = name[0:len(name) - 4]
	return name

def readcsv():
	"""Read the git-manager.csv file in and return the values as a nested list."""
	with open(file1, "r") as csvfile:
		csvreader = reader(csvfile)
		rows = []
		for row in csvreader:
			rows.append(row)
	return rows

def writecsv(values):
	"""Write the data into the git-manager.csv file"""
	with open(file1, "a") as csvfile:
		csvobj = writer(csvfile)
		for i in values:
			csvobj.writerow(i)

def updatecsv(name):
	rows = readcsv()
	for i in rows:
		if name == i[1]:
			i[3] = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
	with open(file1, "w") as csvfile:
		csvobj = writer(csvfile)
		csvobj.writerows(rows)

def removecsv(item):
	"""Remove the row from the csv file."""
	rows = readcsv()
	if not len(rows) == 0:
		for i in rows:
			if item == i[1]:
				rows.remove(i)
	with open(file1, "w") as csvfile:
		csvobj = writer(csvfile)
		csvobj.writerows(rows)

def check(url):
		"""Checks the repo is already present or not by comparing the repo name with the name in the csv file."""
		for i in readcsv():
			if extract_name(url).strip() == i[1].strip():
				return False
		return True
							
def scan():
       """Scans the entire disk and find the cloned repo's."""
       lists = []
       for dirpath,_,filenames in walk(home):
            for f in filenames:
            	a = path.abspath(path.join(dirpath, f))
            	if a.endswith(".git/logs/HEAD"):
            		with open(a, "r") as f:
            			for line in f:
            				repo_url = findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+/(?:[-\w.]|(?:%[\da-fA-F]{2}))+/(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
            				if repo_url != None and len(repo_url) > 0:        				
            					lists.append([repo_url[0], extract_name(repo_url[0]), a[0:len(a) - 14], ctime(path.getmtime(a))])            	
       if path.isfile(file1):
       	updated_lists = []
       	rows = readcsv()
       	if len(rows) != 0 and len(lists) != 0:
       		for i in lists:
       			if i not in rows:
       				updated_lists.append(i)
       		lists = updated_lists
       return lists

def help():
	"""Prints the help text."""
	print("""
[1] Clone 
Enter the url of the repository to clone.

[2] Update
Enter the repository number to update.

[3] Delete
Enter the repository number to delete.

[4] List
It will list the cloned repo's in your storage.

[5] Scan
It will check for any other repo's are cloned using git clone.
 
[6] Help 
Get help.
	
[7] About
Get some info about this tool.
	
[8] Exit
Exit from the tool.
""")					
def clear():
	"""Clear the terminal screen."""
	system("clear")

def pause():
	"""Wait for user input before clear the terminal screen."""
	input("\n\nPress enter to continue...")
	clear()
		
def install(url):
	"""Install the repo using git clone."""
	system("git clone " + url)
	print("\nRepo installed successfully")
	
def update():
		"""Delete the repo and re-install the repo."""
		lists = readcsv()
		if len(lists) > 0:
			i = 1
			for j in lists:
				print(f"[{i}] {j[1]}")
				i += 1
		while(True):
			try:
				number = int(input("Enter repo number : "))
				if number > i:
					print("Enter correct number")
				else:
					break
			except ValueError:
				print("Enter numbers only")
		number -= 1
		location = lists[number][2]
		rmtree(location)
		url = lists[number][0]
		name = lists[number][1]
		url = url + " " + location
		system("git clone " + url)
		updatecsv(name)
		print(f"\n{name} repo updated successfully")

def delete():
		"""Delete the repo."""
		lists = readcsv()
		if len(lists) > 0:
			i = 1
			for j in lists:
				print(f"[{i}] {j[1]}")
				i += 1
		while(True):
			try:
				number = int(input("Enter repo number : "))
				if number > i:
					print("Enter correct number")
				else:
					break
			except ValueError:
				print("Enter numbers only")
		number -= 1
		location = lists[number][2]
		rmtree(location)
		name = lists[number][1]
		removecsv(name)
		print(f"\n{name} repo deleted successfully")
		
def list_repo():
	"""Display the csv file in a tabular form."""
	rows = readcsv()
	rows.insert(0, ["repo_url", "repo_name", "path", "last_updated"])
	maximum = [0] * len(rows[0])
	for row in rows:
		for index, column in enumerate(row):
			maximum[index] = max(len(column), maximum[index])
	for row in rows:
		data = ""
		for index, column in enumerate(row):
			data += column.ljust(maximum[index]) + "  ¦  "
		print("-" * len(data))
		print(data)
	print("-" * len(data)) 
						
def main():
	"""Main function"""
	clear()
	print(f"""
───▄▄▄▄▄▄─────▄▄▄▄▄▄

─▄█▓▓▓▓▓▓█▄─▄█▓▓▓▓▓▓█▄

▐█▓▓▒▒▒▒▒▓▓█▓▓▒▒▒▒▒▓▓█▌

█▓▓▒▒░    Git    ░▒▒▓▓█

█▓▓▒▒░           ░▒▒▓▓█

▐█▓▓▒▒  Manager  ▒▒▓▓█▌

─▀█▓▓▒▒░░░░░░░░░▒▒▓▓█▀

───▀█▓▓▒▒░░░░░▒▒▓▓█▀

─────▀█▓▓▒▒░▒▒▓▓█▀

──────▀█▓▓▒▓▓█▀

────────▀█▓█▀

──────────▀ 
NOTE : DON'T DELETE THE FILE : {file1}.
""")      
	if path.isfile(file1):
		rows = readcsv()
		if not len(rows) == 0:
			for i in rows:
				location, name = i[2], i[1]
				if not path.exists(location):
					if input(f"{name} repo is missing. Do you want to clone it again (y or n) : ") == "y":
						url = i[0]
						install(url + " " + location)
						updatecsv(name)
						pause()
					else:
						removecsv(name)				
		
	else:
		help()
		fields = []
		lists = scan()
		for i in lists:
			print(f"Available cloned repo => {i[1]}")
			fields.append(i)
		writecsv(fields)
		pause()
		
	while(True):
		print("""
[1] Install		[5] Scan
[2] Update	   	[6] Help
[3] Delete	  	[7] About
[4] List		[8] Exit
""")
		choice = input("Enter choice: ")
		if choice == "1":
			url = input("\nPro tip : To clone in different location enter the path with the url(for ex : <repo url>SPACE<path>\nEnter repo url: ")
			if connection(url):
				if check(url):
					name = extract_name(url)							
					repo_data = [[url, name, getcwd() + "/" + name + "/", datetime.now().strftime("%a %b %d %H:%M:%S %Y")]]
					install(url)
					writecsv(repo_data)
				else:
					print("Repo already cloned.")
			else:
				print("""
Problem may be occured
  * Network problem
  * Invalid url""")
			pause()
			
		elif choice == "2":
			update()
			pause()
			
		elif choice == "3":
			delete()
			pause()
			
		elif choice == "4":
			list_repo()
			pause()
			
		elif choice == "5":
			lists = scan()
			if len(lists) > 0:
				for i in lists:
					print(f"New repo => {i[1]}")
				writecsv(lists)
			else:
				print("Nothing found")
			pause()
		
		elif choice == "6":
			help()
			pause()
			
		elif choice == "7":
			print("""
A simple tool to make Git less tiresome!
Developed by : 
	* Gowtham S
Contributor : 
	* Anish M
Repository link : https://www.github.com/gowtham758550/Git-Manager/
Buy me a coffee : https://www.buymeacoffee.com/gowtham758550
""")
			pause()
			
		elif choice == "8":
			print("Thank you")
			exit()
			
		else:
			print("Enter correct choice")


if __name__ == "__main__":
	try:
		main()
	except Exception as a:
		print(f"{a}\nPlease make issue about the error you facing at https://github.com/gowtham758550/Git-Manager/issues")
