import natsort
import os
import re
import shutil


def count_files(): # counts the number of files in a directory with the ability to search for files with a specific extension
    path = input("Enter the path: ")
    extension = input("Enter the extension(if left blank will search all files): ")
    tot_count = 0
    for _, _, files in natsort.natsorted(os.walk(path)):
        for file in files:
                if file and file.lower().endswith(extension):
                    tot_count += 1
        
    if extension:
        print(f"There is a total of {tot_count} files with the extension {extension}")
    else:
        print(f"There is a total of {tot_count} files")

def numerate_files(): # adds a number to the start of the filename with the ability to rename files with a specific extension
    path = input("Enter the path: ")
    extension = input("Enter the extension: ")
    count = 1
    answer = input(f"About to rename all your files! Are you sure? (y/n) ")
    if answer.lower() == "y":
        for root, _, files in natsort.natsorted(os.walk(path)):
            for file in files:
                if file.lower().endswith(extension):
                    filtered_filename = re.sub(r'^[^a-zA-Z]*', '', file)
                    new_name = os.path.join(root, str(count) + "- " + filtered_filename)
                    shutil.move(os.path.join(root, file), new_name)
                    print(f"renamed {file} to \n{str(count)}- {filtered_filename}")
                    count += 1


def add_keyword(): # adds a keyword to the start of the filename
    path = input("Enter the path: ")
    keyword = input("Enter the keyword to add: ")
    answer = input(f"About to rename all your files! Are you sure? (y/n) ")
    if answer.lower() == "y":
        for root, _, files in natsort.natsorted(os.walk(path)):
            for file in files:
                shutil.move(os.path.join(root, file), os.path.join(root, (keyword + "- " + file)))


def filter_files(): # removes all the symbols until the first Letter is found with the ability to search for files with a specific extension
    path = input("Enter the path: ")
    extension = input("Enter the extension: ")
    answer = input(f"About to rename all your files! Are you sure? (y/n) ")
    if answer.lower() == "y":
        for root, _, files in natsort.natsorted(os.walk(path)):
            for file in files:
                if file.lower().endswith(extension):
                    filter = re.sub(r'^[^a-zA-Z]*', '', file)
                    shutil.move(os.path.join(root, file), os.path.join(root, filter))
                    print(f"renamed {file} to:\n{filter}")
                

def numerate_folders(): # adds a number to the start of folders
    path = input("Enter the path: ")
    count = 1
    answer = input(f"About to rename all your folders! Are you sure? (y/n) ")
    if answer.lower() == "y":
        for folder in natsort.natsorted(os.listdir(path)):
            filtered_folder = re.sub(r'^[^a-zA-Z]*', '', folder)
            new_name = os.path.join(path, str(count) + "- " + filtered_folder)
            shutil.move(os.path.join(path, folder), new_name)
            print(f"renamed {folder} to {str(count)}- {filtered_folder}")
            count += 1


def filter_folders(): # removes all the symbols until the first Letter is found
    path = input("Enter the path: ")
    answer = input(f"About to rename all your folders! Are you sure? (y/n) ")
    if answer.lower() == "y":
        for folder in natsort.natsorted(os.listdir(path)):
            filter = re.sub(r'^[^a-zA-Z]*', '', folder)
            shutil.move(os.path.join(path, folder), os.path.join(path, filter))
            print(f"renamed {folder} to {filter}")


def search_files(): # searches for files with a specific keyword
    path = input("Enter the path: ")
    keyword = input("Enter the keyword to search for: ")
    f_path = r"C:\Users\andre.camacho\Desktop\Projects\Python\File handler\outputs" + "\\" + keyword + ".txt"
    for root, _, files in natsort.natsorted(os.walk(path)):  
        for file in files:
            if keyword in file.lower().split():
                with open(f_path, "a+") as f:
                    f.write(root + "\n")
            else: 
                print("keyword does not exist")


def search_folders(): # searches for folders with a specific keyword
    path = input("Enter the path: ")
    keyword = input("Enter the keyword to search for: ")
    for root, folders, _ in natsort.natsorted(os.walk(path)):
        for folder in folders:
            if keyword in folder.lower():
                with open("Found folders.txt", "a+") as file:
                    file.write(root + "\n")


def remove_duplicates_in_file():
    file_path = input("Enter the path to the file: ")
    unique_lines = []
    for file in os.listdir(file_path):
        with open(os.path.join(file_path, file), "r+") as f:
            for line in f:
                line = line.strip()  # Remove leading/trailing whitespaces and newlines
                if line not in unique_lines:
                    unique_lines.append(line)

        with open(os.path.join(file_path, file), "w") as f:
            for line in unique_lines:
                f.write(line + "\n")

        print("Duplicates removed successfully!")


def main():
    print("What would you like to do?")
    print("Write:")
    print("c to Count files inside a directory")
    print("n to Add a number to the start of the filename starting on 1")
    print("rf to Add a keyword of your choice to the start of the filename")
    print("f to Remove all the symbols from the filename until the first Letter is found")
    print("s to Search for a keyword in a file")
    print("nf to Add a number to the start of the folder's name starting on 1")
    print("ff to Remove all the symbols from the folder's name until the first Letter is found")
    print("sf to Search for a keyword in a folder's name")
    print("rd to Remove duplicate Lines from a txt file")
    choice = input ("Your Choice: ") 

    if choice.lower() == "c":
        count_files()

    elif choice.lower() == "n":
        numerate_files()
    
    elif choice.lower() == "rf":
        add_keyword()
    
    elif choice.lower() == "f":
        filter_files()

    elif choice.lower() == "s":
        search_files()

    elif choice.lower() == "nf":
        numerate_folders()

    elif choice.lower() == "ff":
        filter_folders()

    elif choice.lower() == "sf":
        search_folders()

    elif choice.lower() == "rd":
        remove_duplicates_in_file()

    else:
        print("Invalid choice, please try again")

if __name__ == "__main__":
    main()