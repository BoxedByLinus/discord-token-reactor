# Token reactor made by plexus

import tls_client
import random
import string
from colorama import Fore, init



def react_tokens(channel, message_id, endpoint):

    session = tls_client.Session(client_identifier='chrome_112')
    proxy = random.choice(open('proxies.txt', 'r').read().splitlines()) # Not needed but recommended
    tokens = open('tokens.txt', 'r').read().splitlines()

    for token in tokens:


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
            "location": "message",
            "type": 0
        }

        r = session.put(f"https://discord.com/api/v9/channels/{channel}/messages/{message_id}/reactions/{endpoint}", headers=headers, json=payload, proxy=f"http://{proxy}") # remove ', proxy=f"http://{proxy}"' if you dont want to use proxies

        if r.status_code == 204:
            print(f"   {Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]{Fore.GREEN} Added reaction: {token[:27]}******* ")
        else:
            print(f"   {Fore.WHITE}[{Fore.RED}!{Fore.WHITE}]{Fore.RED} Failed to add reaction: {token[:27]}*******")






def main():

    init(autoreset=True)

    channel = int(input(f"   {Fore.WHITE}[{Fore.CYAN}?{Fore.WHITE}]{Fore.CYAN} Enter the channel ID: "))
    message_id = int(input(f"   {Fore.WHITE}[{Fore.CYAN}?{Fore.WHITE}]{Fore.CYAN} Enter the message ID: "))
    endpoint = input(f"   {Fore.WHITE}[{Fore.CYAN}?{Fore.WHITE}]{Fore.CYAN} Enter the api endpoint (refer to repo for help): ")

    react_tokens(channel, message_id, endpoint)


main()

