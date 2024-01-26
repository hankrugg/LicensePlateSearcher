'''

Search.py

Created by Hank Rugg on January 25, 2024

Text based version of the county search algorithm.
Running this program will allow you to interact through the console.
This class is used
'''
import sys

from Reader import Reader
from LicensePlate import LicensePlate


class Search:
    def __init__(self, filepath):
        self.searching = True
        self.reader = Reader(filepath)

    def searchByPrefix(self, prefix):
        # check to make sure that is a valid prefix
        if prefix in list(self.reader.records.keys()):
            # if it is valid, make a license plate and return it
            plate = LicensePlate(self.reader.records[prefix][0], self.reader.records[prefix][1], prefix)
            return plate
        return "That is not a county prefix."

    def searchByCounty(self, county):
        prefix = None
        # look through values to see if county name is valid
        for record in self.reader.records:
            if self.reader.records[record][0].lower() == county.lower():
                # set the index to the prefix
                prefix = record
        if prefix == None:
            # if it isnt valid, bail
            return "That is not a county."
        else:
            # make a license plate and return it
            plate = LicensePlate(self.reader.records[prefix][0], self.reader.records[prefix][1], prefix)
            return plate

    def searchByCountySeat(self, countySeat):
        prefix = None
        # look through values to see if county seat name is valid
        for record in self.reader.records:
            if self.reader.records[record][1].lower() == countySeat.lower():
                # set the index to the prefix
                prefix = record
        if prefix == None:
            # if it isnt valid, bail
            return "That is not a county seat."
        else:
            # make a license plate and return it
            plate = LicensePlate(self.reader.records[prefix][0], self.reader.records[prefix][1], prefix)
            return plate


if __name__ == '__main__':
    search = Search("MontanaCounties.csv")
    # get choice and print search results
    while search.searching:
        choice = input("Press 1 to search by prefix, 2 to search by county, 3 to search by county seat, x to quit")
        if choice == '1':
            prefix = input("Enter the county prefix you want to search for.")
            print(search.searchByPrefix(prefix))
        elif choice == '2':
            county = input("Enter the county you want to search for.")
            print(search.searchByCounty(county))
        elif choice == '3':
            countySeat = input("Enter the county seat you want to search for.")
            print(search.searchByCountySeat(countySeat))
        elif choice == 'x':
            sys.exit()
        else:
            print("Invalid Choice")
