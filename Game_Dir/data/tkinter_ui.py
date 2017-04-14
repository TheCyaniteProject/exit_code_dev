#!/usr/bin/python
# -*- coding: utf-8 -*-

"""============================================================
This file is licensed under the "GNU General Public License v3.0"
And is provided by;
"Allison Marie Bennett", TheCyaniteProject@gmail.com
============================================================"""

"""============================================================
Game UI
============================================================"""

"""========================= Imports ======================="""
import data.settings as settings
import data.console as console
import data.web as web
import os
import subprocess
from Tkinter import *
import ttk
from data.autocomp import *
"""========================================================="""

# UI Settings
root = Tk()
root.title(settings.title)
root.geometry("1000x500")
root.minsize(1000 , 500)
#root.resizable(width=False, height=False)


# Console stuff
def send_console():
    send(concom.get())
    concom.delete(0, END)

def send(command):
    command = command.partition('#')[0]
    command = command.rstrip()
    if command.strip() == '':
        return
    if command.strip().startswith('@'):
        command = command.split('@', 1)[1]
    else:
        con_post('\n> %s\n' % command)
    con_post(console.run(command))
    root.after(5, (conlog.see(END)))

def con_post(text):
    conlog.config(state=NORMAL)
    conlog.insert(END, str(text))
    root.after(5, (conlog.see(END)))
    conlog.config(state=DISABLED)

def set_url(URL):
    browser_url.delete(0, END)
    browser_url.insert(0, URL)

def go_from(URL):
    browser_url.delete(0, END)
    browser_url.insert(0, URL)
    web.open_webPage(URL)

def return_url(event):
    web.open_webPage(browser_url.get())

def return_console(event):
   send_console()

# UI Frames
frame_console = LabelFrame(root, width=400, text='Console')
frame_console.pack(anchor=E, fill=Y, expand=False, side=RIGHT)
frame_console.pack_propagate(0)

frame_apps = LabelFrame(root, height=100, width=400)#, text='Apps')
frame_apps.pack(anchor=W, fill=X, expand=False, side=BOTTOM)
#frame_apps.pack_propagate(0)

frame_tabs = LabelFrame(root, width=400, text='Desktop')
frame_tabs.pack(anchor=W, fill=BOTH, expand=True, side=LEFT)
frame_tabs.pack_propagate(0)

def click_move(event):
    root.after(5, concom.focus_set)

# Console Frame
conlog = Text(frame_console, wrap = WORD)
conlog.pack(padx=2, anchor=E, fill=BOTH, expand=True, side=TOP)
conlog.config(state=DISABLED)

Button(frame_console, text=' Submit ', cursor='hand2', command=send_console).pack(anchor=E, fill=NONE, expand=False, side=RIGHT)

concom = AutocompleteEntry(frame_console)
concom.set_completion_list(console.command_list)
concom.pack(pady=2, padx=2, anchor=E, fill=BOTH, expand=True, side=LEFT)
concom.bind('<Return>', return_console)
concom.focus_set()

show_con = True
def toggle_console():
    global show_con
    if show_con == True:
        console_button.configure(text='Show')
        frame_console.configure(width=1)
        show_con = False
    else:
        console_button.configure(text='Hide')
        frame_console.configure(width=400)
        show_con = True

console_button = Button(text='Hide', cursor='hand2', command=toggle_console)
console_button.place(anchor=NE, relx=1, rely=0, y=11)

# Tabs Frame
applications = ttk.Notebook(frame_tabs)
applications.pack(anchor=W, fill=BOTH, expand=True, side=LEFT)
# Tab0
tab0 = Frame(applications, bg='white')
applications.add(tab0, text = "Home")
Label(tab0, text='Tip: Click on an app to open it\'s window.', bg='white').pack()
# Tab1
tab1 = Frame(applications)
applications.add(tab1, text = "Explorer")
applications.tab(1, state='hidden')
# Tab2
tab2 = Frame(applications)
applications.add(tab2, text = "Browser")
applications.tab(2, state='hidden')
# Tab3
tab3 = Frame(applications)
applications.add(tab3, text = "QuickPad")
applications.tab(3, state='hidden')


def on_disable():
        TF = False
        for i in range(applications.index(END)-1):
            i+=1
            if not applications.tab(i)['state'] == 'hidden':
                TF = True
                applications.tab(0, state='hidden')
                return
        if TF == False:
            applications.tab(0, state='normal')
            applications.select(0)
