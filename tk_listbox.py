#coding:utf-8

import os
from  FolderClass import Folder
import tk_init as tki
import logging

#logging.disable(logging.INFO)

selectedPast = []

def Listbox_click(event):
	lbxLine = tki.Listbox.curselection()

	if len(lbxLine) != 0:
		clickedContent = tki.Listbox.get(lbxLine)
		selectedPast.append(clickedContent)
	else:
		clickedContent = selectedPast[-1]


	clickedContentObject = Folder.get_folder_in_foldList(clickedContent)
	logging.info('===========Clicked on "'+ clickedContentObject.name + '"==============')

	if clickedContentObject.dirEntry.is_dir():
		if is_open_in_Listbox(clickedContentObject):
			Listbox_delete_contentList(clickedContentObject.contentList, lbxLine)

		else:
			Listbox_insert_contentList(clickedContentObject.contentList, lbxLine)
	
	elif clickedContentObject.dirEntry.is_file():
		tki.Listbox_display_file_content(clickedContentObject)

def do_pop_menu(event):
	try:
		tki.pop_menu.tk_popup(event.x_root, event.y_root, 0)

		nearFolderClick = tki.Listbox.get(tki.Listbox.nearest(event.y))
		nearFolder = Folder.get_folder_in_foldList(nearFolderClick)
		
		if nearFolder == None:
			if Folder.is_in_mainFold(nearFolder):
				selectedPast.append(Folder.mainFold.name)
				
		if nearFolder != None:
			selectedPast.append(nearFolderClick)

		logging.info('===========Pop menu at ({} , {}) - "{}"'.\
			format(event.x_root, event.y_root,tki.Listbox.get(tki.Listbox.nearest(event.y))))
	finally:
		tki.pop_menu.grab_release()

def add_file(event):
	try:
		fileName = tki.NameEntry.get()
		logging.info('LBX - Adding "%s"'%fileName)

		tki.CreationBox.grid_forget()

		selectedContent = Folder.get_folder_in_foldList(selectedPast[-1])
		
		if selectedContent == None:
			selectedContent = FolderClass.Folder.mainFold

		lbxLine = get_lbx_line(selectedContent.lbx_name)

		
		if selectedContent.dirEntry.is_dir():
			
			if is_open_in_Listbox(selectedContent):
				Listbox_delete_contentList(selectedContent.contentList, (lbxLine,))
				selectedContent.add_file(fileName)
				Listbox_insert_contentList(selectedContent.contentList, (lbxLine,))
			else:
				selectedContent.add_file(fileName)
				Listbox_insert_contentList(selectedContent.contentList, (lbxLine,))
		
		elif selectedContent.dirEntry.is_file():
			parentFolder = os.path.dirname(selectedContent.path)
			
			if os.path.split(parentFolder)[1] == Folder.mainFold.name:
				parentFolder = Folder.mainFold
				parentLbxLine = (-1,)
			else:
				parentFolder = Folder.get_folder_in_foldList(os.path.split(parentFolder)[1])
				parentLbxLine = (get_lbx_line(parentFolder),)


			Listbox_delete_contentList(parentFolder.contentList, parentLbxLine)
			parentFolder.add_file(fileName)
			Listbox_insert_contentList(parentFolder.contentList, parentLbxLine)

	except Exception as exception:
		logging.error('LBX - Add %s item to lbx FAILED:\n %s'%(fileName, exception))

def add_folder(event):
	try:
		fileName = tki.NameEntry.get()
		logging.info('LBX - Adding "%s"'%fileName)

		tki.CreationBox.grid_forget()

		selectedContent = Folder.get_folder_in_foldList(selectedPast[-1])
		
		if selectedContent == None:
			selectedContent = FolderClass.Folder.mainFold

		lbxLine = get_lbx_line(selectedContent.lbx_name)

		
		if selectedContent.dirEntry.is_dir():
			
			if is_open_in_Listbox(selectedContent):
				Listbox_delete_contentList(selectedContent.contentList, (lbxLine,))
				selectedContent.add_folder(fileName)
				Listbox_insert_contentList(selectedContent.contentList, (lbxLine,))
			else:
				selectedContent.add_file(fileName)
				Listbox_insert_contentList(selectedContent.contentList, (lbxLine,))
		
		elif selectedContent.dirEntry.is_file():
			parentFolder = os.path.dirname(selectedContent.path)
			
			if os.path.split(parentFolder)[1] == Folder.mainFold.name:
				parentFolder = Folder.mainFold
				parentLbxLine = (-1,)
			else:
				parentFolder = Folder.get_folder_in_foldList(os.path.split(parentFolder)[1])
				parentLbxLine = (get_lbx_line(parentFolder),)


			Listbox_delete_contentList(parentFolder.contentList, parentLbxLine)
			parentFolder.add_folder(fileName)
			Listbox_insert_contentList(parentFolder.contentList, parentLbxLine)

	except Exception as exception:
		logging.error('LBX - Add %s item to lbx FAILED:\n %s'%(fileName, exception))

