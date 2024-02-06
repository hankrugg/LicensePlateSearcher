'''

Search.py

Created by Hank Rugg on January 25, 2024

Provides functions to be used in Gui.py
'''

import csv

from LicensePlate import LicensePlate
from Reader import Reader


class Search:
    def __init__(self, filepath, extraFile):
        self.searching = True
        self.reader = Reader(filepath, extraFile)

    # used to check if the choice in is the 56 counties in some form
    def checkInput(self, choice):
        choice = choice.lower()
        if choice in self.reader.records.keys():
            return True
        return False

    # used to check if the choice in is the extra counties
    def checkCityInput(self, choice):
        choice = choice.lower()
        if choice in self.reader.extraRecords.keys():
            return True
        return False

    # adds the city to the .csv file for future use
    def setCityInRecords(self, city, choice):
        choice = choice.lower()
        city = city.lower()
        self.reader.extraRecords[city] = self.reader.records[choice]
        with open('extra.csv', 'a+', newline='') as csvfile:
            # storing the county, the city in that county they added, and the license prefix
            fieldnames = ['County', 'County City', 'License Plate Prefix']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # write to the file
            writer.writerow({'County': self.reader.records[choice][0], 'County City': city,
                             'License Plate Prefix': self.reader.records[choice][2]})
            # used with open() so no need to close the file

    # search through the 56 counties
    def searchByInput(self, choice):
        choice = choice.lower()
        if self.checkInput(choice):
            plate = LicensePlate(self.reader.records[choice][0], self.reader.records[choice][1],
                                 self.reader.records[choice][2])
            return plate
        else:
            return 'No results found!'

    # search through the cities in the extra file
    def searchByCity(self, city):
        self.reader.loadExtraFile()
        city = city.lower()
        if self.checkCityInput(city):
            # get the county from the extra records
            county = self.reader.extraRecords[city][0].lower()
            # fetch the license plate associated with that county via the city
            plate = LicensePlate(self.reader.records[county][0], self.reader.records[county][1],
                                 self.reader.records[county][2])
            return plate
        else:
            return 'No results found, try adding below!'

