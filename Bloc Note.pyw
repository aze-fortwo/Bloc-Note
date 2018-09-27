#coding:utf-8

import tkinter as tk
from tkinter import font
from tkinter import TclError
import io
import os
from tkinter import ttk
from PIL import Image

def createWidgets(self):

	File = list()# file
	f = dict()	#file + folder
	F = list()	#folder

	for folder in os.listdir("."):
		if os.path.isdir(folder):
			F.append(folder)

	# Folder
	for t in F:
		if not os.path.exists(t):
			os.makedirs(t)
	i=0

	# File
	while i < len(F):
		for file in os.listdir(F[i]):
			File.append(file)
		i += 1
	i=0

	# Dico File + Folder
	while i < len(F):
		for file in os.listdir(F[i]):
			f[file] = F[i]
		i += 1	
	
	i = 0

	Textfont = font.Font(family='Times New Roman', size=12, weight='normal', slant='roman')

	self.txt = tk.Text(fen, width = 60, wrap=tk.WORD, font=Textfont)
	self.Lbx=tk.Listbox(fen, activestyle='none',selectforeground='white',highlightthickness=0,\
				selectmode=tk.SINGLE, height=30,exportselection =0,selectbackground='light grey')
	self.E = tk.Entry(self, width = 12)
	self.alert = tk.Message(self, aspect=300, justify=tk.RIGHT)

	# Insertion des dossiers dans la listbox
	while i < len(F):
		self.Lbx.insert(tk.END,F[i])
		self.Lbx.itemconfig(tk.END, foreground="blue")
		i += 1
	# Grid Zone
	self.E.grid(row=0,column=0,sticky=tk.N+tk.W)
	self.Lbx.grid(row=1, column=0, columnspan = 4, sticky=tk.N+tk.S+tk.W+tk.E)
	self.txt.grid(row=0, column=4,columnspan=3, rowspan=2,sticky=tk.N+tk.S)

	
	def __init__(self, master=None):
		Tk.Frame.__init__(self, master)
		self.grid(sticky=N+S+E+W)
		self.createWidgets()

	def clear_info():
		self.alert.grid_forget()

	# Récupère l'indice de Lbx
	def wich_file(event):
		pos = self.Lbx.curselection()
		pose = int(pos[0])
		file = self.Lbx.get(pose)
		pose += 1

		# Si c'est un fichier .txt
		if file.find('.txt') != -1:
			for item, key in f.items(): # On cherche dans le dictionnaire
				if item == file:
					fold = key 	# On obtient le folder
					self.E.delete(0, last= tk.END) # Clear l'entry
					self.E.insert(0, file) 	# Afiche le fichier sélectionné
					open_file(folder=fold, file = file)	
		# Sinon
		else:
			next_file = self.Lbx.get(pose)	# Ligne suivant
			if next_file.find('.txt') == -1:	# Si la ligne suivante n'est pas un .txt
				for fichier in os.listdir(file):	# On cherche les fichier dedans
					self.Lbx.insert(pose, fichier)# On les insert sous le fold dans Lbx
					self.Lbx.itemconfig(pose, foreground='orange')
					pose += 1 # On passe à la ligne suivante
			
			# Si la ligne suivante est un fichier
			elif next_file.find('.txt') != -1:
				for fichier in os.listdir(file):	# On cherche les fichier dedans
					self.Lbx.delete(pose)# On les insert sous le fold dans Lbx

			
			fold = file
			file += '.txt'
			self.E.delete(0, last= tk.END)
			self.E.insert(0, file)
			open_file(folder=fold, file = file)

	# Ouvre et affiche le texte en rapport à Lbx
	def open_file(folder,file):
		clear_info()
		if file.find('.txt') != -1:
			fichier = folder+'\\'+str(file)
			ofi = io.open(fichier,encoding='utf-8',mode = 'r')
			text = ofi.read()
			self.txt.delete(0.0, index2= tk.END)
			self.txt.insert('insert',text)
			ofi.close()
		else:
			fichier = folder+'\\'+folder+'.txt'
			ofi = open(fichier,'r')
			text = ofi.read()
			self.txt.delete(0.0, index2= tk.END)
			self.txt.insert('insert',text)
			ofi.close()

	# Sauvegarde le text dans le fichier approprié
	def save_text(event):
		clear_info()
		pos = self.Lbx.curselection()
		try:
			pose = int(pos[0])
		except IndexError:
			pass
		fichier = self.Lbx.get(pose)	# Sélection Lbx
		
		# Si un fichier est sélectionné
		if fichier.find('.txt') != -1:
			for item, key in f.items():		# Recherche du dossier parent
				if item == fichier:
					fold = key 				# On récupère le dossier

			text = self.txt.get(0.0, index2=tk.END) # On récupère le texte
			fichier = fold+'\\'+str(fichier)		# Path
			ofi = io.open(fichier,encoding="utf-8", mode = "w+") # Ouverture fichier
			ofi.write(text)	# Modification
			ofi.close()

		# Si un dossier est sélectionné
		else :
			text = self.txt.get(0.0, index2=tk.END) # On récupère le texte
			fold = fichier 	# Le dossier à le même nom que le fichier
			fichierr = fold+'\\'+fichier+'.txt' # Path
			ofi = io.open(fichierr,encoding="utf-8", mode = "w+") # Ouverture fichier
			ofi.write(text) # Sauvegarde
			ofi.close()

		alertMsg = 'Sauvé'
		self.alert.config(text=alertMsg)
		self.alert.grid(row=1,column=6,sticky=tk.E+tk.N)

	# Créer un fichier.txt dans le dossier approprié
	def new_note():
		clear_info()
		if self.E.get() == '0/':		# Jamais marché ^^
			self.E.config(text='insert filename')
		else:
			fil = self.Lbx.curselection()
			pose = int(fil[0])
			LbxSelect = self.Lbx.get(pose) # Sélection Lbx

			# Si un fichier est sélectionné
			if LbxSelect.find('.txt') != -1:
				for item, key in f.items():	# Recherche du dossier parent
					if item == LbxSelect:
						fold = key 			# On récupère le dossier
						print(fold)
			else:
				fold = str(LbxSelect)

			Notename = self.E.get()			# Nom du nouveau fichier
			if Notename.find('.txt') == -1:	# Si le nom n'est pas en '.txt'
				Notename += '.txt'			# Ajoute le '.txt'
		
			self.E.delete(0, last=tk.END)	# Nettoie l'entrée

			path = fold +'\\'+ Notename		#Path
			ofi = io.open(path,encoding="utf-8",mode='w+') # Création du nouveau fichier
			pose += 1
			ofi.close()

			self.Lbx.insert(pose,Notename)	# Insertion du fichier dans la liste
			self.Lbx.itemconfig(pose, foreground='orange')
			open_file(folder = fold,file = Notename) #Lecture et affichage du fichier
		
			f[Notename] = fold				# Ajoute le fichier et le folder au dictionnaire
			File.append(Notename)			# Ajoute le fichier à la liste des fichiers

		alertMsg = 'NewNote'
		self.alert.config(text=alertMsg)
		self.alert.grid(row=1,column=6,sticky=tk.E+tk.N)

	# Supprime le dossier ou fichier sélectionne dans la Lbx
	def del_note():
		clear_info()
		file = self.E.get()		# Récupère l'entrée

		# Si l'entrée est un fichier
		if file.find('.txt') != -1:
			for item, key in f.items(): # On cherche son doffier parent
				if item == file:
					fold = key 			# On l'enregistre
		
		self.E.delete(0, last= tk.END) 	# Clear l'entrée
		path = fold+'\\'+file
		os.remove(path)					# SUppression du fichier
		pos = self.Lbx.curselection()	# Récupération de l'indice Lbx
		self.Lbx.delete(pos)			# Suppression de l'indice

		alertMsg = 'Supprimé'
		self.alert.config(text=alertMsg)
		self.alert.grid(row=1,column=6,sticky=tk.E+tk.N)

	# Créer un folder à la fin de la liste
	def add_folder():
		clear_info()
		path = self.E.get() # Récupère le nom du dossier

		# Si il n'existe pas de dossier du même nom
		if not os.path.exists(path): 
			os.makedirs(path)	# On en créer un
		
		self.Lbx.insert(tk.END, path)	# Ajoute le dossier en fin de Lbx
		self.Lbx.itemconfig(tk.END, foreground='blue') # Colore le dossier en bleu
		Notename = path+'.txt'
		chem = path+'\\'+Notename
		ofi = io.open(chem, encoding='utf-8', mode='w+') # Créer un subfolder du même nom
		ofi.close()

		f[path] = Notename # Ajoute le dossier au dico

		alertMsg = 'NewDoc'
		self.alert.config(text=alertMsg)
		self.alert.grid(row=2,column=7,sticky=tk.E+tk.N)



	# Binding List
	self.Lbx.bind("<<ListboxSelect>>", wich_file)
	self.txt.bind("<Control-KeyPress-s>", save_text)

	self.Fold_button_img = tk.PhotoImage(file='af.png')
	self.Addfold = tk.Button(self, image = self.Fold_button_img,command = add_folder, width="15", height="15")
	self.Addfold.grid(row=0, column=1, sticky=tk.N+tk.E)

	self.Note_Button_img = tk.PhotoImage(file='db.png')
	self.Nb = tk.Button(self, command = new_note, image = self.Note_Button_img, width="15", height="15")
	self.Nb.grid(row=0, column=2, sticky=tk.N+tk.E)

	self.Del_Note_img = tk.PhotoImage(file='dlt.png')
	self.Dlt = tk.Button(self, image = self.Del_Note_img,command = del_note, width="15", height="15")
	self.Dlt.grid(row=0, column=3, sticky=tk.N+tk.E)
