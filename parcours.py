from graphe import Graphe, Graphe_pondere_oriente, Graphe_pondere, GrapheOriente
from collections import deque
from math import inf


def parcours_profondeur_recursif(graphe, sommet, visites = []):
    visites.append(sommet)
    for voisin in graphe.voisins(sommet):
        if voisin not in visites:
            parcours_profondeur_recursif(graphe, voisin, visites)
    return visites

def cycle_oriente(graphe, sommet, visites = []):
    visites.append(sommet)
    deja_vus = [sommet]
    for voisin in graphe.voisins(sommet):
        if voisin in deja_vus:
            return True
        deja_vus.append(voisin)
        if voisin not in visites:
            cycle_oriente(graphe, voisin, visites)
            visites.append(voisin)
    return False


def parcours_profondeur(graphe, sommet):
    pile = []
    pile.append(sommet)
    visites = []
    while pile != []:
        sommet_courant = pile.pop()
        if sommet_courant not in visites:
            visites.append(sommet_courant)
            for voisin in graphe.voisins(sommet_courant):
                if voisin not in visites:
                    pile.append(voisin)
    return visites


def parcours_largeur(graphe, sommet):
    file = deque()
    file.appendleft(sommet)
    visites = []
    while len(file) != 0:
        sommet_courant = file.pop()
        if sommet_courant not in visites:
            visites.append(sommet_courant)
            for voisin in graphe.voisins(sommet_courant):
                if voisin not in visites:
                    file.appendleft(voisin)
    return visites

def cycle_largeur(graphe, sommet):
    "On utilise la classe deque ( double-ended queue) comme file avec les seules méthodes appendleft ( entrée ) , pop ( sortie) et len (pour savoir quand la file est vide )"
    file = deque()
    file.appendleft(sommet)
    visites = []
    while len(file) != 0:
        sommet_courant = file.pop()
        if sommet_courant not in visites:
            visites.append(sommet_courant)
            for voisin in graphe.voisins(sommet_courant):
                if voisin not in visites:
                    file.appendleft(voisin)
        else:
            return True
    return False

def cycle_profondeur(graphe, sommet):
    "On utilise une simple liste comme pile avec les seules méthodes ( empiler ) , pop ( dépiler) et len (pour savoir quand la pile est vide )"

    pile = []
    pile.append(sommet)
    visites = []
    while pile != []:
        sommet_courant = pile.pop()
        if sommet_courant not in visites:
            visites.append(sommet_courant)
            for voisin in graphe.voisins(sommet_courant):
                if voisin not in visites:
                    pile.append(voisin)
        else:
            return True
    return False

def minimum(dico: dict):
    if len(dico) == 0:
        return None
    mini = inf
    for clef in dico.keys():
        if dico[clef] <= mini:
            mini = dico[clef]
            clef_min = clef
    return clef_min

def dijkstra(graphe: Graphe, sommet_depart)->dict:
    visites = []
    distances = {}
    distances_minimales = {}
    for sommet in graphe.sommets:
        distances[sommet] = inf
    distances[sommet_depart] = 0
    while len(distances) != 0:
        sommet_choisi = minimum(distances)
        print("dico : ", distances, "minimum : ", sommet_choisi)
        visites.append(sommet_choisi)
        for voisin in graphe.voisins(sommet_choisi):
            sommet = voisin[0]
            distance = voisin[1]
            if sommet not in visites:
                if distances[sommet_choisi] + distance < distances[sommet]:
                    distances[sommet] = distances[sommet_choisi] + distance
        distances_minimales[sommet_choisi] = distances[sommet_choisi]
        distances.pop(sommet_choisi)

    return distances_minimales

def dijkstra_alternate(graphe: Graphe, sommet_depart)->dict:
    "On n'utilise pas la liste sommets_visites, on la remplace par distance_minimales.keys()"
    distances = {}
    distances_minimales = {}
    for sommet in graphe.sommets:
        distances[sommet] = inf
    distances[sommet_depart] = 0
    while len(distances) != 0:
        sommet_choisi = minimum(distances)
        print("dico : ", distances, "minimum : ", sommet_choisi)
        distances_minimales[sommet_choisi] = distances[sommet_choisi]
        for voisin in graphe.voisins(sommet_choisi):
            sommet = voisin[0]
            distance = voisin[1]
            if sommet not in distances_minimales.keys():
                if distances[sommet_choisi] + distance < distances[sommet]:
                    distances[sommet] = distances[sommet_choisi] + distance
        distances.pop(sommet_choisi)

    return distances_minimales

def parcours_exhaustif(graphe):
    if graphe.sommets == []:
        return []
    parcours = []
    for sommet in graphe.sommets:
        if sommet not in parcours:
            parcours_local = parcours_profondeur(graphe, sommet)
            parcours += parcours_local
            if len(parcours) == len(graphe.sommets):
                return parcours
    return parcours

def composantes_connexes(graphe):
    def present(parcours, sommet):
        for composante in parcours:
            for s in composante:
                if s == sommet:
                    return True
        return False

    if graphe.sommets == []:
        return []
    parcours = []
    longueur = 0
    for sommet in graphe.sommets:
        if not present(parcours, sommet):
            parcours_local = parcours_profondeur(graphe, sommet)
            parcours.append(parcours_local)
            longueur += len(parcours_local)
            if longueur == len(graphe.sommets):
                return parcours
    return parcours




if __name__ == "__main__":
    '''
    graphe = Graphe_pondere([0, 1, 2, 3,4], [[0,1,8], [0, 2, 5],[0, 3, 4], [1,2,1], [1,3,3]])
    #graphe = Graphe_pondere_oriente(['a', 'b', 'c', 'd', 'e', 'f', 'g'], [('a', 'b', 5), ('a', 'c', 2), ('a', 'd', 7), ('c', 'd', 2),                                                              ('d', 'b', 1), ('d', 'e', 2), ('b', 'e', 2), ('f', 'g', 4)])
    #graphe = Graphe_pondere_oriente(['a', 'b', 'c', 'd', 'e'], [('a', 'b', 5), ('b', 'c', 3), ('c', 'd', 2), ('c', 'a', 5), ('d', 'a', 2), ('a', 'd', 3), ('d', 'c', 2) , ('d', 'e', 1), ('e', 'c', 1)])
    print(parcours_profondeur_recursif(graphe, sommet=1))
    print(parcours_profondeur(graphe, 1))
    print(parcours_largeur(graphe, 1))
    print(cycle_largeur(graphe, 1))
    graphe2 = GrapheOriente([1,2,0], [[1,2], [0,1],[3, 4], [2, 3], [4,1]])
    graphe2.affiche()
    print(cycle_oriente(graphe2, 1))
    #print(dijkstra_alternate(graphe, 'a'))
    #print(graphe.dijkstra_chemin('a'))
    #print(graphe.plus_court_chemin("d", "g"))
    #print(graphe.matrice_distances())
    #graphe.affiche_distances()
    #print(graphe.ordonne_par_distance())
    print(graphe.dijkstra(1))
    '''
    graphe = Graphe([0, 1, 2, 3, 4, 5], [[0, 1], [1, 2], [3, 4]])
    graphe.affiche()
    print(composantes_connexes(graphe))




