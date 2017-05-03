#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
============================================================
This file is licensed under the "GNU General Public License v3.0"
And is provided by;
"Allison Marie Bennett", TheCyaniteProject@gmail.com
============================================================
Game Settings
============================================================
"""
from time import strftime
import os
import configparser
import random


def get_time():
    return strftime('%Y-%m-%d %H:%M.%S')

print('Loading Game @ {}\n{}\n\nHello world!\n'.format(get_time(), os.getcwd()))


# Settings and Configuration
print('Loading Default Settings...')
# Game settings
title = 'Exit.Code() - Exit Reality.'
settings_file = 'data\\config.ini'
game_dir = os.getcwd()
no_warning = False

# Default Configs
default_user = 'none'
user_dir = '%game_dir%\\data\\users\\'
generation_ini = 'data\\gen.py'
game_seed = 'default'


player_rank = 1
player_exp = 0
exp_multi = 100
player_ip = '0.0.0.0'
current_ip = player_ip

email_ac = None
payme_ac = None
easybits_ac = None

payme = 0.0
bits = 0.0
wallet_multi = 100
wallet_tax = 0.0

# Caps
rank_cap = 99999999999
exp_max = 99999999999
payme_max = 999999999.99
payme_min = 0.0001
bits_max = 9999999.9999
bits_min = 0.000001

"""==========
Payme \ Bits Converion Rates
Payme \ Bits: 100.0 \ 1.0 (payme / 100.0)
Bits \ Payme: 1.0 \ 100.0 (bits * 100.0)
=========="""

# Other Variable Creation
systemRestart = False
user_home_dir = '\\systems\\user_home\\os_root_dir'
system_id = ''
file_types = ('.sh', '.txt', '.log', '.app', '.contact')
text_types = ('.sh', '.txt', '.log')

pronouns = {
    'female': ['She', 'Her', 'Her\'s'],
    'male': ['He', 'His', 'His'],
    'floofball': [
        '"RainbowDashies\' Pyromancing Floof-ball"',
        '"RainbowDashies\' Pyromancing Floof-ball"\'s',
        '"RainbowDashies\' Pyromancing Floof-ball"\'s']
}

# System stuff
world_IPs = []
discovered_IPs = []
visited_IPs = []
max_ip_gen = 15


# Other
conf = configparser.ConfigParser()
seeded = random.Random()
seeded.seed(game_seed)

print('Done Loading Defaults.')


def hashpass(key):
    key = key.strip().rstrip()
    sha = hashlib.sha256(key.encode()).hexdigest()
    return sha


# Loading Settings
def load_game_settings():
    global user_dir
    global game_seed
    global default_user
    global username
    global user_home_dir
    print('Loading Game Config..')
    if os.path.isfile(settings_file) is not True:
        print('error: settings file not found! - "%s\\%s" - falling back to defaults' % (game_dir, settings_file))
    else:
        conf.read(settings_file)
        if 'system' in conf.sections():
            items = [i for (i, n) in conf['system'].items()]
            if 'default_user' in items:
                default_user = conf['system']['default_user']
                username = default_user
            if 'user_dir' in items:
                user_dir = conf['system']['user_dir']
            if 'user_home_dir' in items:
                user_home_dir = conf['system']['user_home_dir']
            if 'default_seed' in items:
                game_seed = conf['system']['default_seed']

    if '%game_dir%' in user_dir:
        user_dir = ''.join((game_dir, user_dir.split('%game_dir%')[1]))
    print('Done Loading Game Config.')


def load_player_settings():
    global username
    global game_seed
    global player_rank
    global player_exp
    global bits
    global payme
    global exp_multi
    global payme_ac
    global easybits_ac
    global email_ac
    global player_ip
    print('Loading Player Config..')
    if os.path.isfile(('%s%s\\user.ini' % (user_dir, username.lower())).split(game_dir + '\\')[1]) is not True:
        print('error: settings file not found! - "%s" - falling back to defaults' % (('%s%s\\user.ini' % (user_dir, username.lower())).split(game_dir + '\\')[1]))
    else:
        conf.read(('%s%s\\user.ini' % (user_dir, username.lower())).split(game_dir + '\\')[1])
        if 'info' in conf.sections():
            items = [i for (i, n) in conf['info'].items()]
            if 'username' in items:
                username = conf['info']['username']
            if 'seed' in items:
                game_seed = conf['info']['seed']
            if 'ranking' in items:
                player_rank = int(conf['info']['ranking'])
            if 'exp' in items:
                player_exp = int(conf['info']['exp'])
            if 'easybits_ac' in items:
                easybits_ac = conf['info']['easybits_ac']
            if 'payme_ac' in items:
                payme_ac = conf['info']['payme_ac']
            if 'email_ac' in items:
                email_ac = conf['info']['email_ac']
            if 'player_ip' in items:
                player_ip = conf['info']['player_ip']

    exp_multi = exp_multi * player_rank
    print('Done Loading Player Config.')
load_game_settings()
load_player_settings()
# os.system('pause')     # Debug

"""
login_creds = {
    'cyanite':{
        'email.com':[True, 'cyanite@email.com'],
        'easybits.com':[True, 'cyanite_GHpNWEx8BQ0'],
        'payme.net':[True, 'cyanite_GHpNWEx8BQ0']
        }
    }"""

login_creds = {username.lower(): {}}

# User Wallet Loading
if payme_ac is not None:
    with open('%s%s\\wallets\\payme\\%s.ini' % (user_dir, username.lower(), payme_ac), 'r') as f:
        try:
            payme = float(f.readlines()[0].strip().rstrip())
            login_creds[username.lower()]['payme.net'] = [True, str(payme_ac.strip().rstrip())]
        except:
            print('!!!Could not load Payme Balence!!!')

if easybits_ac is not None:
    with open('%s%s\\wallets\\easybits\\%s.ini' % (user_dir, username.lower(), easybits_ac), 'r') as f:
        try:
            bits = float(f.readlines()[0].strip().rstrip())
            login_creds[username.lower()]['easybits.com'] = [True, str(easybits_ac.strip().rstrip())]
        except:
            print('!!!Could not load Easybits Balence!!!')

# User Email Loading
if email_ac is not None:
    try:
        login_creds[username.lower()]['email.com'] = [True, str(email_ac.strip().rstrip())]
    except:
        print('!!!Could not load Email account!!!')


# Load Existing IPs
def load_world_IPs():
    global world_IPs
    world_IPs = []
    if os.path.isfile('%s%s\\systems\\worldips.ini' % (user_dir, username.lower())):
        with open('%s%s\\systems\\worldips.ini' % (user_dir, username.lower()), 'r') as f:
            for system in f.readlines():
                world_IPs.append(system.strip().rstrip())
load_world_IPs()


def load_discovered_IPs():
    global discovered_IPs
    discovered_IPs = []
    if os.path.isfile('%s%s\\systems\\discoveredips.ini' % (user_dir, username.lower())):
        with open('%s%s\\systems\\discoveredips.ini' % (user_dir, username.lower()), 'r') as f:
            for system in f.readlines():
                if system.strip().rstrip() in world_IPs:
                    discovered_IPs.append(system.strip().rstrip())
                else:
                    print('orphaned system: {} from DISCOVERED'.format(system))
load_discovered_IPs()


def load_visited_IPs():
    global visited_IPs
    visited_IPs = []
    if os.path.isfile('%s%s\\systems\\visitedips.ini' % (user_dir, username.lower())):
        with open('%s%s\\systems\\visitedips.ini' % (user_dir, username.lower()), 'r') as f:
            for system in f.readlines():
                if system.strip().rstrip() in world_IPs:
                    visited_IPs.append(system.strip().rstrip())
                else:
                    print('orphaned system: {} from VISITED'.format(system))
load_visited_IPs()

# ===== Debug Output
print('\n===== User Config Settings =====')
print('username = {}'.format(username))
print('user_dir = {}'.format(user_dir))
print('user_home_dir = {}'.format(user_home_dir))
print('game_seed = {}'.format(game_seed))
print('=====\n')

print('=====\nAccount Ranking: {uname} | Rank: {rank} - EXP: {exp}/{exp_mult}\n=====\n'.format(uname=username, rank=player_rank, exp=player_exp, exp_mult=exp_multi))
print('=====\nAccount Balance: {uname} | Payme: {payme} - Bits: {bits}\n=====\n'.format(uname=username, payme=payme, bits=bits))

# =====

working_dir = os.path.join(user_dir, username.lower(), 'systems\\user_home\\os_root_dir')
system_home = working_dir  # Current Dir
system_ip = player_ip      # Current System IP
current_ip = system_ip     # Spoofable IP
player_home = working_dir  # Never changes
print('Moved player @ {}'.format(working_dir))
