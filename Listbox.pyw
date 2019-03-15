#coding:utf-8

from tkinter import *
import os

app = Tk()
exept = ['bc.pyw','af.png','db.png','dlt.png','Menu.txt','bc.pyw','test.pyw']

fold = [x for x in os.listdir('.') if x not in exept]
access = Listbox(app, activestyle='none',selectforeground='white',highlightthickness=0,\
			selectmode=SINGLE, height=25,exportselection =0,selectbackground='light grey')
access.grid()

foldDic = {}

for x in fold:
	foldDic[x] = str(os.getcwd()) + "\\" + x
	x = '▼ ' + x
	access.insert(0,x)

def filter(string):
	badChars =['▼', '▲', ' ']
	
	for char in badChars:
		while char in string:
			i = 0
			while i < len(string):
				if string[i] == char:
					if i != 0 and i != len(string):
						string = string[:i-1] + string[i+1:]
					elif i == 0:
						string = string[i+1:]
					elif i == len(string):
						string = string[:i-1]
				i += 1
	return string


def select_access(event):
	currentSelection = access.curselection()
	selected = access.get(currentSelection)
	fileSelected = filter(selected)
	text = ""

	# If folder select -> show content
	if '▼' in selected:
		
		# Spacing for folder content
		basicLen = len(os.getcwd().split('\\'))+1
		pathLen = len(foldDic[fileSelected].split('\\'))
		# 1 Folder of difference = 1 tabulation
		i = 0
		while pathLen - i > basicLen :
			text += '    '
			i += 1

		# Replace close arrow by open arrow
		text += '▲ ' + filter(selected)
		access.delete(currentSelection)
		access.insert(currentSelection,text)
		
		# For content of the folder		
		for element in os.listdir(foldDic[fileSelected]):
			text = '' 
			i = 0
			# 1 Folder of difference = 1 tabulation
			while 1 + pathLen - i > basicLen :
				text += '    '
				i += 1

			# Set the new position in access
			newElementPos = currentSelection[0] + 1 

			# If it's not a file
			if '.' not in element:
				# Add it to the folder dictionnary
				foldDic[element] = foldDic[fileSelected] + '\\' + element
				# Check if it's a folder
				if os.path.isdir(foldDic[element]):
					text +=	'▼ ' + element

			else:
				text += element

			access.insert(newElementPos,text)

	elif '▲' in selected:
		# CHECK IF IT IS PARENT FILE FOR CLOSIN ALL OF FILES BELOW
		text = '▼ ' + filter(selected)
		access.delete(currentSelection)
		access.insert(currentSelection,text)
		print(access.get())
		for element in os.listdir(foldDic[fileSelected]):
			while element in access.get():
				newElementPos = currentSelection[0] + 1 
				access.delete(newElementPos)


access.bind("<<ListboxSelect>>", select_access)

app.mainloop()
