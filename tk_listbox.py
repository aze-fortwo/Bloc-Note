#coding:utf-8

import os
from  FolderClass import Folder
import tk_init as tki
import logging

def Listbox_click(event):
	lbx_line = tki.Listbox.curselection()
	clicked_content = tki.Listbox.get(lbx_line)

	logging.info('============Clicked on "'+ clicked_content + '"==============')



	clicked_folder = Folder.get_folder_in_foldList(clicked_content)

	if is_open_in_Listbox(clicked_folder):
		Listbox_delete_contentList(clicked_folder.contentList, lbx_line)

	else:
		Listbox_insert_contentList(clicked_folder.contentList, lbx_line)


"""--------------------------Listbox_click method-------------------------"""


def is_in_foldList(searched_folderName):
	logging.info('LBX - Is "{}" in foldList ?\n'.format(searched_folderName))
	try:
		if searched_folderName in Folder.foldList:
			logging.info('LBX - YES')
			return True
		else:
			logging.info('LBX - NO')
			return False

	except Exception as exception:
		logging.error("LBX - Searching foldList for {} FAILED:\n<{}>".\
				format(searched_folderName, exception))



def is_open_in_Listbox(folder):
	logging.info('Is "{}" open in listbox ?'.format(folder.name))
	
	try:
		contentListContent_in_lbx = len(folder.contentList)

		for content in folder.contentList:
			if os.path.split(content.path)[0] == folder.path:
				if content.lbx_name in tki.Listbox.get(0,last=tki.tk.END):
					contentListContent_in_lbx -= 1


		if contentListContent_in_lbx == 0:
			logging.info('YES')
			return True

		else:
			logging.info("NO")
			return False
	
	except Exception as exception:
		logging.error('Is "{}" open in Lbx FAILED:\n<{}>'.format(folder.name,\
														 exception))



def Listbox_delete_contentList(contentList, lbx_line):
	logging.info("Delete {} item(s) from listbox.".format(len(contentList)))
	try:
		for content in contentList:
			tki.Listbox.delete(lbx_line[0]+1)
			logging.info('Delete "{}" from listbox.'.format(content.name))

	except Exception as exception:
		logging.error("Delete {} items from listbox FAILED:\n<{}>".\
				format(len(contentList), exception))



def Listbox_insert_contentList(contentList, lbx_line):
	logging.info("Add {} item(s) to listbox :".format(len(contentList)))
	
	try:
		for content in contentList:
			logging.info('Add "{}" to listbox.'.format(content.name))
			tki.Listbox.insert(lbx_line[0]+1, content.lbx_name)

	except Exception as exception:
		logging.error("Add {} items from listbox FAILED:\n<{}>".\
				format(len(contentList),type(exception).__name__, len(contentList)))


