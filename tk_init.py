#coding:utf-8

import tkinter as tk
import tk_listbox as Lbx

app = tk.Tk()

Background = tk.Frame(app)

Listbox = tk.Listbox(Background)

Text = tk.Text(Background, width = 60, wrap=tk.WORD)

Background.grid(row=0,column=0)
Listbox.grid(row=0, column=0, sticky='NSEW')
Text.grid(row=0,column=1, sticky='NSEW')

Listbox.bind('<<ListboxSelect>>',Lbx.Listbox_click)