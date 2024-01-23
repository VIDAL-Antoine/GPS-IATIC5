# Mini-GPS

Individual project carried out in IATIC5 (during my engineering degree). 

Based on a map of France, the aim is to build a GPS: from an initial position, the user wants to get to a town. However, the principle is to choose the route that best suits the user: in this case, the shortest path. Another option was considered: the number of cities covered.

France will be represented here as a graph/table contained in a csv file representing the adjacency matrix (filled in beforehand). The whole of France will not be represented for storage reasons, so we'll limit ourselves to a few dozen towns.

The algorithm applied to find the shortest path will be Dijkstra's algorithm.

At each city reached (in our graph, a vertex), it will be possible to choose the next destination. If this does not correspond to the one indicated by the GPS, the GPS will have to recalculate the shortest path.


## User information

The application uses external files, mainly an image and csv files. The names of these files cannot be changed.

### Requirements

The application has been tested on Windows 10 and Linux (Ubuntu 22.04). 
As the application runs under Python 3, it is necessary to have it installed for it to launch.

#### Dependencies

- tkinter : `pip3 install tk`
- pandas : `pip3 install pandas`
- Networkx : `pip3 install networkx`
- Matplotlib: `pip3 install matplotlib`
- Pillow : `pip3 install Pillow`

## Startup

To start the application, simply go to the `src` folder and run `python main.py` or `pythonw main.py` (for Windows).

## Tools used to design the application
- Visual Studio Code and VIM for text editing
- Microsoft Office Excel for editing csv files
- Git and Github for file versioning and hosting
- Paint for editing images used to create the map of France used by the application
- LaTeX (Overleaf) for writing documents (report and presentation).

## Authors

- VIDAL Antoine
- MANOUSSAKIS George as tutor
- PILARD Laurence as referent
