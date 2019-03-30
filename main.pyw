#coding: utf-8

import os
from FolderClass import Folder
from FileClass import File
import tk_init as tki


"""----------Init Current Working Directory folder-----------"""

unwanted_Files = [	'tk_listbox.py',	'.git',			'.gitignore',	'Bloc Note.pyw',
					'FolderClass.py',	'README.md',	'main.pyw',		'__pycache__',
					'tk_init.py', 		'FileClass.py']

for content in os.listdir('.'):
	if content not in unwanted_Files:
		path = os.path.join(os.getcwd(), content)
		if os.path.isdir(path):
			discovered = Folder(path)
		else:
			discovered = File(path)
		
		tki.Listbox.insert(tki.tk.END, discovered.lbx_name)


"""
for content in Folder.foldList:
	for subcontent in content.contentList:
		print(subcontent.lbx_name)
"""

"""--------------------Tkinter----------------------------"""


tki.app.mainloop()