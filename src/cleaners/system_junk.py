import os
import platform
import shutil
import tempfile

def delete_temp_files():
    """Delete OS-specific temporary files."""
    os_type = platform.system()
    
    if os_type == "Windows":
        temp_dir = os.environ.get("TEMP")
        if temp_dir:
            try:
                for filename in os.listdir(temp_dir):
                    file_path = os.path.join(temp_dir, filename)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                print("Temporary files deleted successfully.")
            except Exception as e:
                print(f"Error deleting temporary files: {e}")

    elif os_type == "Linux":
        temp_dir = "/tmp"
        try:
            for filename in os.listdir(temp_dir):
                file_path = os.path.join(temp_dir, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            print("Temporary files deleted successfully.")
        except Exception as e:
            print(f"Error deleting temporary files: {e}")

    elif os_type == "Darwin":  # macOS
        temp_dir = "/tmp"
        try:
            for filename in os.listdir(temp_dir):
                file_path = os.path.join(temp_dir, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            print("Temporary files deleted successfully.")
        except Exception as e:
            print(f"Error deleting temporary files: {e}")

    else:
        print("Unsupported operating system.")

def clean_system_junk():
    """Main function to clean system junk."""
    print("Starting system junk cleanup...")
    delete_temp_files()

if __name__ == "__main__":
    clean_system_junk()