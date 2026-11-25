<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/Logo-diginamic-color-blk.png">
    <img src="assets/Logo-diginamic-color.svg" alt="Diginamic Formation" width="358">
  </picture>
</p>

# Python impératif — les fondamentaux

> Apprendre à programmer avec **Python**, dans l'approche impérative · **RNCP37873** Concepteur développeur d'applications
> 2 jours de parcours · **aucun prérequis** en programmation

---

## Pourquoi ce cours

Programmer, c'est écrire à la machine une suite d'instructions assez claire pour qu'elle les exécute sans qu'on ait à la relire. Ce cours prend le temps de poser cette idée brique par brique : ranger des valeurs dans des variables, les transformer, décider, répéter, regrouper dans des fonctions — puis garder chaque projet dans son propre environnement Python.

On commence vraiment de zéro. Le chapitre 00.1 montre les deux façons d'organiser un programme — à l'impérative, à l'objets — pour situer ce qu'on apprend ici ; le 00.2 explique pourquoi Python ; le 00.3 installe le poste de travail et fait tourner votre premier script. Ensuite, chaque chapitre est court, manuel, et se termine par des ateliers dont la correction se déplie sous l'énoncé : rien ne vous oblige à attendre quelqu'un pour savoir si vous avez bon.

Le cours se clôt sur un travail de bout en bout : deux jeux de données réels à exploiter avec ce que vous avez vu, des citations littéraires et les passagers du Titanic. C'est là que les chapitres cessent d'être des exercices.

---

## À l'issue de ce cours

Vous serez capable de :

