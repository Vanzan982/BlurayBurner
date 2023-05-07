import os

from Bluray import Bluray


####
# this class accepts a list of files and a list of blurays and adds the files to the blurays
####
class BlurayBurner:
    # the constructor accepts a list of files and a list of blurays
    def __init__(self, folder):
        self.folders = []
        self.files = []
        self.blurays = []
        self.folder = folder
        self.set_folders()
        self.set_files_from_folder()
        self.burn_bluray()

    # this method get all files from a given folder and its subfolders and returns a list of files
    def set_folders(self):
        self.files = []
        self.folders = []
        # checks if the folder exists
        if os.path.exists(self.folder):
            # get the creation date of the folder

            folder_creation_date = os.path.getctime(self.folder)

            # get all directories below folder
            directories = [x[0] for x in os.walk(self.folder)]

            # get all other directories which are in the same folder as folder and are newer than folder
            other_directories = []
            for directory in os.listdir(os.path.dirname(self.folder)):
                if os.path.isdir(os.path.dirname(self.folder) + "/" + directory) and os.path.getctime(os.path.dirname(self.folder) + "/" + directory) > folder_creation_date:
                    other_directories.append(os.path.dirname(self.folder) + "/" + directory)

            # get all subdirectories of the other directories
            for directory in other_directories:
                for subdirectory in [x[0] for x in os.walk(directory)]:
                    if subdirectory not in directories:
                        directories.append(subdirectory)

            # combine the directories and other_directories lists and put them in the folders list
            self.folders = directories

    # this method get all files from the folders list
    def set_files_from_folder(self, folder):
        self.files = []
        # get all files from the folders list

        for file in os.listdir(folder):
            # check if the file is a file or a folder
            if os.path.isfile(folder + "/" + file):
                # create a new file object and add it to the files list
                self.files.append(folder + "/" + file)

            if os.path.isdir(folder + "/" + file):
                # get all files from the subfolder
                self.set_files_from_folder(folder + "/" + file)

    # this method creates a new bluray, add files to it until it is full, and then adds it to the list of blurays
    def burn_bluray(self):
        bluray = Bluray()
        for file in self.files:
            if bluray.is_full():
                break
            bluray.add_file(file)
            self.files.remove(file)
        self.blurays.append(bluray)

    # this method runs through all blurays and copy the files of each bluray to a destination folder.
    # the destination folder is created if it does not exist
    # every bluray has its own folder in the destination folder which is named 'Bluray_1', 'Bluray_2', etc.
    def copy_to_folder(self, destination_folder):
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        for bluray in self.blurays:
            bluray_folder = destination_folder + "/Bluray_" + str(self.blurays.index(bluray) + 1)
            if not os.path.exists(bluray_folder):
                os.makedirs(bluray_folder)
            for file in bluray.files:
                # the destination directory is created by the bluray_folder. below the bluray folder a directory structure is created
                # which is the same as the source directory structure without the part which is stored in the folder variable
                destination_directory = bluray_folder + "/" + file.directory.replace(self.folder, "")
                if not os.path.exists(destination_directory):
                    os.makedirs(destination_directory)
                # the file is copied to the destination directory
                with open(file.path, 'rb') as source_file:
                    with open(destination_directory + "/" + file.name, 'wb') as destination_file:
                        destination_file.write(source_file.read())

    # this method prints out the contents of the blurays
    def print_contents(self):
        for bluray in self.blurays:
            print("Bluray:")
            for file in bluray.files:
                print(file.name)
            print("Total Size: " + str(bluray.get_total_size()))
            print("Full: " + str(bluray.is_full()))
            print("")

if __name__ == "__main__":
    print("This file is not meant to be run directly. Please run main.py instead.")