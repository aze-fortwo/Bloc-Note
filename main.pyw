#coding: utf-8

import os
import tkinter as tk

from FolderClass import Folder

unwated_Files = ['.git','.gitignore','BlocNote.pyw','FolderClass.py','README.md','main.pyw','__pycache__']



"""----------------Open/close folder/file------------------"""

def is_in_folderList(folderName):
	print('[MAIN] Is {} folder ?'.format(folderName))
	
	for folder in folderList:
		if folder.name == folderName:
			return True
		else:
			return False


def get_folder_in_folderList(folderName):
	print('[MAIN] Get folder "{}" from folderList.'.format(folderName))

	for folder in folderList:
		if folder.name == folderName:
			return folder
		else:
			return None


def is_open(folder):
	print('[MAIN] Is {} open in listbox ?'.format(folder.name))

	if folder.contentList in Listbox.get(0, last=tk.END):
		return True
	else:
		return False


def Listbox_click(event):
	content_clicked = Listbox.get(Listbox.curselection())

	if is_in_folderList(content_clicked):
		folder_clicked = get_folder_in_folderList(content_clicked)
		if is_open(folder_clicked):
			print('OK')
		else:

			Listbox.insert(Listbox.curselection()[0]+1, folder_clicked.contentList)
			

"""--------------------Tkinter----------------------------"""
app = tk.Tk()


Background = tk.Frame(app)

Listbox = tk.Listbox(Background)
Listbox.bind('<<ListboxSelect>>',Listbox_click)



Background.grid(row=0,column=0)
Listbox.grid(row=0, column=0, sticky='NSEW')




"""--------------------folderList Update-------------------"""
folderList = []

for content in os.listdir('.'):
	if content not in unwated_Files:
		if os.path.isdir(content):
			folderList.append(Folder(content))
			Listbox.insert(tk.END,Folder(content).name)


app.mainloop()