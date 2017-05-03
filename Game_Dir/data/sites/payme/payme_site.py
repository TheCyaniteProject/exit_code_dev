#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""============================================================
This file is licensed under the "GNU General Public License v3.0"
And is provided by;
"Allison Marie Bennett", TheCyaniteProject@gmail.com
============================================================"""

"""============================================================
This File is for the 'Payme.net' website
============================================================"""

"""========================= Imports ======================="""
from Tkinter import *
import data.settings as settings
import data.wallet as wallet
reload(wallet)
"""========================================================="""

def web_site(web_page, go_from):
	for widget in web_page.winfo_children():
		widget.destroy()
	#Label(web_page, text='Payme.net - Get Paid.\nYour Payme Balance: $%s' % payme, bg='white', font=(None, 10)).pack(expand=True)
	web_page = Frame(web_page)
	web_page.pack(fill=BOTH, expand=True)
	global sitelocker
	global riddleme
	sitelocker=None
	riddleme=None
	with open('%s%s\\sites\\payme\\site.ini' % (settings.user_dir,settings.username), 'r') as site_settings:
		for line in site_settings.readlines():
			if 'sitelocker' in line:
				sitelocker = float(line.split('=')[1])
			elif 'riddleme' in line:
				riddleme = line.split('=')[1]
	def payme_doLogin():
		global payme_account
		payme_user.configure(bg='white')
		payme_pass.configure(bg='white')
		user = payme_user.get()
		user = user.strip().rstrip()
		passw = payme_pass.get()
		if user.strip().rstrip() == '':
			payme_user.configure(bg='pink')
			return
		if 'payme.net' in settings.login_creds[settings.username.lower()]:
			if settings.login_creds[settings.username.lower()]['payme.net'][0] == True:
				if user.lower() == settings.login_creds[settings.username.lower()]['payme.net'][1].lower():
					payme_account = settings.login_creds[settings.username.lower()]['payme.net'][1]
					print '\n%s\nUser %s logged into payme.net @ %s' % (settings.get_time(),settings.username,payme_account)
					payme_logOn()
					return
		if passw == 'thecheatpass':
			payme_account = user
			print '\n%s\nUser %s logged into payme.net @ %s' % (settings.get_time(),settings.username,payme_account)
			payme_logOn()
			return
		#else:
		flag = wallet.password('payme', user, passw)
		payme_account = user
		if flag == 'to_notExist':
			payme_user.configure(bg='pink')
			return
		elif flag == False:
			payme_pass.configure(bg='pink')
			return
		elif flag == True:
			flag = wallet.verify('payme', user, settings.current_ip)
			if flag == False:
				print '\n%s\nUser %s was denied access to payme.net @ %s\nReason: Your IP is blacklisted for this account.' % (settings.get_time(),settings.username,payme_account)
				return
			elif flag == None:
				wallet.alert('payme', user, settings.current_ip)
				print '\n%s\nUser %s was denied access to payme.net @ %s\nReason: You are not whitelisted.' % (settings.get_time(),settings.username,payme_account)
				return
			print '\n%s\nUser %s logged into payme.net @ %s' % (settings.get_time(),settings.username,payme_account)
			payme_logOn()
		else: raise Exception('unexpectedReturnValue')
	payme_page = LabelFrame(web_page)
	payme_page.pack(anchor=W, side=BOTTOM, fill=BOTH, expand=True)
	Label(web_page, text='Payme.net - Get Paid.', bg='green', font=(None, 10)).pack(anchor=W, side=LEFT, fill=Y, expand=False)

	def add_payme_autofill():
		global autofill_TF
		autofill_TF = False
		make_users = {}
		def autofill(event):
			payme_user.delete(0, END)
			payme_user.insert(0, make_users[usern])
			payme_pass.delete(0, END)
			payme_pass.insert(0, '**********')
		for usern in settings.login_creds:
			for site in settings.login_creds[usern]:
				if site == 'payme.net':
					if settings.login_creds[usern][site][0] == True:
						autofill_TF = True
						make_users[usern]=settings.login_creds[usern][site][1]
		if autofill_TF == False:
			return
		Label(payme_autofill, text='Browser Autofill: ', bg='white').pack()
		for usern in make_users:
			new_autofill = Label(payme_autofill, text=('[%s]' % (make_users[usern])), fg='blue', cursor='hand2', bg='white')
			new_autofill.pack(padx=3)
			new_autofill.bind('<Button-1>', autofill)
	def payme_main():
		def return_next(event):
			payme_pass.focus_set()
		global payme_autofill
		global payme_user
		global payme_pass
		for widget in payme_page.winfo_children():
			widget.destroy()
		payme_logout_button.pack_forget()
		logoframe = LabelFrame(payme_page, bg='green', height=100)
		logoframe.pack(anchor=N, fill=X)
		Label(logoframe, text='Payme.net', bg='green', font=(None, 20)).place(anchor=CENTER, rely=.5, relx=.5)
		payme_login = LabelFrame(payme_page)
		payme_login.pack(anchor=N, pady=10)
		payme_user_frame = LabelFrame(payme_login, text='Account ID')
		payme_user_frame.pack(padx=5, pady=2, anchor=N)
		payme_user = Entry(payme_user_frame, width=40)
		payme_user.pack()
		payme_pass_frame = LabelFrame(payme_login, text='Password')
		payme_pass_frame.pack(padx=5, anchor=S, side=LEFT)
		payme_pass = Entry(payme_pass_frame, width=30)
		payme_pass.pack()
		Button(payme_login, text=' Login ', bg='white', cursor='hand2', command=payme_doLogin).pack(padx=6, pady=5, anchor=S, side=RIGHT)
		payme_autofill = LabelFrame(payme_page, bg='white')
		payme_autofill.pack(anchor=N)
		add_payme_autofill()
		if not sitelocker == None:
			global sitelocker_label
			def go_sitelocker(event):
				go_from('www.sitelocker.org')
			sitelocker_label = Label(payme_page, text='SiteLocker v%s Secured' % str(sitelocker), fg='blue', cursor='hand2')
			sitelocker_label.pack(anchor=SW, side=LEFT)
			sitelocker_label.bind('<Button-1>', go_sitelocker)
		if not riddleme == None:
			global riddleme_label
			def go_riddleme(event):
				go_from('www.riddleme.org')
			riddleme_label = Label(payme_page, text='RiddleMe On', fg='blue', cursor='hand2')
			riddleme_label.pack(anchor=SE, side=RIGHT)
			riddleme_label.bind('<Button-1>', go_riddleme)
	def payme_doLogout():
		go_from('http://www.payme.net')
	payme_logout_button = Button(web_page, text=' Logout ', bg='green', relief=FLAT, cursor='hand2', command=payme_doLogout)
	payme_logout_button.pack(anchor=W, side=RIGHT)
	payme_main()
	def payme_logOn():
		for widget in payme_page.winfo_children():
			widget.destroy()
		payme_logout_button.pack(anchor=W, side=RIGHT)
		LabelFrame(payme_page, text='History', width=200).pack(anchor=E, side=RIGHT, fill=Y, expand=False)
		actions_frame = LabelFrame(payme_page, text='Actions', height=150)
		actions_frame.pack(anchor=W, side=BOTTOM, fill=X, expand=False)
		actions_frame.pack_propagate(0)
		account_frame = LabelFrame(payme_page, text='Account')
		account_frame.pack(anchor=W, side=LEFT, fill=BOTH, expand=True)
		Label(account_frame, text='Account: %s' % (payme_account), fg='darkgreen', font=(None, 15)).pack(padx=20, pady=10, anchor=NW)
		amount_label = Label(account_frame, text='Balance: $%s' % (wallet.check('payme', payme_account)), fg='darkgreen', font=(None, 15))
		amount_label.pack(padx=20, pady=10, anchor=NW)
		def bal_refresh():
			amount_label.configure(text='Balance: $%s' % (wallet.check('payme', payme_account)))
		Button(account_frame, text='Refresh', command=bal_refresh).pack(padx=20, pady=5, anchor=NW)
		global frame_open
		frame_open = False
		def send_payme():
			global frame_open
			if not frame_open == False:
				return
			frame_open = True
			frame0 = LabelFrame(payme_page, width=250, height=120, bg='green')
			frame0.place(anchor=CENTER, relx=.5, rely=.5)
			frame0.pack_propagate(0)
			frame = LabelFrame(frame0, text='Send Currency')
			frame.pack(side=TOP, fill=BOTH, expand=True)
			ac_frame = LabelFrame(frame, text='Account')
			ac_frame.pack(padx=5, pady=2, anchor=W, side=TOP, fill=X)
			ac_entry = Entry(ac_frame)
			ac_entry.pack(pady=2, fill=X)

			am_frame = LabelFrame(frame, text='Amount')
			am_frame.pack(padx=5, pady=2, anchor=W, side=LEFT)
			am_entry = Entry(am_frame, width=10)
			Label(am_frame, text='$').pack(pady=2, fill=X, side=LEFT)
			am_entry.pack(pady=2, fill=X, side=RIGHT)
			def send():
				amount = float(am_entry.get().strip().rstrip())
				flag = wallet.check('payme', payme_account, amount=amount)
				if flag == True:
					flag = wallet.give('payme', ac_entry.get().strip().rstrip(), payme_account, amount)
					if flag == 'to_notExist':
						ac_entry.configure(bg='pink')
						return
					else:
						ac_entry.configure(bg='white')
					bal_refresh()
					close()
				else: print False
			def close():
				global frame_open
				frame_open = False
				frame0.destroy()
			Button(frame, text='Cancel', command=close).pack(padx=5, pady=2, anchor=W, side=RIGHT)
			Button(frame, text='Send', command=send).pack(padx=5, pady=2, anchor=W, side=RIGHT)
		Button(actions_frame, text='Send Currency', command=send_payme).pack(padx=20, side=LEFT)






