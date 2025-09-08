import os
import hashlib

def secure_delete(file_path, passes=3):
    """
    Securely delete a file by overwriting it multiple times before deletion.
    
    :param file_path: Path to the file to be securely deleted.
    :param passes: Number of overwrite passes (default is 3).
    """
    if not os.path.isfile(file_path):
        print(f"Error: {file_path} is not a valid file.")
        return

    # Get the size of the file
    file_size = os.path.getsize(file_path)

    # Overwrite the file multiple times
    with open(file_path, 'r+b') as f:
        for _ in range(passes):
            # Generate random data to overwrite the file
            random_data = os.urandom(file_size)
            f.seek(0)
            f.write(random_data)
            f.flush()
            os.fsync(f.fileno())

    # Finally, delete the file
    os.remove(file_path)
    print(f"Securely deleted: {file_path}")

def main():
    # Example usage
    file_to_delete = input("Enter the path of the file to securely delete: ")
    secure_delete(file_to_delete)

if __name__ == "__main__":
    main()