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

def get_size(files):
    sizes = {}
    for file in files:
        size = os.path.getsize(file)
        if size in sizes:
            sizes[size].append(file)
        elif size not in sizes:
            sizes[size] = [file]
    return sizes

def return_possible_duplicates(sizes):
    possible_duplicates = []

    for s in sizes:
        if len(sizes[s]) > 1:
            possible_duplicates.append(sizes[s])
    return possible_duplicates

def get_file_hash(file):
    hasher = hashlib.md5()
    with open (file, "rb") as g:
        hasher.update(g.read())
        hash_value = hasher.hexdigest()
    return hash_value

def find_duplicates(files):
    hashes = {}
    for f in files:
        hash = get_file_hash(f)
        if hash in hashes:
            hashes[hash].append(f)
        else:
            hashes[hash] = [f]
    return hashes

def return_duplicates(hashes):
    duplicates = []
    for h in hashes:
        if len(hashes[h]) > 1:
            duplicates.append(hashes[h]) # You should append the whole list of duplicates
    return duplicates


def main():
    folder = ask_folder()
    files = list_files(folder)
    sizes = get_size(files)
    new_files = return_possible_duplicates(sizes)
    new_files = [item for sublist in new_files for item in sublist]  # Flatten the list of lists
    hashes = find_duplicates(new_files)
    duplicates = return_duplicates(hashes)
    
    if duplicates:
        for d in duplicates:
            print("Duplicates group:")
            for file in d:
                print(f"- {file}")
    elif not duplicates:
        print("No duplicates found")

main()
