import argparse
import Bluray_Burner


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # get command line arguments of this script
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", help="the folder which contains the files to be burned to bluray")
    args = parser.parse_args()

    # get the folder from the command line arguments
    myFolder = args.folder
    # create a new BlurayBurner object
    bluray_burner = Bluray_Burner.BlurayBurner(myFolder)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
