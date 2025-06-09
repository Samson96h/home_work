import os

def get_data(fname, folder, files):
    with open(fname, "w") as result_file:
        for file_name in files:
            file_path = os.path.join(folder, file_name)
            with open(file_path, "r") as f:
                contents = f.read()
                result_file.write(f"--- {file_name} ---\n{contents}\n--------------------------------\n")

def main():
    folder = os.path.join(os.getcwd(), "files")
    file_list = os.listdir(folder)
    get_data("result.txt", folder, file_list)

if __name__ == "__main__":
    main()