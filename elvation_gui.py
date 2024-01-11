# THE ELAVATION APP GUI
# AUTHOR :: YIGIT AKOYMAK

import tkinter as tk

from elavation import elevation_calculator

class ElevationApp(elevation_calculator):
    def __init__(self, master):
        self.master = master
        self.master.title("Elevation Lookup")
        
        self.lat_label = tk.Label(master, text="Latitude:")
        self.lat_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.lat_entry = tk.Entry(master)
        self.lat_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.lon_label = tk.Label(master, text="Longitude:")
        self.lon_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.lon_entry = tk.Entry(master)
        self.lon_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.lookup_button = tk.Button(master, text="Lookup Elevation", command=self.lookup_elevation)
        self.lookup_button.grid(row=2, column=0, columnspan=2, pady=10)
