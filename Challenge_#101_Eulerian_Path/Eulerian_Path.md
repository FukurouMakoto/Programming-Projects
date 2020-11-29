What is a Eulerian Path?
    
    In graph theory, an Eulerian Path (or Eulerian Trail) is a trail in a finite graph that visits every edge exactly once (allowing for revisiting vertices). Similarly, an Eulerian circuit or Eulerian cycle is an Eulerian trail that starts and ends on the same vertex. 

    A Eulerian Path is a path that visits every edge exactly once. Eulerian Circuit is an Eulerian Path which starts and ends on the same vertex.

How to find whether a given graph is Eulerian or not?

    The problem is the same as the following question:
    "Is it possible to draw a given graph without lifting pencil from the paper and without tracing any of the edges more than once?"

    A graph is called Eulerian if it has an Eulerian Cycle and called Semi-Eulerian if it has an Eulerian Path. 

    In order to find out if a graph has a Eulerian cycle, the following two conditions will be true:
        1) All vertices with non-zero degree are connected. Vertices with zero degrees do not matter because they don't belong to Eulerian Cycle or Path.
        2) All vertices have an even degree.
    
    In order to find out if a graph has a Eulerian path, the following two conditions will be true:
        1) All vertices with non-zero degree are connected. Vertices with zero degrees do not matter because they don't belong to Eulerian Cycle or Path.
        2) if zero or two vertices have odd degree & all other vertices have even degree. Note that only one vertex with odd degree is not possible in an undirected graph (sum of all degrees is always even in an undirected graph).
    
    Note that a graph with no edges is considered Eulerian because there are no edges to traverse.

How does this work?

    In Eulerian path, each time we visit a vertex v, we walk through two unvisited edges with one end point as v. Therefore, all middle vertices in Eulerian Path must have even degree. For Eulerian Cycle, any vertex can be middle vertex, therefore all vertices must have even degree.



Notes for program:

I need to find a way to test whether or not a graph is Eulerian. To do this, I need to decide on a method for how best to go about this. 
I will most likely need to find a python module that works with graphs, possibly something like numpy as well for math functions. The module will need to be able to read the vertices of the graphs and its points. 
The program will then need to collect this information and pass it thru some kind of logic that will determine whether or not it is Eulerian.
I then also need to have some firm grasp of what exactly are the conditions for Eulerian. I will most likely have to read up on graph theory.
As it is now I do not understand the theory behind Eulerian too well.