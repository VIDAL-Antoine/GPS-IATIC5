import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from tkinter import *
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

#Constructions des arêtes
df_towns_edges = pd.read_csv("towns_edges_2d_array.csv")
df_towns_edges = df_towns_edges.set_index("Town")
for rowIndex, row in df_towns_edges.iterrows(): #iterate over rows
    for columnIndex, value in row.items():
        if value > 0:
            G.add_edge(rowIndex, columnIndex, weight=value)
labels = nx.get_edge_attributes(G,"weight")

#Détermination du plus court chemin
shortest_path = nx.dijkstra_path(G, "Bourges", "Lille")
shortest_path_edges = [(shortest_path[i],shortest_path[i+1]) for i in range(len(shortest_path)-1)]

edge_color_list = ["black"]*len(G.edges)
for i, edge in enumerate(G.edges()):
    if edge in shortest_path_edges or (edge[1],edge[0]) in shortest_path_edges:
        edge_color_list[i] = "red"


nx.draw(G, pos, with_labels=True, edge_color=edge_color_list)
#nx.draw_networkx_edge_labels(G, pos, edge_labels=labels) #Afficher les poids des arêtes
plt.savefig("france_graphe.png")
#plt.show()

root = Tk()
img = ImageTk.PhotoImage(Image.open("france_graphe.png"))
panel = Label(root, image = img)
panel.pack()
b = Button(root,text="Supprimer image",command=lambda:panel.destroy())
b.pack()

root.mainloop()