disable_1V = True
def disable_1():
    global explorer_app
    global disable_1V
    if disable_1V == False:
        applications.tab(1, state='hidden')
        explorer_app.set('Explorer')
        disable_1V = True
    else:
        applications.tab(1, state='normal')
        applications.select(1)
        explorer_app.set('Explorer [X]')
        disable_1V = False
    on_disable()

disable_2V = True
def disable_2():
    global browser_app
    global disable_2V
    if disable_2V == False:
        applications.tab(2, state='hidden')
        go_from('browser://home')
        browser_app.set('Browser')
        disable_2V = True
    else:
        reload(web)
        applications.tab(2, state='normal')
        applications.select(2)
        browser_app.set('Browser [X]')
        disable_2V = False
    on_disable()

quickpad_dir = None
disable_3V = True
def disable_3():
    global quickpad_app
    global disable_3V
    global quickpad_dir
    if disable_3V == False:
        applications.tab(3, state='hidden')
        pad_clear()
        quickpad_app.set('QuickPad')
        disable_3V = True
        quickpad_dir = None
    else:
        applications.tab(3, state='normal')
        applications.select(3)
        quickpad_app.set('QuickPad [X]')
        disable_3V = False
    on_disable()

# Applications
# Web Browser
def clear_web_page():
    for widget in web_page.winfo_children():
        widget.destroy()

def clear_working_folder():
    for widget in working_folder.winfo_children():
        widget.destroy()

def web_go():
    web.open_webPage(browser_url.get())

# File Explorer
def folder_link(name):
    name = name.split('<DIR>', 1)[1].strip()
    def link_click(event):
        send(('@cd %s'% name))
    folder = Label(working_folder, text='[%s]' % name, fg='blue', bg='white', cursor='hand2')
    folder.pack(padx=10, anchor=W, side=TOP)
    folder.bind('<Button-1>', link_click)

def unknown_link(name):
    if not ' ' in name:
        return
    name = name.strip().split(' ', 1)[1]
    file = Label(working_folder, text='?: %s' % name, bg='white')
    file.pack(padx=10, anchor=W, side=TOP)

def file_link(name):
    name = name.strip().split(' ', 1)[1]
    def link_click(event):
        send(('cat "%s"'% name))
    file = Label(working_folder, text='F: %s' % name, fg='blue', bg='white', cursor='hand2')
    file.pack(padx=10, anchor=W, side=TOP)
    file.bind('<Button-1>', link_click)

def app_link(name):
    name = name.strip().split(' ', 1)[1]
    def link_click(event):
        send(('%s'% name))
    if name.endswith('.sh'): link = 'S: %s' % name
    else: link = 'A: %s' % name
    app = Label(working_folder, text=link, fg='blue', bg='white', cursor='hand2')
    app.pack(padx=10, anchor=W, side=TOP)
    app.bind('<Button-1>', link_click)

'''def get_dir():
    command = 'dir "%s\\"' % settings.working_dir
    dir_tree = ''
    dir_call = subprocess.check_output(command, shell=True)
    for line in dir_call.splitlines():
        if 'AM' in line:
            dir_tree = dir_tree+line.split('AM')[1]+'\n'
        elif 'PM' in line:
            dir_tree = dir_tree+line.split('PM')[1]+'\n'
    return dir_tree'''

def update_folders():
    clear_working_folder()
    Label(working_folder, bg='white').pack(anchor=W, side=TOP)
    folder_url.delete(0, END)
    folder_url.insert(0, (settings.system_id+(settings.working_dir+'\\').split('os_root_dir', 1)[1]))
    if console.can_run == False:
        folder = Label(working_folder, text='[Access Denited]', bg='white')
        folder.pack(padx=10, anchor=W, side=TOP)
        return
    for line in console.get_dir().split('\n'):
        if '<DIR>' in line:
            folder_link(line)
        elif line.endswith(('.txt', '.log')):
            file_link(line)
        elif line.endswith(('.sh', '.app')):
            app_link(line)
        elif not line.endswith(settings.file_types):
            continue
        elif not ('Dir' in line) or not ('File' in line):
            unknown_link(line)

def move_home():
    send('@cd .')

def move_up():
    send('@cd ..')

def return_dir(event):
    send('@cd %s' % folder_url.get())

# QuickPad

