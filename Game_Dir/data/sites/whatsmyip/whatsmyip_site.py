#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""============================================================
This file is licensed under the "GNU General Public License v3.0"
And is provided by;
"Allison Marie Bennett", TheCyaniteProject@gmail.com
============================================================"""

"""============================================================
This File is for the 'whatsmyip.com' website
============================================================"""

"""========================= Imports ======================="""
from tkinter import *
from tkinter import ttk
import data.settings as settings
"""========================================================="""

def web_site(web_page):
	for widget in web_page.winfo_children():
		widget.destroy()
	web_page = Frame(web_page)
	web_page.pack(fill=BOTH, expand=True)
	logoframe = LabelFrame(web_page, bg='red', height=100)
	logoframe.pack(anchor=N, fill=X)
	Label(logoframe, text='WhatsMyIP', bg='red', font=(None, 24)).place(anchor=W, rely=.5, relx=0)
	Label(web_page, text='\n', font=(None, 15)).pack(anchor=N, fill=X)
	Label(web_page, text='Your IP Address is:', font=(None, 15)).pack(anchor=N, fill=X)
	test = Entry(web_page, relief=FLAT, bg='lightgrey', justify=CENTER, font=(None, 30))
	test.pack(anchor=N, fill=X)
	test.insert(0, settings.current_ip)
	test.configure(state='readonly')
