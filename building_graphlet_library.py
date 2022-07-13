#Building A Library
import networkx as nx
import matplotlib.pyplot as plt

def plot(G):
    nx.draw(G)
    plt.show()

class Graphlet:
    def __init__(self, pattern, name, degree):
        self.name=name
        self.pattern=pattern
        self.degree=degree
    def __str__(self):
        return str(self.name)

#3 node motifs

#2-star
lib1 = nx.Graph()
lib1.add_edge(1,2)
lib1.add_edge(2,3)
graphlet3_2_star=Graphlet(lib1, "2-Star", 3)

#triangle
lib2=nx.Graph()
lib2.add_edge(1,2)
lib2.add_edge(2,3)
lib2.add_edge(1,3)
graphlet3_triangle=Graphlet(lib2, "Triangle", 3)

#4 node motifs

#tailed-triangle
lib3=nx.Graph()
lib3.add_edge(1,2)
lib3.add_edge(2,3)
lib3.add_edge(1,3)

lib3.add_node(4)
lib3.add_edge(3,4)
graphlet4_tailed_triangle=Graphlet(lib3, "Tailed-Triangle", 4)

#4-chordalcycle
lib4=nx.Graph()
lib4.add_edge(1,2)
lib4.add_edge(2,3)
lib4.add_edge(3,4)
lib4.add_edge(1,4)
lib4.add_edge(2,4)
graphlet4_4_chordalcycle=Graphlet(lib4, "4-Chordalcycle", 4)

#4-clique
lib5=nx.Graph()
lib5.add_edge(1,2)
lib5.add_edge(2,3)
lib5.add_edge(3,4)
lib5.add_edge(1,3)
lib5.add_edge(2,4)
lib5.add_edge(1,4)
graphlet4_4_clique=Graphlet(lib5, "4-Clique", 4)

#4 cycle
lib6=nx.Graph()
lib6.add_edge(1,2)
lib6.add_edge(2,3)
lib6.add_edge(3,4)
lib6.add_edge(1,4)
graphlet4_4_cycle=Graphlet(lib6, "4-Cycle", 4)

#3-star
lib7=nx.Graph()
lib7.add_edge(1,2)
lib7.add_edge(2,3)
lib7.add_edge(2,4)
graphlet4_3_star = Graphlet(lib7, "3-Star", 4)

#4-path
lib8=nx.Graph()
lib8.add_edge(1,2)
lib8.add_edge(2,3)
lib8.add_edge(3,4)
graphlet4_4_path=Graphlet(lib8, "4-Path", 4)

graphlet_library = [graphlet3_2_star,graphlet3_triangle,graphlet4_tailed_triangle,graphlet4_4_chordalcycle,graphlet4_4_clique,graphlet4_4_cycle,graphlet4_3_star,graphlet4_4_path]

"""
for i in graphlet_library:
    plot(nx.Graph(i.pattern))
"""
##Writing part to a text_file.
'''
f=open('graphlet_library.txt','w')
for graphlet in lib_ls:
    f.write(str(graphlet.pattern) + str(graphlet.name) + str(graphlet.degree))
f.close()
'''