def pad_warn(text='None', color='white'):
    frame = LabelFrame(body_frame)
    frame.place(anchor=NE, relx=1, rely=0)
    Label(frame, bg=color, text=text).pack(padx=3, anchor=W, side=LEFT)
    Button(frame, text='Dismiss', relief=FLAT, command=frame.destroy).pack(anchor=W, side=LEFT)

def save_file(file, mode=True):
    if mode == True:
        file_dir = os.path.join(settings.working_dir,file)
    else:
        file_dir = os.path.join(quickpad_dir,file)
    if not file.endswith(settings.text_types):
        pad_warn('File type can only be: %s' % str(settings.text_types), 'pink')
        return
    for i in file:
        if i in '/\:*?"<>|':
            pad_warn('File names can\'t contain any of the following: / \ : * ? " < > |', 'pink')
            return
    with open(file_dir, 'w') as f:
        f.write(pad_entry.get(0.0, END))
    pad_warn('The file was saved.')
    console.reload_autofill()
    concom.set_completion_list(console.command_list)

def save_confirm(file, save_frame=False, save_as=False):
    pad_entry.configure(state='disabled')
    def file_done():
        file_frame.destroy()
        pad_entry.configure(state='normal')
    def file_save(mode=True):
        if not save_as == False:
            save_as.destroy()
        if not save_frame == False:
            save_frame.destroy()
        if not file_frame == False:
            file_frame.destroy()
        save_file(file, mode=mode)
        pad_entry.configure(state='normal')
    def file_save2():
        file_save(mode=False)
    file_frame = False
    if quickpad_dir == None:
        file_save()
        return
    elif os.path.join(settings.working_dir,file) == os.path.join(quickpad_dir,file):
        file_save()
        return
    file_frame = LabelFrame(body_frame)
    file_frame.place(anchor=NW, relx=0, rely=0)
    Label(file_frame, bg='white', text='File is not open in current directory').pack(padx=3, anchor=W, side=LEFT)
    Button(file_frame, text='Save here', relief=FLAT, command=file_save).pack(anchor=W, side=LEFT)
    Button(file_frame, text='Save original', relief=FLAT, command=file_save2).pack(anchor=W, side=LEFT)
    Button(file_frame, text='Cancel', relief=FLAT, command=file_done).pack(anchor=W, side=LEFT)

pad_filename = StringVar()
pad_filename.set('"\\new.txt"')
def pad_save(filename=None, save_as=False):
    if filename == None:
        filename = pad_filename.get().rsplit('\\', 1)[1].replace('"', '')
    pad_entry.configure(state='disabled')
    def file_done():
        file_frame.destroy()
        pad_entry.configure(state='normal')
    def file_save():
        if not quickpad_dir == None:
            save_confirm(filename, save_frame=file_frame, save_as=save_as)
        else:
            if not save_as == False:
                save_as.destroy()
            file_frame.destroy()
            save_file(filename)
            pad_entry.configure(state='normal')
    file_frame = LabelFrame(body_frame)
    file_frame.place(anchor=NW, relx=0, rely=0)
    Label(file_frame, bg='white', text='Are you sure you want to save/overwrite "%s"?' % filename).pack(padx=3, anchor=W, side=LEFT)
    Button(file_frame, text='Save', relief=FLAT, command=file_save).pack(anchor=W, side=LEFT)
    Button(file_frame, text='Cancel', relief=FLAT, command=file_done).pack(anchor=W, side=LEFT)

def pad_save_as():
    pad_entry.configure(state='disabled')
    def file_done():
        file_frame.destroy()
        pad_entry.configure(state='normal')
    def file_save():
        if '.' in save_entry.get():
            if not save_entry.get().endswith(settings.text_types):
                pad_warn('File type can only be: %s' % str(settings.text_types), 'pink')
                return
        for i in save_entry.get():
            if i in '/\:*?"<>|':
                pad_warn('File names can\'t contain any of the following: / \ : * ? " < > |', 'pink')
                return
        pad_save(save_entry.get().strip(), file_frame)
    file_frame = LabelFrame(body_frame)
    file_frame.place(anchor=NW, relx=0, rely=0)
    save_entry = Entry(file_frame, width=20)
    save_entry.pack(padx=3, anchor=W, side=LEFT)
    save_entry.insert(0, pad_filename.get().rsplit('\\', 1)[1].replace('"', ''))
    Button(file_frame, text='Save', relief=FLAT, command=file_save).pack(anchor=W, side=LEFT)
    Button(file_frame, text='Cancel', relief=FLAT, command=file_done).pack(anchor=W, side=LEFT)

