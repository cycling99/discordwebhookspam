import time
import os

os.system('title syphoncore company - Discord Webhook Spammer')

statement = '''
[2024] syphoncore company

Syphoncore company software does NOT log cookies, or information of anykind.
Syphoncore does NOT permit the resale of this software or any other redistribution other than the offical GitHub page.

We are not responsible if anything happens to your Discord account during, or after the use of our software.
'''

banner = '''
 ██████  ██ ███████  ██████  ██████  ██████  ██████  
 ██   ██ ██ ██      ██      ██    ██ ██   ██ ██   ██ 
 ██   ██ ██ ███████ ██      ██    ██ ██████  ██   ██ 
 ██   ██ ██      ██ ██      ██    ██ ██   ██ ██   ██ 
 ██████  ██ ███████  ██████  ██████  ██   ██ ██████

 - Webhook Spammer made by syphoncore company
'''

# os functions
def pause():
    os.system('pause' if os.name == 'nt' else 'pause')

try:
    import requests
except ImportError:
    print("'requests' module was not found, installing requests...")
    os.system("pip install requests")
    print(" ")
    print(f"Installed 'requests' module, restart this software for changes to take affect.")
    pause()
    exit()

try:
    from colorama import Fore, Style, init
except ImportError:
    print("'colorama' module was not found, installing requests...")
    os.system("pip install colorama")
    print(" ")
    print(f"Installed 'colorama' module, restart this software for changes to take affect.")
    pause()
    exit()

init()

RATELIMIT = 1 # default: 1

def send_webhook_message(webhook_url, message, counter, username=None, avatar_url=None):
    """
    Sends a message to a Discord webhook with a counter.

    :param webhook_url: str, the URL of the Discord webhook
    :param message: str, the content of the message to send
    :param counter: int, the message counter
    :param username: str, optional, the username to display as the sender
    :param avatar_url: str, optional, the URL of the avatar image to display
    """

    message_with_counter = f"{message} (Message #{counter})"

    payload = {
        "content": message,
        "username": username,
        "avatar_url": avatar_url
    }

    while True:
        response = requests.post(webhook_url, json=payload)

        if response.status_code == 204:
            print(Fore.GREEN + f"[SUCCESS] Message {counter} sent successfully!")
            break
        elif response.status_code == 429:  
            retry_after = max(int(response.headers.get("Retry-After", RATELIMIT * 1000)) // 1000, RATELIMIT)
            print(Fore.YELLOW + f"[?] Rate limit encountered. Retrying after {retry_after} seconds...")
            time.sleep(retry_after)
        elif response.status_code == 404:  
            print(Fore.RED + Style.BRIGHT + "[ERROR] Webhook not found. (Most likely deleted)")
            pause()
            exit()
        else:
            print(Fore.RED + Style.BRIGHT + f"[ERROR] Failed to send message: {response.status_code}, {response.text}")
            break

print(statement)
time.sleep(5)
os.system('cls')
print(Style.BRIGHT + Fore.BLUE + banner)

if __name__ == "__main__":
    WEBHOOK_URL = input(Fore.WHITE + "Enter your Discord webhook URL >>> ")
    MESSAGE = input(Fore.WHITE + "Enter the message to send >>> ")
    USERNAME = input(Fore.WHITE + "Enter the username to display (optional, press Enter to skip) >>> ") or None
    AVATAR_URL = input(Fore.WHITE + "Enter the avatar URL (optional, press Enter to skip) >>> ") or None
    REPEAT_COUNT = int(input(Fore.WHITE + "Enter how many times you want the message spammed >>> "))

    for i in range(1, REPEAT_COUNT + 1):
        send_webhook_message(WEBHOOK_URL, MESSAGE, i, USERNAME, AVATAR_URL)

pause()
