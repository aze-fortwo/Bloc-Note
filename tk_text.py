#coding:utf -8

import FolderClass as Fclass
import tk_init as tki 
import logging

def save_text(event):
	try:
		lbxSelection = tki.Listbox.curselection()
		if len(lbxSelection) == 1:
			lbxSelection = tki.Listbox.get(lbxSelection)
		else:
			lbxSelection = tki.Listbox.get(0)
		
		curFile = Fclass.Folder.get_folder_in_foldList(lbxSelection)

		logging.info('TXT - Saving text from "%s"'%curFile.name)

		with open(curFile.path, encoding='utf-8', mode='r') as ofi:
			curFile.content = ofi.read()

		tki.pop_alert('Saving text from "%s"'%curFile.name)

	except Exception as exception:
		logging.error('TXT - Saving {} FAILED:\n {}'.format(curFile.name, exception))



