[← Chapitre précédent](10-formatter-les-chaines-de-caracteres.md) · [Sommaire](Readme.md) · [Chapitre suivant →](12-les-modules-standards-de-python.md)

# 11 - Les structures conditionnelles

> Jusqu'ici, vos scripts lisaient leurs instructions de haut en bas, sans jamais
> bifurquer. Une condition, c'est la première bifurcation : on teste quelque
> chose, et on n'exécute du code **que** si le test passe. Tout le reste du
> chapitre est une affaire de détails — l'ordre des branches, l'indentation, et
> la place des gardes.

**Durée :** ≈ 40 min (lecture ≈ 18 min + atelier 15 min + réflexion 7 min) · + 12 min facultatif · **Prérequis :** [Les opérateurs mathématiques](09-les-operateurs-mathematiques.md), [Les booléens](04-les-booleens.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Écrire** une branche `if`, `elif`, `else` et **prévoir** laquelle sera exécutée.
- **Respecter** le rôle de l'indentation, qui délimite les blocs en Python.
- **Composer** des tests complexes avec `and`, `or`, `^` et `not`.
- **Utiliser** le `match case`, y compris avec des motifs et des conditions gardes.

---

## I. Une condition, des branches

La **conditionnelle** est un **pilier de la programmation**. Elle permet de tester une affirmation ou une expression, qui retourne `True` ou `False`. C'est dans les conditions que nous utilisons les [opérateurs de comparaison](09-les-operateurs-mathematiques.md).

La condition permet de **créer des branches** dans lesquelles nous écrivons du code. Le code sera alors exécuté seulement si la condition attachée à cette branche a été évaluée comme `True`.

### A. Écrire une branche

Une branche doit adopter la syntaxe suivante : `if | elif + condition + ':'`.

```python
condition = ((2 + 2) == 4)
if condition: # condition jugée vraie
    print("2 + 2 est bien égal à 4.") # code de la branche exécuté
```

Le deux-points final n'est pas décoratif : il annonce que le bloc décalé en dessous appartient à la condition.

### B. Enchaîner et imbriquer les conditions

On peut tout à fait enchaîner les conditions ou les imbriquer.

```python
pi = 3.14
if pi > 1:
    print("pi est bien supérieur à 1")
    if pi > 2:
        print("pi est bien supérieur à 2 aussi !")
```

Une condition peut donc se trouver à l'intérieur d'une autre. Gardez-le en tête : plus l'imbrication est profonde, plus le code est difficile à relire.

### C. `if… else` : une seule branche exécutée

Dans le cadre d'une condition `if.. else`, seule une des deux branches sera évaluée quoiqu'il arrive.

```python
age = 17
if age >= 18:       # sera évaluée comme False
    print("majeur")
else:
    print("mineur") # le code sera exécuté sans même évaluer la condition
```

La branche `else` ne teste rien : elle reçoit tout ce que la condition `if` a refusé.

### D. `if… elif… else` : on s'arrête au premier vrai

Dans une condition `if.. elif.. else`, plusieurs conditions peuvent être évaluées jusqu'à ce qu'on trouve une condition qui renvoie `True`.

```python
age = 18
if age > 18:                    # sera évaluée False
    print("vétéran")
elif age == 18:                 # sera évaluée True
    print("tout juste majeur")
else:                           # ne sera jamais évaluée
    print("mineur")
```

Dès qu'une branche est vraie, les suivantes ne sont **pas** évaluées. C'est commode, et c'est aussi ce qui rend l'ordre des tests important : placez le plus restrictif en premier.

---

## II. L'importance de l'indentation

En Python, **l'indentation est extrêmement importante** : c'est elle qui remplace les accolades de la plupart des autres langages pour délimiter un bloc. Il est donc important que le code situé dans une des branches de la condition **soit décalé d'un cran** par rapport à la condition elle-même.

```python
age = 17
if age >= 18:
print("majeur") # ce code soulèvera une erreur IndentationError
```

> ⚠️ La règle vaut pour **tous** les blocs vus dans ce cours et pour tous ceux qui
> viennent : boucles, fonctions, `match case`. Un bloc non indenté n'est pas un
> bloc moins important, c'est une erreur — ou pire, un bloc qui fait autre chose
> que ce que vous vouliez.

---

## III. L'opérateur ternaire

Vous pouvez écrire une condition **sur une seule ligne** grâce à l'opérateur ternaire. À utiliser avec mesure et discernement pour garder un code clair.

```python
age = 17
print("majeur") if age >= 18 else print("mineur")
```

Autre exemple :

```python
x = 10
y = 20

# l'opérateur ternaire sert ici à ranger la plus petite des deux valeurs dans 'min_value'
min_value = x if x < y else y

print(min_value) # Output: 10
```

Lisez-le de gauche à droite comme une phrase : « `min_value` vaut `x` **si** `x` est plus petit que `y`, **sinon** `y` ».

---

## IV. Les opérateurs logiques

Les opérateurs logiques permettent de faire des conditions plus complexes.

| Opérateur | Signification |
| --- | --- |
| `and` | ET |
| `or` | OU |
| `^` | OU EXCLUSIF |
| `not` | NON |

```python
nom = "Gérard"

cond_and = nom.startswith('G') and nom.endswith('d')         # ET
cond_or  = nom.startswith('G') or nom.endswith('d')          # OU
cond_xor = nom.startswith('G') ^ nom.endswith('d')           # OU EXCLUSIF
cond_not = not nom.startswith('x') and not nom.endswith('d') # NON
cond_in  = not 'r' in nom or not 'x' in nom                  # DANS

print(cond_and) # True car "Gérard" commence bien par 'G' et finit bien par 'd'
print(cond_or)  # True aussi car au moins une des conditions est vraie
print(cond_xor) # False car une seule des conditions doit être vraie
print(cond_not) # False car "Gérard" ne commence pas par 'x' mais finit par 'd'
print(cond_in)  # True car certes, r est dans "Gérard" mais pas 'x'
```

Matrice des opérateurs logiques :

| A | B | A AND B | A OR B | A XOR B | NOT A |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 |

La dernière ligne est celle qui piège le plus : `A OR B` est vrai dès qu'**au moins** une des deux est vraie, y compris les deux. Si vous voulez « l'un ou l'autre, mais pas les deux », c'est `^` (OU exclusif) qu'il faut.

---

## V. Le `match case`

Nouveauté apportée depuis la version 3.10, Python propose un **match case** dont la syntaxe rappelle le `switch case` présent dans la plupart des langages de programmation. Il remplit la même fonction, mais **apporte de puissantes fonctionnalités supplémentaires**.

### A. Égalité de valeur

Le match case est particulièrement pertinent lorsqu'on sait d'avance quelles **valeurs déterminées** une variable va prendre dans le futur et que l'on doit organiser les conditions en conséquence.

```python
mot = "toto"

match mot:
    case "titi":
        print("titi")
    case "tata":
        print("tata")
    case "toto":
        print("toto")
```

### B. Égalité de motif

La fonctionnalité supplémentaire qu'apporte le match case, c'est qu'il est prévu pour fonctionner avec des **égalités de motifs** : on ne compare plus une valeur, on décrit une **forme**.

```python
coords = [(1, 3, 7), (34, 2), (123, 2, 82)]

for coord in coords:
    match coord:
        case [x, y]:
            print("Coordonnées en 2 dimensions")
        case [x, y, z]:
            print("Coordonnées en 3 dimensions")
```

Ici, `[x, y]` ne dit pas « ces coordonnées valent-elles x et y » mais « cette collection a-t-elle **deux** éléments ». Le tuple `(34, 2)` a la bonne forme, le tuple à trois éléments prend l'autre cas.

### C. Ajouter une condition garde

On peut même rajouter des conditions à l'intérieur des `case` pour ajouter de la précision.

```python
coords = [(0, 0), (1, 3, 7), (34, 2), (123, 2, 82), (0, 0, 0)]

for coord in coords:
    match coord:
        case [x, y] if x == y == 0:
            print("Coordonnées en 2 dimensions situées à l'origine du repère")
        case [x, y]:
            print("Coordonnées en 2 dimensions")
        case [x, y, z] if x == y == z == 0:
            print("Coordonnées en 3 dimensions situées à l'origine du repère")
        case [x, y, z]:
            print("Coordonnées en 3 dimensions à des endroits aléatoires")
```

**L'ordre des cas est décisif** : comme dans une suite de `elif`, le premier motif qui matche gagne et les suivants ne sont plus essayés. Écrivez donc le cas **gardé** avant le cas général — dans l'autre sens, `(0, 0)` serait attrapé par `case [x, y]` et votre garde ne servirait jamais. Vous reverrez exactement ce point dans l'exercice 3.

> 📌 **Syntaxe du match case.** On remarquera que, contrairement aux autres
> langages dans lesquels le match case est implémenté, ici le mot `break` n'est
> pas obligatoire entre les différents cas : un cas exécuté ne « tombe » pas dans
> le suivant.

---

### Exercice 1 — Pair, impair, ou n'importe quoi (~8 min)

```python
# Demander à l'utilisateur de taper un nombre
# Si celui-ci est pair, printer "Vous avez entré un nombre pair."
# Si celui-ci est impair, printer "Vous avez entré un nombre impair."
# Si l'information entrée n'est pas un nombre printer "Vous devez entrer un nombre!"
```

**Avant d'ouvrir le corrigé**, vérifiez que :

- [ ] Le cas « ce n'est pas un nombre » est traité **avant** de tester la parité.
- [ ] Vous convertissez la saisie en entier avant d'utiliser `%`.
- [ ] Un seul des trois messages peut s'afficher pour une saisie donnée.

<details>
<summary>Corrigé</summary>

```python
nombre = input("Taper un nombre")

if not nombre.isdigit():
    print("Vous devez entrer un nombre!")
elif int(nombre) % 2 == 0:
    print("Vous avez entré un nombre pair.")
elif int(nombre) % 2 != 0:
    print("Vous avez entré un nombre impair.")
```

Deux points à voir :

- La dernière branche pourrait s'écrire `else:` : après les deux premières, il ne reste que les impairs. Écrire `elif int(nombre) % 2 != 0` explicite le raisonnement, `else` rend le code plus court — les deux se défendent.
- `isdigit()` répond `False` pour `"−3"` ou `"2,5"` : la saisie part alors dans le message d'erreur. C'est le comportement attendu ici, mais cela veut dire que ce script ne traite pas les nombres négatifs.

</details>

---

### Exercice 2 — Le OU exclusif (~7 min)

```python
# Demander à un utilisateur de taper un mot
# Si celui-ci possède la lettre e OU la lettre a printer "Beep"
# Si celui-ci possède la lettre e OU la lettre a, mais sans que les deux conditions soient vraies en même temps, printer "Boop"
```

**Avant d'ouvrir le corrigé**, vérifiez que :

- [ ] Vous avez repéré que les deux consignes se recouvrent : la seconde est un cas particulier de la première.
- [ ] L'ordre des branches est ce qui rend le message « Boop » atteignable.

<details>
<summary>Corrigé</summary>

```python
mot = input("Taper un mot")

if ('a' in mot) ^ ('e' in mot):
    print("Boop")
else:
    print("Rien à signaler!")
```

**Attention, le corrigé du cours d'origine est plus bavard que l'énoncé.** La correction distribuée affichait `"Opérateur OU exclusif"` au lieu de `"Boop"`, et ne traitait pas le premier message (« Beep ») : elle testait seulement le OU exclusif, puis imprimait « Rien à signaler! » dans tous les autres cas — y compris quand une seule des deux lettres était présente, ce qui est précisément le cas « Boop ».

Voici donc la version qui respecte **les deux** consignes de l'énoncé, en profitant du fait que les branches sont évaluées dans l'ordre :

```python
mot = input("Taper un mot")

if ('a' in mot) or ('e' in mot):
    if ('a' in mot) ^ ('e' in mot):
        print("Boop")
    else:
        print("Beep")
else:
    print("Rien à signaler!")
```

Un mot contenant les deux lettres (`"chat"` n'a que `a`, `"cheval"` a les deux) entre dans le premier `if`, puis échoue au OU exclusif : il reçoit « Beep ». Un mot qui n'a qu'une des deux lettres reçoit « Boop ». Le sens de `^` est exactement « l'un ou l'autre, pas les deux » — voyez la matrice plus haut.

</details>

---

### Exercice 3 — Couleurs en match case (~12 min, facultatif)

```python
# A l'aide d'un match case et d'une boucle, printer "RGB" lorsque la couleur présente dans la liste suivante est une couleur au format RGB (Red Green Blue), et printer "RGBA" lorsque la couleur est au format RGBA (Red Green Blue Alpha).

# Si r, g, et b sont égaux à 0 (quel que soit le format de la couleur), alors il faudra printer "Couleur noire" en priorité seulement si la valeur d'alpha (si elle existe) est supérieure à 0

# Si r, g, et b sont égaux à 255 (quel que soit le format de la couleur), alors il faudra printer "Couleur blanche" en priorité seulement si la valeur d'alpha (si elle existe) est supérieure à 0

# Résultat attendu: RGB RGBA RGB de couleur noire RGBA RGBA RGBA de couleur blanche RGBA

colors = [(12, 72, 89), (23, 77, 200, 1), (0, 0, 0), (123, 123, 67, 1), (255, 255, 255, 0), (255, 255, 255, 1), (0, 0, 0, 0)]

for color in colors:
	match color:
		# Ecrire le code ici
```

> ⚠️ Le gabarit ci-dessus est indenté avec des **tabulations**, comme dans le
> fichier d'origine. Reprenez-le avec 4 espaces : Python 3 refuse de mélanger
> tabulations et espaces dans un même bloc.

<details>
<summary>Corrigé</summary>

```python
colors = [(12, 72, 89), (23, 77, 200, 1), (0, 0, 0), (123, 123, 67, 1), (255, 255, 255, 0), (255, 255, 255, 1), (0, 0, 0, 0)]

for color in colors:
    match color:
        case [r, g, b] if r == g == b == 0:
            print("RGB de couleur noire")
        case [r, g, b] if r == g == b == 255:
            print("RGB de couleur blanche")
        case [r, g, b]:
            print("RGB")
        case [r, g, b, a] if r == g == b == 0 and a > 0:
            print("RGBA de couleur noire")
        case [r, g, b, a] if r == g == b == 255 and a > 0:
            print("RGBA de couleur blanche")
        case [r, g, b, a]:
            print("RGBA")
```

Le motif `[r, g, b]` n'attrape que les couleurs à trois composantes, `[r, g, b, a]` seulement celles à quatre : c'est la longueur qui décide, pas les valeurs. Les gardes `if …` placées **avant** chaque cas général font le reste du tri.

Vérification avec les sept couleurs proposées, dans l'ordre : `(12, 72, 89)` → `RGB` ; `(23, 77, 200, 1)` → `RGBA` ; `(0, 0, 0)` → `RGB de couleur noire` ; `(123, 123, 67, 1)` → `RGBA` ; `(255, 255, 255, 0)` → `RGBA`, car un alpha nul ne donne pas la priorité « blanche » ; `(255, 255, 255, 1)` → `RGBA de couleur blanche` ; `(0, 0, 0, 0)` → `RGBA`. On retrouve bien la ligne attendue.

</details>

---

## Points clés

- Une condition ne peut exécuter qu'une seule branche, et les branches sont testées **dans l'ordre** : la plus restrictive passe en premier.
- L'indentation remplace les accolades : sans décalage, il n'y a pas de bloc (`IndentationError`).
- `and`, `or`, `^`, `not` composent les tests ; `or` reste vrai quand les deux le sont, `^` exige qu'un seul le soit.
- Le `match case` compare des **motifs** (une forme, une longueur), et ses gardes `if` doivent précéder le cas général.
- `break` n'est pas nécessaire entre deux `case` : on ne « tombe » jamais du cas précédent dans le suivant.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Dans une suite `if / elif / elif / else`, combien de conditions sont évaluées au maximum ?

- A. Une seule, la première, les autres étant seulement exécutées si elle réussit
- B. Toutes, puis la dernière vraie est retenue par Python
- C. Autant qu'il en faut jusqu'à la première qui renvoie `True`, le `else` ne servant que si aucune n'est vraie
- D. Exactement deux, la première et la dernière, le milieu de la chaîne étant ignoré

**2.** Un mot contient à la fois `a` et `e`. Que renvoie `('a' in mot) ^ ('e' in mot)` ?

- A. `True`, car les deux lettres sont bien présentes dans le mot
- B. `False`, car le OU exclusif exige qu'une seule des deux conditions soit vraie
- C. `True`, car `^` teste la présence et non l'exclusivité des deux lettres
- D. `False`, car une même chaîne ne peut pas être testée deux fois dans une même expression

**3.** Que se passe-t-il si l'on place `case [x, y]:` **avant** `case [x, y] if x == y == 0:` ?

- A. Rien de visible : Python teste malgré tout la garde en priorité
- B. Une erreur de syntaxe, car une garde doit toujours précéder le motif correspondant
- C. Le cas gardé n'est jamais atteint : le premier motif qui matche gagne et avale les coordonnées `(0, 0)`
- D. Le programme sort du `match` dès le premier cas, comme avec un `break` explicite

**4.** Pourquoi l'opérateur ternaire est-il déconseillé systématiquement ?

- A. Parce qu'il est plus lent que deux lignes de `if` sur n'importe quelle machine
- B. Parce qu'il n'est disponible qu'à partir de Python 3.10 et casse les anciens postes
- C. Parce qu'il ne peut contenir qu'un `print()` et interdit tout calcul dans la valeur
- D. Parce qu'une seule ligne condense trois décisions : très lisible une fois, beaucoup moins quand la logique s'épaissit

**5.** *Question ouverte (2-3 lignes).* Vous testez une note scolaire : « mention très bien » à partir de 16, « mention bien » à partir de 14, « mention assez bien » à partir de 12, rien en dessous. Écrivez la suite de branches, et dites pourquoi l'ordre décroissant des seuils est indispensable.

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. C.** L'évaluation s'arrête à la première condition vraie.
**Pourquoi :** c'est ce qui rend l'ordre important, et ce qui rend aussi inutile d'écrire `elif note >= 12` après avoir testé `>= 14` : si on est arrivé là, c'est que la note est déjà en dessous de 14. Le `else` final reçoit tout ce qui n'a matché aucune condition.

**2. B.** `^` est le OU **exclusif** : vrai si une seule des deux conditions est vraie.
**Pourquoi :** ici les deux sont vraies, donc le résultat est `False` — voyez la dernière ligne de la matrice. C'est la différence entre « au moins un des deux » (`or`) et « exactement un des deux » (`^`).

**3. C.** Le premier motif qui matche gagne.
**Pourquoi :** un `match case` fonctionne comme une suite de `elif`. Le motif sans garde attrape toutes les paires, y compris `(0, 0)`, et la garde ne sera jamais consultée. Aucune erreur n'est levée : c'est un bug silencieux.

**4. D.** Sa limite est la lisibilité, pas la performance ni la compatibilité.
**Pourquoi :** « à utiliser avec mesure et discernement », dit le chapitre. Dès qu'il y a un calcul, un appel et une alternative dans la même ligne, la relecture coûte plus cher que les trois lignes de `if` équivalentes.

**5.** Attendu :

```python
if note >= 16:
    print("mention très bien")
elif note >= 14:
    print("mention bien")
elif note >= 12:
    print("mention assez bien")
```

L'ordre décroissant est indispensable : en commençant par `>= 12`, une note de 18 entrerait dans la première branche et n'atteindrait jamais « très bien ».
**Pourquoi :** les branches sont évaluées dans l'ordre et la première vraie bloque les autres. Un test d'intervalle doit donc être écrit du plus restrictif au moins restrictif — ou, à l'inverse, en bornant explicitement chaque intervalle (`12 <= note < 14`).

</details>

---

[← Chapitre précédent](10-formatter-les-chaines-de-caracteres.md) · [Sommaire](Readme.md) · [Chapitre suivant →](12-les-modules-standards-de-python.md)
