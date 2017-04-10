#!/usr/bin/python
# -*- coding: utf-8 -*-

"""============================================================
This file is licensed under the "GNU General Public License v3.0"
And is provided by;
"Allison Marie Bennett", TheCyaniteProject@gmail.com
============================================================"""

"""============================================================
This File is for the 'ShhhhMail.com' website
============================================================"""

"""========================= Imports ======================="""
from tkinter import *
from tkinter import ttk
"""========================================================="""

def web_site(web_page):
	for widget in web_page.winfo_children():
		widget.destroy()
	Label(web_page, text='ShhhhMail.net - Keep it down, with the #1 Rated Anonymous Email Cliant\nShhhhMail is not yet implimented.', bg='white', font=('Courier', 10)).pack(expand=True)