def pad_clear():
    pad_entry.delete(0.0, END)
    pad_filename.set('"\\new.txt"')

def pad_open():
    if disable_3V == True:
        disable_3()
    else:
        print 'quick: error: QuickPad already open'

def pad_insert(file_dir, file):
    global quickpad_dir
    with open(file_dir, 'r') as f:
        if disable_3V == True:
            disable_3()
        pad_entry.delete(0.0, END)
        pad_entry.insert(0.0, f.read())
        quickpad_dir = settings.working_dir
        pad_filename.set('%s%s\\%s' % (settings.system_id,((settings.working_dir).split('os_root_dir', 1)[1]),file))

# File Explorer
tab1.configure(bg='white')
working_folder = LabelFrame(tab1, bg='white')
working_folder.pack(padx=2, fill=BOTH, expand=True, side=BOTTOM)
Button(tab1, text='Home', relief=FLAT, bg='white', cursor='hand2', command=move_home).pack(anchor=W, expand=False, side=LEFT)
Button(tab1, text='Up', relief=FLAT, bg='white', cursor='hand2', command=move_up).pack(anchor=W, expand=False, side=LEFT)
folder_url = Entry(tab1)
folder_url.pack(padx=2, pady=2, anchor=W, fill=X, expand=True, side=LEFT)
folder_url.bind('<Return>', return_dir)
folder_url.insert(0, '\\')
Button(tab1, text='Refresh', relief=FLAT, bg='white', cursor='hand2', command=update_folders).pack(anchor=E, expand=False, side=RIGHT)
Button(tab1, text='GO', relief=FLAT, bg='white', cursor='hand2', command=move_up).pack(anchor=E, expand=False, side=RIGHT)
update_folders()

# Web Browser
tab2.configure(bg='white')
web_page = LabelFrame(tab2, bg='white')
web_page.pack(padx=2, fill=BOTH, expand=True, side=BOTTOM)
browser_url = Entry(tab2)
Button(tab2, text='Home', relief=FLAT, bg='white', cursor='hand2', command=lambda: go_from('browser://home')).pack(anchor=W, expand=False, side=LEFT)
browser_url.pack(padx=2, pady=2, anchor=W, fill=X, expand=True, side=LEFT)
browser_url.bind('<Return>', return_url)
browser_url.insert(0, 'browser://home')
Button(tab2, text=' ··· ', relief=FLAT, bg='white', cursor='hand2').pack(anchor=E, expand=False, side=RIGHT)
Button(tab2, text='GO', relief=FLAT, bg='white', cursor='hand2', command=web_go).pack(anchor=E, expand=False, side=RIGHT)
web_go()

# QuickPad
tab3.configure(bg='white')
body_frame = LabelFrame(tab3)
body_frame.pack(padx=2, fill=BOTH, expand=True, side=BOTTOM)
pad_entry = Text(body_frame, relief=FLAT)
pad_entry.pack(fill=BOTH, expand=True)
Button(tab3, text='Save', relief=FLAT, bg='white', cursor='hand2', command=pad_save).pack(anchor=E, expand=False, side=LEFT)
Button(tab3, text='Save As', relief=FLAT, bg='white', cursor='hand2', command=pad_save_as).pack(anchor=E, expand=False, side=LEFT)
Label(tab3, bg='white', textvariable=pad_filename).pack(anchor=E, expand=False, side=RIGHT)

#Apps Menu
list_scripts_open = False
def list_scripts():
    global list_apps_open
    global list_scripts_open
    global scripts_list
    if list_apps_open == True:
        apps_list.destroy()
        list_apps_open = False
    if list_scripts_open == False:
        scripts_list = LabelFrame(width=105, height=29)
        scripts_list.place(anchor=SW, relx=0, x=110, rely=1, y=-57)
        if len(console.player_scripts) == 0:
            Label(scripts_list, text='None', width=13).pack(side=BOTTOM, fill=X)
        for script in console.player_scripts:
            def create_script(script):
                def run_script():
                    con_post('\n> %s\n' % script)
                    con_post(console.run(script))
                script_name = script
                if len(script_name) > 15:
                    script_name = script_name[:12]+'...'
                Button(scripts_list, text=script_name, width=13, cursor='hand2', command=run_script).pack(side=BOTTOM, fill=X)
            create_script(script)
        list_scripts_open = True
    else:
        scripts_list.destroy()
        list_scripts_open = False

