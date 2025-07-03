import argparse
import shutil
import os


def parse_arguments():
    parser = argparse.ArgumentParser(description="Sort files in a folder by their extensions")
    parser.add_argument("-s", "--src", help="Source folder", required=True)
    return parser.parse_args()

def get_extension(file_name):
    return file_name.split('.')[-1] if '.' in file_name else 'no_extension'


def move_file_to_folder(file_path, dest_folder, file_name):
    os.makedirs(dest_folder, exist_ok=True)
    dest_path = os.path.join(dest_folder, file_name)

    try:
        if not os.path.exists(dest_path):
            shutil.move(file_path, dest_path)
            print(f"Moved {file_name} → {os.path.basename(dest_folder)}/")
        else:
            print(f"Skipped {file_name} (already exists in {os.path.basename(dest_folder)}/)")
    except Exception as e:
        print(f"Error moving {file_name}: {e}")


def sort_files_by_extension(source_dir):
    for file_name in os.listdir(source_dir):
        full_path = os.path.join(source_dir, file_name)

        if os.path.isfile(full_path):
            ext = get_extension(file_name)
            folder_path = os.path.join(source_dir, ext)
            move_file_to_folder(full_path, folder_path, file_name)

def main():
    args = parse_arguments()
    if not os.path.isdir(args.src):
        print(f"Error: {args.src} is not a valid directory.")
        return
    sort_files_by_extension(args.src)

if __name__ == "__main__":
    main()