def is_open_in_Listbox(folder):
	logging.info('LBX - is_open_in_Listbox({})'.format(folder.name))
	
	try:
		contentListContent_in_lbx = len(folder.contentList)

		for content in folder.contentList:
			if content.lbx_name in tki.Listbox.get(0,last=tki.tk.END):
				if os.path.split(content.path)[0] == folder.path:
					contentListContent_in_lbx -= 1


		if contentListContent_in_lbx == 0:
			logging.info('LBX - YES')
			return True

		else:
			logging.info("LBX - NO")
			return False
	
	except Exception as exception:
		logging.error('LBX - is_open_in_Listbox({}) FAILED:\n<{}>'.\
				format(folder.name,exception))

def Listbox_delete_contentList(contentList, lbx_line):
	logging.info("LBX - DEL - {} items(s) from listbox at lbx_line{}".\
			format(len(contentList), lbx_line[0]))
	try:
		newList = []
		for content in contentList:
			newList.append(content)

		newList.sort(key= lambda content:content.name, reverse=True)
		for content in newList:
			logging.info('LBX -  -  "{}" line {}.'.\
					format(content.name, lbx_line[0]+1))
			if content.dirEntry.is_dir():
				if is_open_in_Listbox(content):
					Listbox_delete_contentList(content.contentList,(lbx_line[0]+1,))
			tki.Listbox.delete(lbx_line[0]+1)

	except Exception as exception:
		logging.error("LBX - DEL - Listbox_delete_contentList({} item(s)) FAILED:\n<{}>".\
				format(len(contentList), exception))

def Listbox_insert_contentList(contentList, lbx_line):
	logging.info("LBX - ADD - {} item(s) to listbox :".format(len(contentList)))
	
	try:
		for content in contentList:
			logging.info('LBX -  -  "{}" to listbox.'.format(content.name))
			tki.Listbox.insert(lbx_line[0]+1, content.lbx_name)
			if content.dirEntry.is_dir():
				tki.Listbox.itemconfig((lbx_line[0]+1,), foreground='blue')
			else:
				tki.Listbox.itemconfig((lbx_line[0]+1,), foreground='red')

	except Exception as exception:
		logging.error("LBX - ADD - {} item(s) from listbox FAILED:\n<{}>".\
				format(len(contentList),exception))

def delete_content():
	selectedContent = selectedPast[-1]
	selectedContent = Folder.get_folder_in_foldList(selectedContent)
	lbxLine = get_lbx_line(selectedContent)
	
	logging.info('LBX - Deleting "%s"'%selectedContent.name)
	
	parentFolder = os.path.dirname(selectedContent.path)
	if os.path.split(parentFolder)[1] != Folder.mainFold.name:
		parentFolder = Folder.get_folder_in_foldList(os.path.split(parentFolder)[1])
	else:
		parentFolder = Folder.mainFold


	if selectedContent != None:
		if selectedContent.dirEntry.is_file():
			parentFolder.delete_content(selectedContent)
			
			count = 0
			for lbxContent in tki.Listbox.get(0, last=tki.tk.END):
				if lbxContent == selectedContent.lbx_name:
					break
				count += 1
			tki.Listbox.delete(count)
		
		elif selectedContent.dirEntry.is_dir():
			if is_open_in_Listbox(selectedContent):
				Listbox_delete_contentList(parentFolder.contentList, (lbxLine,))
				parentFolder.delete_content(selectedContent)
			else:
				parentFolder.delete_content(selectedContent)
			
			count = 0
			for lbxContent in tki.Listbox.get(0, last=tki.tk.END):
				if lbxContent == selectedContent.lbx_name:
					break
				count += 1
			tki.Listbox.delete(count)

def get_lbx_line(contentName):
	index = 0

	for content in tki.Listbox.get(0, last=tki.tk.END):
		if content == contentName:
			break
		index += 1

	return index
