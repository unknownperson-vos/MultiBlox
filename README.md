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

## 🧠 Overview

Roblox normally prevents you from opening more than one client at a time using internal **mutexes and events**.  
MultiBlox automatically detects newly launched Roblox processes, **closes the required handles**, and lets you open **as many Roblox instances as your system can handle**.

On top of that, MultiBlox provides:
- Real-time process detection
- Roblox account identification (username, user ID, avatar)
- Per-instance process analytics
- Custom automation (scripts on open/close)
- Extensive logging & debugging tools
- A clean, modern GUI

All of this runs **locally**, without injecting code into Roblox.

---

## ✨ Features

### 🧩 Multi-Instance Core
- ✅ Automatically bypasses Roblox single-instance restrictions
- ✅ Closes `ROBLOX_singletonEvent` and `ROBLOX_singletonMutex`
- ✅ Supports **custom regex-based handle detection**
- ✅ Optional **forced handle closure** when Roblox is stubborn
- ✅ Works with **custom Roblox bootstrappers**

---

### 🔍 Real-Time Process Detection
- Live detection of:
  - New Roblox processes
  - Closed Roblox processes
- Automatic updates to the instance list
- Animated activity indicator when Roblox is running

---

### 👤 Roblox Account Detection
- Automatically extracts **UserID** from Roblox logs
- Fetches:
  - Username
  - Profile picture
- Displays account info per PID
- Gracefully handles rate limits & missing data

---

### 📊 Per-Instance Process Information
For every Roblox instance, you can view:
- PID
- Roblox version
- Launch time & uptime
- CPU usage
- RAM usage
- Thread count (with stability rating)
- Handle status (Event & Mutex)

All displayed in a clean dedicated window.

---

### ⚙️ Advanced Settings Panel
Toggle features instantly with visual feedback:

- 🔁 Mutant (Mutex) Closer
- 📦 Quarantine Roblox Installers (TEMP-based)
- 📝 Save logs on exit
- 💪 Force handle closure
- 🧊 Low CPU mode (dynamic sleep scaling)

All settings are saved automatically to:
```
data/configs/configs.json
```

---

### 🧪 Custom Regex Engine
Add your own regex patterns to:
- Detect custom `singletonEvent`
- Detect custom `singletonMutex`

Perfect for:
- Custom Roblox builds
- Modified clients
- Future Roblox updates

---

### 🤖 Automation & Custom Scripts
Run scripts automatically:
- 🟢 When Roblox opens
- 🔴 When Roblox closes

Supported file types:
- `.py`
- `.ps1`
- `.bat`
- `.js`
- `.go`

Perfect for:
- Auto VPN switching
- Account setup
- Logging
- Monitoring tools

---

### 🗂 Installer Quarantine System
- Temporarily moves `RobloxPlayerInstaller.exe` to TEMP
- Prevents Roblox from force-updating while MultiBlox is open
- Automatically restores installers on exit

---

### 🧾 Advanced Logging
- Color-coded logs:
  - ✅ SUCCESS (green)
  - ❌ FAILED (red)
  - ℹ️ INFO (orange)
- Logs can be automatically saved to: ``data/logs/``
- Unique timestamped filenames

---

### 🧠 Low CPU Mode
- Dynamically reduces CPU usage when idle
- Ideal for long-running sessions

---

### 📖 Built-in Documentation
- Step-by-step in-app documentation
- Beginner friendly
- No external links required

---

### 💬 Community & Support
- One-click Discord invite
- Clipboard auto-copy for invite link

---

### 💖 Donations
MultiBlox is **free & open-source**.  
If you want to support development, donations are accepted in:

- 🟠 Bitcoin (BTC) : bc1qq3kuqn39h4uf2kr80230gqrj8k4gf9sx5ppzuf
- 🔵 Ethereum (ETH) : 0xb89E00a5C4d73239697470B6415f65671F4beb2D
- 🟣 Litecoin (LTC) : LSkcr4zrSM2kF6W19F6VMi7ic2nSEAoibY

Any amount is appreciated ❤️  
The **best way to support** is:
- ⭐ Starring this repository
- 💬 Joining the Discord

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

![MultiBlox Demo](https://cdn.discordapp.com/attachments/1437646588859383889/1450229350933860484/python_eUQjVebckg.png?ex=6941c6d5&is=69407555&hm=4d63d7ee5dd461fbba629e22a635ff7a71362e106ca7b659f4c7169cfee45f92)

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

