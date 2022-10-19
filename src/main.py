from tkinter import *
from tkinter import messagebox
import os
import sys

import controller
import model
import view

def check_files_exist():
    if not os.path.isfile("towns_coords.csv"):
        messagebox.showerror("Fichier non trouvé", "Il manque le fichier towns_coords.csv. Veuillez vérifier que les fichiers .csv se trouvent bien dans le répertoire d'exécution. Si besoin vous pouvez les récupérer sur le dépôt Github.")
        sys.exit()
    if not os.path.isfile("towns_edges_2d_array.csv"):
        messagebox.showerror("Fichier non trouvé", "Il manque le fichier towns_edges_2d_array.csv. Veuillez vérifier que les fichiers .csv se trouvent bien dans le répertoire d'exécution. Si besoin vous pouvez les récupérer sur le dépôt Github.")
        sys.exit()

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("GPS")
        self.resizable(False, False)
        model_instance = model.Model()
        view_instance = view.View(self)
        view_instance.grid(row=0, column=0, padx=10, pady=10)
        controller_instance = controller.Controller(model_instance, view_instance)
        view_instance.set_controller(controller_instance)

if __name__ == '__main__':
    #Pour Windows
    from os import environ
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

    check_files_exist()
    app = App()

    def quitter():
        if messagebox.askyesno("Quitter", "Voulez-vous quitter?"):
            app.destroy()
            sys.exit()

    app.protocol("WM_DELETE_WINDOW", quitter)

    app.mainloop()

