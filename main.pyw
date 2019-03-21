#coding: utf-8

import os
import tkinter as tk

from FolderClass import Folder

unwated_Files = ['.git','.gitignore','BlocNote.pyw','FolderClass.py','README.md','main.pyw','__pycache__']



"""----------------Open/close folder/file------------------"""

def is_in_folderList(folderName):
	print('[MAIN] Is "{}" in folderList ?'.format(folderName))
	
	for folder in folderList:
		try:
			if folder.name == folderName:
				return True
				break

		except:
			return False


def get_folderObject_in_folderList(folderName):
	print('[MAIN] Get folder "{}" from folderList.'.format(folderName))

	for folder in folderList:
		try:
			if folder.name == folderName:
				return folder
		except:
			return None


def is_open_in_Listbox(folder):
	print('[MAIN] Is "{}" open in listbox ?'.format(folder.name))
	

	contentList_len = len(folder.contentList)

	for content in folder.contentList:
		if content in Listbox.get(0,last=tk.END):
			contentList_len -= 1
			try:
				if contentList_len == 0:
					return True
					break
			except:
				return False


def Listbox_insert_contentList(contentList):
	print('Add "{}" to listbox.'.format(contentList))
	
	for content in contentList:
		Listbox.insert(Listbox.curselection()[0]+1, content)


def Listbox_delete_contentList( contentList):
	print('Delete "{}" from listbox.'.format(contentList))

	for content in contentList:
		Listbox.delete(Listbox.curselection()[0]+1)


def Listbox_click(event):
	content_clicked = Listbox.get(Listbox.curselection())

	if is_in_folderList(content_clicked):
		folder_clicked = get_folderObject_in_folderList(content_clicked)
		
		if is_open_in_Listbox(folder_clicked):
			Listbox_delete_contentList(folder_clicked.contentList)
		else:
			Listbox_insert_contentList(folder_clicked.contentList)
			

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
			Listbox.insert(tk.END,content)

app.mainloop()