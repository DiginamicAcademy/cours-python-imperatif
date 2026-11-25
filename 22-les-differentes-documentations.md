[← Chapitre précédent](21-les-annotations-de-type.md) · [Sommaire](Readme.md) · [Chapitre suivant →](23-les-modules.md)

# 22 - Les différentes documentations

> Un code qui marche ne suffit pas : il faut qu'il se lise, par votre futur vous
> comme par le collègue qui le reprendra. Il existe plusieurs niveaux de
> documentation en Python, du commentaire posé sur une ligne jusqu'au document
> généré tout seul à partir du fichier source. Ce chapitre les range.

**Durée :** ≈ 20 min (lecture ≈ 15 min + réflexion) · **Prérequis :** [Les fonctions](19-les-fonctions.md) et [Les annotations de type](21-les-annotations-de-type.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Distinguer** un commentaire d'une docstring, et dire qui lit chacun d'eux.
- **Écrire** une docstring de fonction exploitable par une génération automatique de documentation.
- **Placer** la documentation d'un module, d'une classe et d'une variable au bon endroit.
- **Reconnaître** une structure de fichier documentée dans un projet professionnel.

---

## I. La documentation en Python

La documentation est un moyen de communication clé de la programmation, car elle rend votre code plus lisible, facilite la collaboration et permet aux autres développeurs de comprendre et d'utiliser votre code.

La documentation en Python est essentielle pour expliquer le but, le fonctionnement et l'utilisation des modules, des fonctions, des classes et des variables.

Il existe plusieurs types de documentation couramment utilisés pour rendre le code plus compréhensible et accessible.

Elle est également utile pour générer automatiquement des documentations conviviales pour les utilisateurs de vos bibliothèques et modules.

---

## II. Les commentaires

Les commentaires sont le moyen le plus simple de documenter votre code. Ils sont destinés aux développeurs qui lisent le code source et ne sont pas inclus dans la documentation générée automatiquement.

```python
# Ceci est un commentaire simple
```

---

## III. Les docstrings

Les docstrings sont des chaînes de caractères incluses dans le code source qui décrivent une fonction, une classe, un module ou une variable. Elles sont utilisées pour générer une documentation automatique.

### A. Docstring d'une fonction

La documentation de fonction est utilisée pour décrire les fonctions et leurs paramètres. Elle est généralement placée sous la signature de la fonction.

```python
def addition(a, b):
    """
    Cette fonction renvoie la somme de deux nombres.

    Args:
        a (int): Le premier nombre.
        b (int): Le deuxième nombre.

    Returns:
        int: La somme des deux nombres.
    """
    return a + b
```

### B. Docstring d'un module

La documentation de module est généralement placée au début d'un fichier de code et décrit le contenu, le but et l'utilisation du module.

```python
"""
Ce module contient des fonctions pour effectuer des opérations mathématiques de base.
"""

def addition(a, b):
    return a + b
```

### C. Docstring d'une classe

La documentation de classe est utilisée pour décrire les classes et leurs méthodes.

```python
class Personne:
    """
    Cette classe représente une personne avec un nom et un âge.
    """

    def __init__(self, nom, age):
        """
        Initialise une nouvelle instance de la classe Personne.

        Args:
            nom (str): Le nom de la personne.
            age (int): L'âge de la personne.
        """
        self.nom = nom
        self.age = age
```

La documentation d'une méthode s'ajoute donc à celle de la classe qui l'accueille : les deux docstrings ci-dessus coexistent dans le même fichier. La classe elle-même n'est pas encore au programme de ce cours : lisez cet exemple comme une illustration de la place de chaque docstring.

### D. Une fonction qui peut échouer

La docstring sert aussi à annoncer ce que la fonction refuse, et ce que le code qui l'appelle devra traiter.

```python
def division(dividende, diviseur):
    """
    Cette fonction renvoie le résultat de la division.

    Args:
        dividende (float): Le nombre à diviser.
        diviseur (float): Le nombre par lequel diviser.

    Returns:
        float: Le résultat de la division.

    Raises:
        ZeroDivisionError: Si le diviseur est égal à zéro.
    """
    if diviseur == 0:
        raise ZeroDivisionError("Impossible de diviser par zéro.")
    return dividende / diviseur
```

---

## IV. Documenter une variable

La documentation de variable est utilisée pour expliquer le but d'une variable, en particulier lorsqu'elle n'est pas évidente.

```python
nombre_de_clients: int = 100  # Le nombre total de clients dans la base de données
```

---

## V. Les annotations de type comme documentation

Bien que ce ne soit pas une forme de documentation explicite, l'annotation de type est également un moyen de documenter le code en indiquant le type attendu des paramètres et des valeurs de retour des fonctions.

```python
def addition(a: int, b: int) -> int:
    return a + b
```

C'est le sujet du [chapitre précédent](21-les-annotations-de-type.md) : les deux pratiques se cumulent, une docstring explique le **quoi**, l'annotation rappelle le **type**.

---

## VI. Structure de documentation de fichier

Les `${variable}` représentent les informations à changer.

Il est possible de faire un fichier de configuration `.env` à la racine du projet pour chaque personne qui travaille sur le projet et d'importer les informations.

Exemple de fichier qui récupère les informations issues du `.env`

```python
"""
Titre : Documentation fichier Python
Nom du projet : ${PROJECT_NAME}

Nom du fichier : ${NAME}

Date de la dernière révision : ${MONTH_NAME_FULL},${YEAR},${MONTH},${DAY},${TIME}

Auteur(s) : Prenom NOM
Auteur(s) : ${USER}

IDE utilisé : ${PRODUCT_NAME}

Client : e-learning

#-------------------------------------------------

name='$Package_name',
    version='$Version',
    packages=$PackageList,$PackageDirs
    url='$URL',
    license='$License',
    author='$Author',
    author_email='$Author_Email',
    description='$Description'

#-------------------------------------------------

Fichiers du projet :
                    -   Lab1_4.py
"""

# Indispensable hors contexte de PyCharm->en bas à droite
# -*- coding:Utf-8 -*-

################################################
#               Programme principal
################################################

#-----------------------------------------------
#           Zone des 'imports' de modules
#-----------------------------------------------

import pandas as pd

#----------------------------------------------------
#       Zone de déclaration des variables 'globales'
#----------------------------------------------------

ma_variable = 4

#-------------------------------------------------------
#       Zone de déclaration des modules ou des fonctions
#-------------------------------------------------------

def calcul...

#-------------------------------------------------------
#                       PROGRAMME
#-------------------------------------------------------


```

Ce gabarit est un modèle de début de fichier, pas un programme : la ligne `def calcul...` marque l'emplacement où l'écrivain du fichier déclarera ses fonctions, et les `${...}` sont des champs à remplacer (ou à remplir automatiquement par l'éditeur) à la création de chaque fichier.

---

## Points clés

- Un commentaire s'adresse à qui **lit le code** ; il ne participe pas à la documentation générée automatiquement.
- Une docstring est une **chaîne placée dans le code source** — en tête de module, sous la signature d'une fonction, sous l'en-tête d'une classe — et elle sert à la documentation automatique.
- Une docstring de fonction complète annonce les `Args`, le `Returns` et les `Raises`.
- Une variable peu évidente se documente d'un commentaire en fin de ligne, à côté de son annotation de type.
- Les annotations de type documentent sans être de la documentation explicite : elles indiquent le type attendu, pas l'intention.
- Un gabarit de fichier (nom du projet, auteur, date, zones d'imports et de variables) se remplit à la création du fichier.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Quelle est la différence entre un commentaire et une docstring ?

- A. Le commentaire s'adresse aux développeurs qui lisent le source et n'est pas repris par la génération automatique, la docstring si
- B. La docstring est exécutée par l'interpréteur, le commentaire est ignoré par lui
- C. Le commentaire documente une variable, la docstring documente uniquement les classes
- D. La docstring remplace le nom de la fonction, le commentaire remplace le nom du module

**2.** Où se place la documentation d'un module ?

- A. Dans un fichier `README` déposé à côté du code, et nulle part dans le fichier source
- B. Au début du fichier de code, sous forme de chaîne de caractères
- C. Sous la signature de chacune des fonctions du module
- D. À la fin du fichier, pour ne pas gêner la lecture des instructions

**3.** Que trouve-t-on typiquement dans la docstring de `division()` donnée en exemple ?

- A. Le type des variables globales employées par le module entier
- B. Uniquement la description en une phrase, sans détail sur les paramètres
- C. Les `Args`, le `Returns` et les `Raises` de la fonction
- D. La liste des fichiers du projet et le nom de son auteur

**4.** Dans `def calcul...` du gabarit de fichier, que désignent les trois points ?

- A. Une instruction Python qui ne retourne rien, comme `pass`
- B. Une fonction que le module `pandas` importe automatiquement
- C. Un champ à compléter par l'auteur, la ligne n'étant pas du code exécutable
- D. Une erreur de syntaxe que l'éditeur corrige à l'enregistrement

**5.** *Question ouverte (2-3 lignes).* Vous reprenez le fichier d'un collègue : une fonction de trente lignes est suivie d'un commentaire `# vérifie les âges`, et une variable `n = 0` apparaît sans explication. Quels niveaux de documentation du chapitre font défaut, et lequel vous aurait renseigné le premier ?

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. A.** Le commentaire est destiné aux lecteurs du code source et reste hors de la documentation générée ; la docstring, chaîne incluse dans le code source, sert à la générer.
**Pourquoi :** c'est la distinction posée par le chapitre, et c'est ce qui rend les docstrings réutilisables par les outils de documentation conviviales destinées aux utilisateurs d'une bibliothèque.

**2. B.** La documentation de module se place au début du fichier de code.
**Pourquoi :** elle décrit alors le contenu, le but et l'utilisation du module, comme l'illustre l'exemple « Ce module contient des fonctions pour effectuer des opérations mathématiques de base ».

**3. C.** La docstring de `division()` détaille les paramètres (`Args`), la valeur renvoyée (`Returns`) et l'erreur levée (`Raises`).
**Pourquoi :** `Raises: ZeroDivisionError` est précisément ce qui manque à une docstring qui ne ferait que décrire la fonction en une phrase.

**4. C.** Le gabarit de fichier est un modèle, pas un programme : `def calcul...` marque l'emplacement réservé à la déclaration des fonctions.
**Pourquoi :** le chapitre introduit ce bloc comme un « exemple de fichier », avec des `${variable}` à changer ; rien dans ce bloc n'est censé s'exécuter tel quel.

**5.** Attendu : la docstring de fonction (qui eût décrit le rôle, les paramètres et les cas refusés) et, pour la variable, un commentaire de fin de ligne expliquant son but ; le premier renseigné est la docstring, lue par les outils et affichée par l'éditeur.
**Pourquoi :** le chapitre réserve les commentaires aux détails de lecture du source et les docstrings à la description du but et de l'utilisation — donc à ce que l'on consulte en premier quand on appelle une fonction sans ouvrir son code.

</details>

---

[← Chapitre précédent](21-les-annotations-de-type.md) · [Sommaire](Readme.md) · [Chapitre suivant →](23-les-modules.md)
