from graphviz import Graph, Digraph
from math import inf
from tabulate import tabulate

class Graphe:
    def __init__(self, liste_sommets, liste_aretes):
        self.sommets = liste_sommets
        self.aretes = []
        for arete in liste_aretes:
            self.ajoute_arete(arete)

    def ajoute_sommet(self, sommet):
        self.sommets .append(sommet)

    def ajoute_arete(self, arete):
        self.aretes.append(arete)
        origine = arete[0]
        extremite = arete[1]
        if origine not in self.sommets:
            self.sommets.append(origine)
        if extremite not in self.sommets:
            self.sommets.append(extremite)

    def supprime_arete(self, arete):
        origine = arete[0]
        extremite = arete[1]
        if [origine, extremite] in self.aretes:
            self.aretes.remove([origine, extremite])
        elif [extremite, origine] in self.aretes:
            self.aretes.remove([extremite, origine])

    def supprime_sommet(self, sommet):
        if sommet in self.sommets:
            self.sommets.remove(sommet)
            for arete in self.aretes:
                if (arete[0] == sommet) or (arete[1] == sommet):
                    self.aretes.remove(arete)

    def affiche_aretes(self):
        print(self.aretes)

    def affiche_sommets(self):
        print(self.sommets)

    def voisins(self, sommet):
        if sommet in self.sommets:
            liste_voisins = []
            for arete in self.aretes:
                if arete[0] == sommet:
                    liste_voisins.append(arete[1])
                elif arete[1] == sommet:
                    liste_voisins.append(arete[0])
            return liste_voisins
        return []

    def dico_adjacence(self):
        dico = {}
        for sommet in self.sommets:
            dico[sommet] = self.voisins(sommet)
        return dico

    def initialise_matrice(self):
        nb_sommets = len(self.sommets)
        matrice = []
        for _ in range(nb_sommets):
            ligne = []
            for _ in range(nb_sommets):
                ligne.append(0)
            matrice.append(ligne)
        return matrice

    def matrice_adjacence(self):
        matrice = self.initialise_matrice()
        for arete in self.aretes:
            matrice[arete[0]][arete[1]] = 1
            matrice[arete[1]][arete[0]] = 1
        return matrice

    def affiche_matrice(self):
        matrice = self.matrice_adjacence()
        for ligne in matrice:
            print(ligne)

    def affiche(self):
        graphe_affichage = Graph(format='png')
        for arete in self.aretes:
            graphe_affichage.edge(str(arete[0]), str(arete[1]))
        graphe_affichage.render(view=True)

