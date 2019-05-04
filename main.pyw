#coding: utf-8

import os
from FolderClass import Folder
from FileClass import File
import tk_init as tki
import logging

logging.basicConfig(filename='debug.txt',filemode='w+', level = logging.DEBUG,format='MAIN %(message)s')

"""----------Init Current Working Directory folder-----------"""

unwanted_Files = [	'tk_listbox.py',	'.git',			'.gitignore',	'Bloc Note.pyw',
					'FolderClass.py',	'README.md',	'main.pyw',		'__pycache__',
					'tk_init.py', 		'FileClass.py',	'Debug.txt']

for content in os.scandir('.'):
	if content.name not in unwanted_Files:
		if content.is_dir():
			discovered = Folder(content)
		else:
			discovered = File(content)
		
		tki.Listbox.insert(tki.tk.END, discovered.lbx_name)


"""
for content in Folder.foldList:
	for subcontent in content.contentList:
		print(subcontent.lbx_name)
"""

"""--------------------Tkinter----------------------------"""


tki.app.mainloop()