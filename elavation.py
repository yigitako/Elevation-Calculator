# FIND ELEVATION DATA OF A GIVEN LOCATION WITH LATIDUE AND LONGITUDE DATA
# AUTHOR  :: YIGIT AKOYMAK
# LICENSE :: USE AS YOU WISH I DON'T CARE AT ALL.

import tkinter as tk

from ast import literal_eval
from tkinter import messagebox
from urllib.request import urlopen
from urllib.parse import urlencode

class elevation_calculator:
    def lookup_elevation(self):
        try:
            latitude = float(self.lat_entry.get())
            longitude = float(self.lon_entry.get())

            response = self.query_elevation(latitude, longitude)

            elevation = response['results'][0]['elevation']
            messagebox.showinfo("Elevation Result ", f"The elevation at {latitude}, {longitude} is {elevation} meters.")
            

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for latitude and longitude.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def query_elevation(self, latitude, longitude) -> str:
        base_url = 'https://api.open-elevation.com/api/v1/lookup?'
        params = {'locations': f'{latitude},{longitude}'}
        url = base_url + urlencode(params)

        with urlopen(url) as response:
            data = response.read()

        return literal_eval(data.decode('utf-8'))

