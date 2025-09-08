import os
import shutil
import platform

def clear_browser_cache():
    """Clears the cache for Chrome and Firefox browsers."""
    try:
        if platform.system() == "Windows":
            chrome_cache_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data', 'Default', 'Cache')
            firefox_cache_path = os.path.join(os.getenv('APPDATA'), 'Mozilla', 'Firefox', 'Profiles')
        elif platform.system() == "Darwin":  # macOS
            chrome_cache_path = os.path.join(os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/Cache'))
            firefox_cache_path = os.path.join(os.path.expanduser('~/Library/Application Support/Firefox/Profiles'))
        else:  # Linux
            chrome_cache_path = os.path.join(os.path.expanduser('~/.cache/google-chrome/Default/Cache'))
            firefox_cache_path = os.path.join(os.path.expanduser('~/.mozilla/firefox'))

        # Clear Chrome cache
        if os.path.exists(chrome_cache_path):
            shutil.rmtree(chrome_cache_path)
            print("Chrome cache cleared.")
        else:
            print("Chrome cache path does not exist.")

        # Clear Firefox cache
        if os.path.exists(firefox_cache_path):
            for profile in os.listdir(firefox_cache_path):
                profile_path = os.path.join(firefox_cache_path, profile)
                cache_path = os.path.join(profile_path, 'cache2')
                if os.path.exists(cache_path):
                    shutil.rmtree(cache_path)
                    print(f"Firefox cache cleared for profile: {profile}.")
                else:
                    print(f"No cache found for Firefox profile: {profile}.")
        else:
            print("Firefox cache path does not exist.")

    except Exception as e:
        print(f"An error occurred while clearing browser cache: {e}")

if __name__ == "__main__":
    clear_browser_cache()