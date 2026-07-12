#!/usr/bin/env python3
"""
Advent of Code 2025 — Jour 1
============================
Catégorie : warm-up (introductif)

Énoncé simplifié :
------------------
On te donne une liste de nombres. La première partie consiste à trouver
la somme de tous les nombres de la liste.

La deuxième partie ajoute une complication : chaque nombre est préfixé
par un symbole (+ ou -). Il faut calculer la somme algébrique.

Exemple :
    Entrée : [+3, +5, -2, +8]
    Résultat attendu (partie 1) : 3 + 5 + 2 + 8 = 18
    Résultat attendu (partie 2) : 3 + 5 + (-2) + 8 = 14

Objectifs d'apprentissage :
    - Lire et écrire dans un fichier
    - Traiter une liste de chaînes
    - Convertir des chaînes en nombres
    - Accumuler un résultat (boucle ou fonction native)
    - Gestion des signes optionnels avec les nombres négatifs
"""

import sys
from pathlib import Path


def parser_ligne(ligne: str) -> int:
    """
    Convertit une chaîne en entier.
    
    Gère les cas où le signe + est explicite (ex: "+42")
    Python fait ça naturellement avec int().

    Args:
        ligne: Une chaîne représentant un entier (ex: "42", "-7", "+3")

    Returns:
        L'entier correspondant

    Exemple:
        >>> parser_ligne("42")
        42
        >>> parser_ligne("-7")
        -7
    """
    return int(ligne.strip())


def partie_1(nombres: list[int]) -> int:
    """
    Calcule la somme de toutes les valeurs absolues.
    
    C'est-à-dire qu'on additionne les valeurs en ignorant leur signe.
    """
    total = 0
    for n in nombres:
        total += abs(n)
    return total


def partie_2(nombres: list[int]) -> int:
    """
    Calcule la somme algébrique (signes respectés).
    
    On additionne chaque nombre avec son signe.
    """
    total = 0
    for n in nombres:
        total += n
    return total


def charger_fichier(chemin: str) -> list[int]:
    """
    Lit un fichier et retourne la liste des entiers qu'il contient.
    
    Args:
        chemin: Chemin vers le fichier d'entrée

    Returns:
        Liste d'entiers
    """
    contenu = Path(chemin).read_text()
    lignes = contenu.strip().split("\n")
    return [parser_ligne(ligne) for ligne in lignes if ligne.strip()]


def main():
    """
    Point d'entrée principal du programme.
    
    Utilisation :
        python solutions/jour_01.py          # Mode interactif (exemples intégrés)
        python solutions/jour_01.py input.txt # Avec un fichier d'entrée
    """
    # Données d'exemple pour tester sans fichier
    donnees_exemple = [3, 5, -2, 8]

    # Vérifie si un fichier a été fourni en argument
    if len(sys.argv) > 1:
        fichier_entree = sys.argv[1]
        print(f"📂 Chargement des données depuis : {fichier_entree}")
        try:
            donnees = charger_fichier(fichier_entree)
        except FileNotFoundError:
            print(f"❌ Erreur : fichier '{fichier_entree}' introuvable.")
            sys.exit(1)
    else:
        print("📝 Utilisation des données d'exemple intégrées.")
        donnees = donnees_exemple

    # Affiche les données traitées
    print(f"📊 Données : {donnees}")
    print(f"📊 Nombre d'éléments : {len(donnees)}")

    # Calcule et affiche les résultats
    resultat_partie1 = partie_1(donnees)
    resultat_partie2 = partie_2(donnees)

    print()
    print("=" * 40)
    print("🎄 RÉSULTATS")
    print("=" * 40)
    print(f"   Partie 1 (valeurs absolues) : {resultat_partie1}")
    print(f"   Partie 2 (somme algébrique) : {resultat_partie2}")
    print("=" * 40)


# Ce bloc permet d'exécuter le script directement
# Si on importe ce fichier dans un autre, ce code ne s'exécutera pas
if __name__ == "__main__":
    main()