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

"""========================================================="""


def web_site(web_page):
    for widget in web_page.winfo_children():
        widget.destroy()
    Label(web_page, text='''RiddleMe.org - Protect yourself from hackers and spammers\nwith the added security of RiddleMe: WebCapcha.
\nSometimes Anti-Hack Suites are not enough to keep out malicious abusers.\n\nWith RiddleMe,\t\t\t\t\t\t
You can safely block out malicious scripts and automations with a single click.
\nRiddleMe.org is not yet implimented.''', bg='white', font=(None, 10)).pack(expand=True)
