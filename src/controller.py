from re import I
import view

import matplotlib.pyplot as plt
import networkx as nx

from tkinter import *


class Controller:
    G = nx.Graph()
    pos = None
    list_towns_text = None
    start_town = None
    arrival_town = None
    shortest_path = None
    shortest_path_edges = None

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def draw_graph_France(self):
        color_map = ["gray"]*len(Controller.G.nodes())
        for i, node in enumerate(Controller.G.nodes()):
            if node == Controller.start_town:
                color_map[i] = "red"
            elif node == Controller.arrival_town: 
                color_map[i] = "green"
            elif node in Controller.shortest_path:
                color_map[i] = "blue"

        edge_color_list = ["black"]*len(Controller.G.edges())
        for i, edge in enumerate(Controller.G.edges()):
            if edge in Controller.shortest_path_edges or (edge[1],edge[0]) in Controller.shortest_path_edges:
                edge_color_list[i] = "blue"
        
        
        view.View.lbl_best_path.configure(text="Chemin idéal : {}".format(Controller.shortest_path))
        nx.draw(self.G, self.pos, with_labels=True, node_color=color_map, edge_color=edge_color_list)
        plt.savefig("france_graphe.png")
        view.View.update_image_France(view.View)


    def shortest_path_weight(self, start, arrival):
        Controller.start_town = start
        Controller.arrival_town = arrival
        Controller.shortest_path = nx.dijkstra_path(Controller.G, start, arrival)
        Controller.shortest_path_edges = [(Controller.shortest_path[i],Controller.shortest_path[i+1]) for i in range(len(Controller.shortest_path)-1)]
        Controller.draw_graph_France(self)
