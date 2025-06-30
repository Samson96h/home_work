import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--src", help="folder name", required=True)
args = parser.parse_args()


def main(source_dir):
    for file_name in os.listdir(source_dir):
        full_path = os.path.join(source_dir, file_name)

        if os.path.isfile(full_path):
            if '.' in file_name:
                ext = file_name.split('.')[-1]
            else:
                ext = 'no_extension'

            folder_path = os.path.join(source_dir, ext)

            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

            try:
                if not os.path.exists(os.path.join(folder_path, file_name)):
                    os.rename(full_path, os.path.join(folder_path, file_name))
            except Exception as e:
                print(f"Error when moving {file_name}: {e}")


if __name__ == "__main__":
    main(args.src)
