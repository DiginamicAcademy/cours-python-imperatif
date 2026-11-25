"""lire_citations.py — verifie que le corpus hors-ligne est en place.

A lancer depuis ce dossier, sans reseau et sans rien installer :

    python lire_citations.py

Affiche le nombre de citations par auteur, puis deux citations d'Edgar Allan
Poe, pour voir a quoi ressemble une donnee avant de s'en servir.
"""

import json

from quote_offline import REPERTOIRE, quote


def compter_citations(chemin):
    """Rend le nombre de citations contenues dans un fichier du corpus."""
    with open(chemin, encoding="utf-8") as fichier:
        return len(json.load(fichier))


def afficher_inventaire():
    """Liste les fichiers du corpus avec leur nombre de citations.

    Rend le nombre total de citations trouve. Zero signifie que le corpus
    n'est pas encore en place : voir README.md.
    """
    fichiers = sorted(REPERTOIRE.glob("*.json"))
    total = 0
    for chemin in fichiers:
        nombre = compter_citations(chemin)
        total += nombre
        print(f"{nombre:>3} citations  {chemin.name}")
    print(f"\n{len(fichiers)} fichiers, {total} citations")
    return total


if __name__ == "__main__":
    if afficher_inventaire() == 0:
        raise SystemExit("Corpus vide : voir README.md de ce dossier.")

    print("\nEchantillon — Edgar Allan Poe, 2 citations :")
    for citation in quote("Edgar Allan Poe", limit=2):
        print(f"- {citation['quote']}")
        print(f"  [{citation['book']}]")
