
from tkinter import *
from subprocess import Popen
from tkinter import ttk

from data.__VERSION__ import __VERSION__
import os
import sys
import configparser
import importlib
# import ctypes
# import subprocess

import data.new_player_ui as new_player_ui

# Error Debugging
import traceback
import logging
from time import strftime
with open('pid', 'w') as f:
    f.write(str(os.getpid()))

# subprocess.Popen('cls', shell=True)
os.system('cls')

try:
    os.mkdir('logs')
except OSError:
    pass


def get_time():
    return strftime('%Y-%m-%d %H:%M.%S')

logging.basicConfig(level=logging.DEBUG, filename=(os.path.join(str(os.getcwd()), 'logs\\launcher.log')))
# ---------

os.system('@title Exit.Code() [Do not close this window]')

game_exe = 'Exit_Code.py'
generation_ini = 'data\\gen.py'
settings_file = 'data\\config.ini'
game_seed = 'default'
username = 'Guest'
game_dir = os.getcwd()

conf = configparser.ConfigParser()


def load_game_settings():
    global user_dir
    global username
    global generation_ini
    if os.path.isfile(settings_file):
        conf.read(settings_file)
        if 'system' in conf.sections():
            items = [i for (i, n) in conf['system'].items()]
            if 'default_user' in items:
                username = conf['system']['default_user']
            if 'user_dir' in items:
                user_dir = conf['system']['user_dir']
            if 'generation_ini' in items:
                generation_ini = conf['system']['generation_ini']

    if '%game_dir%' in user_dir:
        user_dir = ''.join((game_dir, user_dir.split('%game_dir%')[1]))

load_game_settings()
profile = None


def add_profiles():
    try:
        profile.configure(values=PROFILES)
        for i in range(len(PROFILES) - 1):
            i += 1
            if PROFILES[i].lower() == username.lower():
                profile.current(i)
                break
            else:
                profile.current(0)
    except:
        pass


def check_profiles():
    global PROFILES
    PROFILES = ['Select Profile']
    for folder in os.listdir('data\\users\\'):
        if os.path.isfile(os.path.join('data\\users\\', folder, 'user.ini')):
            with open(os.path.join('data\\users\\', folder, 'user.ini'), 'r') as file:
                for i in file.read().split('\n'):
                    if 'username' in i:
                        PROFILES.append(i.split('=')[1].strip())
    add_profiles()
check_profiles()

if os.path.exists(generation_ini):
    exec('from %s import *' % generation_ini.replace('.py', '').replace('\\', '.'))


def main():

    def start_game():
        global script_path
        global po
        if profile.get() == 'Select Profile':
            return
        script_path = os.path.join(os.getcwd(), game_exe)
        po = Popen([sys.executable, '-u', script_path, '--user', profile.get()], shell=True)

    def new_profile_gui():
        importlib.reload(new_player_ui)
        new_player_ui.main(root, check_profiles)

    def user_settings():
        os.system('@start notepad.exe %s' % settings_file)

    # tkinter UI
    global root
    global profile
    root = Tk()
    root.title('Exit.Code() - Launcher')
    root.geometry('800x310')
    root.iconbitmap('data\\images\\EC-LOGO_SMALL.ICO')
    root.resizable(width=False, height=False)

    # Splash Area
    splash = LabelFrame(root)
    splash.pack(padx=3, pady=2, anchor=S, fill=BOTH, expand=True, side=LEFT)

    try:
        from PIL import Image, ImageTk
        image = Image.open('data\\images\\EC-LOGO.PNG')
        image = image.resize((400, 100), Image.ANTIALIAS)  # The (250, 250) is (height, width)
        __logo__ = ImageTk.PhotoImage(image)
        Label(splash, image=__logo__).pack(side=LEFT, fill=X, expand=True)  # Logo
    except:
        print('Could not find Phil! 3;')
        Label(splash, text='Exit.Code()', fg='darkgreen', font=('Courier', 32)).pack(side=LEFT, fill=X, expand=True)  # Logo

    Label(splash, text=__VERSION__, bg='white', fg='darkgreen').place(anchor=NW, relx=0, x=3, rely=0, y=3)

    # Menu Area
    menu = Frame(root, width=300)
    menu.pack(pady=2, anchor=S, fill=Y, expand=False, side=RIGHT)
    menu.pack_propagate(0)

    Play = Button(menu, text='Play', width=30, height=4, command=start_game)
    Play.pack(padx=5, pady=2, anchor=E, fill=X, expand=False, side=TOP)

    frame = LabelFrame(menu, text='Game Profile')
    frame.pack(padx=5, pady=2, anchor=E, fill=X, expand=False, side=TOP)

    Settings = Button(menu, text='Settings', width=30, height=4, command=user_settings)
    Settings.pack(padx=5, pady=2, anchor=E, fill=X, expand=False, side=TOP)

    Exit = Button(menu, text='Exit', width=30, height=4, command=root.quit)
    Exit.pack(padx=5, pady=2, anchor=E, fill=X, expand=False, side=TOP)

    profile = ttk.Combobox(frame, values=[], state="readonly")
    profile.pack(padx=10, pady=5, anchor=N, fill=BOTH, expand=False, side=TOP)
    add_profiles()

    new_profile = Button(frame, text='New Profile', command=new_profile_gui)
    new_profile.pack(padx=10, anchor=S, fill=BOTH, expand=True, side=BOTTOM)

    root.mainloop()


def start():
    try:
        main()
    except Exception as a:
        logging.exception('@(%s):' % get_time())
        traceback.print_exc(a)
start()
