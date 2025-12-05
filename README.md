![Python](https://img.shields.io/badge/python-3.9+-blue)
![OS](https://img.shields.io/badge/OS-Windows%2010%2F11-green)
![License](https://img.shields.io/badge/license-MIT-orange)
![GitHub all releases](https://img.shields.io/github/downloads/unknownperson-vos/MultiBlox/total)

[![Download](https://img.shields.io/badge/Download-Release-blue?style=for-the-badge&logo=github)](https://github.com/unknownperson-vos/MultiBlox/releases/download/multiblox/MultiBlox.rar)

# ![icon](https://cdn.discordapp.com/attachments/1437646588859383889/1446355058437652510/roblox-logo-roblox-icon-transparent-free-png_1_21x21.png) MultiBlox

This Python-based tool makes multi-accounting on Roblox simple, stable, and fully automated. Once the program is running, users can open Roblox from any browser and log into different accounts without conflicts or forced logouts. The program takes care of session isolation behind the scenes, allowing seamless multi-session gameplay without modifying Roblox files or requiring complex setups.

Designed for convenience and accessibility, it works instantly on any windows machine, no configuration, no patching, and no browser extensions required. Just start the program, open your browsers, and enjoy as many Roblox accounts as you need running at the same time.

![Demo](assets/demo.gif)

---

## 📋 Features

- Open **multiple Roblox sessions** without conflicts.  
- Supports **any modern browser** (Chrome, Edge, Firefox, Opera, etc.).  
- No modifications to Roblox files required.  
- Built with **Python 3.9** for stability and reliability.  
- Uses **handle64.exe** (Microsoft Sysinternals) safely to manage Roblox session handles.  
- Minimal setup: just run `INSTALL.bat` and `START.bat`.  

---

## ✅ Requirements

- **Python 3.9+** *(Recommended: Python 3.9)*  
- Windows 10/11  
- Administrator privileges *(required for Roblox handle management)*  

---

## 🚀 Installation

1. **Install dependencies**  
   Run: ```INSTALL.bat```

This will automatically install all required Python modules.

2. **Start MultiBlox as Administrator**  
Run: ```START.bat```

This ensures MultiBlox has the necessary permissions to manage Roblox sessions.

![MultiBlox Demo](https://cdn.discordapp.com/attachments/1437646588859383889/1445961852021379112/pythonw_oXiRjsSH7o.png?ex=6932406a&is=6930eeea&hm=391f1578e5baaee9132426268517d80fecf27a04b2839dcf267d61c87144c538)

---

## 🔒 About `handle64.exe` (Safe & Official)

MultiBlox uses **handle64.exe**, a tool from the **Microsoft Sysinternals Suite**, to safely interact with Roblox process handles.

- **Official Microsoft page:**  
[https://learn.microsoft.com/en-us/sysinternals/downloads/handle](https://learn.microsoft.com/en-us/sysinternals/downloads/handle)

- **Purpose:**  
`handle64.exe` lists and manages open system handles.

- **Why MultiBlox uses it:**  
Roblox locks certain handles to prevent multiple sessions. MultiBlox uses handle64.exe to detect and release these locks, allowing unlimited sessions.

**Important:** `handle64.exe` is **safe, legitimate, and maintained by Microsoft**.

---

## 🎮 How to Use MultiBlox

1. Open MultiBlox using `START.bat`  
2. Open any browser (Chrome, Edge, Firefox, Opera, etc.)  
3. Log into a Roblox account and press **Play**  
4. Repeat in another browser or private window for additional accounts  
5. MultiBlox automatically handles session isolation

➡️ **You can open as many Roblox sessions as you want**, without logging out other accounts.
---

---
## Star this repository

Please star this repository to support me :)

---

