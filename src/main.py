import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

import os

from tkinter import *
from tkinter.ttk import Combobox
from PIL import ImageTk, Image

def suppress_qt_warnings():
    from os import environ
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"
suppress_qt_warnings() #Pour Windows

G = nx.Graph()

#Constructions des sommets
df_towns_coords = pd.read_csv("towns_coords.csv")
for row in df_towns_coords.itertuples():
    G.add_node(row.town, pos=(row.x, row.y))
pos=nx.get_node_attributes(G,"pos")
list_towns_text = list(G.nodes)

#Constructions des arêtes
df_towns_edges = pd.read_csv("towns_edges_2d_array.csv")
df_towns_edges = df_towns_edges.set_index("Town")
for rowIndex, row in df_towns_edges.iterrows(): #iterate over rows
    for columnIndex, value in row.items():
        if value > 0:
            G.add_edge(rowIndex, columnIndex, weight=value)

#Détermination du plus court chemin
def shortest_path_weight(start, arrival):
    global lbl_best_path
    shortest_path = nx.dijkstra_path(G, start, arrival)
    shortest_path_edges = [(shortest_path[i],shortest_path[i+1]) for i in range(len(shortest_path)-1)]

    edge_color_list = ["black"]*len(G.edges)
    for i, edge in enumerate(G.edges()):
        if edge in shortest_path_edges or (edge[1],edge[0]) in shortest_path_edges:
            edge_color_list[i] = "red"

    lbl_best_path.configure(text="Chemin idéal : {}".format(shortest_path))
    nx.draw(G, pos, with_labels=True, edge_color=edge_color_list)
    if os.path.exists("france_graphe.png"):
        os.remove("france_graphe.png")
    plt.savefig("france_graphe.png")
    update_image()


def update_image():
    global img_France
    global lbl_France
    img_France = ImageTk.PhotoImage(Image.open("france_graphe.png"))
    lbl_France.configure(image=img_France)
    root.update()

def start_path():
    frm_ui_choose_path.pack_forget()
    frm_ui_moving = Frame(master=root)
    frm_town_destination = Frame(master=frm_ui_moving)
    lbl_town_destination = Label(master=frm_town_destination, text="Destination")
    cmb_town_destination = Combobox(master=frm_town_destination, values=list_towns_text)
    btn_town_destination = Button(frm_ui_moving, text="Se déplacer", command=print("aa"))

    frm_ui_moving.pack(fill=Y, side=RIGHT, expand=True)
    frm_town_destination.pack(fill=X, expand=True)

    lbl_town_destination.grid(row=0, column=0)
    cmb_town_destination.grid(row=0, column=1)
    btn_town_destination.pack()

root = Tk()

frm_graph = Frame(master=root)
img_France = ImageTk.PhotoImage(Image.open("france_graphe.png"))
lbl_France = Label(master=frm_graph, image=img_France)
lbl_best_path = Label(master=frm_graph, text="Chemin idéal : ")

frm_ui_choose_path = Frame(master=root)

frm_town_start = Frame(master=frm_ui_choose_path)
lbl_town_start = Label(master=frm_town_start, text="Départ")
cmb_town_start = Combobox(master=frm_town_start, values=list_towns_text)
cmb_town_start.set(list_towns_text[0])

frm_town_arrival = Frame(master=frm_ui_choose_path)
lbl_town_arrival = Label(master=frm_town_arrival, text="Arrivée")
cmb_town_arrival = Combobox(master=frm_town_arrival, values=list_towns_text)
cmb_town_arrival.set(list_towns_text[-1])

btn_confirm = Button(frm_ui_choose_path,text="Obtenir la trajectoire",command=lambda:shortest_path_weight(cmb_town_start.get(), cmb_town_arrival.get()))
btn_start_path = Button(frm_ui_choose_path,text="Démarrer le parcours",command=lambda:start_path())

frm_graph.pack(fill=Y, side=LEFT, expand=True)
frm_ui_choose_path.pack(fill=Y, side=RIGHT, expand=True)

lbl_France.pack()
lbl_best_path.pack()




frm_town_start.pack(fill=X, expand=True)
lbl_town_start.grid(row=0, column=0)
cmb_town_start.grid(row=0, column=1)

frm_town_arrival.pack(fill=X, expand=True)
lbl_town_arrival.grid(row=0, column=0)
cmb_town_arrival.grid(row=0, column=1)

btn_confirm.pack(fill=X)
btn_start_path.pack(fill=X)

root.mainloop()
