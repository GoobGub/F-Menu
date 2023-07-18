import requests
import random
from time import sleep
from colorama import Fore

def selector(token, users):
    while True:
        try:
            response = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                print(f"{Fore.RED}Created groupchat")
            elif response.status_code == 429:
                print(f"{Fore.YELLOW}Rate limited ({response.json()['retry_after']}ms){Fore.RESET}")
            else:
                print(f"{Fore.RED}Error: {response.status_code}{Fore.RESET}")
        except requests.RequestException as e:
            print(f"{Fore.RED}Error: {e}{Fore.RESET}")
        except KeyboardInterrupt:
            break
        finally:
            sleep(1)  # Add a delay to avoid excessive requests


def randomizer(token, ID):
    while True:
        try:
            if len(ID) < 2:
                print(f"{Fore.RED}Error: Not enough friends to choose from{Fore.RESET}")
                break
            users = random.sample(ID, 2)
            response = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                print(f"{Fore.RED}Created groupchat")
            elif response.status_code == 429:
                print(f"{Fore.YELLOW}Rate limited ({response.json()['retry_after']}ms){Fore.RESET}")
            else:
                print(f"{Fore.RED}Error: {response.status_code}{Fore.RESET}")
        except requests.RequestException as e:
            print(f"{Fore.RED}Error: {e}{Fore.RESET}")
        except KeyboardInterrupt:
            break
        finally:
            sleep(1)  # Add a delay to avoid excessive requests


def GcSpammer():
    token = input(f"{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Enter your Discord token: {Fore.RED}")
    print(f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}Do you want to choose user(s) yourself to groupchat spam or do you want to select randoms?')
    sleep(1)
    print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] choose user(s) yourself
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] randomize the users
                        ''')
    try:
        secondchoice = int(input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Second Choice: {Fore.RED}'))
    except ValueError:
        print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Second Choice')
        sleep(1)
        return

    if secondchoice not in [1, 2]:
        print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Second Choice')
        sleep(1)
        return

    if secondchoice == 1:
        setTitle(f"Creating groupchats")
        recipients = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Input the users you want to create a groupchat with (separate by , id,id2,id3): {Fore.RED}')
        user = recipients.split(',')
        if len(user) < 2:
            print(f"{Fore.RED}Error: Not enough users provided{Fore.RESET}")
            sleep(3)
            return
        SlowPrint("\"ctrl + c\" at anytime to stop\n")
        sleep(1.5)
        selector(token, user)

    elif secondchoice == 2:
        setTitle(f"Creating groupchats")
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=getheaders(token)).json()
        IDs = [friend['id'] for friend in friendIds]
        SlowPrint("\"ctrl + c\" at anytime to stop\n")
        sleep(1.5)
        randomizer(token, IDs)


if __name__ == "__main__":
    GcSpammer()
