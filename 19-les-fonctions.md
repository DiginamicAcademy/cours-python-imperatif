[← Chapitre précédent](18-les-sets.md) · [Sommaire](Readme.md) · [Chapitre suivant →](20-les-arguments-flexibles.md)

# 19 - Les fonctions

> Jusqu'ici vous donniez vos instructions à l'ordinateur, ligne par ligne. Une
> fonction, c'est un morceau de code que vous nommez une fois pour l'appeler
> autant de fois que vous voulez — et que vous pouvez oublier une fois écrit.
> Tout le reste du cours, et tout programme un peu honnête, repose dessus.

**Durée :** ≈ 45 min (lecture ≈ 20 min + atelier 15 min + réflexion) · **Prérequis :** [Les variables](01-les-variables.md), [Les listes](14-les-listes.md) et [Les boucles](16-les-boucles.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Distinguer** la définition d'une fonction et son appel.
- **Utiliser** `return` et dire ce que retourne une fonction qui n'en contient pas.
- **Déclarer** des paramètres obligatoires et des paramètres par défaut, dans le bon ordre.
- **Expliquer** ce que l'espace local d'une fonction voit de l'espace global, et l'inverse.
- **Écrire** une fonction récursive à partir d'un exemple.

---

## I. Définitions

Les fonctions sont des **instructions préalablement définies** et qui s'appliqueront dans le code lorsque la fonction sera **appelée**.

Tout comme pour la création d'une variable (voir [le chapitre sur les variables](01-les-variables.md)), le cycle de vie d'une fonction se constitue de plusieurs étapes.

- **Définition de la fonction** : le code de la fonction est défini, en précisant ses éventuels paramètres, le code que la fonction exécute, ainsi que son éventuelle valeur de retour. Ce code est complètement isolé de l'extérieur.
- **Appel de la fonction** : le moment où le code préalablement défini par la fonction est exécuté et a un impact dans le fonctionnement du script.

```python
# Définition de la fonction
def add(a, b):
    return a + b

# Appel de la fonction
result = add(2, 3)
print(result)
```

---

## II. Le mot clé `return`

Le mot clé `return` permet de signaler à la fonction qu'elle doit **retourner une valeur**. Une fois le `return` exécuté, nous **sortons** de la fonction et toute ligne de code qui se situerait à la suite de cette instruction `return` ne sera **jamais exécutée**.

```python
def increment(x):
    x += 1
    return x
    print("Je ne serai jamais éxécuté :(")

print(increment(2))
```

---

## III. Valeur de retour d'une fonction

Une fonction retourne **toujours** quelque chose, même s'il n'y a pas de `return` dans sa définition. Ainsi la valeur retournée dans ce cas sera `None`.
`None`, c'est la valeur du rien en Python.

```python
def do_nothing():
    pass # le mot clé pass signifie que cette ligne de code ne donne aucune instruction

print(do_nothing())
```

---

## IV. Les paramètres d'une fonction

### A. Paramètres obligatoires

Une fonction peut avoir de 0 à plusieurs paramètres. Ces paramètres représentent des **abstractions** qui symbolisent les futurs objets concrets que la fonction va rencontrer lorsque celle-ci sera **appelée**.

```python
def multiply(a, b): # a et b n'existent pas, ce sont des abstractions
    return a * b   # pour tout a et b, la fonction multiply me retournera a * b

result = multiply(2, 3) # 2 et 3 sont des objets concrets lors de l'appel de la fonction
print(result) # 6
```

### B. Paramètres par défaut

On peut définir des **paramètres par défaut**, qui seront **optionnels**, et qui prendront une certaine valeur s'ils ne sont pas présents lors de la phrase d'appel de la fonction.

```python
def dire_bonjour(name = "mystérieux inconnu"):
    return f"Coucou {name} !"

print(dire_bonjour("Stéphane")) # Coucou Stéphane !
print(dire_bonjour())           # Coucou mystérieux inconnu !
```

> ⚠️ Si vous définissez des paramètres par défaut avec des paramètres obligatoires, vous devez vous assurer que les paramètres par défaut sont déclarés après tous les paramètres requis.

---

## V. Hiérarchie du code

### A. Ordre de déclaration et d'appel

L'interpréteur Python va exécuter le script de haut en bas. Ainsi la définition d'une fonction doit toujours se produire **avant** l'appel de cette fonction.

```python
dire_coucou()


def dire_coucou():
    print("coucou !") # name 'dire_coucou' is not defined
```

### B. Espace global et espace local

Comme explicité au début du cours, le code de **définition** d'une fonction n'est **pas accessible** depuis l'extérieur. Cet espace propre à la fonction est appelé l'**espace local**. Le code en dehors de la fonction est appelé l'**espace global**.

L'espace global est disponible pour l'espace local d'une fonction, mais les objets définis dans l'espace local d'une fonction **ne sont pas accessibles** depuis l'espace global.

```python
x = 15 # une variable x définie dans l'espace global
ma_liste = []

def truc():
# python va chercher x dans l'espace local et si il ne le trouve pas, il cherchera x dans l'espace global 
    return x

def alterer_une_liste(element):
# on peut même altérer les objets muables définis dans l'espace global depuis l'espace local
    ma_liste.append(element)

truc()
alterer_une_liste(12)

print(x)        # 15
print(ma_liste) # [12]
```

### C. Les fonctions `globals()` et `locals()`

Ces fonctions permettent de dresser la liste des objets définis dans l'espace global et dans l'espace local.

```python
from pprint import pprint

def faire_un_truc():
    variable_local = 12
    print("\nEspace local de l'intérieur de la fonction faire_un_truc: ")
    pprint(locals())

    print("\nEspace global vu depuis la fonction faire_un_truc: ")
    pprint(globals())
    
    return f"Je fais un truc avec {pi}."

pi = 3.14
faire_un_truc()

print("\nEspace global: ")
pprint(globals())

print("\nEspace local de l'espace global, c'est la même chose en fait: ")
pprint(locals())
```

On voit ici que `variable_local` n'est pas accessible depuis l'espace global, mais que l'intégralité de l'espace global depuis l'intérieur de la fonction `faire_un_truc()` est disponible.

---

## VI. Les fonctions `lambda`

Les fonctions `lambda` ou fonctions anonymes sont des fonctions n'ayant pas de nom et qui sont placées en paramètres d'autres fonctions. Elles sont alors appelées des `callback`.

Les fonctions anonymes sont présentes dans l'exemple de la méthode `filter()` du chapitre sur [les listes](14-les-listes.md), et dans le chapitre pour [trier un dictionnaire](17-les-dictionnaires.md).

---

## VII. Passage d'un paramètre par référence

Comme nous l'avons vu lorsque nous avons parlé des [objets muables et immuables](13-les-objets-muables-et-immuables.md), certains objets sont passés par **valeur**, d'autres par **référence**. Les objets [immuables](13-les-objets-muables-et-immuables.md) comme les nombres sont passés par **valeur**, c'est-à-dire qu'une **copie** de l'objet est créée lorsqu'ils sont appelés dans la fonction, et l'objet originel **n'est pas altéré**.

Au contraire, les listes qui sont des objets **muables**, vont être passées par **référence**, c'est-à-dire par **adresse mémoire**, et seront altérées dans la fonction. On en a vu un exemple dans le code du titre « Espace global et espace local ».

---

## VIII. Récursivité

### A. Définition

Une fonction est dite **récursive** lorsqu'elle **s'appelle elle-même** à l'intérieur de sa propre définition.

```python
def factorielle(nb):
    if nb == 1:
        return 1
    else:
        return nb * factorielle(nb-1)

print(factorielle(5)) # 120 --> 5! == 5 * 4 * 3 * 2 * 1 
```

Dans cet exemple, la fonction va être appelée autant de fois que le nombre donné.

### B. Exemple concret : la recherche dichotomique

La recherche dichotomique est un algorithme de recherche pour trouver la position d'un élément dans un tableau trié. Le principe est le suivant : comparer l'élément avec la valeur de la case au milieu du tableau ; si les valeurs sont égales, la tâche est accomplie, sinon on recommence dans la moitié du tableau pertinente.

```python
liste = [1, 3, 5, 6, 7, 9, 12, 15, 18, 19, 23, 27, 30]  
  
def binary_search(li, mini, maxi, elem):
    if maxi - mini == 1:
        if li[mini] == elem:
            return mini
        return maxi

    # On teste l'élément du milieu  
    milieu = (maxi + mini) // 2  
    if li[milieu] == elem:  
        # On a eu de la chance, on est tombé sur l'élément du premier coup  
        return milieu  
    if li[milieu] > elem:  
        # L'élément au milieu de la liste est > à ce qu'on recherche  
        # Comme la liste est triée, notre élément est forcément avant le milieu
        return binary_search(li, mini, milieu - 1, elem)  
    if li[milieu] < elem:  
        # L'élément au milieu de la liste est < à ce qu'on recherche  
        # Comme la liste est triée, notre élément est forcément après le milieu
        return binary_search(li, milieu + 1, maxi, elem)
  
print(binary_search(liste, 0, len(liste) - 1, 30))
```

> 📌 Cet algorithme mériterait des améliorations, notamment une gestion de l'erreur si l'élément n'est même pas présent dans la liste.

### C. Exemple concret : parcours d'une arborescence

Parcours de l'arborescence courante.

Écrire une fonction récursive qui affiche les noms des fichiers et qui se rappelle si un répertoire est rencontré, en incrémentant l'indentation.
Pour cet exemple, vous aurez besoin d'utiliser le slash (`/`) opérateur qui, dans le cadre de `pathlib`, permet de concaténer un chemin de manière compatible avec tous les systèmes d'exploitation.

```python
import os
from pathlib import Path

def show_tree(dir=".", indent=""):
    p = Path(dir)
    if not p.is_dir():
        print(f"{indent}{dir}")
        return  # Il faut ajouter un return ici pour arrêter l'exécution si ce n'est pas un répertoire

    list_files_dirs = os.listdir(p)
    for fd in list_files_dirs:
        full_path = p / fd  # Construction du chemin complet
        print(f"{indent}{fd}")
        if full_path.is_dir():  # Utilisez full_path.is_dir() pour vérifier si c'est un répertoire
            show_tree(full_path, indent + "-- ")  # On appelle la même fonction avec le nouveau chemin

show_tree()
```

---

## IX. Exercices

### Exercice 1 — Une fonction racine carrée (~5 min)

```python
# Créer une fonction square_root prenant un nombre en paramètre, et retournant la racine carrée de ce nombre (vous pouvez utiliser le module math)
# Printer l'appel de la fonction avec un nombre donné
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Ma fonction **retourne** une valeur, elle ne se contente pas de la printer.
- [ ] J'ai importé le module dont j'ai besoin **avant** de définir la fonction.
- [ ] J'appelle bien la fonction pour afficher le résultat.

<details>
<summary>Voir la correction</summary>

```python
# Créer une fonction square_root prenant un nombre en paramètre, et retournant la racine carrée de ce nombre (vous pouvez utiliser le module math)
# Printer l'appel de la fonction avec un nombre donné

import math
def square_root(number):
    return math.sqrt(number)

print(square_root(4))
```

</details>

---

### Exercice 2 — Une fonction qui ne retourne rien (~5 min)

```python
# Créer une fonction extendator ne prenant aucun paramètre, et qui ne retourne rien.
# Faire en sorte qu'elle modifie la liste suivante définie dans l'espace global en l'étendant de la liste suivante [4, 5, 6]

liste_depart = [1, 2, 3]
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Ma fonction n'a **aucun paramètre** et n'utilise pas `return`.
- [ ] Elle modifie la liste de l'espace global **sans la réaffecter**.
- [ ] J'ai bien appelé la fonction, sinon rien ne se passe.

<details>
<summary>Voir la correction</summary>

```python
# Créer une fonction extendator ne prenant aucun paramètre, et qui ne retourne rien.
# Faire en sorte qu'elle modifie la liste suivante définie dans l'espace global en l'étendant de la liste suivante [4, 5, 6]

liste_depart = [1, 2, 3]

def extendator():
    liste_depart.extend([4, 5, 6])

extendator()

print(liste_depart)
```

C'est le cas d'école vu plus haut : la liste est un objet muable de l'espace global, il est passé par référence, donc la fonction l'altère durablement — alors qu'aucune valeur n'est retournée.

</details>

---

### Exercice 3 — Composer deux fonctions (~5 min)

```python
# Créer une fonction add prenant en paramètres deux nombres et qui retourne l'addition de ses deux nombres
# Créer une fonction carre qui prend un nombre en paramètre et retourne ce dernier élevé au carré
# A l'aide de ses deux fonction, retourner la somme des carrés de 2 et 3 (2² + 3²)
# Printer le résultat
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Chacune de mes deux fonctions **retourne** une valeur.
- [ ] J'ai appelé l'une **dans** l'appel de l'autre, au lieu de recopier le calcul.
- [ ] Le résultat affiché est bien la somme des carrés de 2 et de 3.

<details>
<summary>Voir la correction</summary>

```python
# Créer une fonction add prenant en paramètres deux nombres et qui retourne l'addition de ses deux nombres
# Créer une fonction carre qui prend un nombre en paramètre et retourne ce dernier élevé au carré
# A l'aide de ses deux fonction, retourner la somme des carrés de 2 et 3 (2² + 3²)
# Printer le résultat

def add(x, y):
    return x + y

def carre(x):
    return x * x

print(add(carre(2), carre(3)))
```

</details>

---

### Exercice 4 — Le labyrinthe (~20 min, facultatif)

```python
# Le labyrinthe
# Partant de maze[0][0] (8) dans le labyrinthe, créer une fonction récursive capable de trouver la sortie (9)
# Les 0 présents dans le labyrinthe sont les murs infranchissables
# Les 1 sont des chemins possibles
# Parcours en diagonale interdit
# L'entrée du labyrinthe sera toujours à [0][0]
# La fonction fonctionne quelque soit la longueur et la largeur du labyrinthe
# La fonction ne prévoit pas le cas de figure suivant où quatre 1 sont côte à côte :
# [[8, 1, 1*, 1*]
#  [0, 0, 1*, 1*] -> *quatre 1 en carré interdit boucle infinie probable
#  [0, 0, 0, 9]]

#    x = 0  1  2  3  4  5      y
maze = [[8, 1, 1, 1, 1, 0],  # 0
        [1, 0, 1, 0, 1, 0],  # 1
        [1, 0, 1, 1, 1, 1],  # 2 
        [1, 0, 0, 0, 1, 0],  # 3 
        [1, 1, 1, 0, 1, 0],  # 4      
        [0, 1, 0, 0, 1, 9]]  # 5
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Ma fonction **s'appelle elle-même** avec des coordonnées différentes.
- [ ] Elle **s'arrête** quelque part : soit elle a trouvé la sortie, soit elle a épuisé les chemins.
- [ ] Je ne peux pas repasser deux fois par la même case, sinon je tourne en rond.
- [ ] Je n'explore que quatre directions : gauche, droite, haut, bas.

<details>
<summary>Voir la correction</summary>

```python
#    x = 0  1  2  3  4  5      y
maze = [[8, 1, 1, 1, 1, 0],  # 0
        [1, 0, 1, 0, 1, 0],  # 1
        [1, 0, 1, 1, 1, 1],  # 2 
        [1, 0, 0, 0, 1, 0],  # 3 
        [1, 1, 1, 0, 1, 0],  # 4      
        [0, 1, 0, 0, 1, 9]]  # 5

def find_maze_exit(m: list[list[int]], x: int, y: int):  
    print("Exploration aux indexs:", x, y)  
  
    if m[y][x] == 9:  
        print(x, y)  
        exit()  
  
    m[y][x] = -1  
  
    # on explore à gauche  
    if x > 0:
        # On s'assure de ne pas sortir des limites du labyrinthe  
        if m[y][x - 1] >= 1: 
            find_maze_exit(m, x - 1, y)  
  
    # on explore à droite  
    if x < len(m[0]) - 1:  
        if m[y][x + 1] >= 1:  
            find_maze_exit(m, x + 1, y)  
  
    # on explore en haut  
    if y > 0:  
        if m[y - 1][x] >= 1:  
            find_maze_exit(m, x, y - 1)  
  
    # on explore en bas  
    if y < len(m) - 1:  
        if m[y + 1][x] >= 1:  
            find_maze_exit(m, x, y + 1)  
  
  
find_maze_exit(maze, 0, 0)
```

Le marquage `m[y][x] = -1` est la clé : la case visitée cesse d'être un chemin possible, ce qui empêche la fonction de repartir en arrière et de boucler indéfiniment. C'est exactement le piège des « quatre 1 en carré » annoncé dans l'énoncé.

</details>

---

## X. Aller plus loin

> ⏭️ Facultatif — pas exigé pour la suite du cours.

- La recherche dichotomique et le parcours d'arborescence de ce chapitre sont deux visages de la même idée : un problème se résout en rappelant la même fonction sur une partie plus petite du problème.
- La signature `def find_maze_exit(m: list[list[int]], x: int, y: int):` de la correction facultative annonce le chapitre suivant sur les [annotations de type](21-les-annotations-de-type.md) : vous pouvez déjà la lire comme « `m` est une liste de listes d'entiers, `x` et `y` sont des entiers ».

---

## Points clés

- Une fonction se **définit** avant d'être **appelée** ; l'interpréteur lit le script de haut en bas.
- `return` renvoie une valeur **et sort** de la fonction : le code placé après n'est jamais exécuté.
- Sans `return`, une fonction retourne quand même quelque chose : `None`.
- Les paramètres par défaut se déclarent **après** les paramètres obligatoires.
- L'espace local voit l'espace global, l'inverse est faux — mais un objet muable de l'espace global reste modifiable depuis la fonction.
- Une fonction récursive s'appelle elle-même et a besoin d'un cas d'arrêt, sinon elle tourne jusqu'à l'épuisement.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Que retourne une fonction dont la définition ne contient aucun `return` ?

- A. Rien du tout : l'appel n'a aucune valeur et ne peut pas être affecté à une variable
- B. `None`, la valeur du rien en Python, car une fonction retourne toujours quelque chose
- C. Une erreur, l'absence de `return` rendant la définition incomplète
- D. Le dernier objet calculé par la fonction, même sans instruction pour le renvoyer

**2.** Dans la fonction `increment()` du chapitre, un `print` est placé juste après le `return`. Que se passe-t-il à l'appel de la fonction ?

- A. `1` est retourné puis `coucou` est affiché, les deux instructions étant exécutées dans l'ordre
- B. `coucou` est affiché avant que la valeur soit retournée, l'affichage passant toujours avant la sortie
- C. `coucou` n'est jamais affiché, car le `return` sort de la fonction et rien ne s'exécute après lui
- D. Une erreur, Python refusant une instruction placée après un `return` dans une fonction

**3.** Dans quel ordre déclarer les paramètres d'une fonction ?

- A. Les paramètres obligatoires d'abord, les paramètres par défaut ensuite
- B. Les paramètres par défaut d'abord, pour qu'ils soient écrasés par les valeurs reçues
- C. Dans n'importe quel ordre, Python faisant correspondre chaque valeur à son nom
- D. Les paramètres les plus utilisés d'abord, l'interpréteur s'arrêtant au premier manquant

**4.** Une fonction locale modifie une liste définie dans l'espace global et définit une variable `variable_local`. Que retrouve-t-on dans l'espace global après l'appel ?

- A. La liste inchangée et `variable_local`, puisque l'espace local est visible de l'extérieur
- B. La liste modifiée, car un objet muable est passé par référence, et `variable_local` absente
- C. La liste modifiée et `variable_local`, les deux ayant été rendues accessibles par l'appel
- D. La liste inchangée et `variable_local` absente, l'espace local étant étanche dans les deux sens

**5.** *Question ouverte (2-3 lignes).* Qu'est-ce qu'une fonction récursive, et qu'est-ce qu'elle doit absolument contenir pour ne pas tourner indéfiniment ? Appuyez votre réponse sur un exemple du chapitre.

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. B.** Une fonction retourne toujours quelque chose ; sans `return`, la valeur retournée est `None`.
**Pourquoi :** le chapitre l'illustre avec `do_nothing()` dont le corps est un simple `pass`, et dont l'appel printer `None`.

**2. C.** Le `return` fait sortir de la fonction : la ligne placée après n'est jamais exécutée.
**Pourquoi :** c'est le sens exact de l'exemple `increment()`, dont le `print` annonce lui-même « Je ne serai jamais éxécuté ».

**3. A.** Les paramètres par défaut, qui sont optionnels, se déclarent après tous les paramètres requis.
**Pourquoi :** c'est la mise en garde du chapitre ; dans le cas contraire l'appel ne serait plus décodable par Python.

**4. B.** La liste, muable, est passée par référence : elle est bien altérée. `variable_local`, définie dans l'espace local, reste inaccessible depuis l'espace global.
**Pourquoi :** `alterer_une_liste()` modifie `ma_liste` durablement alors que `print(x)` retrouve sa valeur d'origine ; `globals()` et `locals()` le confirment, l'espace global voyant tout sauf ce que la fonction a défini pour elle.

**5.** Attendu : une fonction récursive s'appelle elle-même dans sa propre définition, et elle doit prévoir un cas d'arrêt qui coupe la chaîne d'appels.
**Pourquoi :** `factorielle()` s'arrête quand `nb == 1` ; `find_maze_exit()` s'arrête quand elle tombe sur la sortie et marque chaque case visitée à `-1` pour ne jamais repartir en arrière et boucler.

</details>

---

[← Chapitre précédent](18-les-sets.md) · [Sommaire](Readme.md) · [Chapitre suivant →](20-les-arguments-flexibles.md)
