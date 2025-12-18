import re
import os
import sys
import requests
import shutil
import json
import random
import string
import threading
import base64
import msvcrt
import zlib
import psutil
import ctypes
import subprocess
import tempfile
from tkinter import filedialog
from datetime import datetime
from io import BytesIO
from PIL import Image, ImageTk, ImageDraw
from time import sleep, time
from pyperclip import copy
from tkinter import *
from tkinter import messagebox

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

window = Tk()

try:
    window.tk.call('tk', 'scaling', 1.0)
except:
    pass

window.title("MultiBlox")
window.geometry("764x805")
window.maxsize(764, 805)
window.minsize(764, 805)
window.iconbitmap("data/assets/mylogo.ico")
backg = PhotoImage(file='data/assets/Background.png')
ssettingsbg = PhotoImage(file='data/assets/SettingsBg.png')
backgprocessinfo = PhotoImage(file='data/assets/ProcessInfo.png')
supportbg = PhotoImage(file='data/assets/SupportBg.png')
donationbg = PhotoImage(file='data/assets/DonationBg.png')
btcbu = PhotoImage(file='data/assets/btcbu.png')
ethbu = PhotoImage(file='data/assets/ethbu.png')
ltcbu = PhotoImage(file='data/assets/ltcbu.png')
statsbg = PhotoImage(file='data/assets/statsbg.png')
title1 = PhotoImage(file='data/assets/title1.png')
title2 = PhotoImage(file='data/assets/title2.png')
title3 = PhotoImage(file='data/assets/title3.png')
title4 = PhotoImage(file='data/assets/title4.png')
title5 = PhotoImage(file='data/assets/title5.png')
title6 = PhotoImage(file='data/assets/title6.png')
doc_page1 = PhotoImage(file='data/assets/page1.png')
doc_page2 = PhotoImage(file='data/assets/page2.png')
doc_page3 = PhotoImage(file='data/assets/page3.png')
doc_page4 = PhotoImage(file='data/assets/page4.png')
doc_page14 = PhotoImage(file='data/assets/page14.png')
doc_page24 = PhotoImage(file='data/assets/page24.png')
doc_page34 = PhotoImage(file='data/assets/page34.png')
doc_page44 = PhotoImage(file='data/assets/page44.png')
prevbu = PhotoImage(file='data/assets/prevbu.png')
nextbu = PhotoImage(file='data/assets/nextbu.png')
joindiscord = PhotoImage(file='data/assets/JoinDiscord.png')
defaultpng = PhotoImage(file='data/assets/Default.png')
opdo = PhotoImage(file='data/assets/opdo.png')
opdoc = PhotoImage(file='data/assets/opdoc.png')
opse = PhotoImage(file='data/assets/opse.png')
opsu = PhotoImage(file='data/assets/opsu.png')
op = PhotoImage(file='data/assets/opsu.png')
OP = PhotoImage(file='data/assets/op.png')
oo = PhotoImage(file='data/assets/oo.png')
oo0 = PhotoImage(file='data/assets/oo0.png')
oo1 = PhotoImage(file='data/assets/oo1.png')
oo2 = PhotoImage(file='data/assets/oo2.png')
oo3 = PhotoImage(file='data/assets/oo3.png')
blankbu = PhotoImage(file='data/assets/blankbu.png')
fullbu = PhotoImage(file='data/assets/fullbu.png')
addbu = PhotoImage(file='data/assets/addbu.png')
browsebu = PhotoImage(file='data/assets/browsebu.png')
viewstats = PhotoImage(file='data/assets/viewstats.png')
noviewstats = PhotoImage(file='data/assets/noviewstats.png')

