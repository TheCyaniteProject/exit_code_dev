#!/usr/bin/env python
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
	def add_bookmark(name, url):
		def link_click(event):
			go_from(url)
		bookmark = Label(bookmarks, text=name, fg='blue', bg='white', cursor='hand2')
		bookmark.pack(anchor=W, side=LEFT)
		bookmark.bind('<Button-1>', link_click)
	text = 'The Web Browser is not fully implimented, and only has a few sites(see Bookmarks)\nWhatever you do; don\'t look for secrets. ;3'
	Label(web_page, text=text, bg='white', font=(None, 10)).pack(anchor=S, fill=BOTH, expand=True, side=BOTTOM)
	bookmarks = LabelFrame(web_page, bg='white')
	bookmarks.pack(anchor=N, fill=X, expand=False, side=TOP)
	Label(bookmarks, text='Bookmarks:', bg='white').pack(anchor=W, side=LEFT)

	# Bookmarks
	add_bookmark('Email.com', 'www.email.com')
	add_bookmark('ShhMail.net', 'www.shhmail.net')
	add_bookmark('PayMe.net', 'www.payme.net')
	add_bookmark('easyBits.com', 'www.easybits.com')
	add_bookmark('DataKult.shop', 'www.datakult.shop')
	add_bookmark('PCGo.shop', 'www.pcgo.shop')
	add_bookmark('whatsmyip.com', 'www.whatsmyip.com')
