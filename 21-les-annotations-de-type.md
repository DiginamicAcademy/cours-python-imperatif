[← Chapitre précédent](20-les-arguments-flexibles.md) · [Sommaire](Readme.md) · [Chapitre suivant →](22-les-differentes-documentations.md)

# 21 - Les annotations de type

> Python ne demande jamais « quel type est cette variable ? » avant de l'exécuter.
> Les annotations de type consistent à le lui dire quand même, pour que l'éditeur
> et vos collègues le sachent avant le premier appel. Ce chapitre n'ajoute aucune
> notion nouvelle à manipuler : seulement une manière d'écrire ce que l'on sait
> déjà.

**Durée :** ≈ 20 min (lecture ≈ 15 min + réflexion) · **Prérequis :** [Les fonctions](19-les-fonctions.md) et [Les variables](01-les-variables.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Expliquer** ce qu'une annotation de type change — et ce qu'elle ne change pas — à l'exécution d'un programme.
- **Annoter** une variable, un paramètre et une valeur de retour.
- **Annoncer** plusieurs types possibles pour une même valeur.
- **Annoter** des collections et des objets de classe.

---

## I. Introduction

Python étant un langage **interprété**, il est typé dynamiquement. Ce qui signifie que les types sont associés aux valeurs au moment de l'exécution, mais l'annotation de type permet d'introduire une forme de typage statique facultatif pour améliorer la qualité et la lisibilité du code. Cette pratique augmente considérablement la qualité et la lisibilité de votre code, et est donc une pratique répandue en milieu professionnel.

Les types sont associés aux variables, aux paramètres de fonction et aux valeurs de retour.

```python
# On précise ici qu'on attend deux integers, et que la fonction retourne un integer
def add(a: int, b: int) -> int:
    return a + b

x: int = 4
y: int = 8
z: str = "coucou"

print(add(x, y))
print(add(x, z)) # soulèvera une erreur explicite
```

L'annotation n'affecte pas l'exécution du code, mais elle peut être utilisée par des outils (comme le greffon SonarLint dans un éditeur de code) et des IDE (Integrated Development Environment, un environnement de développement) pour détecter des erreurs potentielles et améliorer la documentation du code. Elle permet aussi de profiter de l'auto-complétion dans la plupart des IDE modernes, facilitant grandement le développement et empêchant un bon nombre de bugs.

---

## II. Les nouveautés de la 3.10

Depuis la version 3.10, les annotations de types ont été améliorées.

```python
# Synthaxe avant 3.10
from typing import Union
ma_liste: list[Union[int, str]] = [2, "coucou", 1, 76, "test"]

# 3.10: choisir plusieurs types possibles avec l'opérateur | (pipe)
ma_liste: list[int | str] = [2, "coucou", 1, 76, "test"]

# Aliasing de type
Nombre = int | float 

def addition(a: Nombre, b: Nombre) -> Nombre: 
    return a + b
```

---

## III. Les annotations usuelles

### A. Entiers (`int`)

```python
age: int = 25
```

### B. Flottants (`float`)

```python
prix: float = 10.99
```

### C. Chaînes de caractères (`str`)

```python
nom: str = "Alice"
```

### D. Booléens (`bool`)

```python
est_actif: bool = True
```

### E. Listes

```python
from typing import List

nombres: List[int] = [1, 2, 3]
```

### F. Tuples

```python
from typing import Tuple

coordonnees: Tuple[float, float] = (2.5, 3.0)
```

### G. Dictionnaires

```python
from typing import Dict

informations: Dict[str, str] = {"nom": "Bob", "ville": "Paris"}
```

### H. Paramètres et retours de fonctions

```python
def ajouter(a: int, b: int) -> int:
    return a + b
```

### I. Paramètres optionnels

```python
from typing import Optional

def afficher_message(age: int, nom: Optional[str] = None) -> None:
    if nom:
        print(f"{nom} a {age} ans.")
    else:
        print(f"Cet individu a {age} ans.")
```

### J. Objets personnalisés

Si vous avez défini une classe, vous pouvez indiquer le type de l'objet qui sera créé à partir de cette classe.

```python
class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age
```

Vous pouvez annoter le type de l'objet créé avec cette classe comme suit :

```python
def creer_personne(nom: str, age: int) -> Personne:
    return Personne(nom, age)
```

La classe n'est pas encore étudiée dans ce cours : l'exemple sert seulement à montrer qu'un nom de classe est une annotation comme une autre. Vous le retrouverez en détail dans le cours consacré à la programmation orientée objet.

---

## Points clés

- Une annotation de type est **facultative et sans effet à l'exécution** : elle documente et arme les outils, elle ne corrige rien par elle-même.
- Elle se place sur les variables (`x: int = 4`), les paramètres (`a: int`) et la valeur de retour (`-> int`).
- Depuis Python 3.10, `int | str` annonce « l'un ou l'autre », sans passer par `Union` ; on peut donner un nom à ce couple (`Nombre = int | float`).
- Une collection annotée indique aussi son contenu : `List[int]`, `Tuple[float, float]`, `Dict[str, str]` — ou leurs équivalents en minuscules `list[int]`, `tuple[...]`, `dict[...]`.
- `Optional[str]` annonce « une chaîne, ou `None` » ; `-> None` annonce une fonction qui ne retourne rien d'exploitable.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Qu'est-ce qu'une annotation de type apporte à un programme Python ?

- A. Une vérification systématique des types à chaque exécution, qui remplace les tests unitaires
- B. Une forme de typage statique facultatif, lisible par les outils et les IDE, sans effet sur l'exécution
- C. Une accélération de l'exécution, l'interpréteur n'ayant plus besoin de deviner les types
- D. Une obligation syntaxique, toute variable devant désormais déclarer son type

**2.** Comment annoncer, depuis Python 3.10, qu'une variable peut contenir un entier ou une chaîne ?

- A. `ma_liste: int or str`
- B. `ma_liste: [int, str]`
- C. `ma_liste: int | str`
- D. `ma_liste: Optional[int, str]`

**3.** Que signifie `-> None` dans la signature `def afficher_message(age: int, nom: Optional[str] = None) -> None:` ?

- A. Que la fonction ne retourne aucune valeur exploitable, `None` étant la valeur du rien
- B. Que la fonction peut lever une erreur, qu'il faudra intercepter
- C. Que le paramètre `nom` est obligatoire et ne peut pas valoir `None`
- D. Que la fonction retourne une chaîne vide quand aucun nom n'est passé

**4.** Quelle annotation annonce un dictionnaire dont les clés et les valeurs sont des chaînes de caractères ?

- A. `informations: Dict = str`
- B. `informations: Dict[str, str]`
- C. `informations: Dict[str] -> str`
- D. `informations: str | str`

**5.** *Question ouverte (2-3 lignes).* Le chapitre affirme à la fois que l'annotation « n'affecte pas l'exécution » et qu'elle « empêche un bon nombre de bugs ». Comment ces deux phrases sont-elles conciliables ?

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. B.** L'annotation introduit un typage statique facultatif : elle sert aux outils et aux lectureurs du code, pas à l'interpréteur.
**Pourquoi :** le chapitre est explicite, « elle n'affecte pas l'exécution du code » ; c'est justement ce qui la distingue d'un typage imposé.

**2. C.** Depuis la 3.10, l'opérateur `|` (pipe) annonce plusieurs types possibles : `list[int | str]`.
**Pourquoi :** c'est la version moderne de `list[Union[int, str]]`, qui était l'écriture précédente ; on peut en plus lui donner un nom avec un alias de type.

**3. A.** `-> None` annonce que la fonction ne retourne rien d'exploitable ; `Optional[str]` dit de son côté que `nom` peut être une chaîne ou `None`.
**Pourquoi :** le chapitre a vu qu'une fonction sans `return` retourne `None`, la valeur du rien — l'annotation ne fait que l'écrire noir sur blanc.

**4. B.** `Dict[str, str]` précise le type des clés puis celui des valeurs, comme `List[int]` précise le type des éléments d'une liste.
**Pourquoi :** une collection annotée indique son contenu entre crochets ; `Dict` seul n'annonce rien de ce que le dictionnaire transporte.

**5.** Attendu : l'annotation n'est pas vérifiée à l'exécution, mais elle est lue par les outils et l'éditeur, qui signalent l'incohérence **avant** l'exécution.
**Pourquoi :** le chapitre cite SonarLint et les IDE, capables de détecter les erreurs potentielles et de proposer l'auto-complétion ; le bug est donc repéré pendant l'écriture, pas par le programme lui-même.

</details>

---

[← Chapitre précédent](20-les-arguments-flexibles.md) · [Sommaire](Readme.md) · [Chapitre suivant →](22-les-differentes-documentations.md)