class MultiBlox:

    def __init__(self):
        if os.path.exists(os.path.join(tempfile.gettempdir(), "MultiBlox_data")):
            self._RestoreBackups()
        threading.Thread(target=self._Update).start()
        self._Loads_Settings()
        self._Loads_STats()
        self.roblox_ver = open("version/version.txt",'r+').read()
        self.ActiveInstances = 0
        self.Process = "RobloxPlayerBeta.exe"
        self.__CURRENTTIME = 0
        self.__PEAKINSTANCES = 0
        self.cookie_file = ""
        self.__SHOULD_BACKUP = False
        self.__issetting = False
        self.__issupport = False
        self.__isdocumentation = False
        self.__isdonations = False
        self.__isviewstats = False
        self.__Temphandlelines = []
        self.RobloxProfiles = []
        self.MutanT = []
        window.protocol("WM_DELETE_WINDOW", self._OnClose)
        threading.Thread(target=self._DashBoard).start()
        threading.Thread(target=self._ProcessDetection).start()
        threading.Thread(target=self._Runtime).start()

    def _Update(self):
        if os.path.exists("Updater.py"):
            try:
                os.remove("Updater.py")
            except:
                pass
        elif os.path.exists("Updater.exe"):
            try:
                os.remove("Updater.exe")
            except:
                pass
        else:
            pass
        try:
            os.remove("update.zip")
        except:
            pass
        self.up_cur_version = open("version/version.txt","r+").read()
        self.up_git_raw = "https://raw.githubusercontent.com/unknownperson-vos/MultiBlox/refs/heads/main/version/version.txt"
        if self._CheckUpdate():
            self.__SHOULD_BACKUP = True
            copy("https://github.com/unknownperson-vos/MultiBlox")
            messagebox.showinfo("MultiBlox","NEW Update Found ! Github's link copied automatically. Simply paste the link in your browser and download the latest version by clicking on the button 'download latest'. Enjoy")

    def _CheckUpdate(self):
        try:
            cont = requests.get(self.up_git_raw)
            if cont.status_code == 200:
                ver = str(cont.text.strip())
                if ver != self.up_cur_version:
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False

    def _RestoreBackups(self):
        temp_dir = tempfile.gettempdir()
        backup_root = os.path.join(temp_dir, "MultiBlox_data")
        data_root = "data"
        if not os.path.exists(backup_root):
            return
        for folder in ["configs", "stats", "logs"]:
            src = os.path.join(backup_root, folder)
            dst = os.path.join(data_root, folder)
            if not os.path.exists(src):
                continue
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
        try:
            shutil.rmtree(backup_root)
        except:
            pass

    def _BackupData(self):
        temp_dir = tempfile.gettempdir()
        backup_root = os.path.join(temp_dir, "MultiBlox_data")
        if os.path.exists(backup_root):
            shutil.rmtree(backup_root)
        os.makedirs(backup_root, exist_ok=True)
        for folder in ["configs", "stats", "logs"]:
            src = os.path.join("data", folder)
            dst = os.path.join(backup_root, folder)
            if os.path.exists(src):
                shutil.copytree(src, dst)
            else:
                pass

    def _Loads_Settings(self):
        with open("data/configs/configs.json", "r", encoding="utf-8") as f:
            self.__CONFIGS =  json.load(f)
    
    def _Loads_STats(self):
        with open("data/stats/stats.txt", "r") as f:
            encoded = f.read()
        decode = zlib.decompress(base64.b64decode(encoded))
        self.__STATSDICT = json.loads(decode.decode('utf-8'))

    def _Save_STats(self):
        if self.__STATSDICT['SessionOverview']['LongestSession'] < self.__CURRENTTIME:
            self.__STATSDICT['SessionOverview']['LongestSession'] = self.__CURRENTTIME
        if self.__STATSDICT['SessionOverview']['PeakConcurrentInstances'] < self.__PEAKINSTANCES:
            self.__STATSDICT['SessionOverview']['PeakConcurrentInstances'] = self.__PEAKINSTANCES

        json_bytes = json.dumps(self.__STATSDICT).encode('utf-8')
        compressed = base64.b64encode(zlib.compress(json_bytes)).decode('utf-8')
        with open("data/stats/stats.txt", "w") as f:
            f.write(compressed)

    def _SaveDaLogs(self):
        try:
            now = datetime.now()
            date_part = now.strftime("%Y%m%d_%H%M")
            rand_part = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
            file_name = f"{date_part}_{rand_part}.txt"
            LOGS_CONTENT = self.Logs.get("1.0", "end-1c")
            open(f"data/logs/{file_name}","w+").write(LOGS_CONTENT)
        except:
            pass

    def _Apply773Fix(self):
        try:
            cookies_path = os.path.join(os.getenv('LOCALAPPDATA'),r'Roblox\LocalStorage\RobloxCookies.dat')
            if os.path.exists(cookies_path):
                try:
                    self.cookie_file = open(cookies_path, 'r+b')
                    msvcrt.locking(self.cookie_file.fileno(), msvcrt.LK_NBLCK, os.path.getsize(cookies_path))
                    threading.Thread(target=self._UpdateLogs, args=("[SUCCESS] INCONSISTENT Error 773 FIX applied.",), daemon=True).start()
                except OSError:
                    threading.Thread(target=self._UpdateLogs, args=("[FAILED] Could not lock RobloxCookies.dat. It may already be locked.",), daemon=True).start()
            else:
                threading.Thread(target=self._UpdateLogs, args=("[INFO] Cookies file not found. 773 FIX skipped.",), daemon=True).start()
        except Exception as e:
            threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] Error applying 773 fix: {str(e)}",), daemon=True).start()

    def _OnClose(self):
        if self.cookie_file is not None:
            try:
                msvcrt.locking(self.cookie_file.fileno(), msvcrt.LK_UNLCK, os.path.getsize(self.cookie_file.name))
                self.cookie_file.close()
            except:
                pass
        if self.__SHOULD_BACKUP:
            self._BackupData()
        self._Save_STats()
        if self.__CONFIGS['features']['save_logs']:
            self._SaveDaLogs()
        window.destroy()
        if self.__CONFIGS['features']['quarantine_installers']:
            self._RestoreInstallers()
        os._exit(0)

    def _QuarantineInstallers(self):
        versions_path = os.path.join(os.getenv("LOCALAPPDATA"), "Roblox", "Versions")
        quarantine_base = os.path.join(tempfile.gettempdir(), "MultiBlox_Quarantine")
        if not os.path.exists(quarantine_base):
            os.mkdir(quarantine_base)
        try:
            for folder in os.listdir(versions_path):
                full = os.path.join(versions_path, folder)
                if os.path.isdir(full) and folder.startswith("version-"):
                    installer = os.path.join(full, "RobloxPlayerInstaller.exe")
                    if os.path.exists(installer):
                        try:
                            version_id = folder.split("-", 1)[1]
                            version_quarantine = os.path.join(quarantine_base, version_id)
                            if not os.path.exists(version_quarantine):
                                os.mkdir(version_quarantine)
                            os.replace(installer,os.path.join(version_quarantine, "RobloxPlayerInstaller.exe"))
                        except Exception:
                            threading.Thread(target=self._UpdateLogs,args=("[FAILED] Issue while moving RobloxPlayerInstaller.exe to TEMP quarantine",)).start()
            threading.Thread(target=self._UpdateLogs,args=("[SUCCESS] RobloxPlayerInstaller.exe quarantined to TEMP while MultiBlox is open",)).start()
        except Exception:
            threading.Thread(target=self._UpdateLogs,args=("[FAILED] Issue while parsing Roblox version paths",)).start()
    def _RestoreInstallers(self):
        versions_path = os.path.join(os.getenv("LOCALAPPDATA"), "Roblox", "Versions")
        quarantine_path = os.path.join(tempfile.gettempdir(), "MultiBlox_Quarantine")
        if not os.path.exists(quarantine_path):
            return
        try:
            for version_id in os.listdir(quarantine_path):
                q_folder = os.path.join(quarantine_path, version_id)
                installer_q = os.path.join(q_folder, "RobloxPlayerInstaller.exe")
                if not os.path.exists(installer_q):
                    continue
                roblox_folder = os.path.join(versions_path, f"version-{version_id}")
                if not os.path.exists(roblox_folder):
                    continue
                installer_restore = os.path.join(roblox_folder, "RobloxPlayerInstaller.exe")
                try:
                    os.replace(installer_q, installer_restore)
                except Exception:
                    pass
            threading.Thread(target=self._UpdateLogs,args=("[SUCCESS] Restored RobloxPlayerInstaller.exe to Roblox versions",)).start()
        except Exception:
            threading.Thread(target=self._UpdateLogs,args=("[FAILED] Issue while restoring Roblox installers from TEMP quarantine",)).start()
        try:
            shutil.rmtree(quarantine_path, ignore_errors=True)
        except:
            pass

    def _Runtime(self):
        while True:
            sleep(60)
            self.__CURRENTTIME +=1
            self.__STATSDICT['SessionOverview']['TotalRuntime'] +=1

    def _RobloxInfor(self,userid,pid,found):
        try:
            if found:
                founda = "[SUCCESS]"
            else:founda = "[FAILED]"
            r=requests.get(f"https://users.roblox.com/v1/users/{userid}")
            if r.status_code == 200:
                name = r.json()['name']
                Aaccounts = self.__STATSDICT["Accounts"]["FavoriteAccounts"]
                acc = next((a for a in Aaccounts if a["Username"] == name), None)
                if acc:
                    acc["SeenCount"] += 1
                else:
                    Aaccounts.append({"Username": name, "SeenCount": 1})
                    self.__STATSDICT["Accounts"]["TotalAccountsUsed"] += 1
            elif r.status_code == 429:
                threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] Could not fetch username error:{r.status_code} rate limited",)).start()
                name = "NOT Fetched"
            else:
                threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] Could not fetch username error:{r.status_code}",)).start()
                name = "NOT Fetched"
            raw = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar?userIds={userid}&size=420x420&format=Png&isCircular=false")
            if raw.status_code ==200:
                img = str(raw.json()["data"][0]["imageUrl"])
                robloxpic = img.replace("-Avatar-","-AvatarHeadshot-")
            elif raw.status_code == 429:
                threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] Could not fetch profile picture error:{r.status_code} rate limited",)).start()
                robloxpic = "NOT Fetched"
            else:
                threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] Could not fetch profile picture error:{r.status_code}",)).start()
                robloxpic = "NOT Fetched"
            if r.status_code ==200 and raw.status_code == 200:
                self.RobloxProfiles.append(f"{pid}|{name}|{userid}|{robloxpic}|{founda}")
                threading.Thread(target=self._UpdateLogs, args=(f"[SUCCESS] {name} attached to PID:{pid}",)).start()
            else:
                threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] Could not fetch roblox profile",)).start()
        except:
            self.RobloxProfiles.append(f"{pid}|NOT Fetched|NOT Fetched|NOT Fetched|{founda}")
            threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] Could not fetch roblox profile because user id was not found (this doesnt affect multiblox)",)).start()
        threading.Thread(target=self._ToInstancesList,args=("add",pid)).start()

    def _ToInstancesList(self,s,pid):
        if s == "add":
            try:
                for right in self.RobloxProfiles:
                    if str(pid) in right:
                        r=str(right).split("|")
                        self.InstanceList.insert(END, f"{r[4]}  {r[1]}  PID:{r[0]}  UserID:{r[2]}")
            except:
                pass
        else:
            try:
                for profile in self.RobloxProfiles.copy():
                    if str(pid) in profile:
                        self.RobloxProfiles.remove(profile)
                for idx in range(self.InstanceList.size()):
                    item_text = self.InstanceList.get(idx)
                    if f"PID:{pid}" in item_text:
                        self.InstanceList.delete(idx)
                        break
            except:
                pass

    def _CustomScripts(self,scripts):
        for script in scripts:
            try:
                ext = str(script).split(" - ")[0]
                path = str(script).split(" - ")[2]
                if ext == "py":
                    subprocess.Popen(["python", path],creationflags=subprocess.CREATE_NEW_CONSOLE)
                elif ext == "ps1":
                    subprocess.Popen(["powershell.exe","-ExecutionPolicy", "Bypass","-NoExit","-File", path],creationflags=subprocess.CREATE_NEW_CONSOLE)
                elif ext == "bat":
                    subprocess.Popen(["cmd.exe", "/c", "start", path],shell=False)
                elif ext == "js":
                    subprocess.Popen(["cmd.exe", "/c", "start", "node", path],shell=False)
                elif ext == "go":
                    subprocess.Popen(["cmd.exe", "/c", "start", "go", "run", path],shell=False)
                else:
                    pass
            except:
                pass

    def _ProcessDetection(self):
        target = self.Process.lower()
        known = set()
        active_sleep = 0.4
        base_idle_sleep = 0.5
        max_idle_sleep = 5.0
        idle_sleep = base_idle_sleep
        last_change = time()
        while True:
            current = {
                p.info["pid"]
                for p in psutil.process_iter(["pid", "name"])
                if p.info["name"] and p.info["name"].lower() == target
            }
            new = current - known
            closed = known - current
            if new:
                threading.Thread(target=self._Handle, args=(list(new),), daemon=True).start()
                known |= new
                self.ActiveInstances += len(new)
                threading.Thread(target=self._UpdateInstancesC, daemon=True).start()
                for pid in new:
                    if len(self.__CONFIGS['custom_scripts']['on_roblox_open']):
                        threading.Thread(target=self._CustomScripts,args=(self.__CONFIGS['custom_scripts']['on_roblox_open'],)).start()
                    threading.Thread(target=self._UpdateLogs, args=(f"[INFO] Roblox process created PID:{pid}",), daemon=True).start()
                    self.__STATSDICT['SessionOverview']['TotalInstances'] +=1
                    self.__PEAKINSTANCES +=1
                last_change = time()
                idle_sleep = base_idle_sleep
            if closed:
                known -= closed
                self.ActiveInstances -= len(closed)
                threading.Thread(target=self._UpdateInstancesC, daemon=True).start()
                for pid in closed:
                    if len(self.__CONFIGS['custom_scripts']['on_roblox_close']):
                        threading.Thread(target=self._CustomScripts,args=(self.__CONFIGS['custom_scripts']['on_roblox_close'],)).start()
                    threading.Thread(target=self._UpdateLogs, args=(f"[INFO] Roblox process closed PID:{pid}",), daemon=True).start()
                    threading.Thread(target=self._ToInstancesList, args=("remove", pid), daemon=True).start()
                    for mut in self.MutanT.copy():
                        try:
                            if str(mut).split("|")[0] == str(pid):
                                self.MutanT.remove(mut)
                        except:
                            pass
                last_change = time()
                idle_sleep = base_idle_sleep
            if self.__CONFIGS['features']['low_cpu_mode'] and not current:
                sleep_time = idle_sleep
                idle_sleep = min(idle_sleep * 1.5, max_idle_sleep)
            else:
                idle_duration = time() - last_change
                if idle_duration > 5.0:
                    sleep_time = min(active_sleep + (idle_duration - 5) * 0.2, 2.0)
                else:
                    sleep_time = active_sleep
            sleep(sleep_time)
    
    def _CustomHandleRegexMutex(self,lines,handle,pid):
        for RE_GEX in self.__CONFIGS['custom_regex']['singletonMutex']:
            try:
                REGGY = str(RE_GEX).split(" - ")[1]
                handle_value = None
                sleep(1)
                for line in lines:
                    if "ROBLOX_singletonMutex" in line:
                        m = re.search(REGGY, line, re.IGNORECASE)
                        if m:
                            handle_value = m.group(1)
                            break
                        else:
                            pass
                if not handle_value:
                    threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] INVALID Custom regex:{REGGY} mutex handle not closed for PID:{pid}",)).start()
                    self.__STATSDICT['SystemControl']['FailedHandleClosures'] +=1
                else:
                    r = subprocess.run(f'"{handle}" -accepteula -p {pid} -c {handle_value} -y',capture_output=True,text=True,timeout=2,shell=True)
                    if "error" in str(r).lower():
                        threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] INVALID Custom regex:{REGGY} mutex handle not closed for PID:{pid}",)).start()
                        self.__STATSDICT['SystemControl']['FailedHandleClosures'] +=1
                    else:
                        self.__STATSDICT['SystemControl']['TotalHandlesClosed'] +=1
                        self.__STATSDICT['SystemControl']['MutexHandlesClosed'] +=1
                        self.__STATSDICT['Automation']['TotalValidCustomRegex'] +=1
                        threading.Thread(target=self._UpdateLogs, args=(f"[SUCCESS] VALID Custom regex:{REGGY} Closed handle mutex for PID:{pid}",)).start()
                        break
            except:
                threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] INVALID Custom regex:{REGGY} mutex handle not closed for PID:{pid}",)).start()
                self.__STATSDICT['SystemControl']['FailedHandleClosures'] +=1
        if not handle_value:
            self.MutanT.append(f"{pid}|False")
            return False
        else:
            self.MutanT.append(f"{pid}|True")
            return True

    def _CustomHandleRegexEvent(self,lines,handle,pid):
        for RE_GEX in self.__CONFIGS['custom_regex']['singletonEvent']:
            try:
                REGGY = str(RE_GEX).split(" - ")[1]
                handle_value = None
                sleep(1)
                for line in lines:
                    if "ROBLOX_singletonEvent" in line:
                        m = re.search(REGGY, line, re.IGNORECASE)
                        if m:
                            handle_value = m.group(1)
                            break
                        else:
                            pass
                if not handle_value:
                    threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] INVALID Custom regex:{REGGY} event handle not closed for PID:{pid}",)).start()
                    self.__STATSDICT['SystemControl']['FailedHandleClosures'] +=1
                else:
                    r = subprocess.run(f'"{handle}" -accepteula -p {pid} -c {handle_value} -y',capture_output=True,text=True,timeout=2,shell=True)
                    if "error" in str(r).lower():
                        self.__STATSDICT['SystemControl']['FailedHandleClosures'] +=1
                        threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] INVALID Custom regex:{REGGY} event handle not closed for PID:{pid}",)).start()
                    else:
                        self.__STATSDICT['SystemControl']['TotalHandlesClosed'] +=1
                        self.__STATSDICT['SystemControl']['EventHandlesClosed'] +=1
                        self.__STATSDICT['Automation']['TotalValidCustomRegex'] +=1
                        threading.Thread(target=self._UpdateLogs, args=(f"[SUCCESS] VALID Custom regex:{REGGY} Closed handle event for PID:{pid}",)).start()
                        break
            except:
                self.__STATSDICT['SystemControl']['FailedHandleClosures'] +=1
                threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] INVALID Custom regex:{REGGY} event handle not closed for PID:{pid}",)).start()
        if not handle_value:
            return False
        else:
            return True

    def _MutantHandle(self,handle,lines,pid):
        handle_value = None
        sleep(1)
        for line in lines:
            if "ROBLOX_singletonMutex" in line:
                m = re.search(r"([0-9A-F]+):.*ROBLOX_singletonMutex", line, re.IGNORECASE)
                if m:
                    handle_value = m.group(1)
                    break
                else:
                    possible = re.findall(r"\b[0-9A-F]{4,}\b", line)
                    if possible:
                        handle_value = possible[0]
                        break
        if not handle_value:
            threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] Mutant handle not closed for PID:{pid}",)).start()
            self.MutanT.append(f"{pid}|False")
            self.__STATSDICT['SystemControl']['FailedHandleClosures'] +=1
        else:
            subprocess.run(f'"{handle}" -accepteula -p {pid} -c {handle_value} -y',stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL,shell=True)
            threading.Thread(target=self._UpdateLogs, args=(f"[SUCCESS] Closed handle mutant for PID:{pid}",)).start()
            self.MutanT.append(f"{pid}|True")
            self.__STATSDICT['SystemControl']['TotalHandlesClosed'] +=1
            self.__STATSDICT['SystemControl']['MutexHandlesClosed'] +=1
    def _ForceHandle(self,pid,lines,HANDLE):
        threading.Thread(target=self._UpdateLogs, args=(f"[INFO] Trying to force close handle event for PID:{pid}",)).start()
        sleep(0.1)
        threading.Thread(target=self._UpdateLogs, args=(f"[INFO] WAIT 3-4s BEFORE LAUNCHING ROBLOX AGAIN",)).start()
        handle_value = None
        for attempt in range(10):
            for c in range(100):
                for line in lines:
                    if f"Sessions\\{c}\\BaseNamedObjects\\ROBLOX_singletonEvent" in line:
                        raw = str(line).split(":")[0]
                        handle_value = re.sub(r'[^a-fA-F0-9]', '', raw)
                        break
                if handle_value:
                    break
            if handle_value:
                break
            sleep(0.2)
        if not handle_value:
            threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] Failed Again, to close handle event for PID:{pid}",)).start()
            self.__STATSDICT['SystemControl']['FailedHandleClosures'] +=1
            return False
        else:
            subprocess.run(f'"{HANDLE}" -accepteula -p {pid} -c {handle_value} -y',stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL,shell=True)
            threading.Thread(target=self._UpdateLogs, args=(f"[SUCCESS] Closed handle event for PID:{pid}",)).start()
            self.__STATSDICT['SystemControl']['TotalHandlesClosed'] +=1
            self.__STATSDICT['SystemControl']['EventHandlesClosed'] +=1
            return True
    def _Handle(self, newPIDs):
        sleep(2)
        if getattr(sys, "frozen", False):
            BASE = os.path.dirname(sys.executable)
        else:
            BASE = os.path.dirname(os.path.abspath(__file__))
        HANDLE = os.path.join(BASE, "handle", "handle64.exe")
        J = False
        for pid in newPIDs:
            handle_value = None
            handle_found = False
            dog = False
            doggy = False
            try:
                for attempt in range(5):
                    cmd = f'"{HANDLE}" -accepteula -p {pid} -a'
                    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                        stdin=subprocess.DEVNULL, text=True, shell=True)
                    lines = proc.stdout.splitlines()
                    self.__Temphandlelines = lines
                    if len(self.__CONFIGS['custom_regex']['singletonEvent']) > 0:
                        dog = self._CustomHandleRegexEvent(self.__Temphandlelines,HANDLE,pid)
                    if dog:
                        handle_value = True
                    else:
                        for line in lines:
                            if "ROBLOX_singletonEvent" in line:
                                m = re.search(r"([0-9A-F]+):.*ROBLOX_singletonEvent", line, re.IGNORECASE)
                                if m:
                                    handle_value = m.group(1)
                                    break
                                else:
                                    possible = re.findall(r"\b[0-9A-F]{4,}\b", line)
                                    if possible:
                                        handle_value = possible[0]
                                        break
                    if handle_value:
                        handle_found = True
                        break
                    sleep(1)
                if not handle_value:
                    threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] Handle not closed for PID:{pid}",)).start()
                    self.__STATSDICT['SystemControl']['FailedHandleClosures'] +=1
                    if self.__CONFIGS['features']['force_handle_closure']:
                        J = self._ForceHandle(pid,self.__Temphandlelines,HANDLE)
                        if J:
                            handle_found = True
                if J==False and handle_found:
                    subprocess.run(f'"{HANDLE}" -accepteula -p {pid} -c {handle_value} -y',
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL, shell=True)
                    threading.Thread(target=self._UpdateLogs, args=(f"[SUCCESS] Closed handle event for PID:{pid}",)).start()
                    self.__STATSDICT['SystemControl']['TotalHandlesClosed'] +=1
                    self.__STATSDICT['SystemControl']['EventHandlesClosed'] +=1
            except Exception:
                threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] Handle not closed for PID:{pid}",)).start()
                self.__STATSDICT['SystemControl']['FailedHandleClosures'] +=1
            if len(self.__CONFIGS['custom_regex']['singletonMutex']) > 0:
                doggy = self._CustomHandleRegexMutex(self.__Temphandlelines,HANDLE,pid)
            if not doggy:
                if self.__CONFIGS['features']['mutant_closer']:
                    threading.Thread(target=self._MutantHandle,args=(HANDLE,self.__Temphandlelines,pid)).start()
            user_id = None
            try:
                sleep(2)
                for attempt in range(10):
                    for line in self.__Temphandlelines:
                        if "logs" in line and "last.log" in line:
                            logfile = line.split("logs\\")[-1].split(".log")[0] + ".log"
                            roblax = os.path.join(os.getenv("LOCALAPPDATA"), "Roblox", "logs")
                            fulllogfile = os.path.join(roblax, logfile)
                            if os.path.exists(fulllogfile):
                                with open(fulllogfile, "r", encoding="utf-8", errors="ignore") as f:
                                    content = f.read()
                                if "userid:" in content:
                                    user_id = content.split("userid:")[1].split(",")[0].strip()
                                    threading.Thread(target=self._RobloxInfor, args=(user_id, pid, handle_found)).start()
                                    threading.Thread(target=self._UpdateLogs, args=(f"[SUCCESS] Found log file for PID:{pid}",)).start()
                                    break
                    if user_id:
                        break
                    sleep(1)
            except Exception:
                pass
            if not user_id:
                status = "[SUCCESS]" if handle_found else "[FAILED]"
                self.RobloxProfiles.append(f"{pid}|NOT Fetched|NOT Fetched|NOT Fetched|{status}")
                threading.Thread(target=self._RobloxInfor, args=(user_id, pid, handle_found)).start()

    def _PID_Info(self,pid,handle,mutant):
        text_to_return = "============ Handles ============\n\n"
        if handle == "[SUCCESS]":
            text_to_return += "Handle value singletonEvent : CLOSED Successfully\n"
        else:
            text_to_return += "Handle value singletonEvent : OPENED\n"
        if mutant == "False":
            text_to_return += "Handle value singletonMutex : OPENED\n"
        else:
            text_to_return += "Handle value singletonMutex : CLOSED Successfully\n"
        try:
            proc = psutil.Process(int(pid))
            try:
                handle_count = proc.num_handles()
                text_to_return += f"Handles Count : {str(handle_count)}\n"
            except:
                threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] Error while getting handles count PID:{pid}",)).start()
                text_to_return += f"Handles Count : Error\n"
            text_to_return += "\n============ Other ============\n\n"
            text_to_return += f"PID : {str(pid)}\n"
            try:
                exe_path = proc.exe()
                current = os.path.dirname(exe_path).split("version-")[1]
                text_to_return += f"Roblox Version : {str(current)}\n"
            except:
                threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] Error while getting roblox version PID:{pid}",)).start()
                text_to_return += f"Roblox Version : Error\n"
            try:
                start_time = datetime.fromtimestamp(proc.create_time())
                LANCH = start_time.strftime("%Y-%m-%d %H:%M:%S")
                uptime = datetime.now() - start_time
                text_to_return += f"Launch Time : {LANCH}\n"
                text_to_return += f"Uptime : {uptime}\n"
            except:
                threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] Error while getting start launch time PID:{pid}",)).start()
                text_to_return += f"Launch Time : Error\n"
                text_to_return += f"Uptime : Error\n"
            try:
                proc.cpu_percent(interval=None)
                sleep(0.1)
                cpu_usage = proc.cpu_percent(interval=None)
                cpu_usage = cpu_usage / psutil.cpu_count()
                text_to_return += f"CPU Usage : {str(cpu_usage)}%\n"
            except:
                threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] Error while getting CPU usage PID:{pid}",)).start()
                text_to_return += f"CPU Usage : Error\n"
            try:
                mem_info = proc.memory_info()
                ram_mb = mem_info.rss / (1024 * 1024)
                ram_mb2 = round(ram_mb, 2)
                text_to_return += f"RAM : {str(ram_mb2)} MB\n"
            except:
                threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] Error while getting RAM PID:{pid}",)).start()
                text_to_return += f"RAM : Error\n"
            try:
                thread_count = proc.num_threads()
                if thread_count <= 120:
                    htread= "STABLE"
                elif 121 <= thread_count <= 180:
                    htread="HIGH LOAD"
                elif 181 <= thread_count <= 300:
                    htread="UNSTABLE"
                else:
                    htread="CRITICAL"
                text_to_return += f"Threads : {str(thread_count)} ({htread})\n"
            except:
                threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] Error while getting threads PID:{pid}",)).start()
                text_to_return += f"Threads : Error\n"
        except:
            threading.Thread(target=self._UpdateLogs, args=(f"[FAILED] Invalid / Closed / Quarantined PID:{pid}",)).start()
            text_to_return += "\nError: Invalid PID"
        return text_to_return

    def _Update_ProcessInformation(self,event):
        try:
            self.processinfogui.destroy()
        except:
            pass
        selected_index = self.InstanceList.curselection()
        if selected_index:
            line = str(self.InstanceList.get(selected_index[0]))
            pid = line.split("PID:")[1].split(" ")[0].strip()
            for p in self.RobloxProfiles:
                if pid in p:
                    t = p.split("|")
                    name = t[1]
                    userid = t[2]
                    pic = t[3]
                    handle = t[4]
            mutant = "False"
            for a in self.MutanT:
                if pid in a:
                    tt = a.split("|")
                    mutant = tt[1]
                else:
                    mutant = "False"
            text = self._PID_Info(pid,handle,mutant)
            threading.Thread(target=self._ProcessInformation,args=(name,userid,pic,text,pid)).start()
    
    def _ProfilePIIC(self,pic):
        if pic != "NOT Fetched":
            try:
                response = requests.get(pic)
                img = __import__("PIL").Image.open(BytesIO(response.content)).convert("RGBA")
                img = img.resize((120, 120), __import__("PIL").Image.Resampling.LANCZOS)
                tk_image = ImageTk.PhotoImage(img)
                self.ThumbnailLabel.config(image=tk_image)
                self.ThumbnailLabel.image = tk_image
            except:
                pass

    def _ProcessInformation(self,name,userid,pic,text,pid):
        self.processinfogui = Toplevel(window)
        self.processinfogui.title("MultiBlox (Process Information)")
        self.processinfogui.geometry("608x464")
        self.processinfogui.maxsize(608, 464)
        self.processinfogui.minsize(608, 464)
        self.processinfogui.iconbitmap("data/assets/mylogo.ico")
        Bg = Label(self.processinfogui, image=backgprocessinfo,borderwidth=0)
        Bg.place(x=0, y=0)
        self.ThumbnailLabel = Label(self.processinfogui, image=defaultpng,borderwidth=0,bg='#111111')
        self.ThumbnailLabel.place(x=70,y=200)
        rblxname = Label(self.processinfogui, text=name,font=("Consolas",13),bg="#111111",fg="#FFFFFF")
        rblxname.place(x=75,y=370)
        rblxname = Label(self.processinfogui, text=userid,font=("Consolas",13),bg="#111111",fg="#FFFFFF")
        rblxname.place(x=83,y=402)
        processaa = Text(self.processinfogui, bg="#0B0B0B", fg="#FFFFFF",wrap="none",width=42, height=15,font=("Consolas", 13),borderwidth=0)
        processaa.place(x=277,y=198)
        processaa.insert('end',text)
        processaa.config(state="disabled")
        threading.Thread(target=self._ProfilePIIC,args=(pic,)).start()

    def _Bombaclat(self):
        while True:
            if self.ActiveInstances > 0:
                try:
                    for img in (oo1, oo2, oo3, oo2, oo1, oo0):
                        self.processingbu.config(image=img)
                        self.processingbu.current_image = img
                        sleep(0.06)
                except:
                    pass
                sleep(0.8)
            else:
                try:
                    if getattr(self.processingbu, "current_image", None) != oo:
                        self.processingbu.config(image=oo)
                        self.processingbu.current_image = oo
                except:
                    pass
                sleep(2)

    def _ColorsForLogs(self,event=None):
        for tag in self.Logs.tag_names():
            self.Logs.tag_remove(tag, "1.0", "end")
        keywords = {"PID": "blue","FAILED": "red","process": "purple","SUCCESS": "green","attached": "green","INFO":"orange","SETTINGS":"orange","INVALID":"red","VALID":"green","INCONSISTENT":"yellow"}
        content = self.Logs.get("1.0", "end")
        for kw, color in keywords.items():
            for kw, color in keywords.items():
                for match in re.finditer(rf'\b{re.escape(kw)}\b', content, re.MULTILINE):
                    start_index = f"1.0+{match.start()}c"
                    end_index = f"1.0+{match.end()}c"
                    self.Logs.tag_add(kw, start_index, end_index)
                    self.Logs.tag_config(kw, foreground=color)

    def _UpdateInstancesC(self):
        try:
            self.Activeprocessesdisplay.config(text=str(self.ActiveInstances))
        except:
            pass

    def _UpdateLogs(self,m):
        try:
            self.Logs.config(state="normal")
            self.Logs.insert("end", m + "\n")
            self.Logs.see("end")
            self.Logs.config(state="disabled")
            self._ColorsForLogs()
        except:
            pass

    def _Settings_MutantCloser(self):
        if self.__CONFIGS['features']['mutant_closer']:
            self.__CONFIGS['features']['mutant_closer'] = False
            self.__mutantcloser.config(image=blankbu)
            threading.Thread(target=self._UpdateLogs, args=(f"[SETTINGS] Mutant Mutex Closer : OFF",)).start()
        else:
            self.__CONFIGS['features']['mutant_closer'] = True
            self.__mutantcloser.config(image=fullbu)
            threading.Thread(target=self._UpdateLogs, args=(f"[SETTINGS] Mutant Mutex Closer : ON",)).start()

    def _Settings_QuarantineInstallers(self):
        if self.__CONFIGS['features']['quarantine_installers']:
            self.__CONFIGS['features']['quarantine_installers'] = False
            self.__quarantine_installers.config(image=blankbu)
            threading.Thread(target=self._RestoreInstallers).start()
            threading.Thread(target=self._UpdateLogs, args=(f"[SETTINGS] Quarantine Installers : OFF",)).start()
        else:
            self.__CONFIGS['features']['quarantine_installers'] = True
            self.__quarantine_installers.config(image=fullbu)
            threading.Thread(target=self._QuarantineInstallers).start()
            threading.Thread(target=self._UpdateLogs, args=(f"[SETTINGS] Quarantine Installers : ON",)).start()

    def _Settings_SaveLogs(self):
        if self.__CONFIGS['features']['save_logs']:
            self.__CONFIGS['features']['save_logs'] = False
            self.__save_logs.config(image=blankbu)
            threading.Thread(target=self._UpdateLogs, args=(f"[SETTINGS] Save Logs : OFF",)).start()
        else:
            self.__CONFIGS['features']['save_logs'] = True
            self.__save_logs.config(image=fullbu)
            threading.Thread(target=self._UpdateLogs, args=(f"[SETTINGS] Save Logs : ON",)).start()

    def _Settings_ForceHandleClosure(self):
        if self.__CONFIGS['features']['force_handle_closure']:
            self.__CONFIGS['features']['force_handle_closure'] = False
            self.__force_handle_closure.config(image=blankbu)
            threading.Thread(target=self._UpdateLogs, args=(f"[SETTINGS] Force Handle Closure : OFF",)).start()
        else:
            self.__CONFIGS['features']['force_handle_closure'] = True
            self.__force_handle_closure.config(image=fullbu)
            threading.Thread(target=self._UpdateLogs, args=(f"[SETTINGS] Force Handle Closure : ON",)).start()

    def _Settings_LOWCPUMode(self):
        if self.__CONFIGS['features']['low_cpu_mode']:
            self.__CONFIGS['features']['low_cpu_mode'] = False
            self.__low_cpu_mode.config(image=blankbu)
            threading.Thread(target=self._UpdateLogs, args=(f"[SETTINGS] Force Handle Closure : OFF",)).start()
        else:
            self.__CONFIGS['features']['low_cpu_mode'] = True
            self.__low_cpu_mode.config(image=fullbu)
            threading.Thread(target=self._UpdateLogs, args=(f"[SETTINGS] Force Handle Closure : ON",)).start()

    def _Settings_SingletonEventBu(self):
        if self._isonsingletonevent:
            self._isonsingletonevent = False
            self.__singletonEvent.config(image=blankbu)
            self._isonsingletonmutex = True
            self.__singletonMutex.config(image=fullbu)
        else:
            self._isonsingletonevent = True
            self.__singletonEvent.config(image=fullbu)
            self._isonsingletonmutex = False
            self.__singletonMutex.config(image=blankbu)
    
    def _Settings_SingletonMutexBu(self):
        if self._isonsingletonmutex:
            self._isonsingletonevent = True
            self.__singletonEvent.config(image=fullbu)
            self._isonsingletonmutex = False
            self.__singletonMutex.config(image=blankbu)
        else:
            self._isonsingletonevent = False
            self.__singletonEvent.config(image=blankbu)
            self._isonsingletonmutex = True
            self.__singletonMutex.config(image=fullbu)

    def _Settings_LoadALLList(self):
        try:
            for reg in self.__CONFIGS['custom_regex']['singletonEvent']:
                self.__REGEXLIST.insert(END,reg)
        except:
            pass
        try:
            for reg in self.__CONFIGS['custom_regex']['singletonMutex']:
                self.__REGEXLIST.insert(END,reg)
        except:
            pass
        try:
            for cs in self.__CONFIGS['custom_scripts']['on_roblox_open']:
                self.__CUSTOMSCRIPTLIST.insert(END,cs)
        except:
            pass
        try:
            for cs in self.__CONFIGS['custom_scripts']['on_roblox_close']:
                self.__CUSTOMSCRIPTLIST.insert(END,cs)
        except:
            pass
    def _Settings_ReemoveRegexList(self,event):
        selected_index = self.__REGEXLIST.curselection()
        if selected_index:
            to_ramove = str(self.__REGEXLIST.get(selected_index[0]))
            self.__REGEXLIST.delete(selected_index[0])
            if to_ramove.split(" - ")[0] == "singletonEvent":
                self.__CONFIGS['custom_regex']['singletonEvent'].remove(to_ramove)
            else:
                self.__CONFIGS['custom_regex']['singletonMutex'].remove(to_ramove)
    def _Settings_AddRegexList(self):
        regex_to_add = self.__regexentry.get()
        if len(regex_to_add) > 2:
            try:
                re.compile(regex_to_add)
                if self._isonsingletonevent:
                    self.__CONFIGS['custom_regex']['singletonEvent'].append(f"singletonEvent - {regex_to_add}")
                    self.__REGEXLIST.insert(END,f"singletonEvent - {regex_to_add}")
                    threading.Thread(target=self._UpdateLogs, args=(f"[SETTINGS] VALID Custom singletonEvent Regex. Added to list",)).start()
                else:
                    self.__CONFIGS['custom_regex']['singletonMutex'].append(f"singletonMutex - {regex_to_add}")
                    self.__REGEXLIST.insert(END,f"singletonMutex - {regex_to_add}")
                    threading.Thread(target=self._UpdateLogs, args=(f"[SETTINGS] VALID Custom singletonMutex Regex. Added to list",)).start()
            except re.error:
                threading.Thread(target=self._UpdateLogs, args=(f"[SETTINGS] INVALID Regex input",)).start()

    def _Settings_onRobloxOpen(self):
        if self._isonopen:
            self._isonopen = False
            self.__ONOPEN.config(image=blankbu)
            self._isonclose = True
            self.__ONCLOSE.config(image=fullbu)
        else:
            self._isonopen = True
            self.__ONOPEN.config(image=fullbu)
            self._isonclose = False
            self.__ONCLOSE.config(image=blankbu)
    
    def _Settings_onRobloxClose(self):
        if self._isonclose:
            self._isonopen = True
            self.__ONOPEN.config(image=fullbu)
            self._isonclose = False
            self.__ONCLOSE.config(image=blankbu)
        else:
            self._isonopen = False
            self.__ONOPEN.config(image=blankbu)
            self._isonclose = True
            self.__ONCLOSE.config(image=fullbu)

    def _Settings_BrowsePathScript(self):
        path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
        if path:
            if path.endswith((".py", ".go", ".js", ".ps1", ".bat")):
                self.__customscriptpath.config(state="normal")
                self.__customscriptpath.delete(0, "end")
                self.__customscriptpath.insert(0, path)
                self.__customscriptpath.config(state="disabled")
                get_ext = path.split(".")[-1]
                if self._isonopen:
                    self.__CONFIGS['custom_scripts']['on_roblox_open'].append(f"{get_ext} - onOpen - {path}")
                    self.__CUSTOMSCRIPTLIST.insert(END,f"{get_ext} - onOpen - {path}")
                    threading.Thread(target=self._UpdateLogs, args=(f"[SETTINGS] VALID Custom script added to onOpen list",)).start()
                else:
                    self.__CONFIGS['custom_scripts']['on_roblox_close'].append(f"{get_ext} - onClose - {path}")
                    self.__CUSTOMSCRIPTLIST.insert(END,f"{get_ext} - onClose - {path}")
                    threading.Thread(target=self._UpdateLogs, args=(f"[SETTINGS] VALID Custom script added to onClose list",)).start()
            else:
                threading.Thread(target=self._UpdateLogs, args=(f"[SETTINGS] INVALID script selected",)).start()
                threading.Thread(target=self._UpdateLogs, args=(f"[SETTINGS] Files supported : .py, .js, .go, .ps1, .bat",)).start()
        else:
            pass
    
    def _Settings_RemoveCustomScript(self,event):
        selected_index = self.__CUSTOMSCRIPTLIST.curselection()
        if selected_index:
            to_ramove = str(self.__CUSTOMSCRIPTLIST.get(selected_index[0]))
            self.__CUSTOMSCRIPTLIST.delete(selected_index[0])
            if to_ramove.split(" - ")[1] == "onOpen":
                self.__CONFIGS['custom_scripts']['on_roblox_open'].remove(to_ramove)
            else:
                self.__CONFIGS['custom_scripts']['on_roblox_close'].remove(to_ramove)

    def _Save_Settings(self):
        with open("data/configs/configs.json", "w", encoding="utf-8") as f:
            json.dump(self.__CONFIGS, f, indent=4)
    def _Settings_OnClose(self):
        self.__issetting = False
        self.gotoSettings.config(image=opse)
        self._Save_Settings()
        self.settingsgui.destroy()
        threading.Thread(target=self._UpdateLogs, args=(f"[SETTINGS] Saved to configs.json !",)).start()
    def _ThreadSettings(self):
        if self.__issetting:
            pass
        else:
            self.__issetting = True
            self.gotoSettings.config(image=OP)
            threading.Thread(target=self._Settings).start()
    def _Settings(self):
        self._isonsingletonevent = True
        self._isonsingletonmutex = False
        self._isonopen = True
        self._isonclose = False
        self.settingsgui = Toplevel(window)
        self.settingsgui.title("MultiBlox (Settings)")
        self.settingsgui.geometry("771x685")
        self.settingsgui.maxsize(771, 685)
        self.settingsgui.minsize(771, 685)
        self.settingsgui.iconbitmap("data/assets/mylogo.ico")
        self.settingsgui.protocol("WM_DELETE_WINDOW", self._Settings_OnClose)
        Bg = Label(self.settingsgui, image=ssettingsbg,borderwidth=0)
        Bg.place(x=0, y=0)
        self.__mutantcloser = Button(self.settingsgui, image=blankbu,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Settings_MutantCloser)
        self.__mutantcloser.place(x=696,y=196)
        self.__quarantine_installers = Button(self.settingsgui, image=blankbu,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Settings_QuarantineInstallers)
        self.__quarantine_installers.place(x=696,y=295)
        self.__save_logs = Button(self.settingsgui, image=blankbu,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Settings_SaveLogs)
        self.__save_logs.place(x=696,y=393)
        self.__force_handle_closure = Button(self.settingsgui, image=blankbu,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Settings_ForceHandleClosure)
        self.__force_handle_closure.place(x=696,y=476)
        self.__low_cpu_mode = Button(self.settingsgui, image=blankbu,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Settings_LOWCPUMode)
        self.__low_cpu_mode.place(x=696,y=559)
        self.__singletonEvent = Button(self.settingsgui, image=fullbu,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Settings_SingletonEventBu)
        self.__singletonEvent.place(x=27,y=193)
        self.__singletonMutex = Button(self.settingsgui, image=blankbu,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Settings_SingletonMutexBu)
        self.__singletonMutex.place(x=198,y=193)
        self.__regexentry = Entry(self.settingsgui,font=("Consolas", 13),bg='#B1B1B1', fg='#1A1A1A',width=33,borderwidth=0)
        self.__regexentry.place(x=33,y=266)
        add_to_regex = Button(self.settingsgui, image=addbu,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Settings_AddRegexList)
        add_to_regex.place(x=276,y=265)
        self.__REGEXLIST = Listbox(self.settingsgui,highlightthickness=0 ,bg="#0B0B0B", fg="#FFFFFF", width=42, height=5,font=("Consolas", 13) ,borderwidth=0)
        self.__REGEXLIST.place(x=33,y=302)
        self.__ONOPEN = Button(self.settingsgui, image=fullbu,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Settings_onRobloxOpen)
        self.__ONOPEN.place(x=27,y=471)
        self.__ONCLOSE = Button(self.settingsgui, image=blankbu,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Settings_onRobloxClose)
        self.__ONCLOSE.place(x=198,y=471)
        self.__customscriptpath = Entry(self.settingsgui,font=("Consolas", 13),bg='#B1B1B1', fg='#1A1A1A',state="disabled",disabledbackground='#B1B1B1',disabledforeground='#1A1A1A',width=32,borderwidth=0)
        self.__customscriptpath.place(x=33,y=539)
        add_script_path = Button(self.settingsgui, image=browsebu,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Settings_BrowsePathScript)
        add_script_path.place(x=269,y=538)
        self.__CUSTOMSCRIPTLIST = Listbox(self.settingsgui,highlightthickness=0 ,bg="#0B0B0B", fg="#FFFFFF", width=42, height=5,font=("Consolas", 13) ,borderwidth=0)
        self.__CUSTOMSCRIPTLIST.place(x=33,y=574)
        if self.__CONFIGS['features']['quarantine_installers']:
            self.__quarantine_installers.config(image=fullbu)
        if self.__CONFIGS['features']['mutant_closer']:
            self.__mutantcloser.config(image=fullbu)
        if self.__CONFIGS['features']['save_logs']:
            self.__save_logs.config(image=fullbu)
        if self.__CONFIGS['features']['force_handle_closure']:
            self.__force_handle_closure.config(image=fullbu)
        if self.__CONFIGS['features']['low_cpu_mode']:
            self.__low_cpu_mode.config(image=fullbu)
        self.__REGEXLIST.bind("<<ListboxSelect>>", self._Settings_ReemoveRegexList)
        self.__CUSTOMSCRIPTLIST.bind("<<ListboxSelect>>", self._Settings_RemoveCustomScript)
        threading.Thread(target=self._Settings_LoadALLList).start()

    def _Support_OnClose(self):
        self.__issupport = False
        self.gotoSupport.config(image=opsu)
        self.supportgui.destroy()
    def _Thread_Support(self):
        if self.__issupport:
            pass
        else:
            self.__issupport = True
            self.gotoSupport.config(image=OP)
            threading.Thread(target=self._Support).start()
    def _Support_DiscordLink(self):
        copy("https://discord.gg/tMtdpUSrdM")
        messagebox.showinfo("MultiBlox","Discord link copied to clipboard ! Simply paste on discord to join")
    def _Support(self):
        self.supportgui = Toplevel(window)
        self.supportgui.title("MultiBlox (Support)")
        self.supportgui.geometry("512x509")
        self.supportgui.maxsize(512, 509)
        self.supportgui.minsize(512, 509)
        self.supportgui.iconbitmap("data/assets/mylogo.ico")
        self.supportgui.protocol("WM_DELETE_WINDOW", self._Support_OnClose)
        Bg = Label(self.supportgui, image=supportbg,borderwidth=0)
        Bg.place(x=0, y=0)
        discorjoinbu = Button(self.supportgui, image=joindiscord,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Support_DiscordLink)
        discorjoinbu.place(x=174,y=430)
    def _Documentation_OnClose(self):
        self.__isdocumentation = False
        self.gotoDocumen.config(image=opdoc)
        self.documengui.destroy()
    def _Thread_Documentation(self):
        if self.__isdocumentation:
            pass
        else:
            self.__isdocumentation = True
            self.gotoDocumen.config(image=OP)
            threading.Thread(target=self._Documentation).start()
    def _Documentation_Next(self):
        if self._onpage < 4:
            self._onpage +=1
            if self._onpage == 2:
                self.doc_Bg.config(image=doc_page2)
                self.doc_Bg2.config(image=doc_page24)
            elif self._onpage == 3:
                self.doc_Bg.config(image=doc_page3)
                self.doc_Bg2.config(image=doc_page34)
            elif self._onpage == 4:
                self.doc_Bg.config(image=doc_page4)
                self.doc_Bg2.config(image=doc_page44)
    def _Documentation_Previous(self):
        if self._onpage > 1:
            self._onpage = self._onpage -1
            if self._onpage == 1:
                self.doc_Bg.config(image=doc_page1)
                self.doc_Bg2.config(image=doc_page14)
            elif self._onpage == 2:
                self.doc_Bg.config(image=doc_page2)
                self.doc_Bg2.config(image=doc_page24)
            elif self._onpage == 3:
                self.doc_Bg.config(image=doc_page3)
                self.doc_Bg2.config(image=doc_page34)
    def _Documentation(self):
        self._onpage = 1
        self.documengui = Toplevel(window)
        self.documengui.title("MultiBlox (Documentation)")
        self.documengui.geometry("815x861")
        self.documengui.maxsize(815, 861)
        self.documengui.minsize(815, 861)
        self.documengui.iconbitmap("data/assets/mylogo.ico")
        self.documengui.protocol("WM_DELETE_WINDOW", self._Documentation_OnClose)
        self.doc_Bg = Label(self.documengui, image=doc_page1,borderwidth=0)
        self.doc_Bg.place(x=0, y=0)
        self.doc_Bg2 = Label(self.documengui, image=doc_page14,bg='#0B0B0B',borderwidth=0)
        self.doc_Bg2.place(x=225, y=811)
        NextAAA = Button(self.documengui, image=nextbu,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Documentation_Next)
        NextAAA.place(x=452,y=819)
        PrevAAA = Button(self.documengui, image=prevbu,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Documentation_Previous)
        PrevAAA.place(x=325,y=819)
    def _Donations_OnClose(self):
        self.__isdonations = False
        self.gotoDonations.config(image=opdo)
        self.donationgui.destroy()
    def _Thread_Donations(self):
        if self.__isdonations:
            pass
        else:
            self.__isdonations = True
            self.gotoDonations.config(image=OP)
            threading.Thread(target=self._Donations).start()
    def _Donations_BTC(self):
        copy("bc1qq3kuqn39h4uf2kr80230gqrj8k4gf9sx5ppzuf")
        messagebox.showinfo("MultiBlox","Bitcoin Address Copied !")
    def _Donations_ETH(self):
        copy("0xb89E00a5C4d73239697470B6415f65671F4beb2D")
        messagebox.showinfo("MultiBlox","Ethereum Address Copied !")
    def _Donations_LTC(self):
        copy("LSkcr4zrSM2kF6W19F6VMi7ic2nSEAoibY")
        messagebox.showinfo("MultiBlox","Litecoin Address Copied !")
    def _Donations(self):
        self.donationgui = Toplevel(window)
        self.donationgui.title("MultiBlox (Donations)")
        self.donationgui.geometry("530x840")
        self.donationgui.maxsize(530, 840)
        self.donationgui.minsize(530, 840)
        self.donationgui.iconbitmap("data/assets/mylogo.ico")
        self.donationgui.protocol("WM_DELETE_WINDOW", self._Donations_OnClose)
        Bg = Label(self.donationgui, image=donationbg,borderwidth=0)
        Bg.place(x=0, y=0)
        BTCAA = Button(self.donationgui, image=btcbu,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Donations_BTC)
        BTCAA.place(x=28,y=756)
        ETHAA = Button(self.donationgui, image=ethbu,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Donations_ETH)
        ETHAA.place(x=194,y=756)
        LTCAA = Button(self.donationgui, image=ltcbu,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Donations_LTC)
        LTCAA.place(x=360,y=756)
    def _TitleAlgo(self):
        s = self.__STATSDICT
        runtime = s["SessionOverview"]["TotalRuntime"]
        longest = s["SessionOverview"]["LongestSession"]
        instances = s["SessionOverview"]["TotalInstances"]
        peak = s["SessionOverview"]["PeakConcurrentInstances"]
        handles = s["SystemControl"]["TotalHandlesClosed"]
        events = s["SystemControl"]["EventHandlesClosed"]
        mutexes = s["SystemControl"]["MutexHandlesClosed"]
        regex = s["Automation"]["TotalValidCustomRegex"]
        scripts = s["Automation"]["TotalCustomScriptsLaunched"]
        accounts_used = s["Accounts"]["TotalAccountsUsed"]
        if (runtime >= 60 * 60 and longest >= 6 * 60 and instances >= 300 and peak >= 10 and handles >= 15_000 and regex >= 15 and scripts >= 75 and accounts_used >= 10):
            return "Singleton Slayer"
        if (runtime >= 30 * 60 and instances >= 150 and peak >= 7 and handles >= 5_000 and regex >= 5 and scripts >= 20):
            return "Ultimate Operator"
        if (runtime >= 15 * 60 and instances >= 80 and peak >= 5 and handles >= 2_000 and longest >= 3 * 60):
            return "Instance Overlord"
        if (runtime >= 5 * 60 and instances >= 30 and handles >= 500 and events >= 150 and mutexes >= 150 and peak >= 3):
            return "Handle Specialist"
        if (runtime >= 60 and instances >= 10 and handles >= 50):
            return "Active Handler"
        return "Explorer"
    def _ViewSTats_Title(self):
        title = self._TitleAlgo()
        if title=="Active Handler":
            self.StatTitle.config(image=title2)
        elif title =="Handle Specialist":
            self.StatTitle.config(image=title3)
        elif title == "Instance Overlord":
            self.StatTitle.config(image=title4)
        elif title == "Ultimate Operator":
            self.StatTitle.config(image=title5)
        elif title == "Singleton Slayer":
            self.StatTitle.config(image=title6)
        else:
            pass
    def _Fetch_ViewStats(self):
        accounts = self.__STATSDICT["Accounts"]["FavoriteAccounts"]
        top_accounts = sorted(
            accounts,
            key=lambda acc: acc["SeenCount"],
            reverse=True
        )[:3]
        t = ""
        for a in top_accounts:
            t += f"-> {a['Username']} (Used {a['SeenCount']} times)\n"
        text = f'''Session Overview
------------------------------------------------
Total Runtime                   : {self.__STATSDICT['SessionOverview']['TotalRuntime']} mins
Longest Session                 : {self.__STATSDICT['SessionOverview']['LongestSession']} mins
Total Instances                 : {self.__STATSDICT['SessionOverview']['TotalInstances']}
Highest Instance Count          : {self.__STATSDICT['SessionOverview']['PeakConcurrentInstances']}


System Control
------------------------------------------------
Total Handles Closed            : {self.__STATSDICT['SystemControl']['TotalHandlesClosed']}
Total Event Handle Closed       : {self.__STATSDICT['SystemControl']['EventHandlesClosed']}
Total Mutex Handle Closed       : {self.__STATSDICT['SystemControl']['MutexHandlesClosed']}
Total Failed Handle Closures    : {self.__STATSDICT['SystemControl']['FailedHandleClosures']}

Total Valid Custom Regex        : {self.__STATSDICT['Automation']['TotalValidCustomRegex']}
Total Custom Scripts Launched   : {self.__STATSDICT['Automation']['TotalCustomScriptsLaunched']}


Accounts
------------------------------------------------
Total Accounts Used             : {self.__STATSDICT['Accounts']['TotalAccountsUsed']}
Favorite Roblox Accounts
{t}
'''
        self.MyStatss.insert("end",text)
    def _ViewStats_OnClose(self):
        self.__isviewstats = False
        self.gotoViewStats.config(image=viewstats)
        self.statsgui.destroy()
    def _Thread_ViewStats(self):
        if self.__isviewstats:
            pass
        else:
            self.__isviewstats = True
            self.gotoViewStats.config(image=noviewstats)
            threading.Thread(target=self._ViewStats).start()
    def _ViewStats(self):
        self.statsgui = Toplevel(window)
        self.statsgui.title("MultiBlox (Stats)")
        self.statsgui.geometry("586x443")
        self.statsgui.maxsize(586, 443)
        self.statsgui.minsize(586, 443)
        self.statsgui.iconbitmap("data/assets/mylogo.ico")
        self.statsgui.protocol("WM_DELETE_WINDOW", self._ViewStats_OnClose)
        Bg = Label(self.statsgui, image=statsbg,borderwidth=0)
        Bg.place(x=0, y=0)
        self.StatTitle = Label(self.statsgui, image=title1,borderwidth=0,bg="#0B0B0B")
        self.StatTitle.place(x=18, y=122)
        self.MyStatss = Text(self.statsgui, bg="#0B0B0B", fg="#FFFFFF",wrap="none",width=45, height=15,font=("Consolas", 13),borderwidth=0)
        self.MyStatss.place(x=233,y=186)
        threading.Thread(target=self._Fetch_ViewStats).start()
        threading.Thread(target=self._ViewSTats_Title).start()
    def _Updatemesssage(self):
        if os.path.exists("data/Updatemessage.txt"):
            m = open("data/Updatemessage.txt","r").read()
            if "boogaboogaooo" in m:
                pass
            else:
                messagebox.showinfo("MultiBlox",f"{m}")
                open("data/Updatemessage.txt","w+").write(f"{m}\nboogaboogaooo")
    def _DashBoard(self):
        Bg = Label(window, image=backg,borderwidth=0)
        Bg.place(x=0, y=0)
        version = Label(window, text=f"{self.roblox_ver}",font=("Inter",16),bg="#111111",fg="#FFFFFF")
        version.place(x=686,y=77)
        self.Activeprocessesdisplay = Label(window, text=f"{self.ActiveInstances}",font=("Inter",16),bg="#111111",fg="#FFFFFF")
        self.Activeprocessesdisplay.place(x=681,y=146)
        self.gotoSettings = Button(window, image=opse,bg='#111111',borderwidth=0, activebackground="#111111",command=self._ThreadSettings)
        self.gotoSettings.place(x=40,y=435)
        self.gotoSupport = Button(window, image=opsu,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Thread_Support)
        self.gotoSupport.place(x=40,y=535)
        self.gotoDocumen = Button(window, image=opdoc,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Thread_Documentation)
        self.gotoDocumen.place(x=40,y=635)
        self.gotoDonations = Button(window, image=opdo,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Thread_Donations)
        self.gotoDonations.place(x=40,y=735)
        self.gotoViewStats = Button(window, image=viewstats,bg='#111111',borderwidth=0, activebackground="#111111",command=self._Thread_ViewStats)
        self.gotoViewStats.place(x=36,y=318)
        self.InstanceList = Listbox(window, highlightthickness=0,bg="#0B0B0B", fg="#FFFFFF", width=55, height=14,font=("Consolas", 13) ,borderwidth=0)
        self.InstanceList.place(x=343,y=198)
        self.Logs = Text(window, bg="#0B0B0B", fg="#FFFFFF",wrap="none",width=55, height=15,font=("Consolas", 13) ,state="disabled",borderwidth=0)
        self.Logs.place(x=342,y=534)
        self.processingbu = Button(window, image=oo,bg='#111111',borderwidth=0, activebackground="#111111")
        self.processingbu.place(x=694,y=26)
        threading.Thread(target=self._Bombaclat).start()
        threading.Thread(target=self._Updatemesssage).start()
        self.InstanceList.bind("<<ListboxSelect>>", self._Update_ProcessInformation)
        if self.__CONFIGS['features']['quarantine_installers']:
            self._QuarantineInstallers()
        self._Apply773Fix()
        

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    MultiBlox()
    window.mainloop()
else:
    messagebox.showerror("MultiBlox","Admin privileges are required to use MultiBlox. Please run START.bat")