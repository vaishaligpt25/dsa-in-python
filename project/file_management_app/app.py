import os

def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"File name{filename}: Created successfully!")
    except FileExistsError:
        print(f'File name {filename} already exists!')
    except Exception as E:
        print("An error occurred. ")


def view_all_files(filename):
    files = os.listdir()
    if not files:
        print('No File found')
    else:
        print('Files in directory')
    for file in files:
        print(file)


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully.")
    except FileNotFoundError:
       print("File not found")
    except Exception as e:
        print("An error occurred.")

def read_file(filename):
    try:
        with open("sample.txt", "r") as f:
            content = f.read()
            print(f"Content of '{filename})': \n{content}")
    except FileNotFoundError:
        print(f"{filename} does not exist")
    except Exception as e:
        print("An error occurred.")

def edit_file(filename):
    try:
        with open("sample.txt", 'a') as f:
            Content = input("Enter data to add= ")
            f.write(Content + \"n")
            print(f"Content added to {filename} successfully")
    except FileNotFoundError:
        print(f"{filename} does not exist")
    except Exception as e:
        print("An error occurred!")

def main():
    while True:
        print("File Management app!")
        print('1: Create File')
        print('2: View all Files')
        print('3: Delete File')
        print('4: Read File')
        print('5: Edit File')
        print('6: Exit')

        Choice = input("Enter your Choice(1-6): ")
        if Choice == 1:
            filename = input("Enter the file name to create= ")
            create_file(filename)
        elif Choice == 2:
             view_all_files()

