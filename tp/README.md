# Travaux pratiques — mode d'emploi

Les exercices du cours **se trouvent dans les chapitres**, à l'endroit du cours qui enseigne la notion qu'ils pratiquent. Chacun porte un titre de la forme « Exercice N — … », et sa correction se déplie sous l'énoncé avec « Voir la correction ». Il n'y a donc rien à ouvrir ici pour travailler : on suit le chapitre.

Ce dossier garde le **TP de fin de cours**, qui porte sur l'ensemble du programme. Il est **noté**, et sa correction n'est pas publiée.

## Contenu du dossier

| Élément | Détail |
| --- | --- |
| [TP-01-analyse-donnees.md](TP-01-analyse-donnees.md) | l'énoncé du TP : deux jeux de données à exploiter, ≈ 2 h + un approfondissement |
| `data/titanic_survival.csv` | les 14 colonnes des passagers du Titanic, données du TP |
| [`citations-hors-ligne/`](citations-hors-ligne/README.md) | le corpus de citations qui remplace le module en ligne quand le réseau manque |

## Comment travailler

1. L'énoncé se lit en entier avant d'écrire la première ligne : les contraintes de forme comptent autant que les résultats.
2. On travaille **depuis ce dossier** : c'est là que les programmes trouvent `data/` et le corpus de citations.
3. Environnement virtuel conseillé, comme au chapitre 24 : le TP installe des paquets, autant ne pas les déverser dans l'installation partagée.
4. Les fichiers à rendre sont nommés dans l'énoncé : `citations.py`, `titanic.py`, et `auteurs.py` avec `classement_the.csv` pour l'approfondissement.

## Où puiser dans le cours

Les rappels de chapitres utiles sont renvoyés un par un en pied d'énoncé. Les deux gestes que ce cours n'a pas enseignés — ouvrir un fichier, lire un CSV (Comma-Separated Values) — sont expliqués dans l'énoncé lui-même, en une demi-page.
