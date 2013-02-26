#shell1.py
#A model shell
import os
import shutil

def helpMenu():
	print("This is the help menu")
def fhelpMenu(comm):
	if(comm == "--?" or comm == "/?" or comm == "-?"):
		print("This is the help help menu")
		#include valid arguments
	elif(comm == "--v" or comm == "/v" or comm == "-v"):
		print("This is the help --v menu")
	elif(comm == "--q" or comm == "/q" or comm == "-q"):
		print("This is the help --q menu")
	else:
		InvalidFlag()
def curDir():
	print(os.getcwd())
def fcurDir(comm):
	if(comm == "--?" or comm == "/?" or comm == "-?"):
		print("Prints the current working directory, takes no arguments")
	else:
		InvalidFlag()
def showHist(num, lis):
	for x in range (0, num):
		print(str(x + 1) + ":" + str(lis[x]))
def fshowHist(comm, num, lis):
	if(comm == "--?" or comm == "/?" or comm == "-?"):
		print("Prints a history of commands entered in this session")
		#include valid flags
	elif(comm == "--n" or comm == "/n" or comm == "-n"):
		if(num > 0):
			for x in range(num - 1, len(lis)):
				print(str(x + 1) + ":" + str(lis[x]))
	elif(comm == "--x" or comm == "/x" or comm == "-x"):
		if(num <= len(lis)):
			for x in range(0, num):
				print(str(x + 1) + ":" + str(lis[x]))
	else:
		InvalidFlag()
def lisDir(pat):
	directs = os.listdir(pat)
	for x in range(0, len(directs)):
		if(os.path.isdir(directs[x])):
			print("<DIR>\t" + directs[x])
		else:
			print("\t" + directs[x])
def flisDir(pat, flag):
	if(flag == "--?" or flag == "/?" or flag == "-?"):
		print("Help for list")
	else:
		lisDir(flag)
def chDir(pat, newpat):
	if(newpat == "--?" or newpat == "/?" or newpat == "-?"):
		chHelp()
	else:
		pat += "\\" + newpat
		try:
			os.chdir(pat)
			return pat
		except:
			print("Invalid Directory or Path")
			return pat
def chMDir(pat, newpat):
	pat += "\\"
	for x in range(0, len(newpat)):
		if(x > 0):
			pat += " "
		pat += newpat[x]
	try:
		os.chdir(pat)
		return pat
	except:
		print("Invalid Directory or Path")
		return pat
def chHelp():
	print("Help for chDir")
def runHelp():
	print("Run help")
def copyHere(pat, fil):
	if(fil == "--?" or fil == "/?" or fil == "-?"):
		copyHelp()
	else:
		temp = fil.split(".")
		filname = ""
		n = 2
		exist = True
		while(exist):
			for x in range(0, len(temp)):
				if(x == 1):
					filname += str(n) + "."
				filname += temp[x]
			if(os.path.exists(filname)):
				filname = ""
				exist = True
				n += 1
			else:
				exist = False
		shutil.copy2(pat + "\\" + fil, pat + "\\" + filname)
		print("Copied")
def copyThere(pat, fil, loc):
	shutil.copy2(pat + "\\" + fil, loc)
def copyHelp():
	print("Copy Help")
def trashHelp(flag):
	if(flag == "--?" or flag == "/?" or flag == "-?"):
		print("Trash Help")
	else:
		InvalidFlag()
def mvFile(fil, garb, pat, dr):
	if(fil == "--?" or fil == "/?" or fil == "-?"):
		if(dr == "d"):
			delHelp()
		else:
			revHelp()
	else:
		try:
			shutil.move(pat + "\\" + fil, garb + "\\" + fil)
		except:
			print("All paths for deletion must be relative to the current directory")
def delHelp():
	print("Delete Help")
def revHelp():
	print("Revive Help")
def confirmEmpty(garb, pat):
	print("WARNING: This will permanently delete anything in the Trash folder")
	confirm = input("Continue (y/n): ")
	if(confirm.lower() == "y" or confirm.lower() == "yes"):
		emptyTrash(garb, pat)
	elif(confirm.lower() == "n" or confirm.lower() == "no"):
		print("Aborting...")
	else:
		print("Invalid...please try again")
		confirmEmpty(garb, pat)
