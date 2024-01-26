'''

Reader.py

Created by Hank Rugg on January 25, 2024
'''

import csv


class Reader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.records = {}
        self.loadFile()

    # used to load the file into the records dicionary
    def loadFile(self):
        with open(self.filepath) as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                self.records[row[2]] = [row[0], row[1]]
