#coding: utf-8

import os
from FolderClass import Folder
import tk_init as tki


"""----------Init Current Working Directory folder-----------"""

unwanted_Files = [	'tk_listbox.py',	'.git',			'.gitignore',	'Bloc Note.pyw',
					'FolderClass.py',	'README.md',	'main.pyw',		'__pycache__',
					'tk_init.py']

for content in os.listdir('.'):
	if content not in unwanted_Files:
		path = os.getcwd() + "\\" + content
		folder = Folder(path)
		tki.Listbox.insert(0, folder.name)


"""--------------------Tkinter----------------------------"""


tki.app.mainloop()