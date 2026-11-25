"""capture_citations.py — reconstruit le corpus hors-ligne, une seule fois.

Ce script n'est pas un exercice. Il sert a reconstituer les fichiers .json de
ce dossier quand l'un d'eux manque ou doit etre renouvele. Il a besoin du
reseau, et de deux paquets installes par pip :

    pip install quote certifi
    python capture_citations.py

Il ecrit dans ce dossier, avec la meme normalisation des noms que
quote_offline.py : un auteur, un fichier.
"""

import json
import os

import certifi
from quote import quote

from quote_offline import REPERTOIRE, nom_de_fichier

# A placer avant le premier appel : le module de citations interroge un site en
# HTTPS, et certains postes (WSL, proxy d'entreprise) ne connaissent pas ses
# certificats. Sans cette ligne : ssl.SSLCertVerificationError.
os.environ["SSL_CERT_FILE"] = certifi.where()

AUTEURS = [
    "Edgar Allan Poe", "Victor Hugo", "Gustave Flaubert", "Ernest Hemingway",
    "Agatha Christie", "Friedrich Nietzsche", "Arthur Schopenhauer",
    "Simone De Beauvoir", "Guy De Maupassant", "Voltaire", "Emile Zola",
    "Georges Orwell", "Frank Herbert", "Isaac Asimov", "Tolkien",
    "William Shakespeare",
]
NB_CITATIONS = 30


def capturer(auteur, nombre):
    """Ecrit les citations d'un auteur dans le corpus, rend le nombre ecrit.

    Rend None quand la source ne donne rien : dans ce cas aucun fichier n'est
    touche, pour ne pas vider un corpus existant a cause d'un nom mal ecrit.
    """
    donnees = quote(auteur, limit=nombre)
    if not donnees:
        print(f"  {auteur} : aucune citation recue, fichier laisse en place")
        return None
    chemin = REPERTOIRE / nom_de_fichier(auteur)
    with open(chemin, "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=2)
    print(f"  {auteur} : {len(donnees)} citations -> {chemin.name}")
    return len(donnees)


if __name__ == "__main__":
    print(f"Corpus hors-ligne : {REPERTOIRE}\n")

    sans_citation = []
    for auteur in AUTEURS:
        if capturer(auteur, NB_CITATIONS) is None:
            sans_citation.append(auteur)

    if sans_citation:
        print("\nAuteurs sans citation :")
        for auteur in sans_citation:
            print(f"  - {auteur} (verifiez l'orthographe du nom)")
