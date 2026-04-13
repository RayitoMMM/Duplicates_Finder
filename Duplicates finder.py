import os
import hashlib

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

def get_file_hash(file):
    hasher = hashlib.md5()
    with open (file, "rb") as g:
        hasher.update(g.read())
        hash_value = hasher.hexdigest()
    return (hash_value)

def find_duplicates(files):
    hashes = {}
    for f in files:
        hash = get_file_hash(f)
        hashes[hash] = [f]
    return(hashes)

def main():
    folder = ask_folder()
    files = list_files(folder)
    duplicates = find_duplicates(files)

    print(duplicates)

    #print("Files found:")
    #for f in files:
        #hash_data = get_file_hash(f)
        #print(f"{f} : {hash_data}")

main()