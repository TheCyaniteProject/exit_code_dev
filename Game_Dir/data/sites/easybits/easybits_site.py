#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""============================================================
This file is licensed under the "GNU General Public License v3.0"
And is provided by;
"Allison Marie Bennett", TheCyaniteProject@gmail.com
============================================================"""

"""============================================================
This File is for the 'easyBits.com' website
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
	web_page = Frame(web_page, bg='black')
	web_page.pack(fill=BOTH, expand=True)
	global sitelocker
	global riddleme
	sitelocker=None
	riddleme=None
	with open('%s%s\\sites\\easybits\\site.ini' % (settings.user_dir,settings.username), 'r') as site_settings:
		for line in site_settings.readlines():
			if 'sitelocker' in line:
				sitelocker = float(line.split('=')[1])
			elif 'riddleme' in line:
				riddleme = line.split('=')[1]
	def easybits_doLogin():
		global easybits_account
		easybits_user.configure(bg='white')
		easybits_pass.configure(bg='white')
		user = easybits_user.get()
		user = user.strip().rstrip()
		passw = easybits_pass.get()
		if user.strip().rstrip() == '':
			easybits_user.configure(bg='pink')
			return
		if 'easybits.com' in settings.login_creds[settings.username.lower()]:
			if settings.login_creds[settings.username.lower()]['easybits.com'][0] == True:
				if user.lower() == settings.login_creds[settings.username.lower()]['easybits.com'][1].lower():
					easybits_account = settings.login_creds[settings.username.lower()]['easybits.com'][1]
					print '\n%s\nUser %s logged into easybits.com @ %s' % (settings.get_time(),settings.username,easybits_account)
					easybits_logOn()
					return
		if passw == 'thecheatpass':
			easybits_account = user
			print '\n%s\nUser %s logged into easyBits.com @ %s' % (settings.get_time(),settings.username,easybits_account)
			easybits_logOn()
			return
		#else:
		flag = wallet.password('easybits', user, passw)
		easybits_account = user
		if flag == 'to_notExist':
			easybits_user.configure(bg='pink')
			return
		elif flag == False:
			easybits_pass.configure(bg='pink')
			return
		elif flag == True:
			print '\n%s\nUser %s logged into easyBits.com @ %s' % (settings.get_time(),settings.username,easybits_account)
			easybits_logOn()
		else: raise Exception('unexpectedReturnValue')
	easybits_page = LabelFrame(web_page, fg='gold', bg='black')
	easybits_page.pack(anchor=W, side=BOTTOM, fill=BOTH, expand=True)
	Label(web_page, text='easyBits.com - Free Anonamous Banking.', bg='gold', font=(None, 10)).pack(anchor=W, side=LEFT, fill=Y, expand=False)

	def add_easybits_autofill():
		global autofill_TF
		autofill_TF = False
		make_users = {}
		def autofill(event):
			easybits_user.delete(0, END)
			easybits_user.insert(0, make_users[usern])
			easybits_pass.delete(0, END)
			easybits_pass.insert(0, '**********')
		for usern in settings.login_creds:
			for site in settings.login_creds[usern]:
				if site == 'easybits.com':
					if settings.login_creds[usern][site][0] == True:
						autofill_TF = True
						make_users[usern]=settings.login_creds[usern][site][1]
		if autofill_TF == False:
			return
		Label(easybits_autofill, text='Browser Autofill: ').pack()
		for usern in make_users:
			new_autofill = Label(easybits_autofill, text=('[%s]' % (make_users[usern])), fg='blue', cursor='hand2')
			new_autofill.pack(padx=3)
			new_autofill.bind('<Button-1>', autofill)
	def easybits_main():
		def return_next(event):
			easybits_pass.focus_set()
		global easybits_autofill
		global easybits_user
		global easybits_pass
		for widget in easybits_page.winfo_children():
			widget.destroy()
		easybits_logout_button.pack_forget()
		logoframe = LabelFrame(easybits_page, bg='gold', height=100)
		logoframe.pack(anchor=N, fill=X)
		Label(logoframe, text='easyBits.com', bg='gold', font=(None, 20)).place(anchor=CENTER, rely=.5, relx=.5)
		easybits_login = LabelFrame(easybits_page, bg='black')
		easybits_login.pack(anchor=N, pady=10)
		easybits_user_frame = LabelFrame(easybits_login, text='Account ID', fg='gold', bg='black')
		easybits_user_frame.pack(padx=5, pady=2, anchor=N)
		easybits_user = Entry(easybits_user_frame, width=40)
		easybits_user.pack()
		easybits_pass_frame = LabelFrame(easybits_login, text='Password', fg='gold', bg='black')
		easybits_pass_frame.pack(padx=5, anchor=S, side=LEFT)
		easybits_pass = Entry(easybits_pass_frame, width=30)
		easybits_pass.pack()
		Button(easybits_login, text=' Login ', bg='gold', cursor='hand2', command=easybits_doLogin).pack(padx=6, pady=5, anchor=S, side=RIGHT)
		easybits_autofill = LabelFrame(easybits_page)
		easybits_autofill.pack(anchor=N)
		add_easybits_autofill()
		if not sitelocker == None:
			global sitelocker_label
			def go_sitelocker(event):
				go_from('www.sitelocker.org')
			sitelocker_label = Label(easybits_page, text='SiteLocker v%s Secured' % str(sitelocker), fg='blue', cursor='hand2')
			sitelocker_label.pack(anchor=SW, side=LEFT)
			sitelocker_label.bind('<Button-1>', go_sitelocker)
		if not riddleme == None:
			global riddleme_label
			def go_riddleme(event):
				go_from('www.riddleme.org')
			riddleme_label = Label(easybits_page, text='RiddleMe On', fg='blue', cursor='hand2')
			riddleme_label.pack(anchor=SE, side=RIGHT)
			riddleme_label.bind('<Button-1>', go_riddleme)
	def easybits_doLogout():
		go_from('http://www.easybits.com')
	easybits_logout_button = Button(web_page, text=' Logout ', bg='gold', relief=FLAT, cursor='hand2', command=easybits_doLogout)
	easybits_logout_button.pack(anchor=W, side=RIGHT)
	easybits_main()
	def easybits_logOn():
		for widget in easybits_page.winfo_children():
			widget.destroy()
		global amount_label
		easybits_logout_button.pack(anchor=W, side=RIGHT)
		LabelFrame(easybits_page, text='History', width=200).pack(anchor=E, side=RIGHT, fill=Y, expand=False)
		actions_frame = LabelFrame(easybits_page, text='Actions', height=150)
		actions_frame.pack(anchor=W, side=BOTTOM, fill=X, expand=False)
		actions_frame.pack_propagate(0)
		account_frame = LabelFrame(easybits_page, text='Account')
		account_frame.pack(anchor=W, side=LEFT, fill=BOTH, expand=True)

		Label(account_frame, text='Account: %s' % (easybits_account), fg='orange', font=(None, 15)).pack(padx=20, pady=10, anchor=NW)
		amount_label = Label(account_frame, text='Balance: %sB' % (wallet.check('easybits', easybits_account)), fg='orange', font=(None, 15))
		amount_label.pack(padx=20, pady=10, anchor=NW)
		def bal_refresh():
			amount_label.configure(text='Balance: %sB' % (wallet.check('easybits', easybits_account)))
		Button(account_frame, text='Refresh', command=bal_refresh).pack(padx=20, pady=5, anchor=NW)
		global frame_open
		frame_open=False
		def send_easybits():
			global frame_open
			if not frame_open == False:
				return
			frame_open = True
			frame0 = LabelFrame(easybits_page, width=250, height=120, bg='black')
			frame0.place(anchor=CENTER, relx=.5, rely=.5)
			frame0.pack_propagate(0)
			frame = LabelFrame(frame0, text='Send Bits',)
			frame.pack(side=TOP, fill=BOTH, expand=True)
			ac_frame = LabelFrame(frame, text='Account')
			ac_frame.pack(padx=5, pady=2, anchor=W, side=TOP, fill=X)
			ac_entry = Entry(ac_frame)
			ac_entry.pack(pady=2, fill=X)

			am_frame = LabelFrame(frame, text='Amount')
			am_frame.pack(padx=5, pady=2, anchor=W, side=LEFT)
			am_entry = Entry(am_frame, width=10)
			am_entry.pack(pady=2, fill=X, side=LEFT)
			Label(am_frame, text='B').pack(pady=2, fill=X, side=RIGHT)

			def send():
				amount = float(am_entry.get().strip().rstrip())
				flag = wallet.check('easybits', easybits_account, amount=amount)
				if flag == True:
					flag = wallet.give('easybits', ac_entry.get().strip().rstrip(), easybits_account, amount)
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
		def buy_easybits():
			global frame_open
			if not frame_open == False:
				return
			frame_open = True
			frame0 = LabelFrame(easybits_page, width=250, height=120, bg='black')
			frame0.place(anchor=CENTER, relx=.5, rely=.5)
			frame0.pack_propagate(0)
			frame = LabelFrame(frame0, text='Buy Bits',)
			frame.pack(side=TOP, fill=BOTH, expand=True)
			ac_frame = LabelFrame(frame, text='Payme Account')
			ac_frame.pack(padx=5, pady=2, anchor=W, side=TOP, fill=X)
			token = None
			amount = 0.0
			def authorize():
				reload(wallet)
				global amount
				amount = am_entry.get()
				if amount.strip().rstrip() == '':
					am_entry.configure(bg='pink')
					return
				try: amount = float(amount)
				except:
					am_entry.configure(bg='pink')
					return
				wallet.payme_popup(easybits_page, test, amount, api='buy.easybits.com')
			def test(token2):
				global token
				token = token2
				if token == None:
					return
				elif token == False:
					am_entry.configure(bg='pink')
					return
				else:
					am_entry.configure(bg='white', state='disabled')
					ac_button.destroy()
					ac_label = Label(ac_frame, text=token)
					ac_label.pack(pady=2, fill=X)
					buy_button.configure(state='normal')
			ac_button = Button(ac_frame, text='Authorize', command=authorize)
			ac_button.pack(pady=2, fill=X)

			am_frame = LabelFrame(frame, text='Amount')
			am_frame.pack(padx=5, pady=2, anchor=W, side=LEFT)
			am_entry = Entry(am_frame, width=10)
			am_entry.pack(pady=2, fill=X, side=LEFT)
			Label(am_frame, text='B').pack(pady=2, fill=X, side=RIGHT)
			def buy():
				global token
				global amount
				if token == None: raise Exception('tokenIsNone')
				flag = wallet.convert('easybits', token, easybits_account, amount)
				print (float(amount) * 100.0)
				bal_refresh()
				close()
			def close():
				global frame_open
				frame_open = False
				frame0.destroy()
			Button(frame, text='Cancel', command=close).pack(padx=5, pady=2, anchor=W, side=RIGHT)
			global buy_button
			buy_button = Button(frame, text='Buy', command=buy)
			buy_button.pack(padx=5, pady=2, anchor=W, side=RIGHT)
			buy_button.configure(state='disabled')
		def sell_easybits():
			global frame_open
			if not frame_open == False:
				return
			frame_open = True
			frame0 = LabelFrame(easybits_page, width=250, height=120, bg='black')
			frame0.place(anchor=CENTER, relx=.5, rely=.5)
			frame0.pack_propagate(0)
			frame = LabelFrame(frame0, text='Sell Bits',)
			frame.pack(side=TOP, fill=BOTH, expand=True)
			ac_frame = LabelFrame(frame, text='Payme Account')
			ac_frame.pack(padx=5, pady=2, anchor=W, side=TOP, fill=X)
			token = None
			amount = 0.0
			def authorize():
				reload(wallet)
				global token
				wallet.payme_popup(easybits_page, test, api='sell.easybits.com')
			def test(token2):
				global token
				token = token2
				if token == None:
					return
				else:
					ac_button.destroy()
					ac_label = Label(ac_frame, text=token)
					ac_label.pack(pady=2, fill=X)
					sell_button.configure(state='normal')
			ac_button = Button(ac_frame, text='Authorize', command=authorize)
			ac_button.pack(pady=2, fill=X)

			am_frame = LabelFrame(frame, text='Amount')
			am_frame.pack(padx=5, pady=2, anchor=W, side=LEFT)
			am_entry = Entry(am_frame, width=10)
			am_entry.pack(pady=2, fill=X, side=LEFT)
			Label(am_frame, text='B').pack(pady=2, fill=X, side=RIGHT)
			def sell():
				global token
				global amount
				amount = am_entry.get()
				if amount.strip().rstrip() == '':
					am_entry.configure(bg='pink')
					return
				try: amount = float(amount)
				except:
					am_entry.configure(bg='pink')
					return
				if token == None: raise Exception('tokenIsNone')
				flag = wallet.convert('payme', token, easybits_account, (amount * 100.0))
				bal_refresh()
				close()
			def close():
				global frame_open
				frame_open = False
				frame0.destroy()
			Button(frame, text='Cancel', command=close).pack(padx=5, pady=2, anchor=W, side=RIGHT)
			global sell_button
			sell_button = Button(frame, text='Sell', command=sell)
			sell_button.pack(padx=5, pady=2, anchor=W, side=RIGHT)
			sell_button.configure(state='disabled')
		Button(actions_frame, text='Send Bits', command=send_easybits).pack(padx=20, side=LEFT)
		Button(actions_frame, text='Buy Bits', command=buy_easybits).pack(padx=20, side=LEFT)
		Button(actions_frame, text='Sell Bits', command=sell_easybits).pack(padx=20, side=LEFT)

