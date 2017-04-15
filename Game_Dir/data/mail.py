#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
============================================================
This file is licensed under the "GNU General Public License v3.0"
And is provided by;
"Allison Marie Bennett", TheCyaniteProject@gmail.com
============================================================
Mail délivery
============================================================
"""
import os
import data.settings as settings


def check_email():
    retval = {}
    for file in os.listdir('%s%s\\sites\\email\\mail\\' % (settings.user_dir, settings.username)):
        if file.endswith('.log'):
            log = {}
            chat = []
            with open('%s%s\\sites\\email\\mail\\%s' % (settings.user_dir, settings.username, file), 'r') as f:
                f = f.read()
            log['to'] = f.split('<to>', 1)[1].split('</to>', 1)[0]
            log['from'] = f.split('<from>', 1)[1].split('</from>', 1)[0]
            chat_log = f.split('<log>', 1)[1].split('</log>', 1)[0]
            chat_log2 = chat_log
            for line in chat_log.split('\n'):
                if '<msg=' in line:
                    chat.append([chat_log2.split('<msg=', 1)[1].split('>', 1)[0].strip().rstrip(), chat_log2.split('>', 1)[1].split('</msg>', 1)[0].strip().rstrip()])
                    chat_log2 = chat_log2.split('</msg>', 1)[1]
            log['chat'] = chat
            retval[file] = log

            log = {}
            chat = []

            log['from'] = f.split('<to>', 1)[1].split('</to>', 1)[0]
            log['to'] = f.split('<from>', 1)[1].split('</from>', 1)[0]
            chat_log = f.split('<log>', 1)[1].split('</log>', 1)[0]
            chat_log2 = chat_log.replace('<msg=f>', '#FROM#').replace('<msg=t>', '<msg=f>').replace('#FROM#', '<msg=t>')
            for line in chat_log.split('\n'):
                if '<msg=' in line:
                    chat.append([chat_log2.split('<msg=', 1)[1].split('>', 1)[0].strip().rstrip(), chat_log2.split('>', 1)[1].split('</msg>', 1)[0].strip().rstrip()])
                    chat_log2 = chat_log2.split('</msg>', 1)[1]
            log['chat'] = chat
            retval[file + '_REV'] = log
    return retval


def dict(string=None, file=None, service='email'):
    service = service.lower()
    if service == 'email':
        if file is not None:
            if string is not None:
                return False
            if os.path.exists(file):
                with open(file, 'r') as f:
                    string = f.read()
            else:
                return False
        if string is None:
            return False
        else:
            letter = {'type': 'email'}
            for line in string.split('\n'):
                try:
                    if 'TO:' in line:
                        letter['to'] = line.split('TO:')[1]
                    if '<to>' in line:
                        letter['to'] = string.split('<to>', 1)[1].split('</to>', 1)[0]
                    if 'FROM:' in line:
                        letter['from'] = line.split('FROM:')[1]
                    if '<from>' in line:
                        letter['from'] = string.split('<from>', 1)[1].split('</from>', 1)[0]
                    if 'BODY:' in line:
                        letter['body'] = string.split('BODY:')[1]
                    if '<body>' in line:
                        letter['body'] = string.split('<body>', 1)[1].split('</body>', 1)[0]
                except Exception as err:
                    print(err)
                    return False
    return letter


def format(string=None, values=None):
    if type(string) is not type(''):
        return False
    if type(values) is not type({}):
        return False
    for target, value in values.iteritems():
        try:
            string = string.replace(target, value)
        except:
            return False
    return string


def send(letter=None, location=None, service='email'):
    service = service.lower()
    if type(letter) is not type({}):
        return False
    if service is None:
        if 'type' in letter:
            service = letter['type']
        else:
            return False
    if service == 'email':
        if location is None:
            location = os.path.join(settings.user_dir, settings.username, 'sites\\email\\mail\\')
        if not location.endswith(settings.text_types):
            if os.path.exists(location):
                if os.path.isfile(location + 'email(1).log'):
                    num = 1
                    while os.path.isfile(location + 'email(%s).log' % num):
                        num += 1
                    location = location + 'email(%s).log' % num
                else:
                    location = location + 'email(1).log'
            else:
                return False
        email = ''
        emails = check_email()
        flag = False
        for file in emails:
            if '_REV' in file:
                continue
            if emails[file]['to'].lower().strip().rstrip() == letter['to'].lower():
                if emails[file]['from'].lower().strip().rstrip() == letter['from'].lower():
                    # try:
                    with open('%s%s\\sites\\email\\mail\\%s' % (settings.user_dir, settings.username, file), 'r') as f:
                        f = f.read()
                    email = f.split('</log>', 1)[0] + '\n<msg=f>\n%s\n</msg>\n\n</log>' + f.split('</log>', 1)[1]
                    with open('%s%s\\sites\\email\\mail\\%s' % (settings.user_dir, settings.username, file), 'w') as f:
                        f.write(email)
                    # except:
                        # return False
                    flag = True
                    break
            elif emails[file]['from'].lower().strip().rstrip() == letter['to'].lower():
                if emails[file]['to'].lower().strip().rstrip() == letter['from'].lower():
                    with open('%s%s\\sites\\email\\mail\\%s' % (settings.user_dir, settings.username, file), 'r') as f:
                        f = f.read()
                    email = f.split('</log>', 1)[0] + '\n<msg=t>\n%s\n</msg>\n\n</log>' + f.split('</log>', 1)[1]
                    with open('%s%s\\sites\\email\\mail\\%s' % (settings.user_dir, settings.username, file), 'w') as f:
                        f.write(email)
                    flag = True
                    break
        if flag is not True:
            email = '<to>%s</to>\n<from>%s</from>\n<log>\n<msg=f>\n%s\n</msg>\n</log>' % (letter['to'], letter['from'], letter['body'])
            with open(location, 'w') as f:
                f.write(email)
        return True
    else:
        return False