class Graphe_pondere:
    def __init__(self, liste_sommets, liste_aretes):
        self.sommets = liste_sommets
        self.aretes = []
        for arete in liste_aretes:
            self.ajoute_arete(arete)

    def ajoute_sommet(self, sommet):
        self.sommets .append(sommet)

    def ajoute_arete(self, arete):
        self.aretes.append(arete)
        origine = arete[0]
        extremite = arete[1]
        if origine not in self.sommets:
            self.sommets.append(origine)
        if extremite not in self.sommets:
            self.sommets.append(extremite)

    def supprime_arete(self, arete):
        origine = arete[0]
        extremite = arete[1]
        if [origine, extremite] in self.aretes:
            self.aretes.remove([origine, extremite])
        elif [extremite, origine] in self.aretes:
            self.aretes.remove([extremite, origine])

    def supprime_sommet(self, sommet):
        if sommet in self.sommets:
            self.sommets.remove(sommet)
            for arete in self.aretes:
                if (arete[0] == sommet) or (arete[1] == sommet):
                    self.aretes.remove(arete)

    def affiche_aretes(self):
        print(self.aretes)

    def affiche_sommets(self):
        print(self.sommets)

    def voisins(self, sommet):
        if sommet in self.sommets:
            liste_voisins = []
            for arete in self.aretes:
                if arete[0] == sommet:
                    liste_voisins.append((arete[1], arete[2]))
                elif arete[1] == sommet:
                    liste_voisins.append((arete[0], arete[2]))
            return liste_voisins
        return []

    def dico_adjacence(self):
        dico = {}
        for sommet in self.sommets:
            dico[sommet] = self.voisins(sommet)
        return dico

    def initialise_matrice(self):
        nb_sommets = len(self.sommets)
        matrice = []
        for _ in range(nb_sommets):
            ligne = []
            for _ in range(nb_sommets):
                ligne.append(0)
            matrice.append(ligne)
        return matrice

    def matrice_adjacence(self):
        matrice = self.initialise_matrice()
        for arete in self.aretes:
            matrice[arete[0]][arete[1]] = 1
            matrice[arete[1]][arete[0]] = 1
        return matrice

    def affiche_matrice(self):
        matrice = self.matrice_adjacence()
        for ligne in matrice:
            print(ligne)

    def affiche(self):
        graphe_affichage = Graph(format='png')
        for sommet in self.sommets:
            graphe_affichage.node(str(sommet))
        for arete in self.aretes:
            graphe_affichage.edge(str(arete[0]), str(arete[1]), label=str(arete[2]))
        graphe_affichage.render(view=True)

    def dijkstra(self, sommet_depart) -> dict:
        def minimum(dico: dict):
            if len(dico) == 0:
                return None
            mini = inf
            for clef in dico.keys():
                if dico[clef] <= mini:
                    mini = dico[clef]
                    clef_min = clef
            return clef_min

        visites = []
        distances = {}
        distances_minimales = {}
        for sommet in self.sommets:
            distances[sommet] = inf
        distances[sommet_depart] = 0
        while len(distances) != 0:
            sommet_choisi = minimum(distances)
            print("dico : ", distances, "minimum : ", sommet_choisi)
            visites.append(sommet_choisi)
            for voisin in self.voisins(sommet_choisi):
                sommet = voisin[0]
                distance = voisin[1]
                if sommet not in visites:
                    if distances[sommet_choisi] + distance < distances[sommet]:
                        distances[sommet] = distances[sommet_choisi] + distance
            distances_minimales[sommet_choisi] = distances[sommet_choisi]
            distances.pop(sommet_choisi)

    def dijkstra_mael(self, chosen_sommet):
        def dicomin(dico: dict):
            if len(dico) == 0:
                return None
            mini = inf
            for clef in dico.keys():
                if dico[clef] <= mini:
                    mini = dico[clef]
                    clef_min = clef
            return clef_min

        visites = []
        distances = {}
        distances_min = {}
        for sommet in self.sommets:
            distances[sommet] = inf
        distances[chosen_sommet] = 0
        while distances != {}:
            current_sommet = dicomin(distances)
            visites.append(current_sommet)
            for voisin in self.voisins(current_sommet):
                if voisin[0] not in visites:
                    sommet = voisin[0]
                    distance = voisin[1]
                    print(sommet, distances)
                    if distances[current_sommet] + distance < distances[sommet]:
                        distances[sommet] = (distances[current_sommet] + distance)
            distances_min[current_sommet] = distances[current_sommet]
            distances.pop(current_sommet)
        return distances_min


    def dijkstra_chemin(self, sommet_depart) -> dict:
        def minimum(dico: dict):
            if len(dico) == 0:
                return None
            mini = inf
            for clef in dico.keys():
                if dico[clef][0] <= mini:
                    mini = dico[clef][0]
                    clef_min = clef
            return clef_min

        visites = []
        distances = {}
        distances_minimales = {}
        for sommet in self.sommets:
            distances[sommet] = (inf, [])
        distances[sommet_depart] = (0, [sommet_depart])
        while len(distances) != 0:
            sommet_choisi = minimum(distances)
            visites.append(sommet_choisi)
            for voisin in self.voisins(sommet_choisi):
                sommet = voisin[0]
                distance = voisin[1]
                if sommet not in visites:
                    if distances[sommet_choisi][0] + distance < distances[sommet][0]:
                        distances[sommet] = (distances[sommet_choisi][0] + distance, distances[sommet_choisi][1] + [sommet])
            distances_minimales[sommet_choisi] = distances[sommet_choisi]
            distances.pop(sommet_choisi)

        return distances_minimales

    def plus_court_chemin(self, debut, fin):
        if (debut not in self.sommets) or (fin not in self.sommets):
            return (inf, [])
        dico_distances = self.dijkstra_chemin(debut)
        return dico_distances[fin]

    def matrice_distances(self):
        matrice = []
        for i in range(len(self.sommets)):
            ligne = []
            for j in range(len(self.sommets)):
                debut = self.sommets[i]
                fin = self.sommets[j]
                ligne.append(self.plus_court_chemin(debut, fin))
            matrice.append(ligne)
        return matrice

    def affiche_distances(self):
        matrice = self.matrice_distances()
        matrice_affichee = []
        en_tete = [' '] + [sommet for sommet in self.sommets]
        for i in range(len(matrice)):
            matrice[i] = [self.sommets[i]] +matrice[i]
        print(tabulate(matrice, en_tete))

