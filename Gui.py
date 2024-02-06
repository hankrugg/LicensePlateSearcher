'''

Gui.py

Created by Hank Rugg on January 25, 2024
'''

import tkinter as tk
from tkinter import messagebox
from Search import Search


class Gui(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.search = Search(filepath="MontanaCounties.csv", extraFile="extra.csv")
        self.title("Montana Counties")
        self.geometry('750x400')
        self.canvas = tk.Canvas(self, width=700, height=400)
        self.entry = None
        self.city = None
        self.county = None

    def menu(self):
        self.canvas.pack_forget()
        self.canvas.pack()
        self.entry = tk.Entry(self, width=20)
        self.entry.place(x=250, y=50)
        # place all the buttons on the gui

        choice = tk.Button(self, text='Search by County, County Seat, or Prefix', command=self.searchByInput)
        choice.place(x=50, y=100)

        searchByCity = tk.Button(self, text='Search by City in County', command=self.searchByCity)
        searchByCity.place(x=350, y=100)

        # place the instructions on the gui
        self.instructions()
        self.addNew()

    def instructions(self):
        # make the instructions
        self.canvas.create_text(200, 65, text="input:")
        self.canvas.create_text(320, 25,
                                text="Enter a county prefix, county, city, or county seat and click the submit button to search.")

    def addNew(self):
        self.canvas.create_text(300, 200,
                                text="To add a new record Enter the county name or county prefix the city is in:")
        self.canvas.create_text(250, 230, text="Enter the city:")
        self.city = tk.Entry(self, width=20)
        self.city.place(x=250, y=240)

        self.canvas.create_text(250, 290, text="Enter the county:")
        self.county = tk.Entry(self, width=20)
        self.county.place(x=250, y=300)

        choice = tk.Button(self, text='Add New Record', command=self.setCityInRecords)
        choice.place(x=250, y=350)

    def setCityInRecords(self):
        # gui method to call the search by prefix and implement it on the gui
        county = self.county.get().lower()
        city = self.city.get().lower()
        if not self.search.checkInput(county):
            tk.messagebox.showerror("That is not a county!", "Please enter a valid county!")

        else:
            self.search.setCityInRecords(city, county)
            self.canvas.delete('all')
            self.menu()

    def searchByInput(self):
        # gui method to call the search by prefix and implement it on the gui
        choice = self.entry.get()
        self.canvas.delete('all')
        string = str(self.search.searchByInput(choice))
        self.canvas.create_text(350, 165, text=string)
        self.menu()

    def searchByCity(self):
        # gui method to call the search by prefix and implement it on the gui
        choice = self.entry.get()
        self.canvas.delete('all')
        string = str(f"{choice} : {self.search.searchByCity(choice)}")
        self.canvas.create_text(350, 165, text=string)
        self.menu()


if __name__ == '__main__':
    game = Gui()
    game.menu()
    game.mainloop()
