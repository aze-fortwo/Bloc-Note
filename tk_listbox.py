#coding:utf-8

import os
from  FolderClass import Folder
import tk_init as tki
import logging

def Listbox_click(event):
	lbx_line = tki.Listbox.curselection()
	clicked_content = tki.Listbox.get(lbx_line)


	clicked_folder = Folder.get_folder_in_foldList(clicked_content)
	logging.info('===========Clicked on "'+ clicked_folder.name + '"==============')

	if clicked_folder.dirEntry.is_dir():
		if is_open_in_Listbox(clicked_folder):
			Listbox_delete_contentList(clicked_folder.contentList, lbx_line)

		else:
			Listbox_insert_contentList(clicked_folder.contentList, lbx_line)
	elif clicked_folder.dirEntry.is_file():
		display_file_content(clicked_folder)


"""--------------------------Listbox_click method-------------------------"""

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
		logging.error('LBX - is_open_in_Listbox({}) FAILED:\n<{}>'.format(folder.name,\
														 exception))


def Listbox_delete_contentList(contentList, lbx_line):
	logging.info("LBX - DEL - Listbox_delete_contentList({})".format(contentList))
	try:
		for content in contentList:
			if content.dirEntry.is_dir():
				if is_open_in_Listbox(content):
					Listbox_delete_contentList(content.contentList,(lbx_line[0]+1,))
			tki.Listbox.delete(lbx_line[0]+1)
			logging.info('LBX - DEL - "{}" from listbox.'.format(content.name))

	except Exception as exception:
		logging.error("LBX - DEL - Listbox_delete_contentList({}) FAILED:\n<{}>".\
				format(contentList, exception))


def Listbox_insert_contentList(contentList, lbx_line):
	logging.info("LBX - ADD - {} item(s) to listbox :".format(len(contentList)))
	
	try:
		for content in contentList:
			logging.info('LBX -  -  "{}" to listbox.'.format(content.name))
			tki.Listbox.insert(lbx_line[0]+1, content.lbx_name)
			if content.dirEntry.is_dir():
				tki.Listbox.itemconfig((lbx_line[0]+1,), foreground='blue')
			else:
				tki.Listbox.itemconfig((lbx_line[0]+1,), foreground='green')

	except Exception as exception:
		logging.error("LBX - ADD - {} items from listbox FAILED:\n<{}>".\
				format(len(contentList),type(exception).__name__))


def display_file_content(fileClicked):
	tki.Text.delete(0.0,index2=tki.tk.END)
	tki.Text.insert("insert",fileClicked.content)