class GrapheOriente:
    def __init__(self, liste_sommets, liste_aretes):
        self.sommets = liste_sommets
        self.aretes = []
        for arete in liste_aretes:
            self.ajoute_arete(arete)

    def ajoute_sommet(self, sommet):
        self.sommets .append(sommet)

    def ajoute_arete(self, arete):
        self.aretes.append(arete)
        origine = arete[0]
        extremite = arete[1]
        if origine not in self.sommets:
            self.sommets.append(origine)
        if extremite not in self.sommets:
            self.sommets.append(extremite)

    def supprime_arete(self, arete):
        if arete in self.aretes:
            self.aretes.remove(arete)

    def supprime_sommet(self, sommet):
        if sommet in self.sommets:
            self.sommets.remove(sommet)
            for arete in self.aretes:
                if (arete[0] == sommet) or (arete[1] == sommet):
                    self.aretes.remove(arete)

    def affiche_aretes(self):
        print(self.aretes)

    def affiche_sommets(self):
        print(self.sommets)

    def voisins(self, sommet):
        if sommet in self.sommets:
            liste_voisins = []
            for arete in self.aretes:
                if arete[0] == sommet:
                    liste_voisins.append(arete[1])
            return liste_voisins
        return []

    def dico_adjacence(self):
        dico = {}
        for sommet in self.sommets:
            dico[sommet] = self.voisins(sommet)
        return dico

    def initialise_matrice(self):
        nb_sommets = len(self.sommets)
        matrice = []
        for _ in range(nb_sommets):
            ligne = []
            for _ in range(nb_sommets):
                ligne.append(0)
            matrice.append(ligne)
        return matrice

    def matrice_adjacence(self):
        matrice = self.initialise_matrice()
        for arete in self.aretes:
            matrice[arete[0]][arete[1]] = 1
        return matrice

    def affiche_matrice(self):
        matrice = self.matrice_adjacence()
        for ligne in matrice:
            print(ligne)

    def affiche(self):
        graphe_affichage = Digraph(format='png')
        for arete in self.aretes:
            graphe_affichage.edge(str(arete[0]), str(arete[1]))
        graphe_affichage.render(view=True)