list_apps_open = False
def list_bin():
    global list_apps_open
    global list_scripts_open
    global apps_list
    if list_scripts_open == True:
        scripts_list.destroy()
        list_scripts_open = False
    if list_apps_open == False:
        apps_list = LabelFrame(width=105, height=25)
        apps_list.place(anchor=SW, relx=0, x=110, rely=1, y=-30)
        if len(console.player_apps) == 0:
            Label(apps_list, text='None', width=13).pack(side=BOTTOM, fill=X)
        for app in console.player_apps:
            def create_app(app):
                def run_app():
                    con_post('\n> %s\n' % app)
                    con_post(console.run(app))
                app_name = app
                if len(app_name) > 15:
                    app_name = app_name[:12]+'...'
                Button(apps_list, text=app_name, width=13, cursor='hand2', command=run_app).pack(side=BOTTOM, fill=X)
            create_app(app)
        list_apps_open = True
    else:
        apps_list.destroy()
        list_apps_open = False

explorer_app = StringVar()
explorer_app.set('Explorer')
browser_app = StringVar()
browser_app.set('Browser')
quickpad_app = StringVar()
quickpad_app.set('QuickPad')
frame_open = False
explorer_button = False
browser_button = False
quickpad_button = False
def makeframe():
    global frame_open
    global app_frame
    global explorer_button
    global browser_button
    global quickpad_button
    global list_apps_open
    global list_scripts_open
    console.reload_scripts()
    console.reload_apps()
    if not frame_open:
        #apps_button.configure(text='Applications [X]')
        app_frame = LabelFrame()
        app_frame.place(anchor=SW, relx=0, x=5, rely=1, y=-30)
        Button(app_frame, text='Apps >', relief=FLAT, width=13, cursor='hand2', command=list_bin).pack(side=BOTTOM, fill=X)
        Button(app_frame, text='Scripts >', relief=FLAT, cursor='hand2', command=list_scripts).pack(side=BOTTOM, fill=X)
        ttk.Separator(app_frame, orient=HORIZONTAL).pack(side=BOTTOM, fill=X)
        # Tabs
        quickpad_button = Button(app_frame, textvariable=quickpad_app, cursor='hand2', command=disable_3)
        quickpad_button.pack(side=BOTTOM, fill=X)
        browser_button = Button(app_frame, textvariable=browser_app, cursor='hand2', command=disable_2)
        browser_button.pack(side=BOTTOM, fill=X)
        explorer_button = Button(app_frame, textvariable=explorer_app, cursor='hand2', command=disable_1)
        explorer_button.pack(side=BOTTOM, fill=X)

        frame_open = True
    else:
        #apps_button.configure(text='Applications')
        if list_apps_open == True:
            apps_list.destroy()
            list_apps_open = False
        if list_scripts_open == True:
            scripts_list.destroy()
            list_scripts_open = False
        app_frame.destroy()
        frame_open = False
apps_button = Button(frame_apps, text='Applications', cursor='hand2', command=makeframe)
apps_button.pack(padx=2, pady=2, anchor=W, expand=False, side=LEFT)


# EARLY ACCESS WARNING
warning_msg = """
This game is in Alpha EARLY ACCESS!
That means that there will be BUGS, CRASHING, MISSING FEATURES, etc..
This game is no where near its final form. EVERYTHING is subject to change.
If you encounter any problems please send them to @exit_code_dev on twitter"""
dev_link = 'http://twitter.com/exit_code_dev'

#no_warning
if settings.no_warning == False:
    def open_devtwitter(event):
        import webbrowser
        link.configure(fg='lightblue')
        webbrowser.open('http://twitter.com/exit_code_dev')
        warning.after(1000, lambda:link.configure(fg='blue'))
    warning = LabelFrame(width=3000, height=3000)
    warning.place(anchor=N, relx=.5, rely=0)
    warning.pack_propagate(0)
    Label(warning, text='\nWARNING', fg='red', font=(None, 32)).pack()
    Label(warning, text=warning_msg, font=(None, 10)).pack()
    link = Label(warning, text=dev_link, fg='blue', font=(None, 10), cursor='hand2')
    link.pack()
    link.bind('<Button-1>', open_devtwitter)
    Button(warning, text='I Understand, Take me to the game!', fg='darkgreen', cursor='hand2', font=(None, 13), command=warning.destroy).pack(pady=20)


print '\n===== Game Output =====\n'

# UI Service Loop
root.mainloop()
print '\n===== SystemExit =====\n'
