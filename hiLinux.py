import os


os.system('''wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb
sudo apt install php -y
sudo apt install tail -y
sudo apt install gnome-terminal -y
rm -rf hiLinux.py cloudflared-linux-amd64.deb
clear
echo "run python3 PhishYou.py"''')

## this file gets auto delete after installion