class Graphe_pondere_oriente:
    def __init__(self, liste_sommets, liste_aretes):
        self.sommets = liste_sommets
        self.aretes = []
        for arete in liste_aretes:
            self.ajoute_arete(arete)

    def ajoute_sommet(self, sommet):
        self.sommets .append(sommet)

    def ajoute_arete(self, arete):
        self.aretes.append(arete)
        origine = arete[0]
        extremite = arete[1]
        if origine not in self.sommets:
            self.sommets.append(origine)
        if extremite not in self.sommets:
            self.sommets.append(extremite)

    def supprime_arete(self, arete):
        origine = arete[0]
        extremite = arete[1]
        if [origine, extremite] in self.aretes:
            self.aretes.remove([origine, extremite])

    def supprime_sommet(self, sommet):
        if sommet in self.sommets:
            self.sommets.remove(sommet)
            for arete in self.aretes:
                if (arete[0] == sommet) or (arete[1] == sommet):
                    self.aretes.remove(arete)

    def affiche_aretes(self):
        print(self.aretes)

    def affiche_sommets(self):
        print(self.sommets)

    def voisins(self, sommet):
        if sommet in self.sommets:
            liste_voisins = []
            for arete in self.aretes:
                if arete[0] == sommet:
                    liste_voisins.append((arete[1], arete[2]))
            return liste_voisins
        return []

    def dico_adjacence(self):
        dico = {}
        for sommet in self.sommets:
            dico[sommet] = self.voisins(sommet)
        return dico

    def initialise_matrice(self):
        nb_sommets = len(self.sommets)
        matrice = []
        for _ in range(nb_sommets):
            ligne = []
            for _ in range(nb_sommets):
                ligne.append(0)
            matrice.append(ligne)
        return matrice

    def matrice_adjacence(self):
        matrice = self.initialise_matrice()
        for arete in self.aretes:
            matrice[arete[0]][arete[1]] = 1
        return matrice

    def affiche_matrice(self):
        matrice = self.matrice_adjacence()
        for ligne in matrice:
            print(ligne)

    def affiche(self):
        graphe_affichage = Digraph(format='png')
        for sommet in self.sommets:
            graphe_affichage.node(str(sommet))
        for arete in self.aretes:
            graphe_affichage.edge(str(arete[0]), str(arete[1]), label=str(' ' + str(arete[2])))
        graphe_affichage.render(view=True)

    def dijkstra(self, sommet_depart) -> dict:
        def minimum(dico: dict):
            if len(dico) == 0:
                return None
            mini = inf
            for clef in dico.keys():
                if dico[clef] <= mini:
                    mini = dico[clef]
                    clef_min = clef
            return clef_min
        distances = {}
        distances_minimales = {}
        for sommet in self.sommets:
            distances[sommet] = inf
        distances[sommet_depart] = 0
        while len(distances) != 0:
            sommet_choisi = minimum(distances)
            print("dico : ", distances, "minimum : ", sommet_choisi)
            distances_minimales[sommet_choisi] = distances[sommet_choisi]
            for voisin in self.voisins(sommet_choisi):
                sommet = voisin[0]
                distance = voisin[1]
                if sommet not in distances_minimales.keys():
                    if distances[sommet_choisi] + distance < distances[sommet]:
                        distances[sommet] = distances[sommet_choisi] + distance
            distances.pop(sommet_choisi)
        return distances_minimales

    def dijkstra_alternate(self, sommet_depart) -> dict:
        def minimum(dico: dict):
            if len(dico) == 0:
                return None
            mini = inf
            for clef in dico.keys():
                if dico[clef] <= mini:
                    mini = dico[clef]
                    clef_min = clef
            return clef_min

        visites = []
        distances = {}
        distances_minimales = {}
        for sommet in self.sommets:
            distances[sommet] = inf
        distances[sommet_depart] = 0
        while len(distances) != 0:
            sommet_choisi = minimum(distances)
            print("dico : ", distances, "minimum : ", sommet_choisi)
            visites.append(sommet_choisi)
            for voisin in self.voisins(sommet_choisi):
                sommet = voisin[0]
                distance = voisin[1]
                if sommet not in visites:
                    if distances[sommet_choisi] + distance < distances[sommet]:
                        distances[sommet] = distances[sommet_choisi] + distance
            distances_minimales[sommet_choisi] = distances[sommet_choisi]
            distances.pop(sommet_choisi)
        return distances_minimales


    def dijkstra_chemin(self, sommet_depart) -> dict:
        def minimum(dico: dict):
            if len(dico) == 0:
                return None
            mini = inf
            for clef in dico.keys():
                if dico[clef][0] <= mini:
                    mini = dico[clef][0]
                    clef_min = clef
            return clef_min

        visites = []
        distances = {}
        distances_minimales = {}
        for sommet in self.sommets:
            distances[sommet] = (inf, [])
        distances[sommet_depart] = (0, [sommet_depart])
        while len(distances) != 0:
            sommet_choisi = minimum(distances)
            visites.append(sommet_choisi)
            for voisin in self.voisins(sommet_choisi):
                sommet = voisin[0]
                distance = voisin[1]
                if sommet not in visites:
                    if distances[sommet_choisi][0] + distance < distances[sommet][0]:
                        distances[sommet] = (distances[sommet_choisi][0] + distance, distances[sommet_choisi][1] + [sommet])
            distances_minimales[sommet_choisi] = distances[sommet_choisi]
            distances.pop(sommet_choisi)

        return distances_minimales

    def plus_court_chemin(self, debut, fin):
        if (debut not in self.sommets) or (fin not in self.sommets):
            return (inf, [])
        dico_distances = self.dijkstra_chemin(debut)
        return dico_distances[fin]

    def matrice_distances(self):
        matrice = []
        for i in range(len(self.sommets)):
            ligne = []
            for j in range(len(self.sommets)):
                debut = self.sommets[i]
                fin = self.sommets[j]
                ligne.append(self.plus_court_chemin(debut, fin))
            matrice.append(ligne)
        return matrice

    def affiche_distances(self):
        matrice = self.matrice_distances()
        en_tete = ['Sommet'] + [sommet for sommet in self.sommets]
        for i in range(len(matrice)):
            matrice[i] = [self.sommets[i]] +matrice[i]
        print(tabulate(matrice, en_tete))

    def ordonne_par_distance(self) -> list:
        dico = {}
        for sommet1 in self.sommets:
            for sommet2 in self.sommets:
                distance = self.plus_court_chemin(sommet1, sommet2)[0]
                if distance in dico.keys():
                    dico[distance].append((sommet1, sommet2))
                else:
                    dico[distance] = [(sommet1, sommet2)]
        liste = sorted(dico.items(), reverse = True)
        return liste





if __name__ == "__main__":
    graphe = Graphe([1,2,0], [[1,2], [2, 0], [0,1]])
    print(graphe.dico_adjacence())
    graphe.affiche_matrice()
