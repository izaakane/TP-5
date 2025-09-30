import matplotlib.pyplot as plt
import networkx as nx

class Graphe:
    def __init__(self, start=None, end=None):
        """
        Initialise un graphe orienté pondéré sous forme de dictionnaire d'adjacence.
        Exemple : { 'A': {'B': 2, 'C': 5}, 'B': {'C': 1}, ... }
        """
        self.adjacence = {}
        self.start = start
        self.end = end
        self.chemin_optimal = []

    def ajouter_sommet(self, sommet):
        if sommet not in self.adjacence:
            self.adjacence[sommet] = {}

    def ajouter_arete(self, depart, arrivee, poids):
        self.ajouter_sommet(depart)
        self.ajouter_sommet(arrivee)
        self.adjacence[depart][arrivee] = poids

    def afficher(self):
        for depart, voisins in self.adjacence.items():
            for arrivee, poids in voisins.items():
                print(f"{depart} --({poids})--> {arrivee}")

    def afficher_graphe(self):
        """
        Affiche le graphe avec matplotlib et networkx.
        """
        G = nx.DiGraph()
        for depart, voisins in self.adjacence.items():
            for arrivee, poids in voisins.items():
                G.add_edge(depart, arrivee, weight=poids)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, arrows=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Graphe orienté pondéré")
        plt.show()

    def afficher_chemin_optimal(self):
        """
        Affiche le graphe et met en évidence le chemin optimal entre start et end.
        """
        if not self.chemin_optimal or not self.start or not self.end:
            print("Aucun chemin optimal à afficher. Veuillez d'abord calculer le plus court chemin et définir start/end.")
            return
        G = nx.DiGraph()
        for depart, voisins in self.adjacence.items():
            for arrivee, poids in voisins.items():
                G.add_edge(depart, arrivee, weight=poids)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, arrows=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        # Mettre en évidence le chemin optimal
        edges_chemin = list(zip(self.chemin_optimal, self.chemin_optimal[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges_chemin, edge_color='red', width=3)
        plt.title(f"Chemin optimal de {self.start} à {self.end}")
        plt.show()

    def plus_court_chemin(self, depart, arrivee):
        """
        Algorithme de Dijkstra pour trouver le plus court chemin entre deux sommets.
        Retourne la distance et le chemin sous forme de liste de sommets.
        Met à jour self.chemin_optimal, self.start et self.end.
        """
        import heapq
        file = [(0, depart, [depart])]
        visites = set()
        while file:
            (cout, sommet, chemin) = heapq.heappop(file)
            if sommet == arrivee:
                self.chemin_optimal = chemin
                self.start = depart
                self.end = arrivee
                return cout, chemin
            if sommet in visites:
                continue
            visites.add(sommet)
            for voisin, poids in self.adjacence.get(sommet, {}).items():
                if voisin not in visites:
                    heapq.heappush(file, (cout + poids, voisin, chemin + [voisin]))
        self.chemin_optimal = []
        return float('inf'), []

# ...existing code...

if __name__ == "__main__":
    # Exemple d'utilisation avec le nouveau graphe
    g = Graphe()
    g.ajouter_arete('A', 'B', 4)
    g.ajouter_arete('A', 'C', 2)
    g.ajouter_arete('B', 'C', 5)
    g.ajouter_arete('B', 'D', 10)
    g.ajouter_arete('C', 'E', 3)
    g.ajouter_arete('E', 'D', 4)
    g.ajouter_arete('D', 'F', 11)
    g.afficher()
    g.afficher_graphe()
    distance, chemin = g.plus_court_chemin('A', 'F')
    print(f"Plus court chemin de A à F : {chemin} (distance = {distance})")
