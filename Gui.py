'''

Gui.py

Created by Hank Rugg on January 25, 2024
'''

import tkinter as tk
from Search import Search


class Gui(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.search = Search("MontanaCounties.csv")
        self.title("Montana Counties")
        self.geometry('750x200')
        self.canvas = tk.Canvas(self, width=700, height=200)
        self.canvas.pack()
        self.choice = None

    def menu(self):
        self.choice = tk.Entry(self, width=20)
        self.choice.place(x=250, y=100)
        # place all the buttons on the gui
        prefix = tk.Button(self, text='Prefix', command=self.searchByPrefix)
        prefix.place(x=200, y=50)

        county = tk.Button(self, text='County', command=self.searchByCounty)
        county.place(x=300, y=50)

        countySeat = tk.Button(self, text='County Seat', command=self.searchByCountySeat)
        countySeat.place(x=400, y=50)

    def searchByPrefix(self):
        self.canvas.delete('all')
        string = str(self.search.searchByPrefix(self.choice.get()))
        self.canvas.create_text(325, 150, text=string, fill='black')

    def searchByCounty(self):
        self.canvas.delete('all')
        string = str(self.search.searchByCounty(self.choice.get()))
        self.canvas.create_text(325, 150, text=string, fill='black')

    def searchByCountySeat(self):
        self.canvas.delete('all')
        string = str(self.search.searchByCountySeat(self.choice.get()))
        self.canvas.create_text(325, 150, text=string, fill='black')



if __name__ == '__main__':
    game = Gui()
    game.menu()
    game.mainloop()
