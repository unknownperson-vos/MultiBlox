import re
import os
import threading
import psutil
import ctypes
import subprocess
from time import sleep
from pyperclip import copy
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("MultiBlox")
window.geometry("392x440")
window.maxsize(392, 440)
window.minsize(392, 440)
window.iconbitmap("assets/mylogo.ico")
backg = PhotoImage(file='assets/background.png')
copp = PhotoImage(file='assets/copy.png')

class MultiBlox:

    def __init__(self):
        self.PIDs = []
        self.ModPIDs = []
        self.Process = "RobloxPlayerBeta.exe"
        threading.Thread(target=self._ProcessDetection).start()
        threading.Thread(target=self.Blox).start()
    
    def _ProcessDetection(self):
        while True:
            current_pids = set()
            for proc in psutil.process_iter(["pid", "name"]):
                if proc.info["name"] and proc.info["name"].lower() == self.Process.lower():
                    pid = proc.info["pid"]
                    current_pids.add(pid)
                    if pid not in self.ModPIDs:
                        self.PIDs.append(pid)
            if len(self.PIDs) > 0:
                self._Handle(self.PIDs)
                for piiid in self.PIDs:
                    self.ModPIDs.append(piiid)
                self.PIDs.clear()
            for pid in list(self.ModPIDs):
                if pid not in current_pids:
                    self.ModPIDs.remove(pid)
            sleep(0.3)
    def _Handle(self,newPIDs):
        sleep(2)
        for pid in newPIDs:
            try:
                cmd_find = f'handle64.exe -accepteula -p {pid} -a'
                proc = subprocess.run(cmd_find, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL, text=True, shell=True)
                lines = proc.stdout.splitlines()
                handle_value = None
                c = 0
                for _ in range(100):
                    for line in lines:
                        if f"\\Sessions\\{c}\\BaseNamedObjects\\ROBLOX_singletonEvent" in line:
                            my_value = line.split(":")[0]
                            handle_value = re.sub(r'[^a-fA-F0-9]', '', my_value)
                            break
                    if handle_value:
                        break
                    c += 1
                if not handle_value:
                    pass
                else:
                    subprocess.run(f'handle64.exe -accepteula -p {pid} -c {handle_value} -y',stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL,shell=True)
            except:
                pass

    def _Discord(self):
        threading.Thread(target=self.Discord).start()
    def Discord(self):
        copy("https://discord.gg/tMtdpUSrdM")
        messagebox.showinfo("MultiBlox","Discord server link copied ! Thank you for joining our community")

    def _Donate(self):
        threading.Thread(target=self.Donate).start()
    def Donate(self):
        copy("bc1qq3kuqn39h4uf2kr80230gqrj8k4gf9sx5ppzuf")
        messagebox.showinfo("MultiBlox","Bitcoin address copied ! Thank you for donations")

    def Blox(self):
        Bg = Label(window, image=backg,borderwidth=0)
        Bg.place(x=0, y=0)
        CopyDiscord = Button(window, image=copp,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Discord)
        CopyDiscord.place(x=265,y=336)
        CopyDonation = Button(window, image=copp,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Donate)
        CopyDonation.place(x=265,y=376)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def on_close():
    window.destroy()
    os._exit(0)

if is_admin:
    MultiBlox()
    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()
else:
    messagebox.showerror("MultiBlox","Admin privileges are required to use MultiBlox. Please run START.bat")