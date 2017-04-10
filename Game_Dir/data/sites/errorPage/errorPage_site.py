#!/usr/bin/python
# -*- coding: utf-8 -*-

"""============================================================
This file is licensed under the "GNU General Public License v3.0"
And is provided by;
"Allison Marie Bennett", TheCyaniteProject@gmail.com
============================================================"""

"""============================================================
This File is for the browser errorPage
============================================================"""

"""========================= Imports ======================="""
from tkinter import *
from tkinter import ttk
import data.settings as settings
"""========================================================="""

def web_site(web_page, go_from):
	for widget in web_page.winfo_children():
		widget.destroy()
	main = Frame(web_page, bg='white')
	main.place(anchor=S, relx=.5, rely=.5)
	Label(main, text='404! :\'(', bg='white', font=(None, 60)).pack(pady=10)
	Label(main, text='Sorry, it looks like the page you requested does not exist.', bg='white', font=(None, 13)).pack()
	Label(main, text='Please check that the URL is correct and try again.', bg='white', font=(None, 10)).pack()
