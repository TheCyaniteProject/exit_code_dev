#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
============================================================
This file is licensed under the "GNU General Public License v3.0"
And is provided by;
"Allison Marie Bennett", TheCyaniteProject@gmail.com
============================================================
Game Console
============================================================
"""
import os
import sys
import shlex
import contextlib
import data.settings as settings
import data.apps as apps
import data.wallet as wallet
import data.sys_make as sys_make
from Tkinter import *
import tkinter_ui
import StringIO
import argparse
import subprocess

settings.system_id = ''
can_run = True
player_apps = []


def reload_apps():
    global player_apps
    player_apps = []
    for app in os.listdir(os.path.join(settings.user_dir, settings.username.lower(), 'systems\\user_home\\os_root_dir\\bin\\')):
        if app.endswith('.app'):
            player_apps.append(app)

print('\n===== Loading Player Apps =====')
reload_apps()
for i in player_apps:
    print(i)
print('===== Done Loading Player Apps =====\n')

player_scripts = []


def reload_scripts():
    global player_scripts
    player_scripts = []
    for script in os.listdir(os.path.join(settings.player_home, 'bin\\')):
        if script.endswith('.sh'):
            player_scripts.append(script)
print('\n===== Loading Player Scripts =====')
reload_scripts()
for i in player_scripts:
    print(i)
print('===== Done Loading Player Scripts =====\n')


# This is for capturing print() so i can use argparser
@contextlib.contextmanager
def stdout_redirect(where):
    sys.stdout = where
    try:
        yield where
    finally:
        sys.stdout = sys.__stdout__
print('===== Loading Console Commands ====')
# The actual console commands


class Console():

    # ============================
    # do_   = Visable command
    # hdo_  = Invisable command
    # ============================

    # --- Help menu --- #
    def do_help(self, args):
        usage = """usage: help [-h] <command>

Shows helpful information about commands

positional arguments:
  <command>   Use 'help <command>' for specific help."""
        if len(args) >= 1:
            for i in args:
                if i in '--help':
                    cmd_help = argparse.ArgumentParser(usage=usage, prog='help')

                    # Processes the command - Capture '--help' or argument errors (e.g: Typos)
                    try:
                        arg = cmd_help.parse_args(args)
                    except:
                        return

        if len(args) == 0:
            help = """
  Use 'help <command>' for specific help.
===========================================\n  """
            # sys.stdout.write('  ')
            for i in sorted(dir(Console), key=str.lower):
                if i.startswith('do_'):
                    help = help + str(i).split('do_')[1] + '  '
            help = help + '\n'
            print(help)
        elif len(args) == 1:
            if 'do_' + args[0] in dir(Console):
                fn = 'Console().do_%s(["--help"])' % args[0]
                eval(fn)
            elif 'hdo_' + args[0] in dir(Console):
                fn = 'Console().hdo_%s(["--help"])' % args[0]
                eval(fn)
            else:
                print('help: error: help could not find "%s"' % args[0])
        else:
            print('help: error: you can only pass one object at a time')

    # --- Other commands --- #

    def do_dir(self, args):
        usage = """usage: help [-h] <command>

Prints out the current working directory

