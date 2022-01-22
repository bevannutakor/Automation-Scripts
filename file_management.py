import os
import shutil
class Organize:
    def __init__(self, main_path, file_folders=[[]]):
        self.main_path = main_path
        self.main_path_list = os.listdir(main_path)
        self.file_folders = file_folders
    
    #OS doesn't have a method to create a file in a specific path it has to be created in the working path of this python file so I had to do some logic stuff

    def create_directories(self):
        #need to add input for paths but that can come later
        add_new_folder = True
        while(add_new_folder):
            add_new_folder_input = input("Would you like to add a new folder(Y/N): ").lower()
            if add_new_folder_input == "y":
                name_of_folder = input("What is the name of the folder: ")
                corresponding_ext = input("what extension do you want to organize in this folder: ")
                self.file_folders.append([name_of_folder,corresponding_ext])
            else:
                add_new_folder = False 
            
    def move_folders(self):
        for i in range(len(self.file_folders)):
            if self.file_folders[i][0] not in self.main_path_list:
                os.makedirs(self.file_folders[i][0])
                shutil.move(self.file_folders[i][0], self.main_path)
                #Diagnosis is that the file only gets moved to the desired path once the whole program is done running for some reason? this affects the organize_files function which has to create a random binary file cause it thinks the file does not exist
            else:
                print("This folder already exists")
    
    def organize_files(self):
       for i in range(len(self.main_path_list)):
           for j in range(len(self.file_folders)):
               if self.main_path_list[i].endswith(self.file_folders[j][1]):
                   shutil.move(self.main_path + "/" + self.main_path_list[i], self.file_folders[j][0]) 
            




initialize = Organize("/Users/user/Downloads", [])

initialize.create_directories()
initialize.move_folders()
initialize.organize_files()
