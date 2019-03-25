#coding:utf-8

from  FolderClass import Folder
import tk_init as tki


def Listbox_click(event):
	content_clicked = tki.Listbox.get(tki.Listbox.curselection())

	if is_in_foldList(content_clicked):
		folder_clicked = Folder.get_folder_in_foldList(content_clicked)
		
		if is_open_in_Listbox(folder_clicked):
			Listbox_delete_contentList(folder_clicked.contentList)
		else:
			Listbox_insert_contentList(folder_clicked.contentList)


def is_in_foldList(searched_folderName):
	print('[MAIN] Is "{}" in foldList ?'.format(searched_folderName))
	
	for folder in Folder.foldList:
		print(folder.name, searched_folderName)
		try:
			if folder.name == searched_folderName:
				return True
				break
			
		except:
			return False
			print("Searching foldList for {} FAILED".format(searched_folderName))


def get_folderObject_in_foldList(searched_folderName):
	print('[MAIN] Get folder "{}" from foldList.'.format(searched_folderName))

	for folder in Folder.foldList:
		try:
			if folder.name == searched_folderName:
				return folder
		except:
			return None


def is_open_in_Listbox(folder):
	print('[MAIN] Is "{}" open in listbox ?'.format(folder.name))
	
	contentList_len = len(folder.contentList)
	for content in folder.contentList:
		if content in tki.Listbox.get(0,last=tki.tk.END):
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
		tki.Listbox.insert(tki.Listbox.curselection()[0]+1, content)


def Listbox_delete_contentList(contentList):
	print('Delete "{}" from listbox.'.format(contentList))

	for content in contentList:
		tki.Listbox.delete(tki.Listbox.curselection()[0]+1)