positional arguments:
  <command>   Use 'help <command>' for specific help."""
        if len(args) >= 1:
            for i in args:
                if i in '--help':
                    cmd_dir = argparse.ArgumentParser(usage=usage, prog='dir')

                    # Processes the command - Capture '--help' or argument errors (e.g: Typos)
                    try:
                        arg = cmd_dir.parse_args(args)
                    except:
                        return

        if len(args) == 0:
            cmddir(settings.working_dir)
        elif len(args) == 1:
            cmddir(args[0])

    def do_apps(self, args):
        cmd_apps = argparse.ArgumentParser(description="Lists all the apps in your \\bin\\ folder", prog='apps')

        # Processes the command - Capture '--help' or argument errors (e.g: Typos)
        try:
            arg = cmd_apps.parse_args(args)
        except SystemExit:
            return

        cmdapps()

    def do_echo(self, args):
        cmd_echo = argparse.ArgumentParser(description="Prints out whatever you pass it", prog='echo')
        cmd_echo.add_argument("text", metavar=("<text>"), help="The text to echo (\"in quotes\")", default=None)

        # Processes the command - Capture '--help' or argument errors (e.g: Typos)
        try:
            arg = cmd_echo.parse_args(args)
        except SystemExit:
            return

        # formatting
        if '\\t' in arg.text:
            arg.text = arg.text.replace('\\t', '\t')
        if '\\n' in arg.text:
            arg.text = arg.text.replace('\\n', '\n')

        print(arg.text)

    def do_scripts(self, args):
        cmd_scripts = argparse.ArgumentParser(description="Lists all the scripts in your \\bin\\ folder\n(not fully implimented)", prog='scripts')
        cmd_scripts.add_argument("-s", metavar=("<script>"), help="The script to modify", default=None)
        cmd_scripts.add_argument("--del", help="Deletes the script (reqs \"-s\")", action="store_true")
        cmd_scripts.add_argument("--edit", help="Edits the script (reqs \"-s\")", action="store_true")
        cmd_scripts.add_argument("--new", help="Creates a new script", action="store_true")

        # Processes the command - Capture '--help' or argument errors (e.g: Typos)
        try:
            arg = cmd_scripts.parse_args(args)
        except SystemExit:
            return

        cmdscripts()

    def do_dc(self, args):
        cmd_disconnect = argparse.ArgumentParser(description="Disconnect from a remote system", prog='disconnect{dc}')

        # Processes the command - Capture '--help' or argument errors (e.g: Typos)
        try:
            arg = cmd_disconnect.parse_args(args)
        except SystemExit:
            return

        cmddisconnect()

    def hdo_disconnect(self, args):
        self.do_dc(args)

    def do_connect(self, args):
        cmd_connect = argparse.ArgumentParser(description="Connect to another system on the net", prog='connect')
        cmd_connect.add_argument("ip", metavar=("<IP address>"), help="The address to connect to", default=None)
        cmd_connect.add_argument("-w", "--web", help="Open in default web browser", action="store_true")

        # Processes the command - Capture '--help' or argument errors (e.g: Typos)
        try:
            arg = cmd_connect.parse_args(args)
        except SystemExit:
            return

        # Main program code
        if arg.web:
            if tkinter_ui.disable_2V:
                tkinter_ui.disable_2()
            tkinter_ui.go_from(str(arg.ip))
        else:
            cmdconnect(arg.ip)

    def do_clear(self, args):
        cmd_clear = argparse.ArgumentParser(description="Clears the screen", prog='clear')

        # Processes the command - Capture '--help' or argument errors (e.g: Typos)
        try:
            arg = cmd_clear.parse_args(args)
        except SystemExit:
            return

        tkinter_ui.conlog.config(state='normal')
        tkinter_ui.conlog.delete(0.0, 'end')
        tkinter_ui.conlog.config(state='disabled')

    def hdo_cls(self, args):
        self.do_clear(args)

    def do_quick(self, args):
        cmd_quick = argparse.ArgumentParser(description="Opens a text file in QuickPad", prog='quick')
        cmd_quick.add_argument("-f", metavar=("<file>"), help="The file to open", default=None)

        # Processes the command - Capture '--help' or argument errors (e.g: Typos)
        try:
            arg = cmd_quick.parse_args(args)
        except SystemExit:
            return

        cmdquick(arg.f)

    def do_whois(self, args):
        cmd_whois = argparse.ArgumentParser(description="Request detailed information about an address\n(not implimented)", prog='whois')
        cmd_whois.add_argument("addr", metavar=("<address>"), help="The IP/WEB address to lookup", default=None)

        # Processes the command - Capture '--help' or argument errors (e.g: Typos)
        try:
            arg = cmd_whois.parse_args(args)
        except SystemExit:
            return

        cmdwhois(arg.addr)

    def do_nmap(self, args):
        cmd_nmap = argparse.ArgumentParser(description="Run a detailed scan on an address", prog='nmap')
        cmd_nmap.add_argument("-ip", metavar=("<address>"), help="The IP/WEB address to scan", default=None)

        # Processes the command - Capture '--help' or argument errors (e.g: Typos)
        try:
            arg = cmd_nmap.parse_args(args)
        except SystemExit:
            return

        if arg.ip:
            cmdnmap(arg.ip)
        else:
            cmdnmap()

    def do_cd(self, args):
        cmd_cd = argparse.ArgumentParser(description="Change the current working directory", prog='chdir{cd}')
        cmd_cd.add_argument("cd", metavar=("<folder>"), help="The folder to move to", default=None)

        # Processes the command - Capture '--help' or argument errors (e.g: Typos)
        try:
            arg = cmd_cd.parse_args(args)
        except SystemExit:
            return

        if can_run is not True:
            print('chdir{cd}: error: Access Denied')
            return

        cmdcd(arg.cd)

    def hdo_chdir(self, args):
        self.do_cd(args)

    def do_cat(self, args):
        cmd_cat = argparse.ArgumentParser(description="Displays the contents of a text file", prog='cat')
        cmd_cat.add_argument("file", metavar=("<file>"), help="The file to display", default=None)

        # Processes the command - Capture '--help' or argument errors (e.g: Typos)
        try:
            arg = cmd_cat.parse_args(args)
        except SystemExit:
            return

        cmdcat(arg.file)

    def hdo_type(self, args):
        self.do_cat(args)

    def do_ls(self, args):
        cmd_ls = argparse.ArgumentParser(description="Prints out the current working directory", prog='ls')

        # Processes the command - Capture '--help' or argument errors (e.g: Typos)
        try:
            arg = cmd_ls.parse_args(args)
        except SystemExit:
            return

        cmddir(settings.working_dir)

    def do_del(self, args):
        cmd_del = argparse.ArgumentParser(description="Deletes a file", prog='del')
        cmd_del.add_argument("file", metavar=("<file>"), help="The file to delete", default=None)

        # Processes the command - Capture '--help' or argument errors (e.g: Typos)
        try:
            arg = cmd_del.parse_args(args)
        except SystemExit:
            return

        cmddel(arg.file)

    def hdo_payme(self, args):
        print('$%s' % settings.payme)

    def hdo_easybits(self, args):
        print('%sB' % settings.bits)

    def hdo_cheat(self, args):
        cmd_cheat = argparse.ArgumentParser(prog='cheat')
        cmd_cheat.add_argument("cheat", metavar=("<code>"), default=None)

        # Processes the command - Capture '--help' or argument errors (e.g: Typos)
        try:
            arg = cmd_cheat.parse_args(args)
        except SystemExit:
            return

        cmdcheat(arg.cheat)

command_list = []
shown_c = 0
hidden_c = 0
for i in dir(Console):
    if 'hdo_' in i:
        hidden_c += 1
    elif 'do_' in i:
        command_list.append(i.split('do_')[1])
        shown_c += 1
help_commands = []
for i in command_list:
    help_commands.append('help %s' % i)
command_list = command_list + help_commands + player_apps + player_scripts
print('Loaded %s commands, and %s hidden commands.' % (shown_c, hidden_c))


def reload_autofill():
    reload_scripts()
    reload_apps()
    global command_list
    command_list = []
    for i in dir(Console):
        if 'do_' in i:
            command_list.append(i.split('do_')[1])
    help_commands = []
    for i in command_list:
        help_commands.append('help %s' % i)
    command_list = command_list + help_commands + player_apps + player_scripts

# These comments are temporary
"""
> whois <webaddress>
Domain Name: <webaddress in CAPS>
Domain Status: ok
Registrant Name: <persons name>
Registrant Organization:
Registrant Street:
Registrant City:
Registrant State/Providence:
Registrant Postal Code:
Registrant Country: <country-code>
Registrant Phone:
Registrant Email:

> whois <IP address>
Information related to '<IP name>'
person: <persons name>
e-mail:
address: <person/company>
address: <street, city, postal, state/providence, country-name>
phone:
country: <country-code>
source: WHOIS
"""

"""
> nmap <location>
Starting Nmap..
Scanning <location> (<IP>):
PORT    STATE   SERVICE  VERSION
ID/tcp  open    <name>   <Name of whatever the service is and version>
Device type: general perpose
Running: <os name>
OS details: <os name and version>
"""

# Assets for command functions
print('Loading Command Assets...')


def get_dir(command=False):
    # Calling
    if command is False:
        command = 'dir "%s\\"' % settings.working_dir
    dir_tree = ''
    dirs = []
    others = []
    dir_call = subprocess.check_output(command, shell=True)
    # Stripping
    for line in dir_call.splitlines():
        if 'AM' in line:
            dir_tree = dir_tree + line.split('AM')[1] + '\n'
        elif 'PM' in line:
            dir_tree = dir_tree + line.split('PM')[1] + '\n'
    # Sorting (Dirs first):
    for line in dir_tree.splitlines():
        if '<DIR>' in line:
            dirs.append(line)
        else:
            others.append(line)
    dir_tree = ''
    for dir in sorted(dirs, key=str.lower):
        dir_tree = dir_tree + dir + '\n'
    for file in sorted(others, key=str.lower):
        dir_tree = dir_tree + file + '\n'
    return dir_tree


def get_ufile_path(file):
    file = file.strip().rstrip()
    if os.path.isfile(os.path.join(settings.working_dir, file)):
        return os.path.join(settings.working_dir, file)
    elif os.path.isfile(os.path.join(settings.player_home, 'bin\\', file)):
        return os.path.join(settings.player_home, 'bin\\', file)
    elif file.startswith('\\'):
        file = file.split('\\', 1)[1]
        if os.path.isfile(os.path.join(settings.player_home, file)):
            return os.path.join(settings.player_home, file)
        elif os.path.isfile(os.path.join(settings.system_home, file)):
            return os.path.join(settings.system_home, file)
        else:
            return False
    else:
        return False


def get_upath(path):
    if os.path.exists(os.path.join(settings.working_dir, path)):
        return os.path.join(settings.working_dir, path)
    elif os.path.exists(os.path.join(settings.player_home, path)):
        return os.path.join(settings.player_home, path)
    elif os.path.exists(os.path.join(settings.system_home, path)):
        return os.path.join(settings.system_home, path)
    else:
        return False


def movewd(new_dir):
    if new_dir.startswith('\\'):
        new_dir = new_dir.split('\\', 1)[1]
    if os.path.exists(os.path.join(settings.user_dir, settings.username.lower(), new_dir)):
        settings.working_dir = os.path.join(settings.user_dir, settings.username.lower(), new_dir)
        output.append('Moved Player @ %s' % settings.working_dir)
    else:
        return False
# Input Example: '\\systems\\[11.111.11.1]\\os_root_dir'


print('Done Loading Command Assets.')
# Command functions
print('Loading Command Functions...')


# cheat "exploit_setpayme 999999999.99"
def cmdcheat(cheat):
    if 'exploit_addpayme' in cheat:
        cheat = cheat.split('exploit_addpayme')[1].strip().rstrip()
        wallet.add('payme', settings.payme_ac, float(cheat))
    elif 'exploit_setpayme' in cheat:
        cheat = cheat.split('exploit_setpayme')[1].strip().rstrip()
        wallet.set('payme', settings.payme_ac, float(cheat))
    elif 'exploit_rempayme' in cheat:
        cheat = cheat.split('exploit_rempayme')[1].strip().rstrip()
        wallet.remove('payme', settings.payme_ac, float(cheat))

    elif 'exploit_addeasybits' in cheat:
        cheat = cheat.split('exploit_addeasybits')[1].strip().rstrip()
        wallet.add('easybits', settings.easybits_ac, float(cheat))
    elif 'exploit_seteasybits' in cheat:
        cheat = cheat.split('exploit_seteasybits')[1].strip().rstrip()
        wallet.set('easybits', settings.easybits_ac, float(cheat))
    elif 'exploit_remeasybits' in cheat:
        cheat = cheat.split('exploit_remeasybits')[1].strip().rstrip()
        wallet.remove('easybits', settings.easybits_ac, float(cheat))

    elif 'exploit_addrank' in cheat:
        cheat = cheat.split('exploit_addrank')[1].strip().rstrip()
        try:
            settings.player_rank = settings.player_rank + int(cheat)
        except:
            print('error: problem')
    elif 'exploit_setrank' in cheat:
        cheat = cheat.split('exploit_setrank')[1].strip().rstrip()
        try:
            settings.player_rank = int(cheat)
        except:
            print('error: problem')
    elif 'exploit_remrank' in cheat:
        cheat = cheat.split('exploit_remrank')[1].strip().rstrip()
        try:
            settings.player_rank = settings.player_rank - int(cheat)
            if settings.player_rank <= 0:
                settings.player_rank = 0
        except:
            print('error: problem')

    elif 'exploit_addexp' in cheat:
        cheat = cheat.split('exploit_addexp')[1].strip().rstrip()
        try:
            settings.player_exp = settings.player_exp + int(cheat)
        except:
            print('error: problem')
    elif 'exploit_setexp' in cheat:
        cheat = cheat.split('exploit_setexp')[1].strip().rstrip()
        try:
            settings.player_exp = int(cheat)
        except:
            print('error: problem')
    elif 'exploit_remexp' in cheat:
        cheat = cheat.split('exploit_remexp')[1].strip().rstrip()
        try:
            settings.player_exp = settings.player_exp - int(cheat)
            if settings.player_exp <= 0:
                settings.player_exp = 0
        except:
            print('error: problem')

    elif 'exploit_makeip' in cheat:
        cheat = cheat.split('exploit_makeip')[1].strip().rstrip()
        if cheat == '':
            cheat = '1'
        if '.' in cheat:
            if ',' in cheat:
                for system in cheat.split(','):
                    print(sys_make.create_ip(system.strip().rstrip()))
            else:
                print(sys_make.create_ip(cheat))
        else:
            try:
                for i in range(int(cheat)):
                    print(sys_make.gen_IP(seed=None, create=True))
            except:
                print('error: problem')


def cmdcat(file):
    if get_ufile_path(file) is not False:
        file_dir = get_ufile_path(file)
    else:
        print('quick: error: file does not exist')
        return
    if not file.endswith(settings.text_types):
        print('cat: error: file is not a text document')
        return
    if can_run is not True:
        if settings.player_home not in file_dir:
            print('cat: error: Access Denied')
            return
    with open(file_dir, 'r') as f:
        print('')
        for line in f.readlines():
            print(line.rsplit('\n', 1)[0])


def cmdquick(file=None):
    if file is None:
        tkinter_ui.pad_open()
        return
    if get_ufile_path(file) is not False:
        file_dir = get_ufile_path(file)
    else:
        print('quick: error: file does not exist')
        return
    if not file.endswith(settings.text_types):
        print('quick: error: file is not a text document')
        return
    if can_run is not True:
        if settings.player_home not in file_dir:
            print('quick: error: Access Denied')
            return
    tkinter_ui.pad_insert(file_dir, file)


def cmddel(file):
    if file.strip().rstrip() == '*':
        if '\\' in file:
            filedir = get_upath(file.rsplit('*', 1)[0])
        else:
            filedir = settings.working_dir
        for file in os.listdir(filedir):
            try:
                os.remove(os.path.join(filedir, file))
                print('del: "%s" was removed' % file)
            except:
                print('del: error: "%s" could not be removed' % file)
        reload_autofill()
        tkinter_ui.concom.set_completion_list(command_list)
        return
    file_dir = '##noFile##'
    if os.path.isfile(os.path.join(settings.working_dir, file)):
        file_dir = os.path.join(settings.working_dir, file)
    elif file.startswith('\\'):
        if os.path.isfile(os.path.join(settings.player_home, file)):
            file_dir = os.path.join(settings.player_home, file)
        elif os.path.isfile(os.path.join(settings.system_home, file)):
            file_dir = os.path.join(settings.system_home, file)
    if not file_dir.endswith(settings.text_types + settings.file_types + tuple('*')):
        print('del: error: "%s" is not a valid file' % file)
        return
    if can_run is not True:
        if settings.player_home not in file_dir:
            print('del: error: Access Denied')
            return
    if os.path.isfile(file_dir):
        os.remove(file_dir)
        print('del: "%s" was removed' % file)
    else:
        print('del: error: "%s" is not a valid file' % file)
    reload_autofill()
    tkinter_ui.concom.set_completion_list(command_list)


def cmdapps():
    apps = ''
    for i in sorted(player_apps):
        apps = apps + str(i) + '  '
    apps = apps + '\n'
    print(apps)


def cmdscripts():
    scripts = ''
    for i in sorted(player_scripts):
        scripts = scripts + str(i) + '  '
    scripts = scripts + '\n'
    print(scripts)


def cmdwhois(address):
    print('whois is not yet implimented')


def cmdnmap(address=None):
    # print(address)
    if address is None:
        if settings.system_id == '':
            print('[127.0.0.1]')
            print('ssh: Open')
            return
        print(settings.system_id)
        with open(settings.system_home.rsplit('os_root_dir', 1)[0] + 'nmap.ini', 'r') as f:
            for line in f.readlines():
                if '=' in line:
                    line = line.split('=', 1)
                    print('%s: %s' % (line[0], line[1]))


def cmddisconnect():
    output.append('\n%s\nDisconnection' % settings.get_time())
    # ===== Debug Setting
    # raise ValueError
    # =====

    if os.path.exists(settings.user_dir + settings.username.lower() + '\\systems\\user_home\\os_root_dir'):
        global can_run
        can_run = True
        if settings.system_home == settings.user_dir + settings.username.lower() + '\\systems\\user_home\\os_root_dir':
            return
        print('Disconnecting from %s...' % settings.system_id)
        movewd('\\systems\\user_home\\os_root_dir')
        settings.system_home = settings.user_dir + settings.username.lower() + '\\systems\\user_home\\os_root_dir'
        settings.system_id = ''
        settings.system_ip = settings.player_ip
        if not settings.current_ip == settings.player_ip:
            settings.current_ip = settings.player_ip
            print('Spoofing was canceled\nYour real ip is now in use')

    tkinter_ui.update_folders()


def cmdconnect(system):
    cmddisconnect()
    output.append('\n%s\nConnection @ [%s]' % (settings.get_time(), system))
    print("Connecting to [%s]..." % system)

    if system in settings.world_IPs:
        if os.path.exists(settings.user_dir + settings.username.lower() + '\\systems\\[%s]\\os_root_dir' % system):
            movewd('\\systems\\[%s]\\os_root_dir' % system)
            settings.system_home = settings.user_dir + settings.username.lower() + '\\systems\\[%s]\\os_root_dir' % system
            settings.system_id = '[%s]' % system
            print('Connection established.')
        else:
            settings.system_home = settings.user_dir + settings.username.lower() + '\\systems\\[%s]' % system
            output.append('\n%s\n===== !System Creation! =====\n%s' % (settings.get_time(), settings.system_home))
            sys_make.build_sys(settings.system_home, IP=system)
            settings.system_home = settings.system_home + '\\os_root_dir'
            movewd('\\systems\\[%s]\\os_root_dir' % system)
            settings.system_id = '[%s]' % system
            print('Connection established.')
        sys_make.create_ip(system, type='visited')
        settings.system_ip = system
        global can_run
        can_run = False
    else:
        print('error: unable to connect to "%s" | server does not exist!' % system)
        output.append('Location does not exist @ [%s]' % system)
    tkinter_ui.update_folders()


def cmdcd(des):

    if '/' in des:
        des = des.replace('/', '\\')
    if des == '\\' or des == '.':
        settings.working_dir = settings.system_home
        tkinter_ui.update_folders()
        return
    if des == '..':

        if not settings.working_dir.endswith('os_root_dir'):
            settings.working_dir = settings.working_dir.rsplit('\\', 1)[0]
        else:
            print('error: cannot move higher')
        tkinter_ui.update_folders()
        return

    if os.path.exists(os.path.join(settings.working_dir, des)):
        settings.working_dir = os.path.join(settings.working_dir, des)
    elif os.path.exists(os.path.join(settings.system_home, des)):
        settings.working_dir = os.path.join(settings.system_home, des)
    else:
        print('error: directory does not exist')
    tkinter_ui.update_folders()


def cmddir(dir, printd=True):
    if dir.startswith('\\'):
        dir = dir.split('\\', 1)[1]
    location = get_upath(dir)
    if location is not False:
        if not location.endswith('\\'):
            location = location + '\\'
    else:
        printd = False
    if printd:
        if settings.player_home not in location:
            if can_run:
                print(" Directory of %s\n" % (settings.system_id + (location).split('os_root_dir', 1)[1]))
            else:
                print('dir: error: Access Denied - using local dir')
                location = os.path.join(settings.player_home, dir)
                print(" Directory of %s\n" % ((location).split('os_root_dir', 1)[1]))
        else:
            if not settings.system_id.strip() == '':
                if can_run:
                    print('dir: directory does not exist in connection')
                else:
                    print('dir: error: Access Denied - using local dir')
                    location = os.path.join(settings.player_home, dir)
            print(" Directory of %s\n" % ((location).split('os_root_dir', 1)[1]))
    if location is False:
        print('dir: directory does not exist')
        return
    command = 'dir "%s"' % location
    for line in get_dir(command).split('\n'):
        if '<DIR>' in line:
            print('   [%s]' % line.split('<DIR>', 1)[1].strip())
        elif line.endswith(('.txt', '.log')):
            print('    F: %s' % line.strip().split(' ', 1)[1].strip())
        elif line.endswith(('.sh')):
            print('    S: %s' % line.strip().split(' ', 1)[1].strip())
        elif line.endswith(('.app')):
            print('    A: %s' % line.strip().split(' ', 1)[1].strip())
        elif not line.endswith(settings.file_types):
            continue
        elif not ('Dir' in line) or not ('File' in line):
            print('    ?: %s' % line.split(' ', 1)[1].strip())
    print('\n')


print('Done Loading Command Functions.')

output = []

""" Main Run function """
print_out = True
running_script = False
running_command = False


def run(command):
    global output
    global print_out
    global running_script
    global running_command
    running_command = True
    dobreak = False
    if print_out:
        print('\n%s\nExecuting Player Command @ "%s"' % (settings.get_time(), command))
    command = command.replace('\\', '\\\\')
    with stdout_redirect(StringIO.StringIO()) as new_stdout:
        # Parses the passed 'args'
        if not command.strip() == '':
            if command.startswith('@'):
                command = command.split('@', 1)[1]
            try:
                sys_args = shlex.split(command)
            except Exception as err:
                output.append('shell: error: ' + str(err))
                print('error: ' + str(err))
                dobreak = True
        if dobreak is not True:
            if 'do_' + sys_args[0] in dir(Console):
                function = sys_args[0]
                sys_args.pop(0)
                fn = 'Console().do_%s(%s)' % (function, sys_args)
                eval(fn)
            elif 'hdo_' + sys_args[0] in dir(Console):
                function = sys_args[0]
                sys_args.pop(0)
                fn = 'Console().hdo_%s(%s)' % (function, sys_args)
                eval(fn)
            else:
                script = sys_args[0]
                sys_args.pop(0)
                if script.endswith('.app'):
                    if get_ufile_path(script) is not False:
                        apps.run(get_ufile_path(script), sys_args)
                    else:
                        print('"%s" is not a valid command, app, or script' % script)
                        return
                elif script.endswith('.sh'):
                    if running_script:
                        print('You cannot run a script from another script, sorry.')
                        return
                    script_dir = None
                    if get_ufile_path(script) is not False:
                        script_dir = get_ufile_path(script)
                        apps.run(script_dir, sys_args)
                    if script_dir is None:
                        print('"%s" is not a valid command, app, or script' % script)
                        return
                    with open(script_dir, 'r') as file:
                        print_out = False
                        linenum = 0
                        for line in file.readlines():
                            linenum += 1
                            line = line.replace('\n', '')
                            if '#' in line:
                                output.append('Script Comment: "%s" | Line: %s' % ('#' + line.split('#', 1)[1], linenum))
                                line = line.split('#', 1)[0].strip().rstrip()
                            if line == '':
                                continue
                            output.append('%s-Executing Script Command @ "%s" | Line: %s' % (settings.get_time(), line, linenum))
                            tkinter_ui.send(line)
                    print_out = True
                    running_script = False
                else:
                    print('"%s" is not a valid command, app, or script' % script)

    new_stdout.seek(0)
    running_command = False
    for i in output:
        print(i)
    output = []
    return new_stdout.read()

print('\n\nFinished Loading Game @ %s\n' % settings.get_time())
