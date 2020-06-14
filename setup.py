import os

cwd=os.getcwd()
alias = "alias git-manager='python {}/main.py'".format(cwd)
home=os.path.expanduser("~")

bashrc = "echo " + alias + " >> ~/.bashrc"

with open(home + "/.bashrc") as f:
    if alias in f.read():
        print("Already installed")
        exit()
    else:
        os.system(bashrc)
        print("Installed")
