#coding:utf-8

import tkinter as tk
import tk_listbox as Lbx
import tk_text as tkt
from threading import Timer

app = tk.Tk()

Background = tk.Frame(app)

Listbox = tk.Listbox(Background)

Text = tk.Text(Background, width = 60, wrap=tk.WORD)

Alert = tk.Message(Background, width=200, bg='white', text="", justify=tk.LEFT)

Background.grid(row=0,column=0)
Listbox.grid(row=0, column=0, sticky='NSEW')
Text.grid(row=0,column=1, sticky='NSEW')

Listbox.bind('<<ListboxSelect>>',Lbx.Listbox_click)
Listbox.bind("<Button-3>", Lbx.do_pop_menu)
Text.bind("<Control-KeyPress-s>", tkt.save_text)
app.bind("<Control-KeyPress-w>", lambda command:app.quit())

pop_menu = tk.Menu(app,tearoff=0)
pop_menu.add_command(label = 'Add File')
pop_menu.add_command(label='Delete')

def pop_alert(text):
	Alert.config(text=text)
	Alert.grid(row=0, column=1, sticky='SW')
	wait = Timer(2, Alert.grid_remove)
	wait.start()
		
