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
    voisins = workgraph.voisins(depart)
    while len(voisins) != 0:
        for v in voisins:
            workgraph.supprime_arete([depart, v])
            if len(workgraph.largeur(v)) == len(workgraph.sommets) or v == voisins[-1]:
                break
            else:
                workgraph.ajoute_arete([depart, v])
        parcours.append(v)
        depart = v
        voisins = workgraph.voisins(v)
    return parcours

graphe = Graphe([], [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e'], [ 'a', 'd']])
graphe = Graphe([], [[0, 1], [0, 2], [1, 2], [1, 3], [1, 4], [2, 4], [2, 5], [3, 4], [4, 5]])
graphe.affiche()
parcours = euler(graphe)
print(parcours)
print(graphe.largeur(0))




