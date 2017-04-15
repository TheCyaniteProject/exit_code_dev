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
	Label(web_page, text='''SiteLocker.org - The most trusted\nWebsite Security Suite for 5 Years Straight.
Majoring in Hack Prevention, and Anti-Exploit Technologies.\n\nSiteLocker.org is not yet implimented.''', bg='white', font=(None, 10)).pack(expand=True)