- **Écrire** des scripts Python qui lisent des valeurs, les transforment et les affichent correctement.
- **Choisir** le type qui convient à une donnée : chaîne, nombre, booléen, liste, tuple, dictionnaire, set.
- **Expliquer** ce que devient une variable quand on la passe à une fonction, selon qu'elle est muable ou immuable.
- **Formater** du texte avec les méthodes de chaînes et les littéraux de formatage (`f-strings`).
- **Traduire** un énoncé en conditions et en boucles, en évitant les pièges classiques (`break`, `continue`, boucle qui ne s'arrête jamais).
- **Découper** un programme en fonctions lisibles, avec arguments par défaut, `*args`, `**kwargs` et annotations de type.
- **Mobiliser** les modules standards, lire une documentation et installer un paquet tiers dans un environnement virtuel.
- **Mener** seul une analyse de données de l'ingestion au résultat affiché.

---

## Prérequis

- **Aucun prérequis en programmation.** Ni algorithme, ni autre langage, ni mathématiques au-delà du collège.
- **Python 3.11 ou plus récent.** C'est le minimum que demande le TP de fin de cours (dictionnaires ordonnés, annotations `X | Y`). Le chapitre [00.3](00-03-installation-du-poste-de-travail.md) installe la bonne version.
- **VS Code recommandé**, parce que les captures d'écran du cours le montrent ; n'importe quel éditeur de texte convient.
- **Droits d'installation de logiciels** sur la machine, et un accès réseau pour le TP (`pip install quote certifi`) — à défaut, le repli hors-ligne est fourni dans le dossier `tp/`.

---

## Comment suivre ce cours

Le découpage en deux journées est **une proposition de parcours, pas un horaire imposé** : les supports se parcourent à votre rythme, et les durées ci-dessous sont celles annoncées en tête de chaque chapitre (lecture, atelier et réflexion compris).

| Parcours | Chapitres | Volume annoncé |
| --- | --- | --- |
| Journée 1 | [00.1](00-01-deux-paradigmes-programmation.md) à [13](13-les-objets-muables-et-immuables.md) | ≈ 340 min, + 20 min d'extensions facultatives |
| Journée 2 | [14](14-les-listes.md) à [24](24-les-environnements-virtuels.md) | ≈ 355 min, + 14 min d'extensions facultatives |
| TP de fin de cours | [TP-01 - Analyser deux jeux de données](tp/TP-01-analyse-donnees.md) | ≈ 2 h, + ≈ 45 min d'approfondissement, en dehors des journées |

La première journée pose les données et la logique : types, chaînes, nombres, conditions. La deuxième organise le code : collections, boucles, fonctions, documentations, modules et environnements virtuels — le chapitre 24 ouvre directement ce qu'il faut pour attaquer le TP. Le TP se fait hors temps de présence, en individuel, et se rend pour notation.

---

## Sommaire

### Journée conseillée 1 — des données aux conditions

| # | Chapitre | Durée |
| --- | --- | --- |
| 00.1 | [Deux paradigmes : impératif et objet](00-01-deux-paradigmes-programmation.md) | 15 min |
| 00.2 | [Introduction à Python](00-02-introduction-a-python.md) | 10 min |
| 00.3 | [Installation du poste de travail](00-03-installation-du-poste-de-travail.md) | 30 min |
| 01 | [Les variables](01-les-variables.md) | 20 min |
| 02 | [Les chaînes de caractères](02-les-chaines-de-caracteres.md) | 15 min |
| 03 | [Les nombres](03-les-nombres.md) | 10 min |
| 04 | [Les booléens](04-les-booleens.md) | 10 min |
| 05 | [Les variables, notions plus avancées](05-variables-notions-plus-avancees.md) | 25 min |
| 06 | [Les constructeurs de types](06-les-constructeurs-de-types.md) | 15 min |
| 07 | [Intéragir avec l'utilisateur](07-interaction-avec-lutilisateur.md) | 10 min |
| 08 | [Les méthodes de chaînes de caractères](08-les-methodes-de-chaines-de-caracteres.md) | 35 min |
| 09 | [Les opérateurs mathématiques](09-les-operateurs-mathematiques.md) | 30 min |
| 10 | [Formatter les chaînes de caractères](10-formatter-les-chaines-de-caracteres.md) | 30 min |
| 11 | [Les structures conditionnelles](11-les-structures-conditionnelles.md) | 40 min (+ 12 fac.) |
| 12 | [Les modules standards de Python](12-les-modules-standards-de-python.md) | 30 min (+ 8 fac.) |
| 13 | [Les objets muables et immuables](13-les-objets-muables-et-immuables.md) | 15 min |

**Total ≈ 340 min** de lecture et d'ateliers, extensions facultatives non comptées.

### Journée conseillée 2 — collections, fonctions, projets

| # | Chapitre | Durée |
| --- | --- | --- |
| 14 | [Les listes](14-les-listes.md) | 45 min |
| 15 | [Les tuples](15-les-tuples.md) | 20 min (+ 6 fac.) |
| 16 | [Les boucles](16-les-boucles.md) | 55 min (+ 8 fac.) |
| 17 | [Les dictionnaires](17-les-dictionnaires.md) | 35 min |
| 18 | [Les sets](18-les-sets.md) | 15 min |
| 19 | [Les fonctions](19-les-fonctions.md) | 45 min |
| 20 | [Les arguments flexibles](20-les-arguments-flexibles.md) | 25 min |
| 21 | [Les annotations de type](21-les-annotations-de-type.md) | 20 min |
| 22 | [Les différentes documentations](22-les-differentes-documentations.md) | 20 min |
| 23 | [Les modules](23-les-modules.md) | 45 min |
| 24 | [Les environnements virtuels](24-les-environnements-virtuels.md) | 30 min |

**Total ≈ 355 min**, extensions facultatives non comptées.

### Et après les chapitres

| | Support | Durée |
| --- | --- | --- |
| 📁 | [Travaux pratiques — mode d'emploi](tp/README.md) | à lire avant le TP |
| 🔴 | [TP-01 - Analyser deux jeux de données](tp/TP-01-analyse-donnees.md) | ≈ 2 h + ≈ 45 min de bonus |
| 📖 | [Glossaire et ressources](A-Glossaire-et-ressources.md) | annexe, à consulter |

---

## Organisation du support

- **Les chapitres sont à la racine du dépôt, dans l'ordre de lecture.** Chacun s'appuie sur la base laissée par le précédent : les suivre dans l'ordre est ce qui fait que rien ne manque.
- **Chaque chapitre suit la même trame** : objectifs, le cours lui-même avec ses ateliers, « Points clés », puis « Vérifiez vos acquis ». Les exercices portent un titre « Exercice N — … » et leur correction se déplie juste en dessous (« Voir la correction ») : ils sont là pour s'entraîner, pas pour être notés.
- **Le dossier `tp/`** garde le TP de fin de cours : [l'énoncé](tp/TP-01-analyse-donnees.md), les données dans `tp/data/` (`titanic_survival.csv`), et le [corpus de citations hors-ligne](tp/citations-hors-ligne/README.md) qui remplace le service en ligne quand le réseau manque. Son [mode d'emploi](tp/README.md) dit quoi rendre et depuis quel dossier travailler.
- **Le glossaire** [A - Glossaire et ressources](A-Glossaire-et-ressources.md) rassemble sigles, termes et documentation officielle. Chaque terme y est renvoyé au chapitre où on le manipule.
- **Le support PDF est reconstitué automatiquement** à chaque version du dépôt, à partir de ce Readme et des chapitres, dans le même ordre que le sommaire : c'est la release qui porte le document à imprimer.
