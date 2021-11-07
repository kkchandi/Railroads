# Railroads

# Objective
The purpose of this repository is to further explore graph data structures and algorithms, specifically the A* Search Algorithm. The rr.py script is written in Python and finds the shortest path via Railroad between two cities in North America. 

# Input & Output
The script first extracts railroad data from three files. The first file is rrNodeCity.txt, which includes information about railroad stations in the form of Node IDs and the corresponding city name. The second file is rrEdges.txt, which includes pairs of directly connected nodes or railroad stations. The last file is rrNodes.txt, which includes the railroad station and its corresponding longitude and latitude. The input of this script is a command line input, accepting two cities' names. The script outputs the shortest distance between them via railraod stations. 

# Program Overview
The script efficiently stores the railroad stations, their IDs, their corresponding city name, and their locations, using the data from the files. The edges of the knowledge graph are then calculated. A helper function calculates the distance between two railroad stations using the Great Circle Distance. A dictionary is used to store the edges of the knowledge graph, which includes two directly connected railroad stations and the distance between them. The script then uses the A* Algorithm to find the shortest path between the inputted cities via railroad. 

# Visualization
The script uses Tkinter to draw out a map of North America, including the different railroad stations. As the program executes, the paths that are being explored by the A* Search algorithm are drawn over in real time. Once the program terminates and the shortest path is identified, this shortest path is highlighted and drawn over in a different color. The final visualization allows the user to view the paths explored the A* Search algorithm and the final shortest path, allowing the user to gain a deeper understanding of the graph algorithm. 


