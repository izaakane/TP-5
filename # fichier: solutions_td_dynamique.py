# fichier: solutions_td_dynamique.py

# ==========================
# Exercice 1 : Triangle de Pascal
# ==========================

# Question 1.1 : Algorithme récursif pour le coefficient binomial C(n, k)
def binomial_recursive(n, k):
    """
    Calcule C(n, k) récursivement.
    Complexité : exponentielle (2^n)
    """
    if k == 0 or k == n:
        return 1
    return binomial_recursive(n-1, k-1) + binomial_recursive(n-1, k)

# Question 1.2 : Algorithme dynamique pour le coefficient binomial C(n, k)
def binomial_dynamic(n, k):
    """
    Calcule C(n, k) par programmation dynamique.
    Complexité : O(n*k)
    """
    C = [[0] * (k+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C[n][k]

# ==========================
# Exercice 2 : Problème du stockage (Sac à dos 0/1)
# ==========================

# Question 2.1 : Formule de récurrence
# T[i][j] = max(T[i-1][j], T[i-1][j-s_i] + v_i) si s_i <= j, sinon T[i-1][j]

# Question 2.2 : Algorithme dynamique
def knapsack(values, sizes, D):
    """
    values: liste des valeurs v_i
    sizes: liste des tailles s_i
    D: capacité du disque
    Retourne la valeur maximale stockable.
    Complexité : O(n*D)
    """
    n = len(values)
    T = [[0]*(D+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(D+1):
            if sizes[i-1] <= j:
                T[i][j] = max(T[i-1][j], T[i-1][j-sizes[i-1]] + values[i-1])
            else:
                T[i][j] = T[i-1][j]
    return T[n][D]

# Question 2.3 : Complexité
# O(n*D), où n est le nombre de programmes et D la capacité.

# ==========================
# Exercice 3 : Chemin le plus long dans un graphe ordonné
# ==========================

# Question 3.1 : L'algorithme glouton ne fonctionne pas toujours (contre-exemple possible).

# Question 3.2 : Formule de récurrence
# L(i) = 1 + max{L(j) | (i, j) ∈ E}, L(n) = 0

# Question 3.3 : Algorithme dynamique pour la longueur du plus long chemin de v1 à vn
def longest_path_length(n, edges):
    """
    n: nombre de sommets (numérotés de 1 à n)
    edges: liste des arcs (i, j)
    Retourne la longueur du plus long chemin de v1 à vn.
    """
    L = [0] * (n+1)
    for i in range(n-1, 0, -1):
        L[i] = max([1 + L[j] for (u, j) in edges if u == i] or [0])
    return L[1]

# Question 3.4 : Retourner le chemin lui-même
def longest_path(n, edges):
    """
    Retourne le plus long chemin de v1 à vn sous forme de liste de sommets.
    """
    L = [0] * (n+1)
    next_node = [None] * (n+1)
    for i in range(n-1, 0, -1):
        max_len = 0
        max_j = None
        for (u, j) in edges:
            if u == i and 1 + L[j] > max_len:
                max_len = 1 + L[j]
                max_j = j
        L[i] = max_len
        next_node[i] = max_j
    # Reconstruction du chemin
    path = [1]
    u = 1
    while next_node[u]:
        u = next_node[u]
        path.append(u)
    return path

# Question 3.5 : Formule de récurrence pour le poids maximal
# P(i) = max{w(i, j) + P(j) | (i, j) ∈ E}, P(n) = 0

# Question 3.6 : Algorithme dynamique pour le poids maximal
def longest_weighted_path(n, edges, weights):
    """
    edges: liste des arcs (i, j)
    weights: dictionnaire {(i, j): poids}
    Retourne le poids du chemin de poids maximal de v1 à vn.
    """
    P = [float('-inf')] * (n+1)
    P[n] = 0
    for i in range(n-1, 0, -1):
        max_weight = float('-inf')
        for (u, j) in edges:
            if u == i:
                max_weight = max(max_weight, weights[(u, j)] + P[j])
        P[i] = max_weight if max_weight != float('-inf') else float('-inf')
    return P[1]

# Question 3.7 : Formule de récurrence pour chemin de poids maximal de ` arcs
# T[i][l] = max{T[j][l-1] + w(j, i) | (j, i) ∈ E}
def longest_weighted_path_k_arcs(n, edges, weights, k):
    """
    Retourne le poids maximal d'un chemin de v1 à vi de longueur k arcs.
    """
    T = [[float('-inf')] * (k+1) for _ in range(n+1)]
    T[1][0] = 0
    for l in range(1, k+1):
        for i in range(1, n+1):
            for (j, ii) in edges:
                if ii == i and T[j][l-1] != float('-inf'):
                    T[i][l] = max(T[i][l], T[j][l-1] + weights[(j, i)])
    # Pour le chemin de v1 à vn de k arcs :
    return T[n][k]

# ==========================
# Exercice 4 : Planning
# ==========================

# Question 4.1 : L'algorithme glouton ne fonctionne pas toujours (contre-exemple possible).

# Question 4.2 : Algorithme dynamique pour le revenu maximal
def max_revenue(l, h):
    """
    l: liste des revenus non-stressants par semaine
    h: liste des revenus stressants par semaine
    Retourne le revenu maximal.
    """
    n = len(l)
    dp = [0] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        option1 = dp[i-1] + l[i-1]
        option2 = dp[i-2] + h[i-1] if i >= 2 else h[i-1]
        dp[i] = max(option1, option2)
    return dp[n]

# ==========================
# Exercice 5 : Multiplications chaînées de matrices
# ==========================

# Question 5.1 : Calcul manuel (voir énoncé, pas de code)

# Question 5.2 : Formule de récurrence
# c(i, j) = min_{i <= k < j} [c(i, k) + c(k+1, j) + d_{i-1}*d_k*d_j]

# Question 5.3 : Algorithme dynamique
def matrix_chain_order(dims):
    """
    dims: liste des dimensions [d0, d1, ..., dn] pour n matrices
    Retourne le nombre minimal de multiplications.
    """
    n = len(dims) - 1
    m = [[0]*n for _ in range(n)]
    for l in range(2, n+1):  # longueur de la chaîne
        for i in range(n-l+1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + dims[i]*dims[k+1]*dims[j+1]
                if q < m[i][j]:
                    m[i][j] = q
    return m[0][n-1]