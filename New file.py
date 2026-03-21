import os

def ask_folder():
    return input("Enter folder name: ")

def list_files(folder):
    while True:
        try:
            all_files = []
            for root, subfolders, files in os.walk(folder):
                for f in files:
                    full_path = os.path.join(root, f)  # full path for clarity
                    all_files.append(full_path)
            return all_files
        except FileNotFoundError:
            print("Invalid folder. Try again.")
            folder = ask_folder()

def main():
    folder = ask_folder()
    files = list_files(folder)
    
    print("Files found:")
    for f in files:
        print(f)

main()