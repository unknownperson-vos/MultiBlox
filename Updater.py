import requests
import os
import shutil
import zipfile
import tempfile
from time import sleep

class Updater:

    def __init__(self):
        print("[+] Looking for updates..")
        self.cur_version = open("version/version.txt","r+").read()
        self.git_raw = "https://raw.githubusercontent.com/unknownperson-vos/MultiBlox/refs/heads/main/version/version.txt"
        state = self._CheckUpdate()
        if state:
            print("\n[+] Update found !")
            self._TempClose()
            self._Update()
            print("\n[+] MultiBlox has been Updated ! Please reopen MultiBlox to see the changes.")
            sleep(5)
            os._exit(0)
        else:
            print("\n[+] No updates found, closing Updater automatically..")
            sleep(1)
            os._exit(0)

    def _DetectExt(self):
        if os.path.exists("MultiBlox.exe"):
            return "exe"
        elif os.path.exists("MultiBlox.pyw"):
            return "pyw"
        else:
            return "unknown"

    def _CheckUpdate(self):
        cont = requests.get(self.git_raw)
        if cont.status_code == 200:
            ver = str(cont.text.strip())
            if ver != self.cur_version:
                return True
            else:
                return False
        else:
            return False

    def _TempClose(self):
        print("[+] Closing MultiBlox..")
        exe_name = "MultiBlox.exe"
        extension = self._DetectExt()
        if extension == "pyw":
            os.system(f"taskkill /F /IM pythonw.exe >nul 2>&1")
        elif extension == "exe":
            os.system(f"taskkill /F /IM {exe_name} >nul 2>&1")
        else:
            pass
        
        sleep(1)

    def _Update(self):
        print("[+] Updating MultiBlox..")
        extension = self._DetectExt()
        tmp_dir = tempfile.mkdtemp()
        zip_path = os.path.join(tmp_dir, "update.zip")
        current_folder = os.getcwd()
        self_updater = "Updater.py" if extension == "pyw" else "Updater.exe"
        try:
            if extension == "pyw":
                zip_url = "https://github.com/unknownperson-vos/MultiBlox/archive/refs/heads/main.zip"
            elif extension == "exe":
                zip_url = "https://github.com/unknownperson-vos/MultiBlox/releases/latest/download/MultiBlox.zip"
            else:
                return
            with requests.get(zip_url, stream=True) as r:
                r.raise_for_status()
                with open(zip_path, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            z = zipfile.ZipFile(zip_path, 'r')
            z.extractall(tmp_dir)
            z.close()
            if extension == "pyw":
                extracted_folder = os.path.join(tmp_dir, "MultiBlox-main")
            else:
                extracted_folder = tmp_dir
            for item in os.listdir(extracted_folder):
                if item.lower() == self_updater.lower():
                    continue
                src = os.path.join(extracted_folder, item)
                dst = os.path.join(current_folder, item)
                if os.path.exists(dst):
                    if os.path.isfile(dst) or os.path.islink(dst):
                        os.remove(dst)
                    else:
                        shutil.rmtree(dst)
                if os.path.isdir(src):
                    shutil.copytree(src, dst)
                else:
                    shutil.copy2(src, dst)

        except Exception as e:
            pass
        finally:
            if os.path.exists(zip_path):
                try:
                    os.remove(zip_path)
                except:
                    pass
            sleep(0.2)
            shutil.rmtree(tmp_dir, ignore_errors=True)

Updater()