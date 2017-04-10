#!/usr/bin/python
# -*- coding: utf-8 -*-

"""============================================================
This file is licensed under the "GNU General Public License v3.0"
And is provided by;
"Allison Marie Bennett", TheCyaniteProject@gmail.com
============================================================"""

"""============================================================
New Profile Creation
============================================================"""

"""========================= Imports ======================="""
from tkinter import *
from tkinter import ttk
import random
import string
import os
import data.sys_make as sys_make

"""========================================================="""

# TODO: Tk.Entry for each variable in user Dict, "Accept" and "Cancel" buttons, a few "?" help buttons.

attempt = 0
warn = False
def main(main_frame, check_profiles):
	# Tkinter UI
	root = Toplevel(main_frame)
	root.title('Exit.Code() - New Profile')
	root.geometry("400x475")
	root.resizable(width=False, height=False)

	# Entries Area
	entries = LabelFrame(root)
	entries.pack(anchor=W, fill=BOTH, expand=True, side=TOP)
	
	def pad_warn(text='nulWarn', color='pink'):
		global warn
		if warn:
			warn.destroy()
		warn = LabelFrame(entries)
		warn.place(anchor=NW, relx=0, rely=0)
		Label(warn, bg=color, text=text).pack(padx=3, anchor=W, side=LEFT)
		Button(warn, text='Dismiss', relief=FLAT, command=warn.destroy).pack(anchor=W, side=LEFT)
	
	# Help Button: Button(frame, text=" ? ", relief=FLAT, cursor='hand2', fg='navy').pack(padx=1, side=RIGHT)
	
	frame = LabelFrame(entries, text='Name')
	frame.pack(padx=10, pady=3, fill=X, side=TOP)
	name = Entry(frame)
	name.pack(padx=3, pady=3, fill=X, expand=True, side=LEFT)
	name.insert(0, 'Jane')
	frame = LabelFrame(entries, text='Username')
	frame.pack(padx=10, pady=3, fill=X, side=TOP)
	username = Entry(frame)
	username.pack(padx=3, pady=3, fill=X, expand=True, side=LEFT)
	username.insert(0, 'JaneDoe001')
	frame = LabelFrame(entries, text='Prefered Pronouns')
	frame.pack(padx=10, pady=3, fill=X, side=TOP)
	pronouns = ttk.Combobox(frame, values=['Please Select', 'She/Her', 'He/Him'], state="readonly")
	pronouns.current(0)
	pronouns.pack(padx=3, pady=3, fill=X, expand=True, side=LEFT)
	frame = LabelFrame(entries, text='Game Seed')
	frame.pack(padx=10, pady=3, fill=X, side=TOP)
	game_seed = Entry(frame)
	game_seed.pack(padx=3, pady=3, fill=X, expand=True, side=LEFT)
	def randomize1():
		game_seed.delete(0, END)
		game_seed.insert(0, ''.join([ ( random.choice(string.digits+string.letters+'._-') ) for i in range(24) ]) )
	Button(frame, text='Randomize', command=randomize1).pack(padx=1, side=RIGHT)
	frame = LabelFrame(entries, text='IP Address')
	frame.pack(padx=10, pady=3, fill=X, side=TOP)
	player_ip = Entry(frame)
	player_ip.pack(padx=3, pady=3, fill=X, expand=True, side=LEFT)
	def randomize2():
		player_ip.delete(0, END)
		player_ip.insert(0, sys_make.gen_IP(create=False))
	Button(frame, text='Randomize', command=randomize2).pack(padx=1, side=RIGHT)
	frame = LabelFrame(entries, text='In-Game Email')
	frame.pack(padx=10, pady=3, fill=X, side=TOP)
	email_ac = Entry(frame)
	email_ac.pack(padx=3, pady=3, fill=X, expand=True, side=LEFT)
	email_ac.insert(0, username.get())
	Label(frame, text='@email.com').pack(padx=1,side=RIGHT)
	frame = LabelFrame(entries, text='PayMe Account Name')
	frame.pack(padx=10, pady=3, fill=X, side=TOP)
	payme_ac = Entry(frame)
	payme_ac.pack(padx=3, pady=3, fill=X, expand=True, side=LEFT)
	payme_ac.insert(0, username.get())
	Label(frame, text='_XXXXXXXX').pack(padx=1, side=RIGHT)
	frame = LabelFrame(entries, text='EasyBits Account Name')
	frame.pack(padx=10, pady=3, fill=X, side=TOP)
	easybits_ac = Entry(frame)
	easybits_ac.pack(padx=3, pady=3, fill=X, expand=True, side=LEFT)
	easybits_ac.insert(0, username.get())
	Label(frame, text='_XXXXXXXX').pack(padx=1,side=RIGHT)
	
	game_seed.insert(0, ''.join((random.choice(string.digits+string.letters) for i in range(24))) )
	player_ip.insert(0, sys_make.gen_IP(create=False))

	# Menu Area
	menu = Frame(root, height=100)
	menu.pack(anchor=W, fill=BOTH, expand=False, side=TOP)
	#menu.pack_propagate(0)
	"""test_profile = {
	'alias' : 'Jane',
	'username' : 'test001',
	'pronouns' : 'female',
	'seed' : 'AwesomeSauce',
	'player_ip' : '111.111.111.111',
	'email_ac' : 'test001@email.com',
	'easybits_ac' : 'test001_1234567890',
	'payme_ac' : 'test001_1234567890',
}"""
	def create_profile():
		global attempt
		profile = {}
		for entrybox in [name, username, email_ac, payme_ac, easybits_ac, player_ip, game_seed]:
			if not entrybox.get().strip().rstrip() == '':
				entrybox.configure(bg='white')
				for i in entrybox.get().strip().rstrip():
					if i in ' ':
						pad_warn('You cannot use spaces', color='pink')
						entrybox.configure(bg='pink')
						return
					elif not i in string.digits+string.letters+'_.-':
						pad_warn('You can only use Numbers, Letters, and:  .  _  -', color='pink')
						entrybox.configure(bg='pink')
						return
					
			else:
				pad_warn('Please fill in all fields', color='pink')
				entrybox.configure(bg='pink')
				return
		validity = sys_make.check_ip(player_ip.get().strip().rstrip())
		if not validity == True:
			player_ip.configure(bg='pink')
			pad_warn('IP Address is not valid. Valid example: 11.111.111.11', color='pink')
			return
		else: player_ip.configure(bg='white')
		
		try:
			if pronouns.get() == 'Please Select':
				if attempt == 1:
					pad_warn('I said.. Select your pronouns.', color='pink')
					attempt +=1
				elif attempt == 2:
					pad_warn('..Stop that.', color='pink')
					attempt +=1
				elif attempt == 3:
					pad_warn('I said STOP!', color='pink')
					attempt +=1
				elif attempt == 4:
					pad_warn('One more time and you\'re gunna be sorry!', color='pink')
					attempt +=1
				elif attempt == 5:
					pad_warn('That\'s it. I\'ve had enough of you.', color='pink')
					pronouns.configure(values=['"RainbowDashies\' Pyromancing Floof-ball"' for i in range(10)])
					pronouns.current(0)
					attempt +=1
				elif attempt > 5:
					pad_warn(' ... ', color='pink')
				else:
					pad_warn('Please select your prefered pronouns', color='pink')
					attempt +=1
				return
			elif not pronouns.get() in ['"RainbowDashies\' Pyromancing Floof-ball"', 'Please Select', 'She/Her', 'He/Him']:
				raise Exception('THEY ESCAPED THE GENDER BINARY!!!! XDDD')
			elif pronouns.get() == 'She/Her': profile['pronouns'] = 'female'
			elif pronouns.get() == 'He/Him': profile['pronouns'] = 'male'
			elif pronouns.get() == '"RainbowDashies\' Pyromancing Floof-ball"': profile['pronouns'] = 'floofball'
			# Non-Trolling stuffs~
			profile['seed'] = game_seed.get().strip().rstrip()
			profile['alias'] = name.get().strip().rstrip()
			profile['username'] = username.get().strip().rstrip()
			profile['email_ac'] = email_ac.get().strip().rstrip()+'@email.com'
			seeded = random.Random()
			seeded.seed(profile['seed']+'payme')
			profile['payme_ac'] = payme_ac.get().strip().rstrip()+'_'+''.join([( seeded.choice(string.digits+string.letters+'_') ) for i in range(8)])
			seeded.seed(profile['seed']+'easybits')
			profile['easybits_ac'] = easybits_ac.get().strip().rstrip()+'_'+''.join([( seeded.choice(string.digits+string.letters+'_') ) for i in range(8)])
			profile['player_ip'] =player_ip.get().strip().rstrip()
		except Exception, err:
			pad_warn('Woah! That was unexpected! Error: %s' % err, color='pink')
			return
		reload(sys_make)
		sys_make.make_player_profile(profile)
		pad_warn('Profile was created', color='white')
		check_profiles()
		
	Button(menu, text=' Create Profile ', height=2, command=create_profile).pack(padx=10, pady=10, side=LEFT)
	Button(menu, text='     Cancel     ', height=2, command=root.destroy).pack(padx=10, pady=10, side=RIGHT)


	root.mainloop()
