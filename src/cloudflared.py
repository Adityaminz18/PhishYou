import os
import platform

def run_command_in_new_terminal(command):
    if platform.system() == "Windows":
        os.system(f"start cmd /k {command}")
    elif platform.system() == "Linux":
        os.system(f"gnome-terminal -- bash -c '{command}; exec bash'")
    elif platform.system() == "Darwin":  # For macOS
        os.system(f"osascript -e 'tell app \"Terminal\" to do script \"{command}\"'")
    else:
        print("Unsupported operating system")

command = "cloudflared --url localhost:8000"
run_command_in_new_terminal(command)
