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
    print(f'{row.town}, {row.x}, {row.y}')
    G.add_node(row.town, pos=(row.x, row.y))

pos=nx.get_node_attributes(G,'pos')



#Consutrctions des arêtes
df_towns_edges = pd.read_csv("towns_edges_2d_array.csv")




nx.draw(G, pos, with_labels=True)
plt.savefig("gps.png")
plt.show()