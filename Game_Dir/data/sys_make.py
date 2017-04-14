#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
============================================================
This file is licensed under the "GNU General Public License v3.0"
And is provided by;
"Allison Marie Bennett", TheCyaniteProject@gmail.com
============================================================
System Creation
============================================================
"""

import os
import data.settings as settings
import data.wallet as wallet
import data.mail as mail
from data.gen import *
import random
import string
# Most of this file is going to be replaced in the near future when i switch from a "folder" system (real folders)

ip_list2 = []
__FILLER__ = '----- DO NOT DELETE THIS FILE -----\nThis file is here to keep your system from removing this folder when it is empty.\nIt is required for my game to work properly!'


test_profile = {
    'alias': 'Jane',
    'username': 'test001',
    'pronouns': 'female',
    'seed': 'testSeed001',
    'player_ip': '111.111.111.111',
    'email_ac': 'test001@email.com',
    'easybits_ac': 'test001_1234567890',
    'payme_ac': 'test001_1234567890',
}


def make_player_profile(dict):
    # user.ini contents
    try:
        profile = '[info]\n'
        profile = profile + 'alias=%s\n' % dict['alias']
        profile = profile + 'username=%s\n' % dict['username']
        profile = profile + 'pronouns=%s\n' % dict['pronouns']
        profile = profile + 'seed=%s\n' % dict['seed']
        profile = profile + 'player_ip=%s\n' % dict['player_ip']
        profile = profile + 'email_ac=%s\n' % dict['email_ac']
        profile = profile + 'easybits_ac=%s\n' % dict['easybits_ac']
        profile = profile + 'payme_ac=%s\n' % dict['payme_ac']
        profile = profile + 'ranking=1\n'
        profile = profile + 'exp=0\n'
        profile_dir = os.path.join(settings.user_dir, dict['username'].lower())
    except:
        return [False, 'profileCreationErr']
    if 'pm_bal' not in dict:
        dict['pm_bal'] = 1000.0
    if 'eb_bal' not in dict:
        dict['eb_bal'] = 10.0
    """
    The Following Lines create the File/Folder strcuture for the Game
    """
    # Create User Directory
    if not os.path.exists(profile_dir):
        os.makedirs(profile_dir)
    if not os.path.isfile(os.path.join(profile_dir, 'user.ini')):
        with open(os.path.join(profile_dir, 'user.ini'), 'w') as f:
            f.write(profile)
    # Create Wallets Directory
    if not os.path.exists(os.path.join(profile_dir, 'wallets\\')):
        os.makedirs(os.path.join(profile_dir, 'wallets\\'))
    if not os.path.exists(os.path.join(profile_dir, 'wallets\\', 'payme\\')):
        os.makedirs(os.path.join(profile_dir, 'wallets\\', 'payme\\'))
    if not os.path.exists(os.path.join(profile_dir, 'wallets\\', 'easybits\\')):
        os.makedirs(os.path.join(profile_dir, 'wallets\\', 'easybits\\'))

    # Create Sites Directory
    if not os.path.exists(os.path.join(profile_dir, 'sites\\')):
        os.makedirs(os.path.join(profile_dir, 'sites\\'))
    if not os.path.exists(os.path.join(profile_dir, 'sites\\', 'email\\')):
        os.makedirs(os.path.join(profile_dir, 'sites\\', 'email\\'))
    if not os.path.exists(os.path.join(profile_dir, 'sites\\', 'email\\', 'mail\\')):
        os.makedirs(os.path.join(profile_dir, 'sites\\', 'email\\', 'mail\\'))
    if not os.path.isfile(os.path.join(profile_dir, 'sites\\', 'email\\', 'mail\\', 'sys')):
        with open(os.path.join(profile_dir, 'sites\\', 'email\\', 'mail\\', 'sys'), 'w') as f:
            f.write(__FILLER__)
    if not os.path.isfile(os.path.join(profile_dir, 'sites\\', 'email\\', 'logins.ini')):
        with open(os.path.join(profile_dir, 'sites\\', 'email\\', 'logins.ini'), 'w') as f:
            f.write('')
    if not os.path.exists(os.path.join(profile_dir, 'sites\\', 'payme\\')):
        os.makedirs(os.path.join(profile_dir, 'sites\\', 'payme\\'))
    if not os.path.isfile(os.path.join(profile_dir, 'sites\\', 'payme\\', 'site.ini')):
        with open(os.path.join(profile_dir, 'sites\\', 'payme\\', 'site.ini'), 'w') as f:
            f.write('[settings]\nsitelocker=1.0\nriddleme=True')
    if not os.path.isfile(os.path.join(profile_dir, 'sites\\', 'email\\', 'site.ini')):
        with open(os.path.join(profile_dir, 'sites\\', 'email\\', 'site.ini'), 'w') as f:
            f.write('[settings]\nsitelocker=1.0\nriddleme=True')
    if not os.path.exists(os.path.join(profile_dir, 'sites\\', 'easybits\\')):
        os.makedirs(os.path.join(profile_dir, 'sites\\', 'easybits\\'))
    if not os.path.isfile(os.path.join(profile_dir, 'sites\\', 'easybits\\', 'site.ini')):
        with open(os.path.join(profile_dir, 'sites\\', 'easybits\\', 'site.ini'), 'w') as f:
            f.write('[settings]\nsitelocker=1.0\nriddleme=True')
    settings.username = dict['username']
    first_ip = gen_IP(create=False)
    first_email = '''
    TO:{to}
    FROM:unknown@shhmail.com
    BODY:Hello newcomer. You can call me Cyn. I don't know why you decided
    to get into this life, nor do I care.
    All I know is that I was told to send you on your way.


    {ip} - If you've got what it takes to lead this life, that's all you'll need.
    I'll contact you if i need anything.
    Don't reply to this address, I don't check it.

    P.S: I have wired you some starting funds. Better grab you some code if you don't
    have some already. I hear DataKult has some good ones. I attached a link.
    <link=datakult.shop text=[www.DataKult.shop]>
    <link=shhmail.net text=[Send Mail Anonamously with ShhMail.net]>
    '''.format(to='to', ip='ip')

    reload(mail)
    var = mail.send(mail.dict(first_email))
    if not var:
        raise Exception('mailError')
    # Create Systems Directory
    if not os.path.exists(os.path.join(profile_dir, 'systems\\')):  # Checks if user dir already exists
        os.makedirs(os.path.join(profile_dir, 'systems\\'))  # Creates dir if it does not
    for file in ['worldips.ini', 'visitedips.ini', 'discoveredips.ini']:
        if not os.path.isfile(os.path.join(profile_dir, 'systems\\', file)):
            with open(os.path.join(profile_dir, 'systems\\', file), 'w') as f:
                f.write(first_ip)
    # Build User Home System
    build_sys((os.path.join(profile_dir, 'systems\\', 'user_home\\')), tree=player, person=dict, player=True)

    return [True, None]


def check_systems():
    for system in settings.discovered_IPs:
        if system not in settings.visited_IPs:
            return [True, system]
    return [False, None]


def import_gen():  # ===== Replaced =====
    print('\n===== Importing Generation File =====')
    # Loading generation settings from generation_ini
    # if os.path.exists(settings.generation_ini):
        # exec('from %s import *' % settings.generation_ini.replace('.py', '').replace('\\', '.'))
    print(female_names_loaded)
    print(male_names_loaded)
    print(last_names_loaded)
    # else:
    #    print 'error: Could not load generation_ini @ %s' % settings.generation_ini
    #    raise SystemExit
    print('===== Finished Importing =====\n')
import_gen()


def check_ip(IP):
    _BL = ['1', '127', '168', '169', '192']
    # Checks if IP is valid :: IP must be exactly four segments of int()-able objects sepperated by a dot(.)
    # checks if the integer range is valid or not blacklisted
    try:
        ints = IP.split('.')  # Exception if no '.' in IP
        for segment in ints:
            if len(str(segment)) > 3:
                raise Exception('notValidIP')
            elif len(str(segment)) < 1:
                raise Exception('notValidIP')
            if int(segment) > 255:
                raise Exception('notValidIP')
            if int(segment) in _BL:
                raise Exception('notValidIP')
        # Exception if not at least four int()-able objects in IP
        int0 = int(ints[0])
        int1 = int(ints[1])
        int2 = int(ints[2])
        int3 = int(ints[3])

        IP2 = '.'.join((str(int0), str(int1), str(int2), str(int3)))  # Joins only the first four segments from IP as IP2
        if not IP2 == IP:  # Checks if IP2 == IP, Exception if IP had more than four segments
            raise Exception('notValidIP')
    except:
        return False
    return True


def create_ip(IP, type='world'):
    validity = check_ip(IP)
    if not validity:
        return False, 'notValidIP'
    # Saves newly-created IP to universe if not already exists
    if type in ['default', None, 'world']:
        if IP not in settings.world_IPs:
            settings.world_IPs.append(IP)
            with open('%s%s\\systems\\worldips.ini' % (settings.user_dir, settings.username.lower()), 'w') as f:
                for system in settings.world_IPs:
                    f.write(str(system) + '\n')
        else:
            return False, 'alreadyExists'
    if type == 'discovered':
        if IP not in settings.discovered_IPs:
            settings.discovered_IPs.append(IP)
            with open('%s%s\\systems\\discoveredips.ini' % (settings.user_dir, settings.username.lower()), 'w') as f:
                for system in settings.discovered_IPs:
                    f.write(str(system) + '\n')
            if IP not in settings.world_IPs:
                settings.world_IPs.append(IP)
                with open('%s%s\\systems\\worldips.ini' % (settings.user_dir, settings.username.lower()), 'w') as f:
                    for system in settings.world_IPs:
                        f.write(str(system) + '\n')
        else:
            return False, 'alreadyExists'
    if type == 'visited':
        if IP not in settings.visited_IPs:
            settings.visited_IPs.append(IP)
            with open('%s%s\\systems\\visitedips.ini' % (settings.user_dir, settings.username.lower()), 'w') as f:
                for system in settings.visited_IPs:
                    f.write(str(system) + '\n')
            if IP not in settings.discovered_IPs:
                settings.discovered_IPs.append(IP)
                with open('%s%s\\systems\\discoveredips.ini' % (settings.user_dir, settings.username.lower()), 'w') as f:
                    for system in settings.discovered_IPs:
                        f.write(str(system) + '\n')
            if IP not in settings.world_IPs:
                settings.world_IPs.append(IP)
                with open('%s%s\\systems\\worldips.ini' % (settings.user_dir, settings.username.lower()), 'w') as f:
                    for system in settings.world_IPs:
                        f.write(str(system) + '\n')
        else:
            return False, 'alreadyExists'
    # console.output.append('\n%s\nNew World IP created!' % settings.get_time())
    # Returns 'True' if no errors
    return True


def gen_IP(seed=None, create=True, guard=False):
    # Setting up seeding
    ipseed = random.Random()
    if seed is None:
        char = string.digits + string.letters + '_'
        seed = ''.join([random.choice(char) for i in range(16)])
    # Creates a random 'IP' within the following guide: Four segments of int()-able(numbers) between 30-230 sepperated by a dot(.)

    def new(seed):
        ip_sec = []
        for i in range(4):
            sec = '1'
            _MIN, _MAX = 30, 255  # Minimum IP val, Maximum IP val
            _BL = ['1', '127', '168', '169', '192']  # Blacklist values.
            while int(sec) in _BL:
                while int(sec) < _MIN:
                    ipseed.seed(seed + str(i) + str(sec))
                    sec = ipseed.choice([i for i in range(_MAX)])
            ip_sec.append(str(sec))
        return '.'.join((str(i) for i in ip_sec))
    IP = new(seed)
    # Create new IP if IP already exists locally
    while IP in ip_list2:
        IP = new(seed + IP)
        if guard:
            while IP in settings.world_IPs:
                IP = new(seed + IP + 'guard')
    ip_list2.append(str(IP))
    # Call create_ip if requested
    if create:
        create_ip(IP)
    return str(IP)


def make_IP_LIST(root, file, seed=None, guard=False):
    global ip_list2
    # Setting up seeding
    iplseed = random.Random()
    if seed is None:
        seed = settings.game_seed + root
    iplseed.seed(seed)
    # Starts creating IP list
    ip_list = []
    # Creates Starter IPs for new Players
    if len(settings.world_IPs) < 19:
        for i in range(20):
            gen_IP(seed + str(i))  # Creates 20 IPs, but does not add them to this list
    ip_num = iplseed.choice([i for i in range(settings.max_ip_gen)])  # Randomly decides how many IP's to use
    for i in range(int(ip_num)):
        iplseed.seed(seed + str(i))
        TF = iplseed.choice([True, False])  # Randomly Decides if -this- IP in the list should be New, or selected from the universe
        if TF:
            IP = iplseed.choice(settings.world_IPs)  # Randomly selects an IP from the universe
            while IP in ip_list:  # Makes sure there are no duplicates
                iplseed2 = iplseed
                iplseed2.seed(seed + str(i) + IP)
                IP = iplseed2.choice(settings.world_IPs)
            ip_list.append(IP)  # Adds IP to list
        else:
            ip_list.append(gen_IP(seed + str(i)))  # Creates new IP, and adds it to the list - gen_IP will check for duplicates on its own
    if guard:  # Makes sure atleast one IP in the list is new, so the player does not run out of systems
        ip_list.append(gen_IP(seed + 'guard', guard=True))
    return ip_list


def make_person(seed, IP=None, create=False, create_ip=False):
    def make_username(seed):  # Creates a username from the Non-Playable-Character details created under this function
        # Setting up seeding
        perseed = random.Random()
        perseed.seed(seed + 'fn')
        # Creates username
        char = string.digits + string.letters + '_'  # legal characters/symbols
        firstname_cut = perseed.choice([True, False])  # Should firstname be cut? ('Jane' = 'J')
        perseed.seed(seed + 'ln')  # Changes seed to increate randomness
        lastname_cut = perseed.choice([True, False])  # Should lastname be cut? ('Doe' = 'D')
        perseed.seed(seed + 'sl')  # Changes seed to increate randomness
        last = perseed.choice([True, False])  # Should lastname exist in username?
        if firstname_cut:  # Cuts firstname
            firstname = person['firstname'][0]
        else:
            firstname = person['firstname']
        if lastname_cut:  # Cuts lastname
            lastname = person['lastname'][0]
        else:
            lastname = person['lastname']
        perseed.seed(seed + 'char')  # Changes seed to increate randomness
        val = perseed.choice([i for i in range(10)])  # Chooses how many characters to randomly add to the end of the username
        end_bit = ''.join([perseed.choice(char) for i in range(val)])  # Randomly grabs (val) amount of characters from legal list to add
        if not end_bit == '':  # Checks if 'end_bit' is empty
            if last:
                var = perseed.choice([True, False])  # Decides order of first/last names in username
                if var:
                    username = (perseed.choice(['.', '_', ''])).join([firstname, lastname, end_bit])  # Creates username with random ('.','_','') sepperator
                else:
                    username = (perseed.choice(['.', '_', ''])).join([lastname, firstname, end_bit])  # Creates username with random ('.','_','') sepperator
            else:
                username = (perseed.choice(['.', '_', ''])).join([person['firstname'], end_bit])  # Creates username with random ('.','_','') sepperator
        else:
            if last:
                var = perseed.choice([True, False])  # Decides order of first/last names in username
                if var:
                    username = (perseed.choice(['.', '_', ''])).join([firstname, lastname])  # Creates username with random ('.','_','') sepperator
                else:
                    username = (perseed.choice(['.', '_', ''])).join([lastname, firstname])  # Creates username with random ('.','_','') sepperator
            else:
                username = person['firstname'] + (perseed.choice(['_', '']))  # Sets firstname as username
        return username.replace(' ', '_')  # Makes sure no nasty spaces exist by accident (some names, like "Dee Dee" contain a space)
    # Creates new Non-Playable-Character
    # Setting up seeding
    perseed = random.Random()
    perseed.seed(seed)
    char = string.digits + string.letters + '_'  # Legal characters/symbols for username
    person = {}
    person['sex'] = perseed.choice(['m', 'f'])  # Randomly desides sex
    if person['sex'] == 'm':  # Randomly chooses Male, or Female NPC name using decided sex from namelists
        person['firstname'] = perseed.choice(male_names)
    elif person['sex'] == 'f':
        person['firstname'] = perseed.choice(female_names)
    person['lastname'] = perseed.choice(last_names)  # Randomly chooses lastname from namelist
    if IP is None:  # Creates IP for NPC if one was not given
        person['IP'] = gen_IP(seed, create=create_ip)
    else:
        person['IP'] = IP
    person['username'] = make_username(seed + 'username')  # Creates NPC's username
    person['email'] = person['username'] + '@email.com'  # Turns username into email address
    perseed.seed(seed + 'bank1')  # Changes seed to increate randomness in lists
    varb1 = perseed.choice([True, False])  # Randomly decides if NPC has a 'Payme' account
    if varb1:  # If yes..
        perseed.seed(seed + 'payme')  # Changes seed to increate randomness in lists
        var = perseed.choice([True, False])  # Randomly decides if Payme username is the same as Default NPC username
        if var:
            person['payme'] = '_'.join([person['username'], ''.join([perseed.choice(char) for i in range(8)])])  # Changes NPC username into Payme username
        else:
            person['payme'] = '_'.join([make_username(seed + 'payme'), ''.join([perseed.choice(char) for i in range(8)])])  # Creates new username
        perseed.seed(seed + 'bank2')  # Changes seed to increate randomness in lists
        varb2 = perseed.choice([True, False])  # Randomly desides if NPC also has an 'EasyBits' account
        if varb2:  # If yes..
            perseed.seed(seed + 'easybits')  # Changes seed to increate randomness in lists
            var = perseed.choice([True, False])  # Randomly decides if EasyBits username is the same as Default NPC username
            if var:
                person['easybits'] = '_'.join([person['username'], ''.join([perseed.choice(char) for i in range(8)])])  # Changes NPC username into EasyBits username
            else:
                person['easybits'] = '_'.join([make_username(seed + 'easybits'), ''.join([perseed.choice(char) for i in range(8)])])  # Creates new username
        else:
            person['easybits'] = None  # Else sets Nul EasyBits username
    else:  # If no.. Creates an EasyBits account for NPC
        person['payme'] = None  # Else sets Nul Payme username
        perseed.seed(seed + 'easybits')  # Changes seed to increate randomness in lists
        var = perseed.choice([True, False])  # Randomly decides if EasyBits username is the same as Default NPC username
        if var:
            person['easybits'] = '_'.join([person['username'], ''.join([perseed.choice(char) for i in range(8)])])  # Changes NPC username into EasyBits username
        else:
            person['easybits'] = '_'.join([make_username(seed + 'easybits'), ''.join([perseed.choice(char) for i in range(8)])])  # Creates new username
    if not person['easybits'] is None:  # Creates EasyBits funds for NPC
        person['eb_bal'] = random.choice([(float(i) / 1000) for i in range(50000)])
    else:
        person['eb_bal'] = None
    if not person['payme'] is None:  # Creates Payme funds for NPC
        person['pm_bal'] = random.choice([(float(i) / 10) for i in range(50000)])
    else:
        person['pm_bal'] = None
    person['user_pass'] = make_username(seed + 'user_pass')  # Creates 'user' password for NPC (System,Email..)
    person['bank_pass'] = make_username(seed + 'bank_pass')  # Creates 'bank' password for NPC (Payme,EasyBits..)
    if len(person['user_pass']) < 8:  # Makes sure 'user' password is longer than 8 character
        person['user_pass'] = make_username(seed + 'user_pass' + person['user_pass'])
    if len(person['bank_pass']) < 8:  # Makes sure 'bank' password is longer than 8 character
        person['bank_pass'] = make_username(seed + 'user_pass' + person['bank_pass'])
    if len(person['user_pass']) > len(person['bank_pass']):  # Swops passwords if 'bank' is shorter than 'user' (making 'bank' the longer one)
        person['bank_pass'], person['user_pass'] = person['user_pass'], person['bank_pass']
    return person


# System Building
def build_sys(root, tree=None, new=True, person=None, seed=None, IP=None, player=False):
    """ Most of this function was given to me on www.StackOverflow.com, i will try and comment on what i understand """
    # Setting up seeding
    seeded = random.Random()
    if seed is None:
        seed = settings.game_seed
    seeded.seed(seed + root)
    # Creates system
    """
    A 'system' in this game is a file-tree located in the %%username%%\\systems\\ folder.
    Each system is created from a leveled/treed dictionary that represents a spesific OS
    These 'dictionary-trees' can be found in the data.gen script.
    """

    if new:
        if player is not True:
            if not os.path.exists(root.rsplit('\\, 1')[0]):  # Checks if root dir already exists
                os.makedirs(root)  # Creates dir if it does not
            with open(root.rsplit('\\, 1')[0] + '\\firewall.ini', 'a+') as f:  # Creates firewall.ini for 'hacking' :: Will be improved
                f.write('firewall=1.0')
            with open(root.rsplit('\\, 1')[0] + '\\nmap.ini', 'a+') as f:  # Creates nmap.ini for 'hacking' :: Will be improved
                f.write('ssh=Open')
            if person is None:  # If no NPC profile was supplied, creates one.
                person = make_person(seed + root, IP=IP)
            with open(root.rsplit('\\, 1')[0] + '\\npc.ini', 'a+') as f:  # Creates NPC npc.ini
                for n, v in person.iteritems():
                    if n not in ['pm_bal', 'eb_bal']:
                        f.write("%s=%s\n" % (n, v))
            if not person['payme'] is None:  # Creates NPC 'Payme' wallet
                wallet.create('payme', person['payme'], amount=person['pm_bal'], passw=person['bank_pass'], user={'email_ac': person['email'], 'IP': person['IP']})
            if not person['easybits'] is None:  # Creates NPC 'EasyBits' wallet
                wallet.create('easybits', person['easybits'], amount=person['eb_bal'], passw=person['bank_pass'], user={'email_ac': person['email'], 'IP': person['IP']})
            with open('%s%s\\sites\\email\\logins.ini' % (settings.user_dir, settings.username), 'r') as logins:  # Adds NPC email to global email logins list
                web_logins = []
                for login in logins.readlines():
                    web_logins.append(login.strip().rstrip())
            if not ('%s:%s:%s' % (person['username'], person['user_pass'], person['email'])) in web_logins:
                web_logins.append('%s:%s:%s' % (person['username'], person['user_pass'], person['email']))
                with open('%s%s\\sites\\email\\logins.ini' % (settings.user_dir, settings.username), 'w') as f:
                    for login in web_logins:
                        f.write(login + '\n')
        else:
            if person is None:
                return [False, 'noUserProfile']
            if not os.path.exists(root.rsplit('\\, 1')[0]):  # Checks if root dir already exists
                os.makedirs(root)  # Creates dir if it does not
            with open(root.rsplit('\\, 1')[0] + '\\firewall.ini', 'a+') as f:  # Creates firewall.ini for 'hacking' :: Will be improved
                f.write('firewall=1.0')
            with open(root.rsplit('\\, 1')[0] + '\\nmap.ini', 'a+') as f:  # Creates nmap.ini for 'hacking' :: Will be improved
                f.write('ssh=Open')
            if not person['payme_ac'] is None:  # Creates Player 'Payme' wallet
                wallet.create('payme', person['payme_ac'], amount=person['pm_bal'], profile=person['username'])
            if not person['easybits_ac'] is None:  # Creates Player 'EasyBits' wallet
                wallet.create('easybits', person['easybits_ac'], amount=person['eb_bal'], profile=person['username'])
            with open('%s%s\\sites\\email\\logins.ini' % (settings.user_dir, person['username']), 'w') as f:
                f.write('')
    if tree is None:  # Randomly picks OS-dictionary-tree from global list if one was not given
        if player:
            tree = player
        else:
            tree = seeded.choice(system_list)  # 'system_list' is a list of allowed OS-dictionary-trees imported from data.gen
    """ Here starts what i don't know much about """
    for k, v in tree.iteritems():
        # Filename
        if '/' in k:
            seeded.seed(seed + root + k)
            k = seeded.choice(k.split('/'))
        if "<username>" in k:
            if player is not True:
                k = k.replace("<username>", seeded.choice((person['firstname'], person['lastname'], person['username'])))
            else:
                k = k.replace("<username>", person['username'])
        if type(v) is not type({}):
            # File Type
            if '/' in v:
                seeded.seed(seed + root + v)
                v = seeded.choice(v.split('/'))
            if v == 'IP-LIST':
                ip_list = make_IP_LIST(root, k)
                with open(os.path.join(root, k), 'w') as f:
                    for system in ip_list:
                        f.write(system + '\n')
                        create_ip(system, type='discovered')
            if v == 'LOGIN-LIST':
                seeded.seed(seed + root + 'creds')
                creds = seeded.choice([0, 1, 1, 2, 3, 3, 4, 5, 5])
                with open(os.path.join(root, k), 'w') as f:
                    credlis = ''
                    if creds in [1, 5]:
                        if person['payme'] is not None:
                            credlis = credlis + '\npayme: %s' % person['payme']
                        if person['easybits'] is not None:
                            credlis = credlis + '\neasybits: %s' % person['easybits']
                    if creds in [2, 4]:
                        if person['payme'] is not None:
                            credlis = credlis + '\npayme: %s' % person['payme']
                        if person['easybits'] is not None:
                            credlis = credlis + '\neasybits: %s' % person['easybits']
                        credlis = credlis + '\nbankpass: %s\n' % person['bank_pass']
                    if creds in [3, 4]:
                        credlis = credlis + '\nemail: %s' % person['email']
                        credlis = credlis + '\nemailpass: %s\n' % person['user_pass']
                    if creds in [1, 5]:
                        credlis = credlis + '\nemail: %s' % person['email']
                    f.write(credlis)
            if v == 'SAFE-GUARD':
                flag = check_systems()[0]
                if flag is False:
                    ip_list = make_IP_LIST(root, k, guard=True)
                    with open(os.path.join(root, k), 'w') as f:
                        for system in ip_list:
                            f.write(system + '\n')
                            create_ip(system, type='discovered')
            if v == 'none':
                pass
        else:
            new_root = os.path.join(root, k)
            if not os.path.exists(new_root):
                os.makedirs(new_root)
                if not os.path.isfile(os.path.join(new_root, 'sys')):
                    with open(os.path.join(new_root, 'sys'), 'w') as f:
                        f.write(__FILLER__)
            build_sys(new_root, tree=v, new=False, seed=seed, person=person, IP=IP, player=player)

# build_sys('test', linux) # Debug
