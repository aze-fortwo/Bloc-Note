#coding:utf-8

import tkinter as tk
from tkinter import font
import os
import time
import io

def Bloc_Note(self):
	global start, fold_list

	start = 1
	exept = ['bc.pyw','af.png','db.png','dlt.png','Menu.txt','test.pyw']
	# List everything in the parent floder, except the not allowed file list
	fold_list = [x for x in os.listdir('.') if x not in exept]
	# foldDic contain all the files associated 
	foldDic = {}


	self.Textfont = font.Font(family='Times New Roman', size=12, weight='normal', slant='roman')
	self.Txt = tk.Text(self,width = 60, wrap=tk.WORD, font=self.Textfont)
	self.Lbx = tk.Listbox(self, activestyle='none',selectforeground='white',highlightthickness=0,\
			selectmode=tk.SINGLE, height=25,exportselection =0,selectbackground='light grey')
	self.alert = tk.Message(self, text="", aspect=300, justify=tk.CENTER)


	self.Txt.grid(row=1,column=1, sticky='NS')
	self.Lbx.grid(row=1,column=0, sticky='NS')
	
	def update_foldDic(path):
		for element in os.listdir(path):
			if "." not in element:
				if element not in foldDic.keys():
					foldDic[element] = path + "\\" + element
					update_foldDic(foldDic[element])

	#=============FILL LISTBOX============
	for x in fold_list:
		# Create in foldDic the root of folder path associated with the folder/file name
		foldDic[x] = str(os.getcwd()) + "\\" + x
		update_foldDic(foldDic[x])
		# Display closed folder on listBox display
		x = '▲ ' + x
		# Print folder / file on listbox
		self.Lbx.insert(0,x)
		# Init List of folder

	# ==============Rreating file/folder================
	def OptionMenuRead():
		clear_info()
		
		# Type of creation request  (folder or file)
		typeFileValue = self.typeFileValue.get()
		# In wich folder you want it blank for nothing
		folder = self.foldListValue.get()
		# What is the folder or the file name
		fileName = self.entry.get()
		#What is the format of the file
		fileFormat = self.typeFileList.get()

		if typeFileValue == 'File':
			path = foldDic[folder] + "\\" + fileName + self.typeFileList.get()
			file = open(path,'w+',encoding='utf-8')
			file.close()
		
		if typeFileValue == 'Folder':
			if folder != '':
				path = folder+'\\'+ fileName
			else:
				path = fileName
			os.mkdir(path)
		
		self.entry_window.destroy()

		txt = "Create " + fileName + "In " + folder
		self.alert.config(text=txt)
		self.alert.grid(row=1,column=1, sticky="EWS")

	# Create folder/File zone
	def entry_fen():
		# < New <FILE/FOLDER> in <FOLDER LIST> named <NAME ENTRY> as <TYPE OF FILE>

		# New window for creation files
		self.entry_window = tk.Toplevel()
		
		# Type of creation: FILE or FOLDER
		self.typeFileValue = tk.StringVar()
		self.typeFileValue.set('File')
		self.typeList = tk.OptionMenu(self.entry_window,self.typeFileValue,'File','Folder')
		
		# In wich folder do you want to make it ?
		self.foldListValue = tk.StringVar()
		self.foldListValue.set(fold_list[0])
		self.foldList = tk.OptionMenu(self.entry_window,self.foldListValue,*foldDic.keys(),'')

		# Name of the file
		self.entry = tk.Entry(self.entry_window, width=10)

		# Submit button
		self.done_button = tk.Button(self.entry_window, text='✔', command=OptionMenuRead)

		# Type of file if (file creation only)
		allowed_types = ['.txt', '.py', '.pyw','.html','.css','.js']
		self.typeFileList = tk.StringVar()
		self.typeFileList.set(allowed_types[0])
		self.typeOfFile = tk.OptionMenu(self.entry_window,self.typeFileList, *allowed_types)
		
		tk.Label(self.entry_window, text='New ').grid(row=1,column=0, sticky='NSW')
		self.typeList.grid(row=1,column=1,sticky='NSW')
		tk.Label(self.entry_window, text=' in ').grid(row=1,column=2,sticky='NSW')
		self.foldList.grid(row=1,column=3,sticky='NSW')
		tk.Label(self.entry_window,text='named :').grid(row=1,column=4,sticky='NSW')
		self.entry.grid(row=1,column=5, sticky='NSW')
		self.typeOfFile.grid(row=1,column=6)
		self.done_button.grid(row=1,column=7)
		
		def change_typeFileList(*args):
			if self.typeFileValue.get() == 'Folder':
				self.typeOfFile.grid_remove()
				self.done_button.grid(row=1,column=6)
	
			elif self.typeFileValue.get() == 'File':
				self.typeOfFile.grid(row=1,column=6)
				self.done_button.grid(row=1,column=7)

		self.typeFileValue.trace('w', change_typeFileList)

	def get_mouse_pos(event):
		global pos_y
		pos_y = event.y

	def delete(file):
		file = filter(file)
		
		if file in foldDic.keys():
			deletePath = foldDic[file]
			os.rmdir(deletePath)
			self.Lbx.delete(self.Lbx.nearest(pos_y))
			alertText = 'The folder '+ file + ' is deleted'
		
		else:
			for folder, path in foldDic.items():
				for element in os.listdir(path):
					if element == file:
						delPath = path + "\\" + file
						os.remove(delPath)

						alertText = "The file " + file + " is deleted"
						self.Lbx.delete(self.Lbx.nearest(pos_y))

		self.alert.config(text=alertText)
		self.alert.grid(row=1,column=1, sticky="EWS")

	pop_menu = tk.Menu(self,tearoff=0)
	pop_menu.add_command(label = 'Add File', command=lambda:entry_fen())
	pop_menu.add_command(label='Delete', command=lambda:delete(self.Lbx.get(self.Lbx.nearest(pos_y))))


	def do_pop_menu(event):
		
		try:
			pop_menu.tk_popup(event.x_root, event.y_root,0)
		finally:
			pop_menu.grab_release()


	# Save all bloc Note data
	def backup():
		
		clear_info()
		for folder, path in foldDic.items():
			for element in os.listdir(path):
				if '.' in element:
					filePath = path + "\\" + element
					with open(filePath, 'r') as infile:
						text = infile.read()
						backup_path = 'C:\\Users\\admin\\Prog\\BACKUP\\' + element
						with open(backup_path, 'w+') as infile:
							infile.write(text)

		self.alert.config(text="Backup Done")
		self.alert.grid(row=1,column=1, sticky="EWS")

		
	# Used for read in ListBox - Return only folder/file name
	def filter(string):
		badChars =['▲', '▼', ' ']
		
		# Every character in bad list
		for char in badChars:
			# While any bad character in ListBox string
			# Reset parsing every time because of 
			# decreasing len(string)

			while char in string:
				i = 0
				# Go into each char of Listbox string
				while i < len(string):
					# If we found it
					if string[i] == char:
						if i != 0:
							# Cut from 0 to bad index then from bad index +1 to end
							string = string[:i] + string[i+1:]
							# break make while i < len(string) restart
							break
						if i == 0:
							# Cut from 0+1 to the end of string
							string = string[i+1:]
							# break make while i < len(string) restart
							break
					i += 1
		return string

	menubar = tk.Menu(self)
	filemenu = tk.Menu(menubar, tearoff=0)
	filemenu.add_command(label='New...', command=entry_fen)
	filemenu.add_separator()
	filemenu.add_command(label='Backup', command=backup)
	menubar.add_cascade(label='File',menu=filemenu)
	self.config(menu=menubar)

	def select_Lbx(event):
		global fileSelected

		clear_info()
		# Where do we have clicked ? ListBox index
		currentSelection = self.Lbx.curselection()
		# What is displayed at this index ?
		selected = self.Lbx.get(currentSelection)
		# Get file/folder name whithout undesired char
		fileSelected = filter(selected)
		# Our new line for ListBox
		text = ""
		

		def close_fold(foldPath):
			# Get from the selected listBox element to the end
			# of the listBox element
			LbxContent = self.Lbx.get(currentSelection,last=tk.END)
			
			# For every content in clicked folder
			for file in os.listdir(foldPath):
				# List all the displayed files on listBox
				for i, name in enumerate(LbxContent):
					# If the displayed files match the content folder
					if filter(name) == filter(file):
						

						# If foldPath content is a Folder Dictionnary key
						if file in foldDic.keys() :
							# Recall function for searching file in it
							close_fold(foldDic[file])

							# Delete from the ListBox the parsed folder
							newElementPos = currentSelection[0] + 1

						# If foldPath content is a file
						else:
							newElementPos = currentSelection[0] + i 
						
						self.Lbx.delete(newElementPos)
					


		# If closed folder selected -> show content
		if '▲' in selected:
				
			foldSave = fileSelected
			# Spacing for folder content
			# basicLen is the size of path from 
			# executable root to the file we clicked on
			basicLen = len(os.getcwd().split('\\'))+1
			# pathLen is the size of the path of the clicked folder/file
			pathLen = len(foldDic[fileSelected].split('\\'))
			# 1 path folder size of difference = 1 tabulation
			i = 0
			while pathLen - i > basicLen :
				text += '    '
				i += 1

			# Replace close arrow by open arrow
			# on selected folder
			text += '▼ ' + filter(selected)
			# Delete old clicked folder
			self.Lbx.delete(currentSelection)
			# Update displayed folder
			self.Lbx.insert(currentSelection,text)
				
			# For every content of the folder		
			for element in os.listdir(foldDic[fileSelected]):
				# Reset text value for coming folder/file name
				text = '' 
				i = 0
				# Re-tabulate file/folder display name
				while 1 + pathLen - i > basicLen :
					text += '    '
					i += 1

				# Set the new position in listBox
				# One below the last content
				newElementPos = currentSelection[0] + 1 
				# If it's not a file
				if '.' not in element:
					# Add it to the folder dictionnary
					foldDic[element] = foldDic[fileSelected] + '\\' + element
					# Check if it's a folder
					if os.path.isdir(foldDic[element]):
						# Add the folder closed symbol
						text +=	'▲ ' + element
					# If it's a file
				else:
					# Add just the file name
					text += element
					#Put it into listBox
				
				self.Lbx.insert(newElementPos,text)



		# If open folder selected -> hide content
		elif '▼' in selected:
				
			# Spacing for folder content
			# basicLen is the size of path from 
			# executable root to the file we clicked on
			basicLen = len(os.getcwd().split('\\'))+1
			# pathLen is the size of the path of the clicked folder/file
			pathLen = len(foldDic[fileSelected].split('\\'))
			# 1 path folder size of difference = 1 tabulation
			i = 0
				
			while pathLen - i > basicLen :
				text += '    '
				i += 1
				
			text += '▲ ' + filter(selected)
			self.Lbx.delete(currentSelection)
			self.Lbx.insert(currentSelection,text)

			close_fold(foldDic[fileSelected])


		# If file is selected -> display on text widget
		else:
			# For every known elements
			for element, value in foldDic.items():
				# Get content of those elements
				content = [x for x in os.listdir(foldDic[element])]
				# In content
				for file in content:
				# If we found the file we clicked on
					if fileSelected == file:
						# Open it 
						with open(foldDic[element] + "\\" + fileSelected,"r",encoding="utf-8") as ofi:
							text = ofi.read()
							self.Txt.delete(0.0,index2=tk.END)
							self.Txt.insert("insert",text)

	def save_text(event):
		global fileSelected
		clear_info()
		
		for element in foldDic.keys():
			content = [x for x in os.listdir(foldDic[element])]
			for file in content:
				if fileSelected == file and self.Txt.get(0.0, index2=tk.END) != "":
					saved = self.Txt.get(0.0, index2=tk.END)
					break

		with open(foldDic[element]+"\\"+fileSelected,"w+", encoding="utf-8") as ofi:
			ofi.write(saved)

		txt = fileSelected + " Saved"
		self.alert.config(text=txt)
		self.alert.grid(row=1,column=1, sticky="EWS")

	def clear_info():
		self.alert.grid_forget()



	self.Lbx.bind("<<ListboxSelect>>", select_Lbx)
	self.Txt.bind("<Control-KeyPress-s>", save_text)
	self.Lbx.bind("<Button-3>", do_pop_menu)
	self.bind("<Motion>", get_mouse_pos)



if __name__ == "__main__":
	self = tk.Tk()
	self.title('Bloc Note 2.0')
	Bloc_Note(self)
	self.mainloop()
