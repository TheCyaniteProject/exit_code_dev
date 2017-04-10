#!/usr/bin/python
# -*- coding: utf-8 -*-

"""============================================================
This file is licensed under the "GNU General Public License v3.0"
And is provided by;
"Allison Marie Bennett", TheCyaniteProject@gmail.com
============================================================"""

"""============================================================
Main Game File
============================================================"""

"""========================= Imports ======================="""
import argparse
import sys
import os
"""========================================================="""



# Error Debugging
import traceback
import logging
from time import strftime

def get_time():
	return strftime('%Y-%m-%d %H:%M.%S')

logging.basicConfig(level=logging.DEBUG, filename=(os.path.join(str(os.getcwd()),'logs\\game.log')))
# ---------

# Command Line Arguments

if len(sys.argv) >= 1:
	arg = argparse.ArgumentParser()
	arg.add_argument("--user", help="Sets the active user profile", default=False)
	arg.add_argument("--nowarn", help="Toggles off 'Early Access' warning", action="store_true")
	args = arg.parse_args()


# TODO: replace all "random.choice" with "seeded.choice"


def main():

	""" Game Settings """
	if args.user:
		if os.path.isfile('data\\config.ini'):
			with open('data\\config.ini', 'r') as f:
				config = f.readlines()
			with open('data\\config.ini', 'w') as f:
				for line in config:
					if 'default_user' in line:
						line = 'default_user=%s\n' % args.user.lower()
					f.write(line)
		else: print('doesntExist')
	#raise SystemExit
	import data.settings as settings

	if args.nowarn:
		settings.no_warning = True
			
	""" Game UI(Tkinter) """ # Everything else is imported as-needed
	
	import data.tkinter_ui # !!! NOTHING CAN GO BELOW THIS !!! (Unless you want it to run AFTER the game has closed)
	
try:
	main()
except Exception, a:
	logging.exception('@(%s):' % get_time())
	traceback.print_exc(a)
	print('Error logged to "logs\\game.log"')