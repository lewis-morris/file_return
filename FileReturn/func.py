from random import shuffle
import os

class file_return:

    def __init__(self, directory="./", include_sub=True, return_list=False, ext=[".jpg"], ):
        """
        Simple class to return files from directory in list.
        Can return single file name for random selection or full list.
        Can search prefixes

        :param directory: (str) Search directory
        :param include_sub: (bool) - should include sub directories
        :param return_list: (bool) - return list True / return random file False
        :param ext: (list(str)) - list of file ext's to return use [] for all files.
        """
        self.directory = directory
        self.include_sub = include_sub
        self.return_list = return_list
        self.ext = ext

    def return_files(self):

        import shutil

        files_list = []
        for root, dirs, files in os.walk(self.directory):

            if len(files) != 0:
                for fl in files:
                    if "." + fl.split(".")[-1] in self.ext or self.ext == []:
                        if root[-1] == "/":
                            files_list.append(root + fl)
                        else:
                            files_list.append(root + "/" + fl)
                        if root == self.directory and self.include_sub == False:
                            break

        if len(files_list) == 0:
            return "No files found"
        elif self.return_list:
            return files_list
        else:
            shuffle(files_list)
            return(files_list[0])