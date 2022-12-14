import view
import model

import matplotlib.pyplot as plt
import networkx as nx

from tkinter import *
from tkinter import messagebox

class Controller:
    G = nx.Graph()
    pos = None
    list_towns_text = []
    start_town = None
    arrival_town = None
    current_town = None
    shortest_path = []
    shortest_path_edges = []
    neighbors_current_town = []

    shortest_path_type_list = ["Le plus court", "Le moins de villes"]
    shortest_path_type_value = shortest_path_type_list[0]

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.start_town = self.list_towns_text[0]
        self.arrival_town = self.list_towns_text[-1]

    def draw_graph_France():
        color_map = ["gray"]*len(Controller.G.nodes())
        for i, node in enumerate(Controller.G.nodes()):
            if node == Controller.start_town:
                color_map[i] = "red"
            elif node == Controller.arrival_town: 
                color_map[i] = "green"
            elif node == Controller.current_town:
                color_map[i] = "yellow"
            elif node in Controller.shortest_path:
                color_map[i] = "blue"

        edge_color_list = ["black"]*len(Controller.G.edges())
        for i, edge in enumerate(Controller.G.edges()):
            if edge in Controller.shortest_path_edges or (edge[1],edge[0]) in Controller.shortest_path_edges:
                edge_color_list[i] = "blue"
        
        
        view.View.lbl_best_path.configure(text="Chemin idéal : {}".format(Controller.shortest_path))
        nx.draw(Controller.G, Controller.pos, with_labels=True, node_color=color_map, edge_color=edge_color_list)
        plt.savefig("france_graphe.png")
        view.View.update_image_France()


    def get_shortest_path(self, start, arrival, type_path):
        if(start == arrival):
            messagebox.showwarning("Attention", "Le départ et la destination sont identiques.")
        else:
            Controller.current_town = start
            model.Model.compute_shortest_path(model, start, arrival, type_path)
            Controller.draw_graph_France()
