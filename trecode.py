from tkinter import Tk, Label
import time
import os
import configparser

def readConfig(path):
    targets = []
    words = []
    config = configparser.ConfigParser()
    config.read(path)
    for option in config.options('Clear'):
        words.append([config.get('Clear', option), ''])
    for option in config.options('Target'):
        targets.append(config.get('Target', option))
    for option in config.options('Change'):
        words.append([option, targets[int(config.get('Change', option))]])
    return words

def recode():
    global prev
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    if len(changes) > 0:
        try:
            curr = root.clipboard_get()
            if curr != prev:
                curr1 = curr
                for p in changes:
                    n = curr1.find(p[0])
                    while n != -1:
                        curr1 = curr1[:n] + p[1] + curr1[n+len(p[0]):]
                        n = curr1.find(p[0])
                if curr1 != curr:
                    curr = curr1
                    root.clipboard_clear()
                    root.clipboard_append(curr1)
                prev = curr
                root.update()
        except:
            pass
    root.after(100, recode)

if __name__ == '__main__':
    path = "tr_settings.ini"
    if os.path.exists(path):
        changes = readConfig(path)
    else:
        changes = []
    root = Tk()
    clock = Label(root, fg='blue', font=('times', 20, 'bold'), bg='gray')
    clock.pack(fill='both', expand=1)
    root.withdraw()
    root.overrideredirect(0)
    root.iconify()

    prev = ''
    time1 = ''
    recode()
    root.mainloop()
