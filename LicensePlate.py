'''

LicensePlate.py

Created by Hank Rugg on January 25, 2024

This is the license plate class that is used when displaying the license plate.
'''


class LicensePlate(object):
    def __init__(self, county, countySeat, prefix):
        self.county = county
        self.countySeat = countySeat
        self.prefix = prefix

    # override the string method to print what we want
    def __str__(self):
        return "{} county has the license prefix {} and {}, Montana as the county seat.".format(self.county,
                                                                                                self.prefix,
                                                                                                self.countySeat)
