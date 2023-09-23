# Bot creator made by plexus

import tls_client
import random
import string
from colorama import Fore, init



def make_bot(token):

    session = tls_client.Session(client_identifier='chrome_112')
    proxy = random.choice(open('proxies.txt', 'r').read().splitlines()) # Not needed but recommended


    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Authorization": token,
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
        "Origin": "https://discord.com",
        "Pragma": "no-cache",
        "Referer": "https://discord.com/developers/applications",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        "X-Track": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiU2FmYXJpIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImF5LUJPIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgNi4xOyBXT1c2NCkgQXBwbGVXZWJLaXQvNTM0LjU3LjIgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzUuMS4yIFNhZmFyaS81MzQuNTIuNyIsImJyb3dzZXJfdmVyc2lvbiI6IjUuMS4yIiwib3NfdmVyc2lvbiI6IjciLCJyZWZlcnJlciI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbiI6Ind3dy5nb29nbGUuY29tIiwic2VhcmNoX2VuZ2luZSI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo3MjExMiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    }

    payload = {
        "name": "plexus",
        "team_id": None
    }


    try:
        r = session.post(url="https://discord.com/api/v9/applications", headers=headers, json=payload, proxy=f'http://{proxy}')
    except Exception as e:
        print(Fore.RED+f"Something went wrong: {e}")
        return

    if r.status_code == 201:

        print(Fore.GREEN+f"(+) Made Bot ID: {r.json()['id']}")

        res = session.post(url=f"https://discord.com/api/v9/applications/{r.json()['id']}/bot/reset", headers=headers, json={}, proxy=f'http://{proxy}')

        if res.status_code == 200:

            print(Fore.GREEN + f"(+) DEBUG: Gotten bot token: {res.json()['token'][:26]}*****")

            session.get("https://discord.com/api/v9/experiments")
            headers['X-Fingerprint'] = "1071861684764938290.LF9Okx-1071881013329932308.016nW7dhymgXw5CWh41HSkoDMH8"

            payload = {
                "bot_public": True,
                "bot_require_code_grant": False,
                "flags": 565248
            }

            response = session.patch(url=f"https://discord.com/api/v9/applications/{r.json()['id']}", headers=headers, json=payload)

            if response.status_code == 200:

                print(Fore.GREEN + f"(+) DEBUG: Intents On: {res.json()['token'][:26]}*****")

                with open("output.txt", "a") as f:
                    f.write(f"{res.json()['token']}:{r.json()['id']}\n")

                print(" ")

               # change_pfp = session.patch(url=f"https://discord.com/api/v9/applications/{r.json()['id']}")
            else:
                print(Fore.RED + f"Error making bot: {r.status_code}\n R.text: {r.text}")
        else:
            print(Fore.RED + f"Error making bot: {r.status_code}\n R.text: {r.text}")
    else:
        print(Fore.RED+f"Error making bot: {r.status_code}\n R.text: {r.text}")

while True: # You can change this loop depending on how many tokens you want to make

    make_bot("") # Add a Email verified user token
