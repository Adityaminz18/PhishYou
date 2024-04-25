import os


os.system('''wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb
sudo apt install php -y
sudo apt install tail -y
rm -rf hiLinux.py cloudflared-linux-amd64.deb
clear
cat "run python3 PhishYou.py"''')

## this file gets auto delete after installion