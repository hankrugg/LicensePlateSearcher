'''

Reader.py

Created by Hank Rugg on January 25, 2024

Creates a reader that is used in Search.py and Gui.py
'''

import csv


class Reader:
    def __init__(self, filepath, extraFile):
        self.filepath = filepath
        self.extraFile = extraFile
        self.records = {}
        self.extraRecords = {}
        self.loadFile()
        self.loadExtraFile()

    # used to load the file into the records dictionary
    # we are setting every value in the file to itself, so searching for any part of the
    # county will bring you to the correct information
    def loadFile(self):
        with open(self.filepath) as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                self.records[row[0].lower()] = row
                self.records[row[1].lower()] = row
                self.records[row[2].lower()] = row

    # loads the "extra" file of cities in each county
    # loads every part of the county as a key and sets the whole thing to the value
    def loadExtraFile(self):
        with open(self.extraFile) as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                self.extraRecords[row[0].lower()] = row
                self.extraRecords[row[1].lower()] = row
                self.extraRecords[row[2].lower()] = row
