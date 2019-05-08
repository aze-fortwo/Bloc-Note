#coding:utf-8

import os
from  FolderClass import Folder
import tk_init as tki
import logging

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
		display_file_content(clickedContentObject)

def is_open_in_Listbox(folder):
	logging.info('LBX - is_open_in_Listbox({})'.format(folder.name))
	
	try:
		contentListContent_in_lbx = len(folder.contentList)

		for content in folder.contentList:
			if os.path.split(content.path)[0] == folder.path:
				if content.lbx_name in tki.Listbox.get(0,last=tki.tk.END):
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
				format(len(contentList),type(exception).__name__))

def display_file_content(fileClicked):
	tki.Text.delete(0.0,index2=tki.tk.END)
	tki.Text.insert("insert",fileClicked.content)

def do_pop_menu(event):
	try:
		tki.pop_menu.tk_popup(event.x_root, event.y_root,0)
	finally:
		tki.pop_menu.grab_release()