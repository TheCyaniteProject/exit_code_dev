#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""============================================================
This file is licensed under the "GNU General Public License v3.0"
And is provided by;
"Allison Marie Bennett", TheCyaniteProject@gmail.com
============================================================"""

"""============================================================
Game Web & Browser
============================================================"""

"""========================= Imports ======================="""
import tkinter_ui
import os
import data.settings as settings
import data.mail as mail
from Tkinter import *
"""========================================================="""

""" Web Pages For Browser """
global sitelocker_ver
global riddleme_mode
global hackable
hackable = False
sitelocker_ver = False
riddleme_mode = False
class WebPages(object):

    # Website URL Links
    webMap = {
    'home':'browserHome',
    'easybits.com':'page_easybits',
    'payme.net':'page_payme',
    'email.com':'page_email',
    'shhmail.net':'page_shmail',
    'sitelocker.org':'page_sitelocker',
    'riddleme.org':'page_riddleme',
    'datakult.shop':'page_datakult',
    'pcgo.shop':'page_pcgo',
    'whatsmyip.com':'page_whatsmyip'
    }

    def errorPage(self):
        global sitelocker_ver
        global riddleme_mode
        global hackable
        hackable = False
        sitelocker_ver = False
        riddleme_mode = False
        import data.sites.errorPage.errorPage_site as errorPage_site
        reload(errorPage_site)
        errorPage_site.web_site(tkinter_ui.web_page, tkinter_ui.go_from)

    def browserHome(self):
        global sitelocker_ver
        global riddleme_mode
        global hackable
        hackable = False
        sitelocker_ver = False
        riddleme_mode = False
        import data.sites.homePage.homePage_site as homePage_site
        reload(homePage_site)
        homePage_site.web_site(tkinter_ui.web_page, tkinter_ui.go_from)

    def page_whatsmyip(self):
        global sitelocker_ver
        global riddleme_mode
        global hackable
        hackable = False
        sitelocker_ver = False
        riddleme_mode = False
        tkinter_ui.set_url('http://www.whatsmyip.com')
        import data.sites.whatsmyip.whatsmyip_site as whatsmyip_site
        reload(whatsmyip_site)
        whatsmyip_site.web_site(tkinter_ui.web_page)

    def page_sitelocker(self):
        global sitelocker_ver
        global riddleme_mode
        global hackable
        hackable = False
        sitelocker_ver = False
        riddleme_mode = False
        tkinter_ui.set_url('http://www.sitelocker.org')
        import data.sites.sitelocker.sitelocker_site as sitelocker_site
        reload(sitelocker_site)
        sitelocker_site.web_site(tkinter_ui.web_page)

    def page_riddleme(self):
        global sitelocker_ver
        global riddleme_mode
        global hackable
        hackable = False
        sitelocker_ver = False
        riddleme_mode = False
        tkinter_ui.set_url('http://www.riddleme.org')
        import data.sites.riddleme.riddleme_site as riddleme_site
        reload(riddleme_site)
        riddleme_site.web_site(tkinter_ui.web_page)


    def page_datakult(self):
        global sitelocker_ver
        global riddleme_mode
        global hackable
        hackable = False
        sitelocker_ver = False
        riddleme_mode = False
        tkinter_ui.set_url('https://www.datakult.shop')
        import data.sites.datakult.datakult_site as datakult_site
        reload(datakult_site)
        datakult_site.web_site(tkinter_ui.web_page)

    def page_pcgo(self):
        global sitelocker_ver
        global riddleme_mode
        global hackable
        hackable = False
        sitelocker_ver = False
        riddleme_mode = False
        tkinter_ui.set_url('https://www.pcgo.shop')
        import data.sites.pcgo.pcgo_site as pcgo_site
        reload(pcgo_site)
        pcgo_site.web_site(tkinter_ui.web_page)

    def page_payme(self):
        global sitelocker_ver
        global riddleme_mode
        global hackable
        hackable = False
        sitelocker_ver = False
        riddleme_mode = False
        tkinter_ui.set_url('https://www.payme.net')
        import data.sites.payme.payme_site as payme_site
        reload(payme_site)
        payme_site.web_site(tkinter_ui.web_page, tkinter_ui.go_from)
        return
        '''
        hackable = [email_site.email_user, email_site.hack_in]
        if not email_site.sitelocker == None:
            sitelocker_ver = email_site.sitelocker
        if not email_site.riddleme == None:
            if not email_site.riddleme.lower() == 'false':
                riddleme_mode = True'''

    def page_easybits(self):
        global sitelocker_ver
        global riddleme_mode
        global hackable
        hackable = False
        sitelocker_ver = False
        riddleme_mode = False
        tkinter_ui.set_url('https://www.easybits.com')
        import data.sites.easybits.easybits_site as easybits_site
        reload(easybits_site)
        easybits_site.web_site(tkinter_ui.web_page, tkinter_ui.go_from)
        return
        '''
        hackable = [email_site.email_user, email_site.hack_in]
        if not email_site.sitelocker == None:
            sitelocker_ver = email_site.sitelocker
        if not email_site.riddleme == None:
            if not email_site.riddleme.lower() == 'false':
                riddleme_mode = True'''

    def page_shmail(self):
        global sitelocker_ver
        global riddleme_mode
        global hackable
        hackable = False
        sitelocker_ver = False
        riddleme_mode = False
        tkinter_ui.set_url('http://www.shhmail.net')
        import data.sites.email.email_site as email_site
        reload(email_site)
        email_site.web_site(tkinter_ui.web_page, tkinter_ui.go_from)
        hackable = [email_site.email_user, email_site.hack_in]
        if not email_site.sitelocker == None:
            sitelocker_ver = email_site.sitelocker
        if not email_site.riddleme == None:
            if not email_site.riddleme.lower() == 'false':
                riddleme_mode = True

    def page_email(self):
        global sitelocker_ver
        global riddleme_mode
        global hackable
        hackable = False
        sitelocker_ver = False
        riddleme_mode = False
        tkinter_ui.set_url('http://www.email.com')
        import data.sites.email.email_site as email_site
        reload(email_site)
        email_site.web_site(tkinter_ui.web_page, tkinter_ui.go_from)
        hackable = [email_site.email_user, email_site.hack_in]
        if not email_site.sitelocker == None:
            sitelocker_ver = email_site.sitelocker
        if not email_site.riddleme == None:
            if not email_site.riddleme.lower() == 'false':
                riddleme_mode = True

class TempPage(object):

    webMap = {
    #'easybits.com':'link_easybits',
    'payme.net':'link_payme',
    #'email.com':'link_email',
    #'shhmail.net':'link_shmail',
    }

    def link_payme(self, link):# payme.net/auth=?-acc=xxxxxxxxxxxxxxxxxx-ip=xxx.xxx.xxx.xxx
        for i in ['auth=', 'acc=', 'ip=']:
            if not i in link:
                tkinter_ui.go_from('https://www.payme.net')
                return
        link = [link.split('auth=',1)[1].split('-',1)[0],  link.split('acc=',1)[1].split('-',1)[0],  link.split('ip=',1)[1]]
        tkinter_ui.set_url('https://www.payme.net/auth=?grant-%s' % link[2])
        file_dir = '%s%s\\wallets\\payme\\%s' % (settings.user_dir,settings.username,link[1])
        with open(file_dir+'.whitelist', 'r') as f:
            list = f.read()
        if not link[2] in list:
            with open(file_dir+'.whitelist', 'w') as f:
                f.write(list+'\n'+link[2])
        else:
            tkinter_ui.go_from('https://www.payme.net')
            return
        with open(file_dir+'.ini', 'r') as f:
            email_address = f.readlines()[2].strip().rstrip()
        email = '''TO:%s\nTOIP:Nul\nFROM:noreply@alert.payme.net\nFROMIP:Nul
SUBJECT: Access Confirmation
BODY:Hello again, Account Holder.
\nThis email is to let you know that you successfully granted
"%s" access to your account "%s".
\nThank you for choosing Payme.net
\nHope you have a nice day,
The Payme Team.
<link:https://www.payme.net, text:[www.Payme.net]>''' % (email_address,link[2],link[1])
        flag = mail.send(mail.dict(email))
        tkinter_ui.go_from('https://www.payme.net')
        tkinter_ui.set_url('https://www.payme.net/auth=?grant-%s' % link[2])

    def go(self, URL):
        URL = URL.replace('http://', '').replace('https://', '').replace('www.', '').split('/',1)
        if URL[0] in TempPage().webMap:
            eval('self.%s(\'%s\')' % (TempPage().webMap[URL[0]],URL[1]))

def web_hack(version=1.0):
    global hack_after
    global wait_time
    if hackable == False:
        print 'error: this page cannot be hacked'
        return
    if hackable[0].get().strip() == '':
        print 'error: no username'
        return
    def hack_after():
        tkinter_ui.con_post('" *hacker voice* we\'re in "')
        hackable[1]()
    wait_time = 20000.0
    wait_time = wait_time / float(version)
    ETA = (wait_time / 1000.0)
    if ETA < 1:
        ETA = 'Less than a second'
    else:
        ETA = str(ETA)+' seconds'
    if wait_time < 10:
        wait_time = 10
    print 'Exploting....This might take a moment'
    print 'ETA: %s..' % ETA
    tkinter_ui.root.after(int(wait_time), hack_after)

def sitelocker(disable=False):
    global sitelocker_ver
    if (disable == False) or (disable == 0):
        return sitelocker_ver
    elif (disable == True) or (disable == 1):
        if sitelocker_ver == False:
            print 'Sitelocker not running here'
            return
        print 'Crashing Sitelocker..'
        sitelocker_ver = False
        return sitelocker_ver
    else:
        raise Exception('\'sitelocker\' can only take \'bool\' object')

def riddleme(disable=False, mode=None):
    global riddleme_mode
    if mode in [None, False, 'default']:
        if (disable == False) or (disable == 0):
            return riddleme_mode
        elif (disable == True) or (disable == 1):
            if riddleme_mode == False:
                print 'Riddleme not running here'
                return
            print 'Crashing Riddleme..'
            riddleme_mode = False
            return riddleme_mode
        else:
            raise Exception('\'riddleme\' can only take \'bool\' object')
    elif mode in ['pop', 'popup']:
        riddleme_mode = 'block'
        ''' Add code here to disable Webpage'''
        riddleframe = LabelFrame(tkinter_ui.web_page, fg='blue', bg='grey', text='RiddleMe', width=200, height=100)
        riddleframe.place(anchor=CENTER, relx=.5, rely=.5)
        riddleframe.pack_propagate(0)
        Label(riddleframe, text='Prove you are human.\nClick the button below.', fg='blue', bg='grey').pack()
        def on_click():
            global riddleme_mode
            riddleme_mode = True
            ''' Add code here to re-enable Webpage'''
            riddleframe.destroy()
        Button(riddleframe, text='I am not a robot! ◄[▫⌂▫]►', fg='blue', command=on_click).pack()


def open_webPage(URL):
    URL = URL.replace('http://', '').replace('https://', '').replace('www.', '').replace('browser://', '')
    if URL.endswith('//'):
        URL = URL.rsplit('//', 1)[0]
    if '/' in URL:
        TempPage().go(URL)
    elif URL.lower() in WebPages.webMap:
        eval('WebPages().%s()' % WebPages.webMap[URL.lower()])
    else:
        WebPages().errorPage()

