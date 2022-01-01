# Proof of concept for a Soda Linux common package installer

import os


print("Steam - Note, will also install flatpak (steam)\nNVIDIA Drivers - nvidia\nDiscord - discord\nVisual Studio Code (OSS variant) - vscode \n")
install = input("This tool will install and configure the software you choose from above. If a piece of software is missing, add it in. Separate all packages with spaces. All must be lowercase.\n")
flatinstall = 0
newinstall = 0

os.system("sudo pacman -Sy")
if "steam" in install:
    newinstall = install.replace('steam', '')
    flatinstall = "com.valvesoftware.Steam"
   # print(newinstall)
   # os.system("sudo pacman -S flatpak {newinstall}")
   # os.system("flatpak install flathub com.valvesoftware.Steam")
    
if flatinstall == 0:
    # os.system(f'sudo pacman -Sy && sudo pacman -S {install}')
    print(f"Updating repos and installing packages {install} from the Arch Linux repos")
else:
    # os.system(f'flatpak install flathub {flatinstall}')
    print(f"Installing {flatinstall} from Flathub, as these packages do not exist in the Arch repos.")
    # os.system(f'sudo pacman -S {newinstall}")
    print(f"Installing {newinstall} with pacman from the Arch Linux repos")
