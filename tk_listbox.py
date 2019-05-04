#coding:utf-8

from  FolderClass import Folder
import tk_init as tki
import logging

logging.basicConfig(filename='debug.txt',filemode='w+', level = logging.DEBUG,format=' %(asctime)s - %(levelname)s - LBX - %(message)s')

def Listbox_click(event):
	lbx_line = tki.Listbox.curselection()
	clicked_content = tki.Listbox.get(lbx_line)

	logging.info('Clicked on "'+ clicked_content + '"')


	if Folder.is_in_foldList(clicked_content):

		clicked_folder = Folder.get_folder_in_foldList(clicked_content)


		if is_open_in_Listbox(clicked_folder):
			Listbox_delete_contentList(clicked_folder.contentList, lbx_line)
		
		else:
			Listbox_insert_contentList(clicked_folder.contentList, lbx_line)


"""--------------------------Listbox_click method-------------------------"""


def is_in_foldList(searched_folderName):
	logging.info('Clicked on "'+ clicked_content + '"')('LBX  Is "{}" in foldList ?\n'.format(searched_folderName))
	try:
		if searched_folderName in Folder.foldList:
			#print('      It is in foldList')
			return True
		else:
			#print('     Not in foldList')
			return False

	except Exception as exception:
		logging.error("Searching foldList for {} FAILED.".format(searched_folderName))



def is_open_in_Listbox(folder):
	logging.info('Is "{}" open in listbox ?'.format(folder.lbx_name))
	try:
		contentList_content_detected_in_lbx = len(folder.contentList)


		for content in folder.contentList:
			if content.lbx_name in tki.Listbox.get(0,last=tki.tk.END):
				contentList_content_detected_in_lbx -= 1


		if contentList_content_detected_in_lbx == 0:
			logging.debug('YES')
			return True

		else:
			logging.debug("NO")
			return False
	
	except Exception as exception:
		logging.error('Is "{}" open in Lbx FAILED.'.format(folder.name))



def Listbox_delete_contentList(contentList, lbx_line):
	logging.info("Delete {} item(s) from listbox.".format(len(contentList)))
	try:
		for content in contentList:
			tki.Listbox.delete(lbx_line[0]+1)
			logging.debug('Delete "{}" from listbox.'.format(content.name))

	except Exception as exception:
		logging.error("Delete {} items from listbox FAILED.".format(len(contentList)))



def Listbox_insert_contentList(contentList, lbx_line):
	logging.info("Add {} item(s) to listbox :".format(len(contentList)))
	
	try:
		for content in contentList:
			logging.debug('Add "{}" to listbox.'.format(content.name))
			tki.Listbox.insert(lbx_line[0]+1, content.lbx_name)

	except Exception as exception:
		logging.error("Add {} items from listbox FAILED.\n".format(type(exception).__name__, len(contentList)))		

