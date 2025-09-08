import os
import platform
import subprocess
import sys
from datetime import datetime, timedelta

def schedule_cleanup(frequency):
    if platform.system() == "Windows":
        schedule_windows_cleanup(frequency)
    elif platform.system() in ["Linux", "Darwin"]:  # Darwin is for macOS
        schedule_linux_mac_cleanup(frequency)
    else:
        print("Unsupported operating system for scheduling cleanups.")

def schedule_windows_cleanup(frequency):
    task_name = "CleanSweepCleanup"
    command = f"{sys.executable} {os.path.join(os.path.dirname(__file__), '..', 'cleansweep.py')}"
    
    # Create the task using schtasks
    if frequency == "daily":
        subprocess.run(["schtasks", "/create", "/tn", task_name, "/tr", command, "/sc", "DAILY", "/st", "00:00"], check=True)
    elif frequency == "weekly":
        subprocess.run(["schtasks", "/create", "/tn", task_name, "/tr", command, "/sc", "WEEKLY", "/d", "SUN", "/st", "00:00"], check=True)
    else:
        print("Invalid frequency. Use 'daily' or 'weekly'.")

def schedule_linux_mac_cleanup(frequency):
    command = f"{sys.executable} {os.path.join(os.path.dirname(__file__), '..', 'cleansweep.py')}"
    cron_job = f"{get_cron_time(frequency)} {command}\n"
    
    # Add the cron job
    with open("temp_cron", "w") as f:
        subprocess.run(["crontab", "-l"], stdout=f)
        f.write(cron_job)
    
    subprocess.run(["crontab", "temp_cron"])
    os.remove("temp_cron")

def get_cron_time(frequency):
    if frequency == "daily":
        return "0 0 * * *"  # At midnight every day
    elif frequency == "weekly":
        return "0 0 * * 0"  # At midnight every Sunday
    else:
        raise ValueError("Invalid frequency. Use 'daily' or 'weekly'.")

if __name__ == "__main__":
    frequency = input("Enter the frequency for cleanup (daily/weekly): ").strip().lower()
    schedule_cleanup(frequency)
    print(f"Cleanup scheduled successfully for {frequency}.")

