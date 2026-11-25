"""quote_offline.py — substitut hors-ligne au paquet `quote`.

Meme forme que le paquet installe par pip : une fonction quote(auteur, limit),
qui rend une liste de dictionnaires a trois cles ('quote', 'book', 'author').
On change une seule ligne d'import, et les exercices tournent sans reseau :

    from quote import quote          # en ligne
    from quote_offline import quote  # ici, sans reseau

Corpus : les fichiers .json de ce dossier, un par auteur
(« Edgar Allan Poe » -> Edgar_Allan_Poe.json). Voir README.md.
"""

import json
from pathlib import Path

REPERTOIRE = Path(__file__).resolve().parent


def normaliser(nom):
    """Efface ce qui sépare les mots d'un nom d'auteur, et la casse.

    « Edgar Allan Poe », « edgar-allan-poe » et « Edgar_Allan_Poe » donnent
    tous « edgarallanpoe » : le corpus est retrouvé quel que soit le
    séparateur employé par le nom du fichier.
    """
    for separateur in (" ", "_", "-", "."):
        nom = nom.replace(separateur, "")
    return nom.casefold()


def nom_de_fichier(auteur):
    """« Edgar Allan Poe » -> « Edgar_Allan_Poe.json », la graphie du corpus."""
    return auteur.replace(" ", "_").replace(".", "").replace(",", "") + ".json"


def trouver(auteur):
    """Cherche le fichier .json d'un auteur. Rend None s'il n'y est pas.

    Le nom exact du corpus est essayé d'abord ; à défaut, on compare les noms
    normalisés fichier par fichier, ce qui accepte un séparateur différent.
    """
    chemin = REPERTOIRE / nom_de_fichier(auteur)
    if chemin.exists():
        return chemin
    cible = normaliser(auteur)
    for candidat in sorted(REPERTOIRE.glob("*.json")):
        if normaliser(candidat.stem) == cible:
            return candidat
    return None


def quote(auteur, limit=30):
    """Rend `limit` citations de `auteur`, sous la forme du paquet `quote`.

    Chaque citation est un dictionnaire à trois clés : 'quote' (le texte),
    'book' (le livre d'origine, parfois vide) et 'author'.

    Le corpus est tronqué à `limit`. S'il contient moins de citations que
    demandé, moins en sont rendues — l'API en ligne fait de même.
    """
    chemin = trouver(auteur)
    if chemin is None:
        raise SystemExit(
            f"Corpus hors-ligne sans rien pour {auteur!r}. Les fichiers .json "
            f"doivent se trouver dans {REPERTOIRE} : voir README.md."
        )
    with open(chemin, encoding="utf-8") as fichier:
        donnees = json.load(fichier)
    return donnees[:limit]
