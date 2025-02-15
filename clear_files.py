import os

endings = [
    '.gz',
    '.xml',
    '.bbl',
    '.lol',
    '.atoc',
    '.aux',
    '.log',
    '.md5',
    '.dpth',
    '.auxlock'
]

def remove_files(dir_name, extensions):
    dirs = []
    for file in os.listdir(dir_name):
        file_name, file_extension = os.path.splitext(file)
        if file_extension == "" and file_name[0] != ".":
            dirs.append(file_name)

        if file_extension in extensions:
            print(file)
            file_path = os.path.join(dir_name, file)
            os.remove(file_path)

    for d in dirs:
        new_dir = os.path.join(dir_name, d)
        remove_files(new_dir, extensions)

    return

def main():
    print("Clearing files...")

    dir_name = os.getcwd()
    remove_files(dir_name, endings)

    print("Unnecessary files cleared.")

if __name__ == "__main__":
    main()