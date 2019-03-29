#coding:utf-8

from  FolderClass import Folder
import tk_init as tki


def Listbox_click(event):
	lbx_line = tki.Listbox.curselection()
	content_clicked = tki.Listbox.get(lbx_line)

	print('\nLBX Clicked on "{}"'.format(content_clicked))

	if Folder.is_in_foldList(content_clicked):
		folder_clicked = Folder.get_folder_in_foldList(content_clicked)
		if is_open_in_Listbox(folder_clicked):
			Listbox_delete_contentList(folder_clicked.contentList, lbx_line)
		else:
			Listbox_insert_contentList(folder_clicked.contentList, lbx_line)


def is_in_foldList(searched_folderName):
	print('\n\tLBX Is "{}" in foldList ?'.format(searched_folderName))
	try:
		if searched_folderName in Folder.foldList:
			print('\t\tIt is in foldList')
			return True
		else:
			print('\t\tNot in foldList')
			return False

	except:
		print("\tSearching foldList for {} FAILED.\n".format(searched_folderName))


def is_open_in_Listbox(folder):
	print('\n\tLBX Is "{}" open in listbox ?'.format(folder.name))
	
	contentList_len = len(folder.contentList)
	for content in folder.contentList:
		if content.name in tki.Listbox.get(0,last=tki.tk.END):
			contentList_len -= 1
			try:
				if contentList_len == 0:
					print('\t    It is')
					return True
					break
			except:
				return False
	if content.name not in tki.Listbox.get(0,last=tki.tk.END):
		print("\t    It's not ")


def Listbox_delete_contentList(contentList, lbx_line):
	print("\n\tLBX Delete {} item(s) from listbox.".format(len(contentList)))

	try:
		for content in contentList:
			print('\t    Delete "{}" from listbox.'.format(content.name))
			tki.Listbox.delete(lbx_line[0]+1)
	except:
		print("\t\tDelete {} items from listbox FAILED.\n".foamt(len(contentList)))

def Listbox_insert_contentList(contentList, lbx_line):
	print("\n\tLBX Add {} item(s) to listbox :".format(len(contentList)))
	
	try:
		for content in contentList:
			print('\t    Add "{}" to listbox.'.format(content.name))
			tki.Listbox.insert(lbx_line[0]+1, content.name)
	except:
		print("Delete {} items from listbox FAILED.\n".foamt(len(contentList)))		

