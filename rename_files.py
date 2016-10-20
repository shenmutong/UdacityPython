import os

def rename_files():
    # get file names form a floder
    root = r"E:\CurrentWork\PythonPlayground\prank"
    file_list = os.listdir(root)
    saved_path = os.getcwd()
    os.chdir(root)
    print(file_list)
    for file_name in file_list:
        print("Old Name -" + file_name)
        print("New Name-" + file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))

    os.chdir(saved_path)
    print(file_list)

rename_files()
