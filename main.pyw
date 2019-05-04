#coding: utf-8

import os
import FolderClass 
import FileClass
import tk_init as tki
import logging

logging.basicConfig(level = logging.DEBUG,\
		format=' %(asctime)s - %(levelname)s - %(message)s',datefmt='%H:%M:%S')
"""----------Init Current Working Directory folder-----------"""

unwanted_Files = [	'tk_listbox.py',	'.git',			'.gitignore',	'Bloc Note.pyw',
					'FolderClass.py',	'README.md',	'main.pyw',		'__pycache__',
					'tk_init.py', 		'FileClass.py',	'Debug.txt']

logging.debug('FIRST SCANNING LOOP')
for content in os.scandir(os.getcwd()):
	if content.name not in unwanted_Files:
		if content.is_dir():
			discovered = FolderClass.Folder(content)
		if content.is_file():
			discovered = FileClass.File(content)
		
		tki.Listbox.insert(tki.tk.END, discovered.lbx_name)


"""
for content in Folder.foldList:
	for subcontent in content.contentList:
		print(subcontent.lbx_name)
"""

"""--------------------Tkinter----------------------------"""


tki.app.mainloop()