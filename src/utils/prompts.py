def get_user_confirmation(prompt):
    """Display a prompt to the user and return their confirmation."""
    response = input(prompt + " (y/n): ").strip().lower()
    return response == 'y'


def prompt_for_directory_selection():
    """Prompt the user to select a directory."""
    directory = input("Please enter the directory path you want to analyze: ").strip()
    return directory


def prompt_for_file_deletion(file_path):
    """Prompt the user for confirmation before deleting a file."""
    return get_user_confirmation(f"Are you sure you want to delete the file: {file_path}?")


def prompt_for_secure_deletion(file_path):
    """Prompt the user for confirmation before secure deletion of a file."""
    return get_user_confirmation(f"Are you sure you want to securely delete the file: {file_path}?")


def prompt_for_uninstall_application(app_name):
    """Prompt the user for confirmation before uninstalling an application."""
    return get_user_confirmation(f"Are you sure you want to uninstall the application: {app_name}?")


def prompt_for_startup_item_management(item_name):
    """Prompt the user for enabling or disabling a startup item."""
    action = input(f"Do you want to enable or disable the startup item: {item_name}? (enable/disable): ").strip().lower()
    return action


def prompt_for_cleanup_schedule():
    """Prompt the user to set a cleanup schedule."""
    schedule = input("Please enter the cleanup schedule (daily/weekly): ").strip().lower()
    return schedule


def prompt_for_largest_files_count():
    """Prompt the user for the number of largest files to display."""
    count = input("How many largest files would you like to display? ")
    return int(count) if count.isdigit() else 10  # Default to 10 if input is invalid


def prompt_for_browser_selection():
    """Prompt the user to select a browser for cache cleaning."""
    browser = input("Which browser do you want to clean the cache for? (chrome/firefox): ").strip().lower()
    return browser if browser in ['chrome', 'firefox'] else 'chrome'  # Default to Chrome if input is invalid


def prompt_for_duplicate_file_action(file_path):
    """Prompt the user for action on a duplicate file."""
    action = input(f"Duplicate file found: {file_path}. Do you want to delete it? (y/n): ").strip().lower()
    return action == 'y'