'''
	# Text Modification
	def set_bold():
		self.txt.tag_add('Bold', tk.SEL_FIRST, tk.SEL_LAST)
		self.txt.tag_config('Bold', font=('Times New Roman',12,'bold'))

	def set_italic():
		self.txt.tag_add('Italic', tk.SEL_FIRST, tk.SEL_LAST)
		self.txt.tag_config('Italic', font=('Times New Roman',12,'normal','italic'))

	def set_underline():
		self.txt.tag_add('Underline', tk.SEL_FIRST, tk.SEL_LAST)
		self.txt.tag_config('Underline', font=('Times New Roman',12,'normal','roman','underline'))

	def set_default():
		self.txt.tag_add('Default', tk.SEL_FIRST, tk.SEL_LAST)
		self.txt.tag_config('Default', font=('Times New Roman',12,'normal','roman'))
	
	self.bold_Button_img = tk.PhotoImage(file='G.png')
	self.bold_Button = tk.Button(self, image = self.bold_Button_img, command=set_bold, width="15", height="15")
	self.bold_Button.grid(row=0, column=4,padx=20, sticky=tk.W+tk.N+tk.S)

	self.italic_Button_img = tk.PhotoImage(file='I.png')
	self.italic_Button = tk.Button(self, image = self.italic_Button_img, command=set_italic, width="15", height="15")
	self.italic_Button.grid(row=0, column=4,padx=40, sticky=tk.W+tk.N+tk.S)	

	self.underline_Button_img = tk.PhotoImage(file='U.png')
	self.underline_Button = tk.Button(self, image = self.underline_Button_img, command=set_underline, width="15", height="15")
	self.underline_Button.grid(row=0, column=4,padx=60, sticky=tk.W+tk.N+tk.S)	

	self.default_Button_img = tk.PhotoImage(file='D.png')
	self.default_Button = tk.Button(self, image = self.default_Button_img, command=set_default, width="15", height="15")
	self.default_Button.grid(row=0, column=4,padx=80, sticky=tk.W+tk.N+tk.S)		
'''	
if __name__ == "__main__":

	fen = tk.Tk()
	fen.title('Bloc Note')
	fen.resizable(False, False)

	x = fen.winfo_pointerx()
	y = fen.winfo_pointery()

	createWidgets(fen)
	




	fen.mainloop()