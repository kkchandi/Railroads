#Khushmeet Chandi
#Artificial Intelligence Period 4
#Railroads
#Objective: Use the A* Search Algorithm to find the shortest path
# between two cities

import sys, time
from math import pi , acos , sin , cos
from Tkinter import *
from Queue import PriorityQueue

nodes =  {} # {ID : (lat, long)}
edgeDistance = {} #{ (edge1, edge2) : distance}
nodeCity2 = {} #{ID:Name}
def solve():    
    edges = {} # {Station : [All its neighbors]} 
    nodeCity = {} #{Name: ID}

    ROOT = Tk()                               #Creates new tkinter
    ROOT.title("AStar display")
    canvas = Canvas(ROOT, background='white') #Sets background
    ROOT.geometry("1200x800")          #Sets geometry
    canvas.pack(fill=BOTH, expand=1)   #Sets fill expand
    
    #Takes in input from rrNodes.txt
    readRRNodes = open("rrNodes.txt", "r").read().splitlines() #A list of all the lines in rrNodes.txt
    for i in readRRNodes:
        j = i.split(" ")
        nodes[j[0]] = (j[1], j[2])

    #Takes in input from rrEdges.txt and find the distances between two cities
    readRREdges = open("rrEdges.txt", "r").read().splitlines() #A list of all the lines in rrEdges.txt
    for i in readRREdges:
        j = i.split(" ")
        if j[0] in edges: edges[j[0]].append(j[1])
        else: edges[j[0]] = [j[1]]
        if j[1] in edges: edges[j[1]].append(j[0])
        else: edges[j[1]] = [j[0]]
        d = calcd(nodes[j[0]][0], nodes[j[0]][1], nodes[j[1]][0], nodes[j[1]][1])
        edgeDistance[(j[0], j[1])] = d
        edgeDistance[(j[1], j[0])] = d
        drawLine(canvas, nodes[j[0]][0], nodes[j[0]][1], nodes[j[1]][0], nodes[j[1]][1], 'black', 1)
    ROOT.update()
    #Takes in input from rrNodeCity.txt
    readNodeCity = open("rrNodeCity.txt", "r").read().splitlines() #A list of all the lines in rrNodeCity.txt
    for i in readNodeCity:
        j = i.split(" ")
        nodeCity[" ".join(j[1:])] = j[0]
        nodeCity2[j[0]] = " ".join(j[1:])

    #Figuring out start and goal
    i=1
    start = sys.argv[i]
    while start not in nodeCity and start not in nodeCity2:
        i+=1
        start += " " + sys.argv[i]
    i+=1
    goal = sys.argv[i]
    while goal not in nodeCity and goal not in nodeCity2:
        i+=1
        goal += " " + sys.argv[i]
    if start in nodeCity: start = nodeCity[start]
    if goal in nodeCity: goal = nodeCity[goal]

    #If we are already at the destination   
    if start == goal: 
        print("0.0 miles")
        drawLine(canvas, nodes[start][0], nodes[start][1], nodes[goal][0], nodes[goal][1], 'green', 3)
        ROOT.update()
        mainloop()
        return 

    openSet = PriorityQueue()
    f = calcd(nodes[start][0], nodes[start][1], nodes[goal][0], nodes[goal][1])
    openSet.put((f, 0.0, start, " "))
    closedSet = {} 
    while True:
        puzzle = openSet.get()
        if int(puzzle[1])%100==0: ROOT.update()
        if puzzle[3]!=" ": drawLine(canvas, nodes[puzzle[2]][0], nodes[puzzle[2]][1], nodes[puzzle[3]][0], nodes[puzzle[3]][1], 'blue', 2.25)
        if puzzle[2] in closedSet: continue
        if puzzle[2]==goal:
            closedSet[puzzle[2]] = puzzle[3]
            print(str(getDistance(canvas, closedSet, puzzle[2])) + " miles")
            ROOT.update()
            mainloop()
            return
        closedSet[puzzle[2]] = puzzle[3]
        for n in edges[puzzle[2]]:
            if n in closedSet: continue
            newF = puzzle[1] + edgeDistance[(puzzle[2], n)] + calcd(nodes[n][0], nodes[n][1], nodes[goal][0], nodes[goal][1])
            openSet.put((newF, puzzle[1]+edgeDistance[(puzzle[2], n)], n, puzzle[2]))
            drawLine(canvas, nodes[puzzle[2]][0], nodes[puzzle[2]][1], nodes[n][0], nodes[n][1], 'red', 1)  
    return

#This function calculates the distance between two points using the Great Circle Distance
#This function was written by Dr. Torbert on 22 Sept 2014 and edited by Mr. White on 5 Oct 2016
def calcd(y1,x1, y2,x2):
   # all assumed to be in decimal degrees
   # if (and only if) the input is strings
   # use the following conversions
   y1  = float(y1)
   x1  = float(x1)
   y2  = float(y2)
   x2  = float(x2)
   R   = 3958.76 
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   # approximate great circle distance with law of cosines 
   # use a try-except to avoid math domain errors
   try: return acos(sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R 
   except: return 0

def drawLine(canvas, x1, y1, x2, y2, color, w):
   x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
   x1, x2 = (x1 - 10)/60, (x2 - 10)/60
   y1, y2 = (y1+130)/70, (y2+130)/70
   canvas.create_line(y1*1200, 900-x1*1200, y2*1200, 900-x2*1200,fill=color, width=w)

#Traces the path from the start to goal -- Prints the number of stations and returns the distance
def getDistance(canvas, graph, last):
    key = graph[last]
    numStations=1
    dist = edgeDistance[(last, key)]
    if last in nodeCity2: print(nodeCity2[last] + " --> " + str(dist) + " miles")
    else: print(last + " --> " + str(dist) + " miles")

    while key!=" " and graph[key]!=" ":
        nextKey = graph[key]
        d = edgeDistance[(key, nextKey)]
        if key in nodeCity2: print(nodeCity2[key] + " --> " + str(d) + " miles")
        else: print(key + " --> " + str(d) + " miles")
        dist+=d
        drawLine(canvas, nodes[key][0], nodes[key][1], nodes[nextKey][0], nodes[nextKey][1], 'green', 2) 
        key = nextKey
        numStations+=1
    print("Number of Stations: " + str(numStations))
    return round(dist, 2)

solve()
