from tkinter import *
from tkinter import messagebox

from controller import Controller
from model import Model
from view import View

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("GPS")
        self.resizable(False, False)
        model = Model()
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)
        controller = Controller(model, view)
        view.set_controller(controller)

if __name__ == '__main__':
    #Pour Windows
    from os import environ
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

    app = App()

    def quitter():
        if messagebox.askyesno("Quitter", "Voulez-vous quitter?"):
            app.destroy()

    app.protocol("WM_DELETE_WINDOW", quitter)

    app.mainloop()
