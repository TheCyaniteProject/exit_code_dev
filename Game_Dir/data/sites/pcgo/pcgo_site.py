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
from Tkinter import *
import data.settings as settings
"""========================================================="""

def web_site(web_page):
	for widget in web_page.winfo_children():
		widget.destroy()
	Label(web_page, text='PCGo.shop - Buy quality computer parts online\nPCGo.shop is not yet implimented.', bg='white', font=(None, 10)).pack(expand=True)
	Label(web_page, text='PCGo will be a website for upgrading your computer, allowing for faster, and more powerful hacks.', bg='white', font=(None, 10)).pack(expand=True)

