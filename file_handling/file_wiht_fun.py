# function for creating file
# myfile = open('myname1.txt', 'x')
# print(bool(myfile))
# exit()

def createFile(fileName):
    try:
        myfile = open('file_handling/demo/' + fileName + '.txt', 'x')
    except FileExistsError:
        print('\nThis file [ ' + fileName + ' ] is already exists. Try with some new name.')
    finally:
        print('\nThis file [ ' + fileName + ' ] is created successfully.')
        myfile.close()

# create folder
import os

def creteNewFolder(folderName):
    try:
        os.mkdir('file_handling/demo/' + folderName)
    except FileExistsError:
        print('\nThis folder ' + folderName + ' is already exists.')
        userChoice()
    else:
        print('\nYour folder ' + folderName + ' is successfully created.')
        userChoice()

# delete folder
def deleteFolder(folderName):
    try:
        os.rmdir('file_handling/demo/' + folderName)
    except FileNotFoundError:
        print('\nThis folder ' + folderName + ' is not exists. Try again.')
        userChoice()
    finally:
        print('\nYou successfully deleted ' + folderName + ' folder.')
        userChoice()

# function for choices: 1: createnew file 2: exit
def userChoice():
    # get user choice
    choicelist = '''
    ---------------------------------------
               Select Your Choice
    ---------------------------------------
    1: Create new file
    2: Create new folder
    3: Delete Folder
    4: Exit
    ---------------------------------------

    '''
    print(choicelist)
    choice = int(input('\nEnter your choice (1/2/3/4): '))

    if choice == 1:
        print('\nAap new file create karna cahte ho.\n')
        # provide file name
        fileName = input('\nEnter your file name: ')
        createFile(fileName)
    elif choice == 2:
        print('\nCreate New folder.')
        folderName = input('\nEnter folder name: ')
        creteNewFolder(folderName)
    elif choice == 3:
        print('\nDelete folder: ')
        folderName = input('\nEnter folder name: ')
        deleteFolder(folderName)
    elif choice == 4:
        print('\nYou are successfully exit.')
    else:
        print('\nWrong choice. Try again with 1 or 2.')

userChoice()


'''
Next work on this file:

1. Create function for delete file and also handle errors in case of file not exists.

2. At last convert these all fucniton part of one class.
'''