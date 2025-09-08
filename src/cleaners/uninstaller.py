import os
import subprocess
import platform

def list_installed_apps():
    """List installed applications based on the operating system."""
    os_type = platform.system()
    apps = []

    if os_type == "Windows":
        # Use WMIC to get a list of installed applications
        try:
            output = subprocess.check_output(['wmic', 'product', 'get', 'name'], universal_newlines=True)
            apps = output.splitlines()[1:]  # Skip the header
        except subprocess.CalledProcessError as e:
            print(f"Error retrieving installed applications: {e}")

    elif os_type == "Linux":
        # Use dpkg for Debian-based systems
        try:
            output = subprocess.check_output(['dpkg', '--get-selections'], universal_newlines=True)
            apps = [line.split()[0] for line in output.splitlines() if line]
        except subprocess.CalledProcessError as e:
            print(f"Error retrieving installed applications: {e}")

    elif os_type == "Darwin":
        # Use system_profiler for macOS
        try:
            output = subprocess.check_output(['system_profiler', 'SPApplicationsDataType'], universal_newlines=True)
            apps = [line.split()[1] for line in output.splitlines() if line.startswith('    ') and len(line.split()) > 1]
        except subprocess.CalledProcessError as e:
            print(f"Error retrieving installed applications: {e}")

    return [app.strip() for app in apps if app.strip()]

def uninstall_app(app_name):
    """Uninstall an application based on the operating system."""
    os_type = platform.system()

    if os_type == "Windows":
        # Use WMIC to uninstall the application
        try:
            subprocess.run(['wmic', 'product', 'where', f'name="{app_name}"', 'call', 'uninstall'], check=True)
            print(f"{app_name} has been uninstalled.")
        except subprocess.CalledProcessError as e:
            print(f"Error uninstalling {app_name}: {e}")

    elif os_type == "Linux":
        # Use apt-get for Debian-based systems
        try:
            subprocess.run(['sudo', 'apt-get', 'remove', '--purge', app_name], check=True)
            print(f"{app_name} has been uninstalled.")
        except subprocess.CalledProcessError as e:
            print(f"Error uninstalling {app_name}: {e}")

    elif os_type == "Darwin":
        # Use brew for macOS
        try:
            subprocess.run(['brew', 'uninstall', app_name], check=True)
            print(f"{app_name} has been uninstalled.")
        except subprocess.CalledProcessError as e:
            print(f"Error uninstalling {app_name}: {e}")

def main():
    """Main function to list and uninstall applications."""
    print("Installed Applications:")
    apps = list_installed_apps()
    for idx, app in enumerate(apps):
        print(f"{idx + 1}: {app}")

    choice = input("Enter the number of the application to uninstall (or 'q' to quit): ")
    if choice.lower() == 'q':
        return

    try:
        app_index = int(choice) - 1
        if 0 <= app_index < len(apps):
            app_name = apps[app_index]
            confirm = input(f"Are you sure you want to uninstall {app_name}? (y/n): ")
            if confirm.lower() == 'y':
                uninstall_app(app_name)
            else:
                print("Uninstallation canceled.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()