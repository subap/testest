from typing import List, Any, Union

import numpy as np
import random
from tkinter import *

##### 1er jour :

def f(a, b, c, d):
    if a == c and b == d:  # Cas ou on évalue l'adjacence du même point
        return 0
    elif (a - c == 1 or c - a == 1) and b == d or (b - d == 1 or d - b == 1) and a == c or (
            a - c == 1 and b - d == -1) or (a - c == -1 and b - d == 1):
        # On a testé si 2 points sont adjacents
        return 1
    else:
        return 0


size = 3

# Ci-dessous renvoie [a,b] tels que x = 4a+b (division euclidienne)
def g(x):
    return [x // size, x % size]


Adj = np.zeros((size**2, size**2))

i = 0
while i <= size**2-1:
    j = 0
    while j <= size**2-1:
        Adj[i, j] = f(g(i)[0], g(i)[1], g(j)[0], g(j)[1])
        j += 1
    i += 1


print("La matrice d'adjacence du plateau total vaut \n", Adj)


####### 2e jour :

def mat_nulle(l):
    return np.zeros((l, l))


def Adj_joueur(*v):
    i = 0
    matriks = mat_nulle(len(v))
    while i <= len(v) - 1:
        j = 0
        while j <= len(v) - 1:
            matriks[i, j] = Adj[v[i], v[j]]
            j += 1
        i += 1
    return matriks


print("La matrice associé à un joueur est créée, on donne un exemple :\n",
      "Adj_joueur(1, 2, 3) = \n", Adj_joueur(1, 2, 3),
      "\n on voit que le point 2 est relié au point 3 mais pas au 7\n")


def puiss_mat(n, M):
    i = 1
    N = np.copy(M)
    while i <= n - 1:
        M = np.dot(M, N)
        i += 1
    return M


# Ci-dessous on veut voir si on peut isoler la frontière du plateau (w est gagnant)


def reduction_points_west(*u):
    i = 0
    v = []
    I = []
    while i <= len(u) - 1:
        if u[i] <= size - 1:        #On sélectionne la frontière Ouest, càd les points 0,1...,size
            v.append(u[i])
            I.append(i)
        i += 1
    return [v, I]


def reduction_points_east(*u):
    i = 0
    v = []
    I = []
    while i <= len(u) - 1:
        if u[i] >= size**2-size:    ##On sélectionne la frontière Est, càd les points opposés
            v.append(u[i])
            I.append(i)
        i += 1
    return [v, I]



w = [1,2,4]
# w = [4, 5, 12, 9, 1, 0, 3, 6, 13]
# ww = [2, 5, 9]
#
print("La frontière Ouest du joueur est constituée de", reduction_points_west(*w)[0],
      "\n et ils ont été joués aux temps suivants :", reduction_points_west(*w)[1],"\n")

print("La frontière Est du joueur est constituée de", reduction_points_east(*w)[0],
      "\n et ils ont été joués aux temps suivants :", reduction_points_east(*w)[1])

# On écrit la suite en supposant que les frontières E-O sont non-vides.

# print(int(Adj_joueur(*w)[reduction_points_west(*w)[1][0], reduction_points_east(*w)[1][0]]))
#
# print(int(puiss_mat(3, Adj_joueur(*w))[reduction_points_west(*w)[1][0], reduction_points_east(*w)[1][0]]),
#       "---> il y a donc connexion entre le point", reduction_points_west(*w)[0][0], "et le point",
#       reduction_points_east(*w)[0][0])


# On veut maintenant tester si étant donné un vecteur de coups joués, il y a connexion ou pas.
def test_connexion_puissance(p, *v):
    i = 0
    frontiere_connexion = []
    while i <= len(reduction_points_west(*v)[1]) - 1:
        j = 0
        while j <= len(reduction_points_east(*v)[1]) - 1:
            frontiere_connexion.append(
                int(puiss_mat(p, Adj_joueur(*w))[reduction_points_west(*v)[1][i], reduction_points_east(*v)[1][j]]))
            j += 1
        i += 1
    return frontiere_connexion


print(test_connexion_puissance(2, *w))


def test_connexion(*v):
    p = 1
    while sum(test_connexion_puissance(p, *v)) == 0 and p <= size**2 - 1:
        # la somme des aij est un indicateur suffisant pour le test.
        # p = 15 est là pour faire s'arrêter l'algorithme au cas où.
        p += 1
    return p


# print("CONNEXION RÉUSSIE, taille de la chaîne de w :", test_connexion(*w) + 1)
# print(test_connexion_puissance(2, *ww))
# print(test_connexion(*ww))


# Maintenant le but est de stocker des coups blancs et noirs dans 2 listes différentes et d'appliquer le test_connexion




def liste_aleatoire_bis(n):  # Cette fonction renvoie n entiers qui ne se répètent pas, entre 0 et 15. n max = 16.
    liste_coups = []
    i = 0
    while i <= n - 1:
        coup = random.randint(0, size**2 - 1)
        if coup not in liste_coups:
            liste_coups.append(coup)
        i += 1
    return liste_coups

print(liste_aleatoire_bis(size**2-5))
