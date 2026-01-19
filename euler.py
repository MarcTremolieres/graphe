from graphe import Graphe
from graphviz import Graph
from copy import deepcopy

def euler(graphe):
    impairs = []
    for sommet in graphe.sommets:
        if len(graphe.voisins(sommet)) % 2 != 0:
            impairs.append(sommet)
    if len(impairs) == 0:
        depart = graphe.sommets[0]
    elif len(impairs) == 2:
        depart = impairs[0]
    else:
        return []
    workgraph = deepcopy(graphe)
    parcours = [depart]
    voisins = graphe.voisins(depart)
    while len(voisins) != 0:
        parcours.append(voisins[0])
        graphe.supprime_arete([depart, voisins[0]])
        depart = voisins[0]
        voisins = graphe.voisins(voisins[0])
    return parcours

graphe = Graphe([], [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e'], [ 'a', 'd']])
graphe.affiche()
parcours = euler(graphe)
print(parcours)



