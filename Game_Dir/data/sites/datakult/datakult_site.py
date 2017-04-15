#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""============================================================
This file is licensed under the "GNU General Public License v3.0"
And is provided by;
"Allison Marie Bennett", TheCyaniteProject@gmail.com
============================================================"""

"""============================================================
This File is for the 'DataKult.com' website
============================================================"""

"""========================= Imports ======================="""
import os
from tkinter import *
from tkinter import ttk
import data.settings as settings
import data.apps as apps
import data.wallet as wallet
reload(apps)
reload(wallet)
"""========================================================="""

def check_flag(flag, name, buy_frame, buy_framem):
	if flag == 'fileAlreadyExists':
		buy_frame.destroy()
		buy_frame = LabelFrame(buy_framem, bg='black', fg='purple')
		buy_frame.pack(pady=50)
		Label(buy_frame, text=name, bg='black', fg='purple').pack(anchor=N, side=TOP)
		Label(buy_frame, text='You already own this file\n(or one with the same name)', bg='black', fg='purple').pack(anchor=N, side=TOP)
		Button(buy_frame, text='Done', bg='purple', fg='black', command=buy_framem.destroy).pack(anchor=S, side=RIGHT)
		return
	elif flag == 'fileNotFound':
		buy_frame.destroy()
		buy_frame = LabelFrame(buy_framem, bg='black', fg='purple')
		buy_frame.pack(pady=50)
		Label(buy_frame, text=name, bg='black', fg='purple').pack(anchor=N, side=TOP)
		Label(buy_frame, text='SYSTEM ERROR: fileNotFound\nPlease contact the developer.\nhttp://twitter.com/exit_code_dev', bg='black', fg='purple').pack(anchor=N, side=TOP)
		Button(buy_frame, text='Done', bg='purple', fg='black', command=buy_framem.destroy).pack(anchor=S, side=RIGHT)
		return
	else:
		buy_frame.destroy()
		buy_frame = LabelFrame(buy_framem, bg='black', fg='purple')
		buy_frame.pack(pady=50)
		Label(buy_frame, text=name, bg='black', fg='purple').pack(anchor=N, side=TOP)
		Label(buy_frame, text='SYSTEM ERROR: unknownError\nPlease contact the developer.\nhttp://twitter.com/exit_code_dev', bg='black', fg='purple').pack(anchor=N, side=TOP)
		Button(buy_frame, text='Done', bg='purple', fg='black', command=buy_framem.destroy).pack(anchor=S, side=RIGHT)
		return

def web_site(web_page):
	for widget in web_page.winfo_children():
		widget.destroy()
	page_frame = Frame(web_page, bg='black')
	page_frame.pack(fill=BOTH, expand=True)
	page_frame.pack_propagate(0)
	main_page = LabelFrame(page_frame, bg='purple')
	main_page.pack(anchor=W, side=BOTTOM, fill=BOTH, expand=True)
	Label(page_frame, text='{DataKult}', bg='black', fg='purple', font=('Courier', 16)).pack(anchor=W, side=LEFT, fill=Y, expand=False)
	product_list = LabelFrame(main_page, bg='purple')
	product_list.pack(anchor=S, side=BOTTOM, fill=BOTH, expand=True)
	Label(main_page, text='', bg='purple', font=('Courier', 10)).pack(anchor=S, side=BOTTOM, fill=X, expand=False)
	Label(main_page, text='Name | Discription | $/B', bg='black', fg='purple', font=('Courier', 10)).pack(anchor=S, side=LEFT, fill=X, expand=False)
	Label(main_page, text='', bg='black', font=('Courier', 10)).pack(anchor=S, side=RIGHT, fill=X, expand=True)
	if not os.path.exists('%s..\\sites\\datakult\\software\\' % (settings.user_dir)):
		print 'locationError: %s..\\sites\\datakult\\software\\' % (settings.user_dir)
		return 'locationError: %s..\\sites\\datakult\\software\\' % (settings.user_dir)
	line_mode = True
	for file in os.listdir('%s..\\sites\\datakult\\software\\' % (settings.user_dir)):
		if not file.endswith('.ini'):
			continue
		def make_listing(file):
			with open('%s..\\sites\\datakult\\software\\%s' % (settings.user_dir, file)) as f:
				file_name = None
				file_easybits = None
				file_payme = None
				file_summary = None
				file_desc = None
				for line in f.readlines():
					if 'name=' in line:
						file_name = line.split('name=', 1)[1].strip().rstrip()
					elif 'easybits=' in line:
						file_easybits = line.split('easybits=', 1)[1].strip().rstrip()
						if not file_easybits in ['None','none','']:
							file_easybits = float(file_easybits)
						else: file_easybits = None
					elif 'payme=' in line:
						file_payme = line.split('payme=', 1)[1].strip().rstrip()
						if not file_payme in ['None','none','']:
							file_payme = float(file_payme)
						else: file_payme = None
					elif 'summary=' in line:
						file_summary = line.split('summary=', 1)[1].strip().rstrip()
					elif 'file=' in line:
						file_file = line.split('file=', 1)[1].strip().rstrip()
					elif 'desc=' in line:
						file_desc = line.split('desc=', 1)[1].strip().rstrip()
			buy_easybits = False
			buy_payme = False
			free_downl = False
			if not file_payme == None:
				if not file_easybits == None:
					buy_easybits = True
					buy_payme = True
					price = '$%s / %sB' % (file_payme,file_easybits)
				else:
					buy_payme = True
					price = '$%s' % (file_payme)
			elif not file_easybits == None:
				buy_easybits = True
				price = '%sB' % (file_easybits)
			else:
				free_downl = True
				price = 'FREE'

			def buyeb_click(name,price,file):
				def do_buy(buy_frame, name, buy_framem):
					if wallet.check('easybits', settings.easybits_ac, price) == False:
						buy_frame.destroy()
						buy_frame = LabelFrame(buy_framem, bg='black', fg='purple')
						buy_frame.pack(pady=50)
						Label(buy_frame, text=name, bg='black', fg='purple').pack(anchor=N, side=TOP)
						Label(buy_frame, text='Insufficient Funds', bg='black', fg='purple').pack(anchor=N, side=TOP)
						Button(buy_frame, text='Done', bg='purple', fg='black', command=buy_framem.destroy).pack(anchor=S, side=RIGHT)
					else: flag = apps.getfile(file)
					if flag == True:
						wallet.remove('easybits', settings.easybits_ac, price)
						buy_frame.destroy()
						buy_frame = LabelFrame(buy_framem, bg='black', fg='purple')
						buy_frame.pack(pady=50)
						Label(buy_frame, text=name, bg='black', fg='purple').pack(anchor=N, side=TOP)
						Label(buy_frame, text='File Downloaded.', bg='black', fg='purple').pack(anchor=N, side=TOP)
						Button(buy_frame, text='Done', bg='purple', fg='black', command=buy_framem.destroy).pack(anchor=S, side=RIGHT)
						return
					else: check_flag(flag, name, buy_frame, buy_framem)


				buy_framem = LabelFrame(product_list, fg='black', bg='purple', height=3000, width=3000)
				buy_framem.place(anchor=N, relx=.5, rely=0)
				buy_framem.pack_propagate(0)
				buy_frame = LabelFrame(buy_framem, bg='black', fg='purple')
				buy_frame.pack(pady=50)
				Label(buy_frame, text=name, bg='black', fg='purple').pack(anchor=N, side=TOP)
				Label(buy_frame, text='Are you sure you want to buy\n%s for %sB?' % (name,price), bg='black', fg='purple').pack(anchor=N, side=TOP)
				Button(buy_frame, text='Buy', bg='purple', fg='black', command=lambda:do_buy(buy_frame, name, buy_framem)).pack(anchor=S, side=LEFT)
				Button(buy_frame, text='Cancel', bg='purple', fg='black', command=buy_framem.destroy).pack(anchor=S, side=RIGHT)


			def buypm_click(name,price,file):
				def do_buy(buy_frame, name, buy_framem):
					if wallet.check('payme', settings.payme_ac, price) == False:
						buy_frame.destroy()
						buy_frame = LabelFrame(buy_framem, bg='black', fg='purple')
						buy_frame.pack(pady=50)
						Label(buy_frame, text=name, bg='black', fg='purple').pack(anchor=N, side=TOP)
						Label(buy_frame, text='Insufficient Funds', bg='black', fg='purple').pack(anchor=N, side=TOP)
						Button(buy_frame, text='Done', bg='purple', fg='black', command=buy_framem.destroy).pack(anchor=S, side=RIGHT)
					else: flag = apps.getfile(file)
					if flag == True:
						wallet.remove('payme', settings.payme_ac, price)
						buy_frame.destroy()
						buy_frame = LabelFrame(buy_framem, bg='black', fg='purple')
						buy_frame.pack(pady=50)
						Label(buy_frame, text=name, bg='black', fg='purple').pack(anchor=N, side=TOP)
						Label(buy_frame, text='File Downloaded.', bg='black', fg='purple').pack(anchor=N, side=TOP)
						Button(buy_frame, text='Done', bg='purple', fg='black', command=buy_framem.destroy).pack(anchor=S, side=RIGHT)
						return
					else: check_flag(flag, name, buy_frame, buy_framem)

				buy_framem = LabelFrame(product_list, fg='black', bg='purple', height=3000, width=3000)
				buy_framem.place(anchor=N, relx=.5, rely=0)
				buy_framem.pack_propagate(0)
				buy_frame = LabelFrame(buy_framem, bg='black', fg='purple')
				buy_frame.pack(pady=50)
				Label(buy_frame, text=name, bg='black', fg='purple').pack(anchor=N, side=TOP)
				Label(buy_frame, text='Are you sure you want to buy\n%s for $%s?' % (name,price), bg='black', fg='purple').pack(anchor=N, side=TOP)
				Button(buy_frame, text='Buy', bg='purple', fg='black', command=lambda:do_buy(buy_frame, name, buy_framem)).pack(anchor=S, side=LEFT)
				Button(buy_frame, text='Cancel', bg='purple', fg='black', command=buy_framem.destroy).pack(anchor=S, side=RIGHT)

			def buyfree_click(name, file):
				def do_buy(buy_frame, name, buy_framem):
					flag = apps.getfile(file)
					if flag == True:
						buy_frame.destroy()
						buy_frame = LabelFrame(buy_framem, bg='black', fg='purple')
						buy_frame.pack(pady=50)
						Label(buy_frame, text=name, bg='black', fg='purple').pack(anchor=N, side=TOP)
						Label(buy_frame, text='File Downloaded.', bg='black', fg='purple').pack(anchor=N, side=TOP)
						Button(buy_frame, text='Done', bg='purple', fg='black', command=buy_framem.destroy).pack(anchor=S, side=RIGHT)
						return
					else: check_flag(flag, name, buy_frame, buy_framem)
				buy_framem = LabelFrame(product_list, fg='black', bg='purple', height=3000, width=3000)
				buy_framem.place(anchor=N, relx=.5, rely=0)
				buy_framem.pack_propagate(0)
				buy_frame = LabelFrame(buy_framem, bg='black', fg='purple')
				buy_frame.pack(pady=50)
				Label(buy_frame, text=name, bg='black', fg='purple').pack(anchor=N, side=TOP)
				Label(buy_frame, text='Are you sure you want to download\n%s?' % (name), bg='black', fg='purple').pack(anchor=N, side=TOP)
				Button(buy_frame, text='Download', bg='purple', fg='black', command=lambda:do_buy(buy_frame, name, buy_framem)).pack(anchor=S, side=LEFT)
				Button(buy_frame, text='Cancel', bg='purple', fg='black', command=buy_framem.destroy).pack(anchor=S, side=RIGHT)

			def more_click(name,desc,price):
				buy_framem = LabelFrame(product_list, fg='black', bg='purple', height=3000, width=3000)
				buy_framem.place(anchor=N, relx=.5, rely=0)
				buy_framem.pack_propagate(0)
				buy_frame = LabelFrame(buy_framem, bg='black', fg='purple')
				buy_frame.pack(pady=50)
				Label(buy_frame, text=name, bg='black', fg='purple').pack(anchor=N, side=TOP)
				Label(buy_frame, text=desc, bg='black', fg='purple').pack(anchor=N, side=TOP)
				Label(buy_frame, text=price, bg='black', fg='purple').pack(anchor=N, side=TOP)
				Button(buy_frame, text='Close', bg='purple', fg='black', command=buy_framem.destroy).pack(anchor=S, side=RIGHT)

			if line_mode == True:
				background = 'black'
				foreground = 'purple'
			else:
				background = 'purple'
				foreground = 'black'

			product_frame = Frame(product_list, bg=background)
			product_frame.pack(anchor=N, side=TOP, fill=X, expand=False)
			Label(product_frame, text='%s | %s |' % (file_name,file_summary), bg=background, fg=foreground, font=('Courier', 10)).pack(side=LEFT, expand=False)
			Button(product_frame, text='Read More', fg=foreground, bg=background, command=lambda: more_click(file_name,file_desc,price)).pack(padx=10,side=LEFT, expand=False)
			if buy_easybits == True:
				Button(product_frame, text='Buy for %sB' % file_easybits, fg=foreground, bg=background, command=lambda: buyeb_click(file_name,file_easybits,file_file)).pack(padx=1,side=RIGHT, expand=False)
			if buy_payme == True:
				Button(product_frame, text='Buy for $%s' % file_payme, fg=foreground, bg=background, command=lambda: buypm_click(file_name,file_payme,file_file)).pack(padx=1,side=RIGHT, expand=False)
			if free_downl == True:
				Button(product_frame, text='Free Download', fg=foreground, bg=background, command=lambda: buyfree_click(file_name,file_file)).pack(padx=1,side=RIGHT, expand=False)
		make_listing(file)
		if line_mode == True:
			line_mode = False
		else:
			line_mode = True



