from tkinter import messagebox
import PIL.ImageTk, PIL.Image
from tkinter import *
from tkinter.ttk import Combobox

import controller

class View(Frame):
    lbl_best_path = None
    frm_ui_choose_route = None
    img_France = None
    lbl_France= None
    frm_ui_moving = None

    def __init__(self, parent):
        super().__init__(parent)
        self.display_choose_route()

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller
    
    def update_image_France():
        View.img_France = PIL.ImageTk.PhotoImage(PIL.Image.open("france_graphe.png"))
        View.lbl_France.configure(image=View.img_France)

    def display_choose_route(self):
        self.frm_graph = Frame(master=self)
        View.img_France = PIL.ImageTk.PhotoImage(PIL.Image.open("france_graphe.png"))
        View.lbl_France = Label(master=self.frm_graph, image=View.img_France)
        View.lbl_best_path = Label(master=self.frm_graph, text="Chemin idéal : {}".format(controller.Controller.shortest_path))

        View.frm_ui_choose_route = Frame(master=self)

        self.frm_town_start = Frame(master=self.frm_ui_choose_route)
        self.lbl_town_start = Label(master=self.frm_town_start, text="Départ")
        self.cmb_town_start = Combobox(master=self.frm_town_start, values=controller.Controller.list_towns_text)
        self.cmb_town_start.set(controller.Controller.list_towns_text[0])

        self.frm_town_arrival = Frame(master=self.frm_ui_choose_route)
        self.lbl_town_arrival = Label(master=self.frm_town_arrival, text="Arrivée")
        self.cmb_town_arrival = Combobox(master=self.frm_town_arrival, values=controller.Controller.list_towns_text)
        self.cmb_town_arrival.set(controller.Controller.list_towns_text[-1])

        self.frm_shortest_path_type = Frame(master=self.frm_ui_choose_route)
        self.lbl_shortest_path_type = Label(master=self.frm_shortest_path_type, text="Type")
        self.cmb_shortest_path_type = Combobox(master=self.frm_shortest_path_type, values=controller.Controller.shortest_path_type_list)
        self.cmb_shortest_path_type.set(controller.Controller.shortest_path_type_list[0])

        self.btn_confirm = Button(self.frm_ui_choose_route,text="Obtenir la trajectoire", command=lambda:controller.Controller.get_shortest_path(controller.Controller, self.cmb_town_start.get(), self.cmb_town_arrival.get(), self.cmb_shortest_path_type.get()))
        self.btn_start_path = Button(self.frm_ui_choose_route,text="Démarrer le parcours", command=lambda:View.start_path(self))

        self.frm_graph.pack(fill=Y, side=LEFT, expand=True)
        self.frm_ui_choose_route.pack(fill=Y, side=RIGHT, expand=True)

        View.lbl_France.pack()
        self.lbl_best_path.pack()


        self.frm_town_start.pack(fill=X, expand=True)
        self.lbl_town_start.grid(row=0, column=0)
        self.cmb_town_start.grid(row=0, column=1)

        self.frm_town_arrival.pack(fill=X, expand=True)
        self.lbl_town_arrival.grid(row=0, column=0)
        self.cmb_town_arrival.grid(row=0, column=1)

        self.frm_shortest_path_type.pack(fill=X, expand=True)
        self.lbl_shortest_path_type.grid(row=0, column=0)
        self.cmb_shortest_path_type.grid(row=0, column=1)

        self.btn_confirm.pack(fill=X, padx=10)
        self.btn_start_path.pack(fill=X, padx=10)

    def start_path(self):
        if not controller.Controller.shortest_path:
            messagebox.showerror("Aucun chemin défini", "Il n'y a pas de chemin optimal défini. Veuillez appuyer sur \"Obtenir la trajectoire\" pour définir un chemin à emprunter.")
        else:
            controller.Controller.neighbors_current_town = list(controller.Controller.G.neighbors(controller.Controller.current_town))
            View.frm_ui_choose_route.pack_forget()
            View.display_choose_next_town(self)

    def display_choose_next_town(self):
        View.frm_ui_moving = Frame(master=self)
        self.frm_town_destination = Frame(master=View.frm_ui_moving)
        self.lbl_town_destination = Label(master=self.frm_town_destination, text="Destination")
        self.cmb_town_destination = Combobox(master=self.frm_town_destination, values=controller.Controller.neighbors_current_town)
        self.cmb_town_destination.set(controller.Controller.neighbors_current_town[0])
        self.btn_town_destination = Button(View.frm_ui_moving, text="Se déplacer", command=lambda:View.move_next_town(self))
        self.btn_return_menu = Button(View.frm_ui_moving, text="Revenir au menu", command=lambda:View.return_menu(self))

        self.frm_ui_moving.pack(fill=Y, side=RIGHT, expand=True)
        self.frm_town_destination.pack(fill=X, expand=True)

        self.lbl_town_destination.grid(row=0, column=0)
        self.cmb_town_destination.grid(row=0, column=1)
        self.btn_town_destination.pack(fill=X, padx=10)
        self.btn_return_menu.pack(fill=X, padx=10)

    def return_menu(self):
        View.frm_ui_moving.pack_forget()
        View.frm_ui_choose_route.pack(fill=Y, side=RIGHT, expand=True)

    def move_next_town(self):
        controller.Controller.current_town = self.cmb_town_destination.get()
        controller.Controller.neighbors_current_town = list(controller.Controller.G.neighbors(controller.Controller.current_town))
        self.cmb_town_destination.configure(values=controller.Controller.neighbors_current_town)
        self.cmb_town_destination.set(controller.Controller.neighbors_current_town[0])
        controller.Controller.draw_graph_France()

        if(controller.Controller.current_town == controller.Controller.arrival_town):
            messagebox.showinfo("Information", "Vous êtes arrivé.")
            controller.Controller.shortest_path.clear()
            View.lbl_best_path.configure(text="Chemin idéal : {}".format(controller.Controller.shortest_path))
            View.frm_ui_moving.pack_forget()
            View.frm_ui_choose_route.pack(fill=Y, side=RIGHT, expand=True)

        elif(controller.Controller.current_town not in controller.Controller.shortest_path):
            messagebox.showwarning("Chemin optimal non pris", "Vous avez emprunté un chemin non optimal. Il est possible que vous vous soyez trompé de chemin. Nous allons déterminer un nouveau chemin optimal depuis votre position actuelle.")
            controller.Controller.get_shortest_path(controller.Controller, controller.Controller.current_town, controller.Controller.arrival_town, controller.Controller.shortest_path_type_value)
