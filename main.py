import ctypes.wintypes, random, ctypes, requests, os, string, pathlib, sys, time, subprocess
from colorama import *
from pystyle import *

init()

count = 0
liste = ["1", "2", "3", "cls"]
ctypes.windll.kernel32.SetConsoleTitleW(f"")

PASTE_BIN_URL = "https://pastebin.com/"

hardwareid = (
    subprocess.check_output("wmic csproduct get uuid").decode().split("\n")[1].strip()
)
site = requests.get(PASTE_BIN_URL)

try:
    if hardwareid in site.text:
        pass
    else:
        print(f"[!] > To buy this tool dm @sowqa on discord!")
        print(f"[?] > Your HardwareID is " + hardwareid)
        time.sleep(30)
        input()
        exit(123)
except:
    print(f"[!] > The connection to our database failed!")
    input()
    exit(123)

LicenseKey = input(f"Enter your key licence > ")
if LicenseKey == "atzne":
    print(
        f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] > {Fore.GREEN}Your key is valid!{Fore.BLUE}"
    )
    time.sleep(2)
else:
    print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] > {Fore.RED}Your key is invalid!")
    print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] > {Fore.RED}Press enter to quit!")
    input("")
    exit(123)

os.system("cls")

banner1 = """
██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ███╗   ██╗██╗████████╗██████╗  ██████╗
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗
██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║
██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║
██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝
"""


def Start():
    print(Center.XCenter(banner1))
    print(
        Center.XCenter(
            f"{Fore.WHITE}╔═════════════════════════╗╔═════════════════════════╗"
        )
    )
    print(
        Center.XCenter(
            f"{Fore.WHITE}                             ║[{Fore.BLUE}1{Fore.WHITE}] - {Fore.BLUE}Nitro Generator {Fore.WHITE}   ║║ # {Fore.BLUE}Sowqa Generator     {Fore.WHITE}  ║"
        )
    )
    print(
        Center.XCenter(
            f"{Fore.WHITE}                             ║[{Fore.BLUE}2{Fore.WHITE}] - {Fore.BLUE}Nitro Checker   {Fore.WHITE}   ║║ # {Fore.BLUE}Github: @sowqa      {Fore.WHITE}  ║"
        )
    )
    print(
        Center.XCenter(
            f"{Fore.WHITE}                             ║[{Fore.BLUE}3{Fore.WHITE}] - {Fore.BLUE}Exit            {Fore.WHITE}   ║║ # {Fore.BLUE}Discord: @sowqa     {Fore.WHITE}  ║"
        )
    )
    print(
        Center.XCenter(
            f"{Fore.WHITE}╚═════════════════════════╝╚═════════════════════════╝"
        )
    )


def nitro_generator():
    yy = 0
    while True:
        code = "" + ("").join(
            random.choices(string.ascii_letters + string.digits, k=16)
        )
        f = open("nitro.txt", "a+")
        f.write(f"https://discord.gift/{code}\n")
        print(
            f"{Fore.WHITE}[{Fore.BLUE}GENERATED{Fore.WHITE}] > {Fore.BLUE}https://discord.gift{Fore.WHITE}/{Fore.BLUE}{code}"
        )
        yy += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f"Generated : {yy}")


def nitro_checker():
    count = 0
    invalidd = 0
    validd = 0
    print("\n")
    if pathlib.Path("nitro.txt").exists():
        with open("nitro.txt") as my_file:
            my_file.seek(0)
            first_char = my_file.read(1)
            if not first_char:
                print(
                    "nitro.txt is empty, if you want nitro codes, use the nitro generator"
                )
            else:
                num_lines = sum(1 for line in open("nitro.txt"))
                with open("nitro.txt") as f:
                    for line in f:
                        nitro = line.strip("\n")
                        r = requests.get(
                            f"https://discordapp.com/api/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
                        )
                        count += 1
                        ctypes.windll.kernel32.SetConsoleTitleW(
                            f"Checked : {count}/{num_lines} | Invalid : {invalidd} | Valid : {validd}"
                        )
                        if r.status_code == 200:
                            print(
                                f"{Fore.WHITE}[{Fore.GREEN}VALID{Fore.WHITE}] > {Fore.GREEN}{nitro}"
                            )
                            f = open("valid.txt", "a+")
                            f.write(f"{nitro}\n")
                            validd += 1
                        else:
                            print(
                                f"{Fore.WHITE}[{Fore.RED}INVALID{Fore.WHITE}] > {Fore.RED}{nitro}"
                            )
                            invalidd += 1
                        ctypes.windll.kernel32.SetConsoleTitleW(
                            f"Checked : {count}/{num_lines} | Invalid : {invalidd} | Valid : {validd}"
                        )
                print(f"\n{Style.BRIGHT}{Fore.BLUE}Nitro codes checked")
                x = input(f"\n\nPress enter to exit")
                os.system("cls")
                Start()
                commands()
                pass


def commands():
    init()
    option = input(f"\n{Fore.BLUE}Choice {Fore.WHITE}> {Fore.BLUE}")
    if option not in liste:
        print(f"\n{Fore.RED}Invalid Selection")
        commands()
    if option == "1":
        nitro_generator()
    elif option == "2":
        nitro_checker()
    elif option == "3":
        x = input(f"\n{Fore.BLACK}{Style.BRIGHT}Press enter to exit{Style.RESET_ALL}")
        sys.exit(0)
        pass
    elif option == "cls":
        os.system("cls")
        Start()
        commands()


Start()
while True:
    try:
        commands()
    except KeyboardInterrupt:
        print("")
        pass
