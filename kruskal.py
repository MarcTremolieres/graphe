from graphviz import Graph, Digraph
from math import inf
from tabulate import tabulate

class Graphe_pondere:
    def __init__(self, liste_sommets = [], liste_aretes = []):
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

    def supprime_arete_old(self, arete):
        origine = arete[0]
        extremite = arete[1]
        if [origine, extremite] in self.aretes:
            self.aretes.remove([origine, extremite])
        elif [extremite, origine] in self.aretes:
            self.aretes.remove([extremite, origine])

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
                    liste_voisins.append((arete[1], arete[2]))
                elif arete[1] == sommet:
                    liste_voisins.append((arete[0], arete[2]))
            return liste_voisins
        return []

    def cycle_profondeur(self):
        visites = []
        pile = [self.sommets[0]]
        while pile !=[]:
            s = pile.pop()
            if s in visites:
                return True
            visites.append(s)
            for v in self.voisins(s):
                if not v[0] in visites:
                    pile.append(v[0])
        return False

    
    def affiche(self):
        graphe_affichage = Graph(format='png')
        for sommet in self.sommets:
            graphe_affichage.node(str(sommet))
        for arete in self.aretes:
            graphe_affichage.edge(str(arete[0]), str(arete[1]), label=str(arete[2]))
        graphe_affichage.render(view=True)

    def kruskal(self):
        krusk = Graphe_pondere()
        self.aretes.sort(key = lambda x: x[2])
        for arete in self.aretes:
            krusk.ajoute_arete(arete)
            if krusk.cycle_profondeur():
                krusk.supprime_arete(arete)
        return krusk


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

    def affiche(self):
        graphe_affichage = Digraph(format='png')
        for sommet in self.sommets:
            graphe_affichage.node(str(sommet))
        for arete in self.aretes:
            graphe_affichage.edge(str(arete[0]), str(arete[1]), label=str(' ' + str(arete[2])))
        graphe_affichage.render(view=True)




if __name__ == "__main__":
    graphe = Graphe_pondere([], [['a', 'b', 5], ['b', 'c', 3], ['c', 'd',7], ['d', 'e',4], [ 'a', 'd',1], ['d', 'f', 6], ['e', 'f', 5]])
    graphe.affiche()
    input("continuer")
    k = graphe.kruskal()
    k.affiche()
