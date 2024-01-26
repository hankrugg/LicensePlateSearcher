'''

Search.py

Created by Hank Rugg on January 25, 2024
'''
import sys

from Reader import Reader
from LicensePlate import LicensePlate

class Search:
    def __init__(self, filepath):
        self.searching = True
        self.reader = Reader(filepath)

    def searchByPrefix(self, prefix):
            try:
                if int(prefix) > 0 and int(prefix) < 57:
                    plate = LicensePlate(self.reader.records[prefix][0], self.reader.records[prefix][1], prefix)
                    return (plate)
                elif prefix == 'x':
                    sys.exit()
                else:
                    return "That is not a county prefix"
            except:
                if prefix == 'x':
                    sys.exit()
                else:
                    return "That is not a county prefix"

    def searchByCounty(self, county):
        prefix = None
        for record in self.reader.records:
            if self.reader.records[record][0].lower() == county.lower():
                prefix = record
        if prefix == None:
            return "That is not a county."
        else:
            plate = LicensePlate(self.reader.records[prefix][0], self.reader.records[prefix][1], prefix)
            return plate

    def searchByCountySeat(self, countySeat):
        prefix = None
        for record in self.reader.records:
            # print(self.reader.records[record][0])
            if self.reader.records[record][1].lower() == countySeat.lower():
                prefix = record
        if prefix == None:
            return "That is not a county seat."
        else:
            plate = LicensePlate(self.reader.records[prefix][0], self.reader.records[prefix][1], prefix)
            return plate



if __name__ == '__main__':
    search = Search("MontanaCounties.csv")
    while search.searching:
        choice = input("Press 1 to search by prefix, 2 to search by county, 3 to search by county seat")
        if choice == '1':
            prefix = input("Enter the county prefix you want to search for.")
            print(search.searchByPrefix(prefix))
        elif choice == '2':
            county = input("Enter the county you want to search for.")
            print(search.searchByCounty(county))
        elif choice == '3':
            countySeat = input("Enter the county seat you want to search for.")
            print(search.searchByCountySeat(countySeat))
        else:
            print("Invalid Choice")
