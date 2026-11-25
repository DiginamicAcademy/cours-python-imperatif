[← Chapitre précédent](22-les-differentes-documentations.md) · [Sommaire](Readme.md) · [Chapitre suivant →](24-les-environnements-virtuels.md)

# 23 - Les modules

> Vous savez écrire des fonctions. Un module, c'est le moment où vous acceptez
> qu'elles vivent dans un autre fichier que celui que vous avez sous les yeux —
> et où vous découvrez que quelqu'un a déjà écrit la moitié de ce que vous alliez
> écrire.

**Durée :** ≈ 45 min (lecture ≈ 25 min + atelier 20 min) · **Prérequis :** [Les fonctions](19-les-fonctions.md) et [Les différentes documentations](22-les-differentes-documentations.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Décrire** ce qu'est un module et ce qu'il contient.
- **Distinguer** les modules intégrés des modules personnalisés.
- **Importer** un module entier, sous un alias, ou seulement l'élément dont on a besoin.
- **Installer**, **lister** et **désinstaller** un package avec `pip`.
- **Employer** trois modules intégrés : `math`, `random` et `re`.
- **Écrire** un module de calcul documenté et annoté, puis l'importer dans un autre fichier.

---

## I. Définition de module

Un **module** en Python est un fichier contenant des déclarations et des définitions de fonctions, de classes, de variables et d'instructions. Ces éléments peuvent être réutilisés dans d'autres programmes Python. Les modules sont une manière efficace d'organiser et de structurer le code pour le rendre plus lisible et réutilisable.

> 📓 [Pypi](https://pypi.org) est un site qui propose un catalogue exhaustif des modules créés par la communauté Python afin d'étendre ses fonctionnalités.

---

## II. Les types de modules

Il existe deux types de modules en Python :

1. **Modules intégrés (built-in modules)** : Ce sont des modules intégrés dans Python et disponibles par défaut. Par exemple, le module `math` pour les opérations mathématiques.

2. **Modules personnalisés (user-defined modules)** : Ce sont des modules que vous créez vous-même pour organiser votre code en le divisant en fichiers séparés.

---

## III. Importer un module

### A. L'instruction `import`

Pour utiliser un module dans votre code, vous devez l'importer à l'aide de l'instruction `import`. Par exemple, pour importer le module `math`, vous pouvez faire ceci :

```python
import math
```

### B. Les alias d'import de module

Vous pouvez importer un module sous un alias (un autre nom) en utilisant le mot-clé `as`. Par exemple, pour importer le module `math` sous l'alias `m`, vous pouvez faire ceci :

```python
import math as m
```

### C. Importer uniquement certains éléments d'un module

Si vous n'avez besoin que de certains éléments d'un module, vous pouvez les importer individuellement. Par exemple, pour importer uniquement la fonction `sqrt` du module `math`, vous pouvez faire ceci :

```python
from math import sqrt
```

---

## IV. Obtenir la liste des éléments d'un module

Pour obtenir la liste de tous les éléments d'un module, vous pouvez utiliser la fonction `dir()`. Par exemple, pour afficher la liste des éléments du module `math`, vous pouvez faire ceci :

```python
import math
print(dir(math))
```

---

## V. Installer, lister et désinstaller un package avec `pip`

### A. Installer un package avec `pip`

Cf <https://pypistats.org/top>

Pour installer un package avec pip (le gestionnaire de paquets livré avec Python, qui télécharge depuis PyPI, le catalogue en ligne) sur le terminal, il suffit de rentrer la commande suivante.

```shell
pip install nom_du_package
```

Pour obtenir la liste des modules installés :

```shell
pip list
```

### B. Désinstaller un package

```shell
pip uninstall nom_du_package 
```

---

## VI. Présentation de quelques modules courants

- Le module `math` : Fournit des fonctions mathématiques avancées pour effectuer des opérations mathématiques complexes.
- Le module `random` : Permet de générer des nombres aléatoires.
- Le module `re` (pour les expressions régulières) : Permet de travailler avec des expressions régulières pour la recherche et la manipulation de motifs de texte.

### A. Des exemples avec le module `math`

```python
import math

x = math.factorial(5) # factorielle vu plus tôt
y = math.sqrt(25)  # Racine carrée
z = math.sin(math.pi)  # Sinus

print(x, y, z)
```

| Méthode                                                             | Description                              |
| ------------------------------------------------------------------- | ---------------------------------------- |
| [`sqrt(x)`](https://docs.python.org/3/library/math.html#math.sqrt)  | Calcule la racine carrée de `x`.         |
| [`pow(x, y)`](https://docs.python.org/3/library/math.html#math.pow) | Calcule `x` élevé à la puissance `y`.    |
| [`exp(x)`](https://docs.python.org/3/library/math.html#math.exp)    | Calcule l'exponentielle de `x`.          |
| [`log(x)`](https://docs.python.org/3/library/math.html#math.log)    | Calcule le logarithme naturel de `x`.    |
| [`cos(x)`](https://docs.python.org/3/library/math.html#math.cos)    | Calcule le cosinus de `x` (en radians).  |
| [`sin(x)`](https://docs.python.org/3/library/math.html#math.sin)    | Calcule le sinus de `x` (en radians).    |
| [`tan(x)`](https://docs.python.org/3/library/math.html#math.tan)    | Calcule la tangente de `x` (en radians). |

### B. Des exemples avec le module `random`

```python
import random

num = random.randint(1, 100)  # Génère un nombre aléatoire entre 1 et 100
lst = random.sample(range(1, 50), 5)  # Sélectionne 5 éléments aléatoires dans une liste

print(num, lst)
```

| Méthode                                                                              | Description                                                                      |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| [`random()`](https://docs.python.org/3/library/random.html#random.random)            | Génère un nombre aléatoire à virgule flottante entre 0 (inclus) et 1 (exclus).   |
| [`randint(a, b)`](https://docs.python.org/3/library/random.html#random.randint)      | Génère un nombre aléatoire entier entre `a` (inclus) et `b` (inclus).            |
| [`choice(sequence)`](https://docs.python.org/3/library/random.html#random.choice)    | Sélectionne un élément aléatoire dans une séquence.                              |
| [`shuffle(sequence)`](https://docs.python.org/3/library/random.html#random.shuffle)  | Mélange aléatoirement les éléments d'une séquence.                               |
| [`sample(sequence, k)`](https://docs.python.org/3/library/random.html#random.sample) | Sélectionne `k` éléments uniques aléatoires dans une séquence sans remplacement. |
| [`random.seed()`](https://docs.python.org/3/library/random.html#random.seed)         | Initialise le générateur de nombres aléatoires avec une valeur de départ.        |

### C. Présentation du module `re`

Le module `re` est utilisé pour travailler avec des **expressions régulières** ou **expressions rationnelles**. Les expressions régulières sont des motifs de texte qui permettent de rechercher, de filtrer et de manipuler des chaînes de caractères de manière complexe.

| Méthode                                                                               | Description                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [`re.search(pattern, string)`](https://docs.python.org/3/library/re.html#re.search)   | Recherche la première occurrence de `pattern` dans `string`.              |
| [`re.match(pattern, string)`](https://docs.python.org/3/library/re.html#re.match)     | Vérifie si `string` commence par `pattern`.                               |
| [`re.findall(pattern, string)`](https://docs.python.org/3/library/re.html#re.findall) | Trouve toutes les occurrences de `pattern` dans `string`.                 |
| [`re.sub(pattern, repl, string)`](https://docs.python.org/3/library/re.html#re.sub)   | Remplace les occurrences de `pattern` par `repl` dans `string`.           |
| [`re.compile(pattern)`](https://docs.python.org/3/library/re.html#re.compile)         | Compile un modèle d'expression régulière pour une utilisation ultérieure. |
| [`re.split(pattern, string)`](https://docs.python.org/3/library/re.html#re.split)     | Divise `string` en une liste en utilisant `pattern` comme séparateur.     |

**Expressions régulières**

Les expressions régulières sont des motifs de texte qui permettent de décrire des modèles de caractères. Par exemple, l'expression régulière `\d` correspond à un chiffre. Les expressions régulières sont très puissantes pour rechercher et manipuler des chaînes de caractères.

Les expressions régulières utilisent des **métacaractères** pour définir des modèles. Voici quelques métacaractères courants :

| Métacaractère | Description                                                                      |
| ------------- | -------------------------------------------------------------------------------- |
| `.`           | Correspond à n'importe quel caractère, sauf un saut de ligne.                    |
| `*`           | Correspond à zéro ou plusieurs occurrences du caractère précédent.               |
| `+`           | Correspond à une ou plusieurs occurrences du caractère précédent.                |
| `?`           | Correspond à zéro ou une occurrence du caractère précédent.                      |
| `\`           | Permet d'échapper un métacaractère pour le traiter comme un caractère ordinaire. |
| `[]`          | Permet de spécifier un ensemble de caractères valides.                           |
| `\|`          | Permet de spécifier une alternative.                                             |

---

## VII. Exercices

### Exercice 1 — Créer un module de calcul (~20 min)

1. Créez un module `calcul.py` contenant des fonctions de base pour les opérations mathématiques: addition, soustraction, multiplication, et division. Utilisez des annotations de type et des docstrings pour chaque fonction.

2. Créez un fichier `main.py` qui importe le module `calcul` et utilise ses fonctions. Assurez-vous d'utiliser des annotations de type pour les variables et les fonctions.

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Mes deux fichiers sont dans le **même répertoire**, sinon l'import ne trouve rien.
- [ ] Chaque fonction porte une **annotation de type** sur les paramètres et sur la valeur de retour.
- [ ] Chaque fonction porte une **docstring** décrivant ses paramètres et ce qu'elle renvoie.
- [ ] Ma fonction de division annonce et lève une erreur quand le diviseur vaut zéro.
- [ ] Dans `main.py`, mes **variables** aussi sont annotées.

<details>
<summary>Voir la correction</summary>

`calcul.py` :

```python
"""
Ce module contient des fonctions pour effectuer des opérations mathématiques de base.
"""

def addition(a: int, b: int) -> int:
    """
    Renvoie la somme de deux nombres.

    Args:
        a (int): Le premier nombre.
        b (int): Le deuxième nombre.
    Returns:
        int: La somme des deux nombres.
    """
    return a + b

def soustraction(a: int, b: int) -> int:
    """
    Renvoie la différence entre deux nombres.

    Args:
        a (int): Le premier nombre.
        b (int): Le deuxième nombre.
    Returns:
        int: La différence entre les deux nombres.
    """
    return a - b

def multiplication(a: int, b: int) -> int:
    """
    Renvoie le produit de deux nombres.

    Args:
        a (int): Le premier nombre.
        b (int): Le deuxième nombre.
    Returns:
        int: Le produit des deux nombres.
    """
    return a * b

def division(a: int, b: int) -> float:
    """
    Renvoie le quotient de la division de deux nombres.

    Args:
        a (int): Le dividende.
        b (int): Le diviseur.

    Returns:
        float: Le quotient de la division.

    Raises:
        ZeroDivisionError: Si le diviseur est égal à zéro.
    """
    if b == 0:
        raise ZeroDivisionError("Impossible de diviser par zéro.")
    return a / b
```

`main.py` :

```python
from calcul import addition, soustraction, multiplication, division

x: int = 10
y: int = 5

somme: int = addition(x, y)
difference: int = soustraction(x, y)
produit: int = multiplication(x, y)
quotient: float = division(x, y)

print(f"{x} + {y} = {somme}")
print(f"{x} - {y} = {difference}")
print(f"{x} * {y} = {produit}")
print(f"{x} / {y} = {quotient}")
```

L'exercice referme le cours sur un objet complet : des fonctions (chapitre 19), leurs annotations de type (chapitre 21), leurs docstrings (chapitre 22), le tout rangé dans un module importable (chapitre 23).

</details>

---

## Points clés

- Un module est un **fichier** de déclarations et de définitions (fonctions, classes, variables, instructions), réutilisables dans d'autres programmes Python.
- Deux origines : les modules **intégrés**, disponibles par défaut, et les modules **personnalisés**, que vous écrivez pour découper votre propre code.
- `import math` amène le module et impose le préfixe `math.` ; `import math as m` change ce préfixe en `m.` ; `from math import sqrt` amène la fonction seule, sans préfixe.
- `dir(math)` liste les éléments d'un module : c'est le réflexe à avoir quand on découvre un module inconnu.
- `pip install`, `pip list` et `pip uninstall` sont les trois commandes de gestion des packages, qui proviennent du PyPI (Python Package Index).
- `math`, `random` et `re` sont trois modules intégrés : calcul, aléatoire, expressions régulières.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Un fichier `.py` que vous avez écrit vous-même pour découper votre projet en morceaux est quel type de module ?

- A. Un module intégré, puisque Python le trouve sans installation
- B. Un module personnalisé, que vous créez pour organiser votre code en fichiers séparés
- C. Un package, seul nom possible dès qu'on écrit soi-même le fichier
- D. Une bibliothèque, le fichier étant par définition réutilisable par d'autres programmes

**2.** On écrit `import math as m`. Comment calculer la racine carrée de 25 ?

- A. `math.sqrt(25)`, le préfixe réel du module ne changeant pas avec l'alias
- B. `m.sqrt(25)`, l'alias `as` remplaçant le préfixe du module
- C. `sqrt(25)`, l'alias amenant la fonction directement dans l'espace de noms
- D. `m(25)`, l'alias se substituant à la fonction cherchée

**3.** Avec `from math import sqrt`, comment appelle-t-on la racine carrée ?

- A. `sqrt(25)`, l'élément importé individuellement s'appelant sans préfixe
- B. `math.sqrt(25)`, `from` conservant le préfixe du module d'origine
- C. `dir(25)`, l'élément importé n'étant accessible que par son nom complet
- D. `import.sqrt(25)`, l'instruction servant alors de préfixe permanent

**4.** Vous voulez savoir quels modules sont déjà présents sur la machine. Quelle commande est la bonne ?

- A. `dir(math)`, qui liste tout ce que la machine contient
- B. `pip list`, qui dresse la liste des modules installés
- C. `pip install nom_du_package`, qui affiche le catalogue du PyPI
- D. `import math`, qui renvoie la liste des modules intégrés

**5.** *Question ouverte (2-3 lignes).* Un collègue vous demande où aller chercher un module ajouté par la communauté Python, et comment vérifier qu'il est bien installé sur son poste avant de l'importer. Que lui répondez-vous, en vous appuyant sur le chapitre ?

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. B.** Deux types seulement sont recensés : intégrés (built-in), disponibles par défaut, et personnalisés (user-defined), que vous créez pour diviser votre code en fichiers séparés.
**Pourquoi :** c'est la définition donnée au début du chapitre, et `math` est l'exemple cité de module intégré.

**2. B.** `as` renomme le module à l'import : le préfixe devient `m`, donc `m.sqrt(25)`.
**Pourquoi :** le chapitre écrit qu'on peut importer un module « sous un alias (un autre nom) », et `import math as m` est l'exemple donné.

**3. A.** Quand on n'importe que `sqrt`, cet élément est directement nommé, sans préfixe de module.
**Pourquoi :** `from math import sqrt` est précisément l'écriture pour « certains éléments seulement » d'un module.

**4. B.** `pip list` donne la liste des modules installés.
**Pourquoi :** le chapitre la présente après la commande d'installation ; `dir()`, lui, liste les éléments **d'un module donné**, pas les modules de la machine.

**5.** Attendu : le catalogue des modules créés par la communauté Python est le site Pypi (PyPI, Python Package Index), que l'on peut parcourir aussi via pypistats pour voir les plus utilisés ; on vérifie la présence locale avec `pip list`, et on installe avec `pip install nom_du_package`.
**Pourquoi :** la note d'ouverture du chapitre décrit Pypi comme le catalogue exhaustif des modules communautaires, et la section sur `pip` donne les trois commandes d'installation, de listing et de désinstallation.

</details>

---

[← Chapitre précédent](22-les-differentes-documentations.md) · [Sommaire](Readme.md) · [Chapitre suivant →](24-les-environnements-virtuels.md)
