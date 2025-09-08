def get_os():
    import platform
    return platform.system()

def execute_command(command):
    import subprocess
    try:
        result = subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.stdout.decode('utf-8'), e.stderr.decode('utf-8')

def is_windows():
    return get_os() == "Windows"

def is_linux():
    return get_os() == "Linux"

def is_mac():
    return get_os() == "Darwin"

def clear_temp_files():
    if is_windows():
        temp_dir = "C:\\Windows\\Temp"
        command = f"del /Q {temp_dir}\\*"
    elif is_linux():
        temp_dir = "/tmp"
        command = f"rm -rf {temp_dir}/*"
    elif is_mac():
        temp_dir = "/tmp"
        command = f"rm -rf {temp_dir}/*"
    else:
        raise OSError("Unsupported operating system")
    
    return execute_command(command)

def list_startup_items():
    if is_windows():
        command = "wmic startup get caption,command"
    elif is_linux():
        command = "ls ~/.config/autostart"
    elif is_mac():
        command = "osascript -e 'tell application \"System Events\" to get the name of every login item'"
    else:
        raise OSError("Unsupported operating system")
    
    return execute_command(command)

def secure_delete(file_path):
    if is_windows():
        command = f"cipher /w:{file_path}"
    elif is_linux() or is_mac():
        command = f"shred -u -n 3 {file_path}"
    else:
        raise OSError("Unsupported operating system")
    
    return execute_command(command)