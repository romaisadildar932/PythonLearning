import os 

def create_file(filename):
    try:
        with open (filename,'x') as f:
            print(f'File name {filename}:Created Successfully')
    except FileExistsError:
        print(f'Filename {filename} already exists')
    except Exception as E:
        print('An error ocuured!')
def view_all_files():
    files = os.listdir()
    if not files:
        print('file not found')
    else:
        print('Files in Directory!')
        for file in files:
            print(file)
def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted successfully!')
    except FileNotFoundError:
        print('File Not Found')
    except Exception as E:
        print('An error occurred!')

def read_file(filename):
    try:
        with open(filename,'r') as f:
            content = f.read()
            print(f'Content of {filename}:{content}')
    except FileNotFoundError:
        print('File Not Found')
    except Exception as E:
        print('An error occurred!')  

def edit_file(filename):
    try:
        with open(filename,'a') as f:
            content = input('Enter data to add=')
            f.write(content + '\n')
            print(f'Content added to {filename} Successfully!')
    except FileNotFoundError:
        print('File Not Found')
    except Exception as E:
        print('An error occurred!') 
def main():
    while True:
        print('File Management App')
        print('1.Create File')
        print('2.View All File')
        print('3.Delete File')
        print('4.Read File')
        print('5.Edit File')
        print('6.Exit')

        choice = (input('Enter your choice(1-6) ='))

        if choice == '1':
            filename = input('Enter a filename to create=')
            create_file(filename)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            filename = input('Enter a filename to delete=')
            delete_file(filename)
        elif choice == '4':
            filename = input('Enter a filename to read=')
            read_file(filename)
        elif choice == '5':
            filename = input('Enter a filename to edit=')
            edit_file(filename)
        elif choice == '6':
            print('Closing the app....')
            break
        else:
            print('Invalid Number')

if __name__ == '__main__':
    main()