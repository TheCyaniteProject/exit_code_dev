#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""============================================================
This file is licensed under the "GNU General Public License v3.0"
And is provided by;
"Allison Marie Bennett", TheCyaniteProject@gmail.com
============================================================"""

"""============================================================
Money Conversion: Password, Check, Set, Add, Remove, Give, Convert
Account Controls: Create, Delete, Verify, Alert, ##Lock, ##Unlock
Widgets: ##Payme, ##Easybits
============================================================"""

import data.settings as settings
import data.mail as mail
import os
from Tkinter import *
"""========================================================="""

""" Money Conversion """

def password(network, toac, passw):
    file_dir = '%s%s\\wallets\\%s\\%s.ini' % (settings.user_dir,settings.username.lower(),network,toac)
    if not os.path.exists(file_dir) == True:
        return 'to_notExist'
    with open(file_dir, 'r') as f:
        try: toac_pass = f.readlines()[1].strip().rstrip()
        except: return True
    if toac_pass.strip().rstrip().lower() == 'none':
        return True
    elif toac_pass.strip().rstrip() == passw.strip().rstrip():
        return True
    else: return False

def check(network, toac, amount=None):
    file_dir = '%s%s\\wallets\\%s\\%s.ini' % (settings.user_dir,settings.username.lower(),network,toac)
    if not os.path.exists(file_dir) == True:
        return 'to_notExist'
    with open(file_dir, 'r') as f:
        toac_bal = float(f.readlines()[0].strip().rstrip())
    if amount == None:
        return toac_bal
    else:
        if toac_bal >= float(amount):
            return True
        else:
            return False
def set(network, toac, amount):
    if not network in ['payme','easybits']:
        raise Exception('"%s" is not a valid Network' % network)
    file_dir = '%s%s\\wallets\\%s\\%s.ini' % (settings.user_dir,settings.username.lower(),network,toac)
    if not os.path.exists(file_dir) == True:
        return 'to_notExist'
    else:
        if network == 'payme':
            if float(amount) > settings.payme_max: amount = settings.payme_max
            if float(amount) < settings.payme_min: amount = 0.0
        else:
            if float(amount) > settings.bits_max: amount = settings.bits_max
            if float(amount) < settings.bits_min: amount = 0.0
        with open(file_dir, 'r') as f:
            try:
                passw = f.read().split('\n', 1)[1].strip().rstrip()
            except:
                passw = 'None'
        with open(file_dir, 'w') as f:
            f.write(str(amount)+'\n'+passw)
        if network == 'payme':
            if toac == settings.payme_ac:
                settings.payme = float(amount)
                return True
        else:
            if toac == settings.easybits_ac:
                settings.bits = float(amount)
                return True

def add(network, toac, amount):
    if not network in ['payme','easybits']:
        raise Exception('"%s" is not a valid Network' % network)
    file_dir = '%s%s\\wallets\\%s\\%s.ini' % (settings.user_dir,settings.username.lower(),network,toac)
    if not os.path.exists(file_dir) == True:
        return 'to_notExist'
    else:
        with open(file_dir, 'r') as f:
            ac_bal = float(f.readlines()[0].strip().rstrip())
        '''if console.running_command == False:
            print '\n%s\nWallet ADD @ ACC/NET/AMOUNT : %s/%s/%s ' % (settings.get_time(),toac,network,amount)
        else:
            console.output.append('\n%s\nWallet ADD @ ACC/NET/AMOUNT : %s/%s/%s ' % (settings.get_time(),toac,network,amount))'''
        flag = set(network,toac,float(amount)+ac_bal)
        return flag

def remove(network, fromac, amount):
    if not network in ['payme','easybits']:
        raise Exception('"%s" is not a valid Network' % network)
    file_dir = '%s%s\\wallets\\%s\\%s.ini' % (settings.user_dir,settings.username.lower(),network,fromac)
    if not os.path.exists(file_dir):
        return 'from_notExist'
    else:
        with open(file_dir, 'r') as f:
            ac_bal = float(f.readlines()[0].strip().rstrip())
        '''if console.running_command == False:
            print '\n%s\nWallet REM @ ACC/NET/AMOUNT : %s/%s/%s ' % (settings.get_time(),fromac,network,amount)
        else:
            console.output.append('\n%s\nWallet REM @ ACC/NET/AMOUNT : %s/%s/%s ' % (settings.get_time(),fromac,network,amount))'''
        flag = set(network,fromac,ac_bal-float(amount))
        return flag

def give(network, toac, fromac, amount, overflow=False):
    if not network in ['payme','easybits']:
        raise Exception('"%s" is not a valid Network' % network)
    toac_dir = '%s%s\\wallets\\%s\\%s.ini' % (settings.user_dir,settings.username.lower(),network,toac)
    if not os.path.exists(toac_dir) == True:
        return 'to_notExist'
    fromac_dir = '%s%s\\wallets\\%s\\%s.ini' % (settings.user_dir,settings.username.lower(),network,fromac)
    if not os.path.exists(fromac_dir) == True:
        return 'from_notExist'
    else:
        with open(toac_dir, 'r') as f:
            toac_bal = float(f.readlines()[0].strip().rstrip())
        with open(fromac_dir, 'r') as f:
            fromac_bal = float(f.readlines()[0].strip().rstrip())
        limit = False ; extra = 0
        if network == 'payme':
            if float(amount)+toac_bal > settings.payme_max:
                limit = True
                extra =  float(amount)+toac_bal - settings.payme_max
            if float(amount) < settings.payme_min: amount = 0.0
        else:
            if float(amount)+toac_bal > settings.bits_max:
                limit = True
                extra =  float(amount)+toac_bal - settings.bits_max
            if float(amount) < settings.bits_min: amount = 0.0
        if limit == True:
            if overflow == False:
                amount = float(amount) - float(extra)
        if not fromac_bal >= amount:
            return 'incFunds'
        remove(network, fromac, amount)
        add(network, toac, amount)
        return True

def convert(network, payme_ac, easybits_ac, amount, overflow=False, tax=False):
    if not network in ['payme','easybits']:
        raise Exception('"%s" is not a valid Network' % network)
    payme_ac_dir = '%s%s\\wallets\\payme\\%s.ini' % (settings.user_dir,settings.username.lower(),payme_ac)
    if not os.path.exists(payme_ac_dir) == True:
        return 'payme_notExist'
    easybits_ac_dir = '%s%s\\wallets\\easybits\\%s.ini' % (settings.user_dir,settings.username.lower(),easybits_ac)
    if not os.path.exists(easybits_ac_dir) == True:
        return 'easybits_notExist'
    else:
        with open(payme_ac_dir, 'r') as f:
            payme_ac_bal = float(f.readlines()[0].strip().rstrip())
        with open(easybits_ac_dir, 'r') as f:
            easybits_ac_bal = float(f.readlines()[0].strip().rstrip())
        limit = False ; extra = 0
        if network == 'payme':
            if float(amount)+payme_ac_bal > settings.payme_max:
                limit = True
                extra = float(amount)+payme_ac_bal - settings.payme_max
            payme_amount = (amount / float(settings.wallet_multi))
        else:
            if float(amount)+easybits_ac_bal > settings.bits_max:
                limit = True
                extra =  float(amount)+easybits_ac_bal - settings.bits_max
            easybits_amount = (amount * float(settings.wallet_multi))
        if limit == True:
            if overflow == False:
                amount = float(amount) - float(extra)
        if tax == False:
            tax = (settings.wallet_tax * float(amount)) / 100.0
        elif tax == None:
            tax = 0.0
        else:
            tax = (tax * float(amount)) / 100.0
        if network == 'easybits':
            if not payme_ac_bal >= easybits_amount:
                return 'incFunds'
        else:
            if not easybits_ac_bal >= payme_amount:
                return 'incFunds'
        if network == 'payme':
            remove('easybits', easybits_ac, payme_amount)
            add('payme', payme_ac, (amount - tax))
            return True
        else:
            remove('payme', payme_ac, easybits_amount)
            add('easybits', easybits_ac, (amount - tax))
            return True


""" Account Controls """

def create(network, acname, amount=None, profile=None, passw=None, user=None):
    if profile == None:
        profile = settings.username
    if user == None:
        user = {'email_ac':settings.email_ac, 'IP':settings.player_ip}
    file_dir = '%s%s\\wallets\\%s\\%s' % (settings.user_dir,profile.lower(),network,acname)
    if amount == None:
        amount = '0.00'
    if not os.path.exists(file_dir+'.ini') == True:
        with open(file_dir+'.ini', 'w') as f:
            f.write('%s\n%s\n%s' % (amount, passw, user['email_ac']))
    if not os.path.exists(file_dir+'.whitelist') == True:
        with open(file_dir+'.whitelist', 'w') as f:
            f.write(user['IP'])
        return True
    else:
        return 'alreadyExists'

def delete(network, acname, profile=None):
    if profile == None:
        profile = settings.username
    file_dir = '%s%s\\wallets\\%s\\%s.ini' % (settings.user_dir,profile.lower(),network,acname)
    if os.path.exists(file_dir) == True:
        os.remove(file_dir)
        return True
    else:
        return 'notExist'

def verify(network, acname, IP=None):
    if IP == None:
        IP = settings.current_ip
    file_dir = '%s%s\\wallets\\%s\\%s' % (settings.user_dir,settings.username.lower(),network,acname)
    try:
        with open(file_dir+'.blacklist', 'r') as f:
            blacklist = f.readlines()
    except: blacklist = []
    try:
        with open(file_dir+'.whitelist', 'r') as f:
            whitelist = f.readlines()
    except:
        with open(file_dir+'.whitelist', 'w') as f:
            f.write('')
        whitelist = []
    if IP in blacklist:
        return False
    elif not IP in whitelist:
        return None
    else:
        return True

def alert(network='payme', acname=None, IP=None):
    if IP == None:
        IP = settings.current_ip
    file_dir = '%s%s\\wallets\\%s\\%s.ini' % (settings.user_dir,settings.username.lower(),network,acname)
    with open(file_dir, 'r') as f:
        email_address = f.readlines()[2].strip().rstrip()
    link = 'payme.net/auth=?-acc=%s-ip=%s' % (acname,IP)
    email = '''TO:%s\nFROM:noreply@alert.payme.net
BODY: Hello Account Holder,
You are recieving this email because you tried to login to your account (%s) from a new location (%s).
The login request was blocked, pending your review.

To confirm that this is in fact you, please click the link at the bottom of this email.

If you do not reconize this activity, that means that someone might have your login credintals. We highly recommend that you change your password as soon as possible.

Hope you have a nice day,
The Payme Team.
<link:%s, text:[Click here to grant %s access to your account]>''' % (email_address,acname,IP,link,IP)
    mail.send(mail.dict(email))
    return True

""" Widgets """

def payme_popup(page_frame, function, amount=None, api=None):
    if not amount == None:
        amount = amount * 100
    global frame1
    def payme_doLogin():
        global payme_account
        payme_user.configure(bg='white')
        payme_pass.configure(bg='white')
        user = payme_user.get()
        user = user.strip().rstrip()
        passw = payme_pass.get()
        if user.strip().rstrip() == '':
            payme_user.configure(bg='pink')
            return
        if 'payme.net' in settings.login_creds[settings.username.lower()]:
            if settings.login_creds[settings.username.lower()]['payme.net'][0] == True:
                if user.lower() == settings.login_creds[settings.username.lower()]['payme.net'][1].lower():
                    payme_account = settings.login_creds[settings.username.lower()]['payme.net'][1]
                    print '\n%s\nUser %s logged into api.payme.net @ %s' % (settings.get_time(),settings.username,payme_account)
                    payme_logOn(amount)
                    return
        if passw == 'thecheatpass':
            payme_account = user
            print '\n%s\nUser %s logged into api.payme.net @ %s' % (settings.get_time(),settings.username,payme_account)
            payme_logOn(amount)
            return
        #else:
        flag = wallet.password('payme', user, passw)
        payme_account = user
        if flag == 'to_notExist':
            payme_user.configure(bg='pink')
            return
        elif flag == False:
            payme_pass.configure(bg='pink')
            return
        elif flag == True:
            flag = wallet.verify('payme', user, settings.current_ip)
            print '\n%s\nUser %s logged into api.payme.net @ %s' % (settings.get_time(),settings.username,payme_account)
            payme_logOn(amount)
        else: raise Exception('unexpectedReturnValue')
    def add_autofill():
        global autofill_TF
        autofill_TF = False
        make_users = {}
        def autofill(event):
            payme_user.delete(0, END)
            payme_user.insert(0, make_users[usern])
            payme_pass.delete(0, END)
            payme_pass.insert(0, '**********')
        for usern in settings.login_creds:
            for site in settings.login_creds[usern]:
                if site == 'payme.net':
                    if settings.login_creds[usern][site][0] == True:
                        autofill_TF = True
                        make_users[usern]=settings.login_creds[usern][site][1]
        if autofill_TF == False:
            return
        Label(wig_autofill, text='Browser Autofill: ').pack()
        for usern in make_users:
            new_autofill = Label(wig_autofill, text=('[%s]' % (make_users[usern])), fg='blue', cursor='hand2')
            new_autofill.pack(padx=3)
            new_autofill.bind('<Button-1>', autofill)
    frame0 = LabelFrame(page_frame, bg='green', width=350, height=200)
    frame0.place(anchor=CENTER, relx=.5, rely=.5)
    frame0.pack_propagate(0)
    Label(frame0, text='Powered By Payme.net', bg='green', font=(None, 10)).pack(side=TOP)
    frame1 = Frame(frame0)
    frame1.pack(side=TOP, fill=BOTH, expand=True)
    frame = LabelFrame(frame1, text='Login to your Payme Account')
    frame.pack(side=TOP, fill=X)
    payme_user_wig = LabelFrame(frame, text='Account ID')
    payme_user_wig.pack(padx=5, pady=2, anchor=N, fill=X)
    payme_user = Entry(payme_user_wig)
    payme_user.pack(fill=X)
    Button(frame, text='Cancel', bg='white', cursor='hand2', command=frame0.destroy).pack(padx=5, pady=5, anchor=S, side=RIGHT)
    Button(frame, text='Login', bg='white', cursor='hand2', command=payme_doLogin).pack(padx=3, pady=5, anchor=S, side=RIGHT)
    payme_pass_wig = LabelFrame(frame, text='Password')
    payme_pass_wig.pack(padx=5, anchor=S, side=LEFT, fill=X, expand=True)
    payme_pass = Entry(payme_pass_wig)
    payme_pass.pack(fill=X)
    wig_autofill = LabelFrame(frame1)
    wig_autofill.pack(side=TOP)
    add_autofill()
    def payme_logOn(amount):
        global frame1
        frame1.destroy()
        frame1 = LabelFrame(frame0, text='Please check the following information:')
        frame1.pack(side=TOP, fill=BOTH, expand=True)
        if amount == None:
            amount = 'Unspecified'
            if not api == None:
                Label(frame1, text='"%s"' % api, fg='darkgreen', font=(None, 13)).pack(padx=2, pady=2, side=TOP, fill=X)
                Label(frame1, text='Would like to Deposit into your account.', font=(None, 10)).pack(padx=2, side=TOP, fill=X)
                ac_bal = Frame(frame1)
                ac_bal.pack(padx=2, side=TOP, fill=X, expand=True)
                Label(ac_bal, text='Your Balance:').pack(padx=2, side=LEFT)
                temp = Entry(ac_bal)
                temp.pack(padx=2, side=RIGHT, fill=X, expand=True)
                temp.insert(0, check('payme', payme_account))
                temp.configure(state='read')
                req_bal = Frame(frame1)
                req_bal.pack(padx=2, side=TOP, fill=X, expand=True)
                Label(req_bal, text='Amount:').pack(padx=2, side=LEFT)
                temp = Entry(req_bal)
                temp.pack(padx=2, side=RIGHT, fill=X, expand=True)
                temp.insert(0, amount)
                temp.configure(state='read')
            else:
                Label(frame1, text='"An Unknown Service"', fg='red', font=(None, 13)).pack(padx=2, pady=2, side=TOP, fill=X)
                Label(frame1, text='Would like to Deposit into your account.', font=(None, 10)).pack(padx=2, side=TOP, fill=X)
                ac_bal = Frame(frame1)
                ac_bal.pack(padx=2, side=TOP, fill=X, expand=True)
                Label(ac_bal, text='Your Balance:').pack(padx=2, side=LEFT)
                temp = Entry(ac_bal)
                temp.pack(padx=2, side=RIGHT, fill=X, expand=True)
                temp.insert(0, check('payme', payme_account))
                temp.configure(state='read')
                req_bal = Frame(frame1)
                req_bal.pack(padx=2, side=TOP, fill=X, expand=True)
                Label(req_bal, text='Amount:').pack(padx=2, side=LEFT)
                temp = Entry(req_bal)
                temp.pack(padx=2, side=RIGHT, fill=X, expand=True)
                temp.insert(0, amount)
                temp.configure(state='read')
        else:
            if not api == None:
                Label(frame1, text='"%s"' % api, fg='darkgreen', font=(None, 13)).pack(padx=2, pady=2, side=TOP, fill=X)
                Label(frame1, text='Would like to Withdraw from your account.', font=(None, 10)).pack(padx=2, side=TOP, fill=X)
                ac_bal = Frame(frame1)
                ac_bal.pack(padx=2, side=TOP, fill=X, expand=True)
                Label(ac_bal, text='Your Balance:').pack(padx=2, side=LEFT)
                temp = Entry(ac_bal)
                temp.pack(padx=2, side=RIGHT, fill=X, expand=True)
                temp.insert(0, check('payme', payme_account))
                temp.configure(state='read')
                req_bal = Frame(frame1)
                req_bal.pack(padx=2, side=TOP, fill=X, expand=True)
                Label(req_bal, text='Amount:').pack(padx=2, side=LEFT)
                temp = Entry(req_bal)
                temp.pack(padx=2, side=RIGHT, fill=X, expand=True)
                temp.insert(0, amount)
                temp.configure(state='read')
            else:
                Label(frame1, text='"An Unknown Service"', fg='red', font=(None, 13)).pack(padx=2, pady=2, side=TOP, fill=X)
                Label(frame1, text='Would like to Withdraw from your account.', font=(None, 10)).pack(padx=2, side=TOP, fill=X)
                ac_bal = Frame(frame1)
                ac_bal.pack(padx=2, side=TOP, fill=X, expand=True)
                Label(ac_bal, text='Your Balance:').pack(padx=2, side=LEFT)
                temp = Entry(ac_bal)
                temp.pack(padx=2, side=RIGHT, fill=X, expand=True)
                temp.insert(0, check('payme', payme_account))
                temp.configure(state='read')
                req_bal = Frame(frame1)
                req_bal.pack(padx=2, side=TOP, fill=X, expand=True)
                Label(req_bal, text='Amount:').pack(padx=2, side=LEFT)
                temp = Entry(req_bal)
                temp.pack(padx=2, side=RIGHT, fill=X, expand=True)
                temp.insert(0, amount)
                temp.configure(state='read')
        def authorize():
            function(payme_account)
            frame0.destroy()
        buttons = Frame(frame1)
        buttons.pack(padx=2, side=TOP, fill=X)
        Button(buttons, text='Cancel', width=10, bg='white', cursor='hand2', command=frame0.destroy).pack(padx=5, pady=5, side=RIGHT)
        Button(buttons, text='Authorize', bg='white', cursor='hand2', command=authorize).pack(padx=10, pady=5, side=LEFT, fill=X, expand=True)


    '''
    if not amount == None:
        flag = check('payme', settings.payme_ac, amount)
        if flag == True:
            return settings.payme_ac
        else:
            return False
    else: return settings.payme_ac'''

def easybits_popup():
    return True






