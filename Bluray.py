class Bluray:
    # a bluray object has a list of files on it which is empty at first. the constructor also defines the default size of the bluray in bytes
    def __init__(self):
        self.files = []
        self.size = 25000000000


    # this method adds a file to the bluray
    def add_file(self, file):
        self.files.append(file)

    # this method returns the total size of all files on the bluray
    def get_total_size(self):
        total_size = 0
        for file in self.files:
            total_size += file.size
        return total_size

    # this method returns whether or not the bluray is full
    def is_full(self):
        return self.get_total_size() >= self.size

if __name__ == "__main__":
    print("This file is not meant to be run directly. Please run main.py instead.")