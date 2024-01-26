'''

LicensePlate.py

Created by Hank Rugg on January 25, 2024
'''

class LicensePlate(object):
    def __init__(self, county, countySeat, prefix):
        self.county = county
        self.countySeat = countySeat
        self.prefix = prefix

    def __str__(self):
        return "{} county has the license prefix {} and {}, Montana as the county seat.".format(self.county, self.prefix, self.countySeat)


if __name__ == '__main__':
    lic = LicensePlate("Butte", "Missoula", 4)
    print(lic)