import os

def ask_folder():
    return input("Enter folder name: ")

def list_files(folder):
    while True:
        try:
            files = os.listdir(folder)
            return files
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