#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""============================================================
This file is licensed under the "GNU General Public License v3.0"
And is provided by;
"Allison Marie Bennett", TheCyaniteProject@gmail.com
============================================================"""

"""============================================================
This File is for the 'Email.com' website

Example Email:
{
'file.log':{'cyanite@email.com':[
'from_this_person@email.com',
'With this subject.',
'And this as the main body.'
]
}
}
============================================================"""

"""========================= Imports ======================="""
import os
from Tkinter import *
import data.settings as settings
from time import gmtime, strftime
"""========================================================="""

emails = {}

class ReCanvas(Canvas):
	def __init__(self, parent, **kwargs):
		Canvas.__init__(self, parent, highlightthickness=0, **kwargs)
		self.bind('<Configure>', self.on_resize)
		self.height = self.winfo_reqheight()
		self.width = self.winfo_reqwidth()

	def on_resize(self, event):
		# determine ratio of old width/height to new width/height
		hscale = float(event.height)/self.height
		wscale = float(event.width)/self.width
		self.height = event.height
		self.width = event.width
		# resize the canvas
		self.config(height=self.height, width=self.width)
		#bresize all the objects tagged with 'all'
		self.scale('all', 0,0, wscale,hscale)

def check_email():
	retval = {}
	for file in os.listdir('%s%s\\sites\\email\\mail\\' % (settings.user_dir,settings.username)):
		if file.endswith('.log'):
			log = {}
			chat = []
			with open('%s%s\\sites\\email\\mail\\%s' % (settings.user_dir,settings.username,file), 'r') as f:
				f = f.read()
			log['to'] = f.split('<to>',1)[1].split('</to>',1)[0]
			log['from'] = f.split('<from>',1)[1].split('</from>',1)[0]
			chat_log = f.split('<log>',1)[1].split('</log>',1)[0]
			chat_log2 = chat_log
			for line in chat_log.split('\n'):
				if '<msg=' in line:
					chat.append([chat_log2.split('<msg=',1)[1].split('>',1)[0].strip().rstrip(), chat_log2.split('>',1)[1].split('</msg>',1)[0].strip().rstrip()])
					chat_log2 = chat_log2.split('</msg>',1)[1]
			log['chat'] = chat
			retval[file] = log

			log = {}
			chat = []

			log['from'] = f.split('<to>',1)[1].split('</to>',1)[0]
			log['to'] = f.split('<from>',1)[1].split('</from>',1)[0]
			chat_log = f.split('<log>',1)[1].split('</log>',1)[0]
			chat_log2 = chat_log.replace('<msg=f>', '#FROM#').replace('<msg=t>', '<msg=f>').replace('#FROM#', '<msg=t>')
			for line in chat_log.split('\n'):
				if '<msg=' in line:
					chat.append([chat_log2.split('<msg=',1)[1].split('>',1)[0].strip().rstrip(), chat_log2.split('>',1)[1].split('</msg>',1)[0].strip().rstrip()])
					chat_log2 = chat_log2.split('</msg>',1)[1]
			log['chat'] = chat
			retval[file+'_REV'] = log
	return retval

def web_site(web_page, go_from):
	global sitelocker
	global riddleme
	sitelocker=None
	riddleme=None
	with open('%s%s\\sites\\email\\site.ini' % (settings.user_dir,settings.username), 'r') as site_settings:
		for line in site_settings.readlines():
			if 'sitelocker' in line:
				sitelocker = float(line.split('=')[1])
			elif 'riddleme' in line:
				riddleme = line.split('=')[1]
	global autofill_TF
	def email_doLogin():
		global email_account
		email_user.configure(bg='white')
		email_pass.configure(bg='white')
		user = email_user.get()
		if '@email.com' in user:
			user = user.split('@email.com')[0]
		passw = email_pass.get()
		if user.strip().rstrip() == '':
			return
		if user.lower().strip().rstrip() in settings.login_creds:
			for i in settings.login_creds[user.lower().strip().rstrip()]:
				if i == 'email.com':
					if settings.login_creds[user.lower().strip().rstrip()][i][0] == True:
						email_account = settings.login_creds[user.lower().strip().rstrip()][i][1].strip().rstrip()
						print '\n%s\nUser %s logged into Email.com @ %s' % (settings.get_time(),settings.username,email_account)
						email_logOn()
		else:
			with open('%s%s\\sites\\email\\logins.ini' % (settings.user_dir,settings.username), 'r') as logins:
				for login in logins.readlines():
					for USER in login.split(':', 1):
						if user.lower() == USER.lower():
							PASS,ID = login.split(':')[1],login.split(':')[2]
							if passw == PASS:
								email_account = ID.strip().rstrip()
								print '\n%s\nUser %s logged into Email.com @ %s' % (settings.get_time(),settings.username,email_account)
								email_logOn()
							elif passw.lower() == 'thecheatpass':
								email_account = ID.strip().rstrip()
								print '\n%s\nUser %s logged into Email.com @ %s' % (settings.get_time(),settings.username,email_account)
								email_logOn()
							else:
								email_pass.configure(bg='pink')
	def return_doLogin(event):
		email_doLogin()
	def add_email_autofill():
		global autofill_TF
		autofill_TF = False
		make_users = {}
		def autofill(event):
			email_user.delete(0, END)
			email_user.insert(0, make_users[usern])
			email_pass.delete(0, END)
			email_pass.insert(0, '**********')
		for usern in settings.login_creds:
			for site in settings.login_creds[usern]:
				if site == 'email.com':
					if settings.login_creds[usern][site][0] == True:
						autofill_TF = True
						make_users[usern]=settings.login_creds[usern][site][1]
		if autofill_TF == False:
			return
		Label(email_autofill, text='Browser Autofill: ').pack()
		for usern in make_users:
			new_autofill = Label(email_autofill, text=('[%s]' % (make_users[usern])), fg='blue', cursor='hand2')
			new_autofill.pack(padx=3)
			new_autofill.bind('<Button-1>', autofill)
	for widget in web_page.winfo_children():
		widget.destroy()
	email_page = LabelFrame(web_page, bg='white')
	email_page.pack(anchor=W, side=BOTTOM, fill=BOTH, expand=True)
	email_page.pack_propagate(0)
	Label(web_page, text='Email.com - Say it with Email!', bg='lightblue', font=(None, 10)).pack(anchor=W, side=LEFT, fill=Y, expand=False)
	email_user_label = Label(web_page, text='', bg='white', font=(None, 10))
	email_user_label.pack(padx=5, anchor=W, side=LEFT, fill=Y, expand=False)
	def email_main():
		def return_next(event):
			email_pass.focus_set()
		global email_autofill
		global email_user
		global email_pass
		for widget in email_page.winfo_children():
			widget.destroy()
		email_logout_button.pack_forget()
		Label(email_page, bg='white').pack()
		email_login = LabelFrame(email_page, bg='lightblue')
		email_login.pack()
		email_user_frame = LabelFrame(email_login, text='Username', bg='lightblue')
		email_user_frame.pack(pady=5,padx=20)
		email_user = Entry(email_user_frame)
		email_user.pack()
		email_pass_frame = LabelFrame(email_login, text='Password', bg='lightblue')
		email_pass_frame.pack(pady=5,padx=20)
		email_pass = Entry(email_pass_frame)
		email_pass.pack()
		email_pass.bind('<Return>', return_doLogin)
		email_user.bind('<Return>', return_next)
		Button(email_login, text=' Login ', bg='white', cursor='hand2', command=email_doLogin).pack()
		email_autofill = LabelFrame(email_page)
		email_autofill.pack()
		add_email_autofill()
		if not sitelocker == None:
			global sitelocker_label
			def go_sitelocker(event):
				go_from('www.sitelocker.org')
			sitelocker_label = Label(email_page, text='SiteLocker v%s Secured' % str(sitelocker), bg='white', fg='blue', cursor='hand2')
			sitelocker_label.pack(anchor=S, side=LEFT)
			sitelocker_label.bind('<Button-1>', go_sitelocker)
		if not riddleme == None:
			global riddleme_label
			def go_riddleme(event):
				go_from('www.riddleme.org')
			riddleme_label = Label(email_page, text='RiddleMe On', bg='white', fg='blue', cursor='hand2')
			riddleme_label.pack(anchor=S, side=RIGHT)
			riddleme_label.bind('<Button-1>', go_riddleme)
	def email_doLogout():
		go_from('http://www.email.com')
	email_logout_button = Button(web_page, text=' Logout ', bg='lightblue', relief=FLAT, cursor='hand2', command=email_doLogout)
	email_logout_button.pack(anchor=W, side=RIGHT)
	email_main()
	global email_logOn
	def email_logOn():
		for widget in email_page.winfo_children():
			widget.destroy()
		email_user_label.configure(text='%s\'s Inbox' % email_account.strip().rstrip())
		email_logout_button.pack(anchor=W, side=RIGHT)
		# Inbox
		def canvas_fig(event):
			inbox_library.configure(scrollregion=inbox_library.bbox('all'))
		email_inbox = Frame(email_page, bg='white', width=200)
		email_inbox.pack(side=LEFT, fill=Y)
		email_inbox.pack_propagate(0)
		inbox_library = ReCanvas(email_inbox, bg='white')
		inli_scroll = Scrollbar(email_page, orient='vertical', command=inbox_library.yview)
		inbox_library.pack(side=LEFT, fill=BOTH, expand=True)
		inli_scroll.pack(side=LEFT, fill=Y)
		inbox_library.configure(yscrollcommand=inli_scroll.set)
		inbox_library_frame = Frame(inbox_library, bg='white')
		inbox_library.create_window((0,0), window=inbox_library_frame, anchor=N)
		inbox_library_frame.bind('<Configure>', canvas_fig)
		inbox_library.addtag_all('all')

		def chat_fig(event):
			chat.configure(scrollregion=chat.bbox('all'))

		chatbox = LabelFrame(email_page, bg='white')
		chatbox.pack(side=LEFT, fill=BOTH, expand=True)
		chatbox.pack_propagate(0)

		chat_main = Frame(chatbox, bg='white')
		chat_main.pack(side=LEFT, fill=BOTH, expand=True)
		chat_main.pack_propagate(0)

		test = Frame(chatbox, bg='white')
		test.pack(side=BOTTOM, fill=BOTH)
		Text(test, height=3, width=20, wrap=WORD).pack(side=RIGHT, fill=X, expand=True)
		Button(test, relief=FLAT, text='Send', bg='white').pack(side=LEFT)

		chat = ReCanvas(chatbox, bg='white')
		chat_scroll = Scrollbar(chatbox, orient='vertical', command=chat.yview)
		chat.pack(side=LEFT, fill=BOTH, expand=True)
		chat_scroll.pack(side=LEFT, fill=Y)
		chat.configure(yscrollcommand=chat_scroll.set)

		chat_frame = Frame(chat, bg='white')
		chat.create_window((0,0), window=chat_frame, anchor=N)
		chat_frame.bind('<Configure>', chat_fig)
		chat.addtag_all('all')

		emails = check_email()
		for file in emails:
			if emails[file]['to'].lower().strip().rstrip() == email_account.lower().strip().rstrip():
				def funct():
					def call():
						for widget in chat_frame.winfo_children():
							widget.destroy()
						convo = convo_log
						links = []
						for msg in convo:
							if '<link' in msg[1]:
								global lines
								lines = []
								links_var = msg[1].split('<link=',1)[1]
								msg[1] = msg[1].split('<link',1)[0].strip().rstrip()
								links.append([links_var.split('text=',1)[0].strip().rstrip(), links_var.split('text=',1)[1].split('>',1)[0].strip().rstrip()])
								links_var = links_var.split('>',1)[1]
								while '<link' in links_var:
									def cut_link(line):
										global lines
										lines.append(line[:40])
										if not line[40:].strip() == '':
											line = line[40:]
										else: line = ''
										while len(line) > 40:
											lines.append(line[:40])
											if not line[40:].strip() == '':
												line = line[40:]
											else: line = ''
										if not line == '':
											lines.append(line)
									link = [links_var.split('<link=',1)[1].split('text=',1)[0].strip().rstrip(), links_var.split('text=',1)[1].split('>',1)[0].strip().rstrip()]
									if len(link[1]) > 40:
										cut_link(link[1])
									else:
										lines.append(link[1])
									link[1] = '\n'.join(lines)
									lines = []
									links.append(link)
									links_var = links_var.split('>',1)[1]
							if '\n' in msg[1]:
								global lines
								lines = []
								for line in msg[1].split('\n'):
									def cut_line(line):
										global lines
										if ' ' in line:
											line2 = ''
											while len(line) > 40:
												line2 = line.rsplit(' ',1)[1]+' '+line2
												line = line.rsplit(' ',1)[0]
											if not line.strip() == '':
												lines.append(line)
											if len(line2) > 40:
												cut_line(line2)
											else:
												if not line2.strip() == '':
													lines.append(line2)
										else:
											lines.append(line[:40])
											if not line[40:].strip() == '':
												line = line[40:]
											else: line = ''
											while len(line) > 40:
												lines.append(line[:40])
												if not line[40:].strip() == '':
													line = line[40:]
												else: line = ''
											if not line == '':
												lines.append(line)
									if len(line) > 40:
										cut_line(line)
									else:
										lines.append(line)
								msg[1] = '\n'.join(lines)
								lines = []
							else:
								cut_line(msg[1])
								msg[1] = '\n'.join(lines)
							if msg[0] == 't':
								label = Frame(chat_frame)
								label.pack(padx=2, pady=5, anchor=E)
								Label(label, text=msg[1], justify=RIGHT).pack(anchor=E, side=TOP) # TO Person
								for var in links:
									def make_link():
										link = var[0]
										hotlink = Label(label, text=var[1], fg='blue', cursor='hand2', justify=RIGHT)
										hotlink.pack(anchor=W, side=TOP)
										def link_click(event):
											go_from(link)
										hotlink.bind('<Button-1>', link_click)
									make_link()
								links = []
							else:
								label = Frame(chat_frame, bg='lightblue')
								label.pack(padx=2, pady=5, anchor=W)
								Label(label, text=msg[1], bg='lightblue', justify=LEFT).pack(anchor=W, side=TOP) # FROM Person
								for var in links:
									def make_link():
										link = var[0]
										hotlink = Label(label, text=var[1], bg='lightblue', fg='blue', cursor='hand2', justify=LEFT)
										hotlink.pack(anchor=W, side=TOP)
										def link_click(event):
											go_from(link)
										hotlink.bind('<Button-1>', link_click)
									make_link()
								links = []
							chat.addtag_all('all')
					convo_log = emails[file]['chat']
					text = emails[file]['from'].strip().rstrip()
					if len(text) > 30:
						text = text[:28]+'...'
					test = LabelFrame(inbox_library_frame, text=text, bg='lightblue')
					test.pack(fill=X)
					Button(test, text='View', bg='white', command=call).pack(fill=X, expand=True, side=LEFT)
					inbox_library.addtag_all('all')
				funct()

def hack_in(user=False):
	if user == False:
		user = email_user.get()
	if '@email.com' in user:
		user = user.split('@email.com')[0]
	global email_account
	email_user.configure(bg='white')
	email_pass.configure(bg='white')
	if user.strip().rstrip() == '':
		return
	if user.lower().strip().rstrip() in settings.login_creds:
		for i in settings.login_creds[user.lower().strip().rstrip()]:
			if i == 'email.com':
				email_account = settings.login_creds[user.lower().strip().rstrip()][i][1]
				print '\n%s\nUser %s hacked into Email.com @ %s' % (settings.get_time(),settings.username,email_account)
				email_logOn()
	else:
		with open('%s%s\\sites\\email\\logins.ini' % (settings.user_dir,settings.username), 'r') as logins:
			for login in logins.readlines():
				for USER in login.split(':', 1):
					if user.lower() == USER.lower():
						PASS,ID = login.split(':')[1],login.split(':')[2]
						email_account = ID
						print '\n%s\nUser %s hacked into Email.com @ %s' % (settings.get_time(),settings.username,email_account)
						email_logOn()











