import controller

import networkx as nx
import pandas as pd


class Model():
    def __init__(self):

        #Constructions des sommets
        df_towns_coords = pd.read_csv("towns_coords.csv")
        for row in df_towns_coords.itertuples():
            controller.Controller.G.add_node(row.town, pos=(row.x, row.y))
        controller.Controller.pos=nx.get_node_attributes(controller.Controller.G,"pos")
        controller.Controller.list_towns_text = list(controller.Controller.G.nodes)

        #Constructions des arêtes
        df_towns_edges = pd.read_csv("towns_edges_2d_array.csv")
        df_towns_edges = df_towns_edges.set_index("Town")
        for rowIndex, row in df_towns_edges.iterrows():
            for columnIndex, value in row.items():
                if value > 0:
                    controller.Controller.G.add_edge(rowIndex, columnIndex, weight=value)
