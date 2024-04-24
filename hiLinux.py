import os


os.system('''wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb
apt install php -y
apt install tail -y
rm -rf hiLinux.py cloudflared-linux-amd64.deb
python3 PhishYou.py''')

## this file gets auto delete after installion