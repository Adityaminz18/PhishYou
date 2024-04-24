import subprocess


def killer():
    # Run the 'ps' command to list all processes
    ps_output = subprocess.check_output(['ps', '-efw']).decode()

    # Filter out lines containing 'php' or 'tail' but not the 'grep' command itself
    php_and_tail_processes = [line.split()[1] for line in ps_output.split('\n') if ('php' in line or 'tail' in line or 'cloudflared' in line) and 'grep' not in line]

    # Terminate each PHP or tail process
    for process_pid in php_and_tail_processes:
        subprocess.run(['kill', '-9', process_pid])


