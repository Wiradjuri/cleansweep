import os
import hashlib

def find_duplicates(directory):
    """Scan the specified directory for duplicate files."""
    if not os.path.isdir(directory):
        raise ValueError(f"The provided path '{directory}' is not a valid directory.")

    file_hashes = {}
    duplicates = []

    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_hash = hash_file(file_path)

            if file_hash in file_hashes:
                duplicates.append(file_path)
            else:
                file_hashes[file_hash] = file_path

    return duplicates

def hash_file(file_path):
    """Generate a hash for the given file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def remove_duplicates(duplicates):
    """Remove the duplicate files from the filesystem."""
    for duplicate in duplicates:
        try:
            os.remove(duplicate)
            print(f"Removed duplicate file: {duplicate}")
        except Exception as e:
            print(f"Error removing file {duplicate}: {e}")

def main():
    """Main function to execute the duplicate finder."""
    directory = input("Enter the directory to scan for duplicates: ")
    duplicates = find_duplicates(directory)

    if duplicates:
        print("Duplicate files found:")
        for dup in duplicates:
            print(dup)

        confirm = input("Do you want to remove these duplicate files? (y/n): ")
        if confirm.lower() == 'y':
            remove_duplicates(duplicates)
        else:
            print("No files were removed.")
    else:
        print("No duplicate files found.")

if __name__ == "__main__":
    main()