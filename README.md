![Image](https://cdn.discordapp.com/attachments/1437646588859383889/1448514190762442762/wp642dwad9383.jpg?ex=693b8977&is=693a37f7&hm=3c0dbbd2d33ba20c6aa208f6985edadf6720bfd1faf400e2917d8c1b43adff54)

![Python](https://img.shields.io/badge/python-3.9+-blue)
![OS](https://img.shields.io/badge/OS-Windows%2010%2F11-green)
![License](https://img.shields.io/badge/license-MIT-orange)
![GitHub all releases](https://img.shields.io/github/downloads/unknownperson-vos/MultiBlox/total)

[![Download](https://img.shields.io/badge/Download-Latest-blue?style=for-the-badge&logo=github)](https://github.com/unknownperson-vos/MultiBlox/releases/latest/download/MultiBlox.zip)

# ![icon](https://cdn.discordapp.com/attachments/1437646588859383889/1446356649907322891/roblox-logo-roblox-icon-transpar213131313ent-free-png_2_cropped.png?ex=6933b019&is=69325e99&hm=3e3ca4dfc9f08bfb482d81860487e3e840482d9ad296400837f3af074c2312f8) MultiBlox

**MultiBlox** is an advanced, beginner-friendly **Roblox multi-instance manager** written in Python with a full graphical interface.  
It allows you to run **multiple Roblox accounts at the same time** by automatically handling Roblox’s singleton restrictions, monitoring processes in real-time, and giving you deep insight into each running instance.

MultiBlox is designed to work not only with the **default Roblox launcher**, but also with **custom bootstrappers** such as:

- ✅ **Bloxstrap**
- ✅ **Fishstrap**
- ✅ **Voidstrap**
- ✅ Other custom Roblox bootstrappers

---

![Demo](assets/demo.gif)

---

## 🤙 For Support

Join our discord server for any questions, bugs, suggestions, etc

Link : https://discord.gg/tMtdpUSrdM

---

## ✨ Features

- ✅ Bypasses Roblox single-instance limitations automatically
- ✅ Allows running unlimited Roblox accounts simultaneously (system dependent)
- ✅ Automatically detects new Roblox processes in real time
- ✅ Automatically detects when Roblox processes close
- ✅ Works with the default Roblox launcher
- ✅ Fully compatible with custom Roblox bootstrappers (Bloxstrap, Fishstrap, Voidstrap, etc.)
- ✅ Closes `ROBLOX_singletonEvent` handles automatically
- ✅ Closes `ROBLOX_singletonMutex` handles automatically
- ✅ Supports advanced regex-based handle detection
- ✅ Allows custom regex patterns for future Roblox updates
- ✅ Optional forced handle closure for stubborn instances
- ✅ No Roblox memory injection
- ✅ No DLL injection
- ✅ Uses process and handle management only
- ✅ Live Roblox instance list with real-time updates
- ✅ Displays each instance’s PID
- ✅ Displays Roblox version per instance
- ✅ Displays launch time and uptime per instance
- ✅ Displays real-time CPU usage per instance
- ✅ Displays real-time RAM usage per instance
- ✅ Displays thread count per instance
- ✅ Thread-based stability indicator
- ✅ Detects handle state per instance (Event & Mutex)
- ✅ Dedicated per-instance information window
- ✅ Extracts UserID automatically from Roblox logs
- ✅ Fetches Roblox username automatically
- ✅ Fetches Roblox profile avatar automatically
- ✅ Gracefully handles Roblox API rate limits
- ✅ Gracefully handles missing or corrupted log files
- ✅ Built-in low CPU usage mode
- ✅ Dynamic sleep scaling when idle
- ✅ Designed for long-running sessions
- ✅ Advanced settings panel with instant toggles
- ✅ Mutex closer toggle
- ✅ Installer quarantine toggle
- ✅ Force handle closure toggle
- ✅ Save logs on exit toggle
- ✅ Low CPU mode toggle
- ✅ Automatically saves settings to JSON
- ✅ Persistent configuration storage
- ✅ Installer quarantine system to prevent forced Roblox updates
- ✅ Temporarily moves Roblox installers to a safe TEMP location
- ✅ Automatically restores installers on exit
- ✅ Custom script execution on Roblox launch
- ✅ Custom script execution on Roblox close
- ✅ Supports `.py`, `.ps1`, `.bat`, `.js`, `.go` scripts
- ✅ Perfect for automation workflows
- ✅ Integrated logging system
- ✅ Color-coded logs (success, info, error)
- ✅ Timestamped log files
- ✅ Optional automatic log saving
- ✅ Clean and modern GUI
- ✅ Animated activity indicators
- ✅ Beginner-friendly interface
- ✅ Built-in documentation
- ✅ One-click Discord invite copy
- ✅ Fully local execution (no external services required)
- ✅ Open-source and transparent
- ✅ Designed for stability and safety
- ✅ Educational and personal-use focused

---

![MultiBlox Demo](https://cdn.discordapp.com/attachments/1437646588859383889/1450229350933860484/python_eUQjVebckg.png?ex=6941c6d5&is=69407555&hm=4d63d7ee5dd461fbba629e22a635ff7a71362e106ca7b659f4c7169cfee45f92)

---

## ▶️ Usage

### Option 1: Prebuilt Executable
1. Download the release
2. Extract the folder
3. Run `MultiBlox.exe`
4. Launch Roblox accounts normally (browser or bootstrapper)

### Option 2: Run From Source
```bash
START.bat
```

---

## 📦 Requirements (Source Code)

- Windows 10 / 11

- Python 3.9+

- Required libraries:
```
pip install psutil requests pillow pyperclip
```

**Additional requirements:**

- handle64.exe (Sysinternals Handle tool)

Must be located in:

- handle/handle64.exe

---

## 🧠 Notes

- No code injection

- No Roblox memory modification

- Uses process & handle management only

- Designed to be as safe and stable as possible

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

## ⭐️ Star this repository

Please star this repository to support me, it takes 2 seconds 😊

---

