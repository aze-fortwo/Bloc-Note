#coding:utf-8

import tkinter as tk
from tkinter import font
import os
import time
import io

def Bloc_Note(app):
	global start, fold_list

	start = 1
	exept = ['bc.pyw','af.png','db.png','dlt.png','Menu.txt']
	fold_list = []

	Textfont = font.Font(family='Times New Roman', size=12, weight='normal', slant='roman')
	Txt = tk.Text(app,width = 60, wrap=tk.WORD, font=Textfont)
	Lbx = tk.Listbox(app, activestyle='none',selectforeground='white',highlightthickness=0,\
			selectmode=tk.SINGLE, height=25,exportselection =0,selectbackground='light grey')



	Txt.grid(row=1,column=1, sticky='NS')
	Lbx.grid(row=1,column=0, sticky='NS')
	

	# Init ListBox of folder
	for folder in os.listdir('.'):
		if folder not in exept:
			Lbx.insert(0,folder)
			Lbx.itemconfig(0, foreground='orange')
			fold_list.append(folder)





	def new_file():

		entry_fen = tk.Toplevel()
		text = 'New file in C:\\' + Lbx.get(Lbx.curselection()) + '\\:'
		lab = tk.Label(entry_fen, text=text)
		lab.grid(row=1,column=0, sticky='NWS')
		entry = tk.Entry(entry_fen, width=10)
		entry.grid(row=1,column=1, sticky='NSW')
		
		def send_new_file(event):
			filename = entry.get() + '.txt'

			if os.path.isdir(Lbx.get(Lbx.curselection())):
				path =os.path.join(Lbx.get(Lbx.curselection()), filename)
			else:
				for index,folder in enumerate(fold_list):
					for file in os.listdir(folder): 
						if file == Lbx.get(Lbx.curselection()):
							path = os.path.join(folder[index], filename)
			with open(path, 'w') as file:
				file.close()
			Lbx.insert(int(Lbx.curselection()[0])+1, filename)
			Lbx.itemconfig(int(Lbx.curselection()[0])+1, foreground='blue')
		
		entry.bind('<Return>', send_new_file)

	def new_folder():
		entry_fen = tk.Toplevel()
		text = 'New folder in C:\\bloc_note_2.0\\:'
		lab = tk.Label(entry_fen, text=text)
		lab.grid(row=1,column=0, sticky='NWS')
		entry = tk.Entry(entry_fen, width=10)
		entry.grid(row=1,column=1, sticky='NSW')

		def send_new_folder(event):
			fold_name = entry.get()
			if not os.path.exists(fold_name):
				os.makedirs(fold_name)
				Lbx.insert(tk.END, fold_name)
				fold_list.append(fold_name)
				Lbx.itemconfig(tk.END, foreground='orange')
		entry.bind('<Return>', send_new_folder)

	def backup():
		for folder in fold_list:
			for file in os.listdir(folder):
				file_path = os.path.join(os.getcwd(),folder,file)
				with open(file_path, 'r') as infile:
					text = infile.read()
					backup_path = 'C:\\Users\\admin\\BACKUP\\'+file
					with open(backup_path, 'w+') as infile:
						infile.write(text)
						compteur += 1

	menubar = tk.Menu(app)
	filemenu = tk.Menu(menubar, tearoff=0)
	filemenu.add_command(label='New_File', command=new_file)
	filemenu.add_command(label='New_Folder', command=new_folder)
	filemenu.add_separator()
	filemenu.add_command(label='Backup', command=backup)
	menubar.add_cascade(label='File',menu=filemenu)
	app.config(menu=menubar)



	def select_Lbx(event):
		global start, lastpos, fold_list
		"""
		Get the folder content when clicking on the list_box 
		and display it
		"""
		if start:
			lastpos = ''

		path = ''
		#_______________OPEN FILE_________________
		# If the selection is a file
		for index,folder in enumerate(fold_list):
			for file in os.listdir(folder):
				if file == Lbx.get(Lbx.curselection()):
					path = os.path.join(os.getcwd(),fold_list[index],Lbx.get(Lbx.curselection()))

		if os.path.isfile(path):
			with open(path, 'r', encoding='utf-8') as ofi:
				text = ofi.read()
				Txt.delete(0.0, index2= tk.END)
				Txt.insert('insert',text)

		#______________DEL SUB-FILE______________
		# If the selected folder is the last selected
		if lastpos == int(Lbx.curselection()[0]):
			if os.path.isdir(Lbx.get(Lbx.curselection())):
				# Read the folder's file and delete the files displayed in Lbx
				for file in os.listdir(Lbx.get(Lbx.curselection())):
					i = 0
			
					# Check if the folder's file are displayed
					while i < int(Lbx.size()):
						# If so delete the display
		
						if file == str(Lbx.get(i)):
							Lbx.delete(i)
						i += 1
			else:
				pass

		
				lastpos = int(Lbx.curselection()[0])


		# ______________GET SUB-FILE______________

		# If the selection is not the same as the last one
		elif lastpos != int(Lbx.curselection()[0]):
			# Get the folder name
			selection = Lbx.get(Lbx.curselection())
			# Get the display pos
			pos = int(Lbx.curselection()[0]+1)
			
			# If the selection is a folder
			if os.path.isdir(selection):
				# Check what's inside
				for file in os.listdir(selection):
					path = os.path.normpath(os.path.join(os.getcwd(),selection,file))
					
					# Check if it is file inside
					if os.path.isfile(path):
						tab = Lbx.get(0, tk.END)
						if file not in tab:
							rest = file
							Lbx.insert(pos, rest)
							Lbx.itemconfig(pos, foreground='blue')

					# If it's another folder ?????
					elif os.path.isdir(path):
						pass
			else:
				pass
			
			lastpos = int(Lbx.curselection()[0])
		
		start = 0

	Lbx.bind("<<ListboxSelect>>", select_Lbx)
	






if __name__ == "__main__":
	app = tk.Tk()
	app.title('Bloc Note 2.0')
	Bloc_Note(app)
	app.mainloop()
