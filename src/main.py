import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from collections import defaultdict

#Pour Windows
from os import environ

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

suppress_qt_warnings()
#Pour Windows


G = nx.Graph()

#Constructions des sommets
df_towns_coords = pd.read_csv("towns_coords.csv")
for row in df_towns_coords.itertuples():
    G.add_node(row.town, pos=(row.x, row.y))
pos=nx.get_node_attributes(G,'pos')

#Consutrctions des arêtes
df_towns_edges = pd.read_csv("towns_edges_2d_array.csv")
df_towns_edges = df_towns_edges.set_index("Town")
for rowIndex, row in df_towns_edges.iterrows(): #iterate over rows
    for columnIndex, value in row.items():
        if value > 0:
            G.add_edge(rowIndex, columnIndex, weight=value)
labels = nx.get_edge_attributes(G,'weight')

nx.draw(G, pos, with_labels=True)
#nx.draw_networkx_edge_labels(G, pos, edge_labels=labels) #Afficher les poids des arêtes
plt.savefig("france_graphe.png")
plt.show()