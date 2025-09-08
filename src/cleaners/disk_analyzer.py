import os

def get_largest_files(directory, n=10):
    """Return the N largest files in the given directory."""
    files = []
    
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                size = os.path.getsize(filepath)
                files.append((size, filepath))
            except OSError:
                continue  # Skip files that can't be accessed

    # Sort files by size in descending order and return the top N
    files.sort(reverse=True, key=lambda x: x[0])
    return files[:n]

def display_largest_files(largest_files):
    """Display the largest files in a readable format."""
    print(f"{'Size (Bytes)':<15} {'File Path'}")
    print("=" * 60)
    for size, filepath in largest_files:
        print(f"{size:<15} {filepath}")

def main():
    directory = input("Enter the directory to analyze: ")
    n = input("Enter the number of largest files to display (default is 10): ")
    
    try:
        n = int(n) if n else 10
    except ValueError:
        print("Invalid input for number of files. Defaulting to 10.")
        n = 10

    if not os.path.isdir(directory):
        print("The provided path is not a valid directory.")
        return

    largest_files = get_largest_files(directory, n)
    if largest_files:
        display_largest_files(largest_files)
    else:
        print("No files found in the specified directory.")

if __name__ == "__main__":
    main()