def emptyTrash(garb, pat):
	directs = os.listdir(garb)
	for x in range(0, len(directs)):
		if(os.path.isdir(garb + directs[x])):
			try:
				shutil.rmtree(garb + "\\" + directs[x])
			except:
				print("Sorry, could not delete directory " + directs[x])
		else:
			try:
				os.remove(garb + "\\" + directs[x])
			except:
				print("Sorry, could not delete file " + directs[x])
def fEmpty(flag):
	if(flag == "--?" or flag == "/?" or flag == "-?"):
		emptyHelp()
def environPrint(env):
	try:
		print(os.environ[env])
	except:
		print("Not a valid environment variable")
def flagPath(flag):
	if(flag == "--?" or flag == "/?" or flag == "-?"):
		print("Path Help")
	else:
		InvalidFlag()
def emptyHelp():
	print("Empty help")
def InvalidFlag():
	print("Invalid flag, enter /? for more options")
def InvalidOption():
	print("Invalid arguments, enter /? for more options")


put = " "
count = 0
commands = []
trash = os.getcwd() + "\\Trash"
put = input(">>")
commands.append(put)
while(put.lower() != "quit"):
	path = os.getcwd()
	splitPut = put.split(" ")
	siz = len(splitPut)
	if(splitPut[0].lower() == "help"):
		if(siz == 2):
			fhelpMenu(splitPut[1].lower())
		elif(siz == 1):
			helpMenu()
		else:
			InvalidOption()
	if(splitPut[0].lower() == "pwd"):
		if(siz == 2):
			fcurDir(splitPut[1].lower())
		elif(siz == 1):
			curDir()
		else:
			InvalidOption()
	if(splitPut[0].lower() == "cd"):
		if(siz == 2):
			path = chDir(path, splitPut[1])
		elif(siz == 1):
			InvalidOption()
		elif(siz > 2):
			path = chMDir(path, splitPut[1:])
		print(path)
	if(splitPut[0].lower() == "list"):
		if(siz == 1):
			lisDir(path)
		elif(siz == 2):
			flisDir(path, splitPut[1].lower())
	if(splitPut[0].lower() == "where"):
		helpMenu()
		#docode
	if(splitPut[0].lower() == "path"):
		if(siz == 2):
			flagPath(splitPut[1])
		elif(siz == 1):
			environPrint("PATH")
		else:
			InvalidOption()
	if(splitPut[0].lower() == "hist"):
		if(siz == 2):
			fshowHist(splitPut[1].lower(), 0, commands)
		elif(siz == 3):
			fshowHist(splitPut[1].lower(), int(splitPut[2].lower()), commands)
		elif(siz == 1):
			showHist(count, commands)
	if(splitPut[0].lower() == "run"):
		if(siz == 2):
			try:
				put = commands[int(splitPut[1]) - 1]
				continue
			except:
				runHelp()
		elif(siz == 1):
			InvalidOption()
		else:
			InvalidFlag()
	if(splitPut[0].lower() == "copy"):
		if(siz == 2):
			copyHere(path, splitPut[1])
		elif(siz == 3):
			copyThere(path, splitPut[1], splitPut[2])
		else:
			InvalidOption()
	if(splitPut[0].lower() == "delete"):
		if(siz == 2):
			mvFile(splitPut[1], trash, path, "d")
		else:
			InvalidOption()
	if(splitPut[0].lower() == "trash"):
		if(siz == 1):
			lisDir(trash)
		elif(siz == 2):
			trashHelp(splitPut[0].lower())
		else:
			InvalidOption()
	if(splitPut[0].lower() == "revive"):
		if(siz == 2):
			mvFile(splitPut[1], path, trash, "r")
		else:
			InvalidOption()
	if(splitPut[0].lower() == "empty"):
		if(siz == 2):
			fEmpty(splitPut[1])
		elif(siz == 1):
			confirmEmpty(trash, path)
		else:
			InvalidOption()
	if(splitPut[0].lower() == "info"):
		helpMenu()
		#docode
	put = input(">>")
	commands.append(put)
	count += 1
print("Quitting...")