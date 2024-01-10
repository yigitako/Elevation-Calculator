# FIND ELEVATION DATA OF A GIVEN LOCATION WITH LATIDUE AND LONGITUDE DATA
# AUTHOR  :: YIGIT AKOYMAK
# LICENSE :: USE AS YOU WISH I DON'T CARE AT ALL.
import tkinter as tk

from ast import literal_eval
from tkinter import messagebox
from urllib.request import urlopen
from urllib.parse import urlencode

'''
ADDED FOR MAGIT COMPABILITY
'''

class ElevationApp:
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
    
    def lookup_elevation(self):
        try:
            latitude = float(self.lat_entry.get())
            longitude = float(self.lon_entry.get())
            
            response = self.query_elevation(latitude, longitude)
            
            elevation = response['results'][0]['elevation']
            
            messagebox.showinfo("Elevation Result:", f"The elevation at {latitude}, {longitude} is {elevation} meters.")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for latitude and longitude.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def query_elevation(self, latitude, longitude) -> str:
        base_url = 'https://api.open-elevation.com/api/v1/lookup?'
        params = {'locations': f'{latitude},{longitude}'}
        url:str = base_url + urlencode(params)
        
        with urlopen(url) as response:
            data = response.read()
        
        return literal_eval(data.decode('utf-8'))

if __name__ == "__main__":
    root = tk.Tk()
    app = ElevationApp(root)
    root.mainloop()

