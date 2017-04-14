
"""============================================================
This file is licensed under the "GNU General Public License v3.0"
And is provided by;
"Allison Marie Bennett", TheCyaniteProject@gmail.com
============================================================"""

""" DO NOT CHANGE VARIABLE NAMES """
with open('data\\names\\names_female.log', 'r') as f:
    female_names = [line for line in f.read().split('\n')]
female_names_loaded = '%s Female names loaded.' % len(female_names)

with open('data\\names\\names_male.log', 'r') as f:
    male_names = [line for line in f.read().split('\n')]
male_names_loaded = '%s Male names loaded.' % len(male_names)

with open('data\\names\\names_last.log', 'r') as f:
    last_names = [line for line in f.read().split('\n')]
last_names_loaded = '%s Last names loaded.' % len(last_names)


usernames = ['username1', 'username2', 'username3']

file_names = 'logged.log/log.txt/loot.log/new.log/New Text Document.txt/New Log File.log/system.log'

linux = {
    'os_root_dir' : {
        'users' : {
            '<username>' : {
                'Desktop' : {file_names:'IP-LISTT/none/none'},
                'Contacts' : {},
                'Documents' : {file_names:'LOGIN-LIST/IP-LIST/none/none'},
                'Downloads' : {file_names:'IP-LIST/IP-LIST/none',
                                file_names:'SAFE-GUARD'
                                },
                'WebDrive' : {}
            }
        },
        'bin' : {},
        'system' : {
            'bin' : {},
            'logs' : {},
            'etc' : {
                'hosts' : {},
                'passwd' : {}
            }
        }
    }
}

windows = linux

player = {
    'os_root_dir' : {
        'users' : {
            '<username>' : {
                'Desktop' : {},
                'Contacts' : {},
                'Documents' : {},
                'Downloads' : {},
                'WebDrive' : {}
            }
        },
        'bin' : {},
        'system' : {
            'bin' : {},
            'logs' : {},
            'etc' : {
                'hosts' : {},
                'passwd' : {}
            }
        }
    }
}

system_list = [linux, windows]


