#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
============================================================
This file is licensed under the "GNU General Public License v3.0"
And is provided by;
"Allison Marie Bennett", TheCyaniteProject@gmail.com
============================================================
Apps, and App Framework
============================================================
"""
import os
from . import console
import data.settings as settings
from . import tkinter_ui
import data.web as web
from shutil import copyfile


def getfile(filename):
    if filename in os.listdir('%s\\data\\apps\\' % settings.game_dir):
        if filename in os.listdir(os.path.join(settings.user_dir, settings.username.lower(), 'systems\\user_home\\os_root_dir\\bin\\')):
            return 'fileAlreadyExists'
        copyfile(os.path.join(settings.game_dir, 'data\\apps\\', filename), os.path.join(settings.user_dir, settings.username.lower(), 'systems\\user_home\\os_root_dir\\bin\\', filename))
    else:
        return 'fileNotFound'
    console.reload_autofill()
    tkinter_ui.concom.set_completion_list(console.command_list)
    return True


class Apps():

    def virus_prerun(self, virusname='Name Not Found', level=0):
        # Future Feature - Anti-Virus goes here
        return False

    def virus_postrun(self, virusname='Name Not Found', level=0):
        print('\n\t!!! WARNING !!!\nA VIRUS WAS RUN ON YOUR SYSTEM!\n\nName From Database: %s\n\nAny damage has already been done.\nYou should investigate.' % virusname)
        return False

    # Tests
    def command_test(self, sys_args):
        print('Hello, World!1')
        print('Hello, World!2')
        print('Hello, World!3')

    # System
    def spoof_system_ip(self, sys_args):
        try:
            dc = sys_args[0][0]
        except:
            dc = False
        if dc is not False:
            if dc in '--dc':
                settings.current_ip = settings.player_ip
                print('Spoofing was canceled\nYour real ip is now in use')
                return
        if settings.system_ip == settings.player_ip:
            print('error: You cannot spoof this IP')
            return
        elif settings.current_ip == settings.system_ip:
            print('error: This IP is already in use')
            return
        elif console.can_run is False:
            print('error: Access Denied')
            return
        print('Spoofing system IP....')
        print('This may take a moment')
        settings.current_ip = settings.system_ip
        print('..........Done.')
        print('==========')
        print('REAL IP:   %s' % settings.player_ip)
        print('PUBLIC IP: %s' % settings.current_ip)
        print('==========')
        print('Disconnecting from this\nsystem will reset your IP')

    def ssh_hack(self, sys_args):
        if settings.system_id == '':
            print('error: as much as you might be tempted, you cannot hack yourself, sorry')
            return
        version = 1.0
        f_ver = 1.0
        ssh_val = None
        with open(settings.system_home.rsplit('os_root_dir', 1)[0] + 'nmap.ini', 'r') as f:
            for line in f.readlines():
                if 'ssh=' in line:
                    try:
                        ssh_val = line.split('ssh=', 1)[1].strip().rstrip()
                    except Exception as err:
                        console.output.append('ssh_hack_err: %s' % err)
        if ssh_val is None:
            print('error: system does not have ssh enabled')
            return
        if not ssh_val.lower() == 'open':
            print('error: system does not have ssh enabled')
            return
        with open(settings.system_home.rsplit('os_root_dir', 1)[0] + 'firewall.ini', 'r') as f:
            for line in f.readlines():
                if 'firewall=' in line:
                    try:
                        f_ver = float(line.split('firewall=', 1)[1].strip().rstrip())
                    except Exception as err:
                        console.output.append('ssh_hack_err: %s' % err)
        if not f_ver <= version:
            print('error: cannot get past firewall')
            return
        print('All done. Now try ;3')
        console.can_run = True
        tkinter_ui.update_folders()

    # Web
    def hack_login(self, sys_args):
        if web.sitelocker() is not False:
            print('error: blocked - Website might have Anti-Hack!')
            return
        if web.riddleme() is not False:
            print('error: our attempt was blocked!')
            if not web.riddleme() == 'block':
                web.riddleme(mode='popup')
            return
        version = 20.0
        web.web_hack(version)

    def bypass_sitelocker(self, sys_args):
        version = 1.0
        web.sitelocker(True)

    def bypass_riddleme(self, sys_args):
        if web.sitelocker() is not False:
            print('error: blocked - Website might have Anti-Hack!')
            return
        version = 1.0
        web.riddleme(True)

    # Malicous Viruses
    def virus_wipe_binfolder(self, sys_args):
        prevent = self.virus_prerun(virusname='worm_bin_cleaner', level=1)
        if prevent:
            return
        bin_dir = os.path.join(settings.user_dir, settings.username.lower(), 'systems\\user_home\\os_root_dir\\bin\\')
        for file in os.listdir(bin_dir):
            os.path.join(bin_dir, file)
        self.virus_postrun(virusname='worm_bin_cleaner', level=1)


def run(app_file, *args):
    if os.path.exists(app_file):
        with open(app_file, 'r') as app:
            command = app.read().split('\n', 1)[0].strip().rstrip()
            if command in dir(Apps):
                fn = 'Apps().%s(%s)' % (command, args)
                eval(fn)
