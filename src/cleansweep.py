# CleanSweep - A System Cleaner Application

import os
import sys
import argparse
from cleaners import (
    system_junk,
    browser_cache,
    disk_analyzer,
    duplicate_finder,
    startup_manager,
    uninstaller,
    secure_delete,
    scheduler,
)
from utils import logger, prompts

def main():
    # Set up logging
    logger.setup_logging()

    # Initialize argument parser
    parser = argparse.ArgumentParser(description="CleanSweep - A System Cleaner Application")
    parser.add_argument(
        "operation",
        choices=[
            "clean_system_junk",
            "clean_browser_cache",
            "analyze_disk",
            "find_duplicates",
            "manage_startup",
            "uninstall_apps",
            "secure_delete",
            "schedule_cleanup",
        ],
        help="Operation to perform",
    )
    parser.add_argument(
        "-p", "--path", type=str, help="Path for disk analysis or duplicate finding"
    )
    parser.add_argument(
        "-n", "--number", type=int, default=10, help="Number of largest files to list"
    )

    args = parser.parse_args()

    # Execute the requested operation
    if args.operation == "clean_system_junk":
        system_junk.clean_junk()
    elif args.operation == "clean_browser_cache":
        browser_cache.clean_cache()
    elif args.operation == "analyze_disk":
        if args.path:
            disk_analyzer.analyze_disk(args.path, args.number)
        else:
            prompts.prompt_for_path(disk_analyzer.analyze_disk, args.number)
    elif args.operation == "find_duplicates":
        if args.path:
            duplicate_finder.find_duplicates(args.path)
        else:
            prompts.prompt_for_path(duplicate_finder.find_duplicates)
    elif args.operation == "manage_startup":
        startup_manager.manage_startup()
    elif args.operation == "uninstall_apps":
        uninstaller.uninstall_apps()
    elif args.operation == "secure_delete":
        secure_delete.secure_delete_files()
    elif args.operation == "schedule_cleanup":
        scheduler.schedule_cleanup()
    else:
        print("Invalid operation selected.")
        sys.exit(1)

if __name__ == "__main__":
    main()