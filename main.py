# TO START THE PROGRAM
# AUTHOR :: YIGIT AKOYMAK
from elvation_gui import ElevationApp
import tkinter as tk

__version__ = "0.11"

if __name__  == "__main__":
    root = tk.Tk()
    app = ElevationApp(root)
    root.mainloop()
