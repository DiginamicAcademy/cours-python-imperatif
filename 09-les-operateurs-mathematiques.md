[← Chapitre précédent](08-les-methodes-de-chaines-de-caracteres.md) · [Sommaire](Readme.md) · [Chapitre suivant →](10-formatter-les-chaines-de-caracteres.md)

# 09 - Les opérateurs mathématiques

> Vous savez ranger une valeur dans une variable et la retoucher avec une méthode
> de chaîne. Il manque le calcul : additionner, comparer, et se demander si
> quelque chose « est dedans ». Voici les sept opérateurs arithmétiques de Python
> et quelques-uns de leurs cousins.

**Durée :** ≈ 30 min (lecture ≈ 9 min + atelier 17 min + réflexion 4 min) · **Prérequis :** [Les variables](01-les-variables.md), [Les nombres](03-les-nombres.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Calculer** avec les sept opérateurs arithmétiques, y compris modulo et division entière.
- **Appeler** une fonction d'une bibliothèque standard comme `math`.
- **Mettre à jour** une variable avec les assignations composées (`+=`, `*=`…).
- **Comparer** deux valeurs et **tester** l'appartenance d'un élément à une collection.

---

## I. Les opérateurs de base

Sept opérateurs couvrent l'essentiel de l'arithmétique :

| Opérateur | Opération | Exemple |
| --- | --- | --- |
| `+` | addition | `15 + 23` |
| `-` | soustraction | `57 - 42` |
| `/` | division | `100 / 25` |
| `*` | multiplication | `6 * 9` |
| `%` | modulo (reste de la division) | `29 % 5` |
| `//` | division entière | `29 // 5` |
| `**` | puissance | `2 ** 10` |

Ce sont `%` et `//` qui surprennent le plus : `29 / 5` demande « combien font 29 divisés par 5 », `29 // 5` demande « combien de fois 5 entre dans 29, sans les décimales », et `29 % 5` demande « ce qu'il reste ». Les trois se lisent donc sur la même division, mais ne répondent pas à la même question.

> 📌 L'opérateur `%` est le plus utile des trois en pratique : tester si un nombre
> est pair, répartir des éléments par groupes, faire tourner un cycle… tout cela
> passe par le reste d'une division.

---

## II. Les opérations avancées avec la bibliothèque `math`

La bibliothèque `math` fournit des fonctions pour des **opérations mathématiques** plus complexes. On l'**importe** avec le mot-clé `import`, puis on appelle ses fonctions (le chapitre [Les modules standards](12-les-modules-standards-de-python.md) détaille ce mécanisme).

```python
import math

racine = math.sqrt(16) # racine carrée
print(racine) # 4

arrondi = math.floor(3.7) # arrondi a l'inférieur
print(arrondi) # 3
```

`math.floor()` arrondit à l'entier inférieur ; `math.ceil()` arrondit à l'entier supérieur — vous en aurez besoin dans l'exercice 2.

📚 [Fonctions proposées par la bibliothèque `math`](https://docs.python.org/3/library/math.html)

---

## III. L'opérateur d'assignation

Comme vous le pratiquez depuis le début du cours, l'opérateur d'assignation d'une valeur à une variable est `=`. Il peut être **couplé à un opérateur mathématique** pour mettre à jour la variable à partir d'elle-même.

```python
x = 3
x += 1 # x = x + 1 --> 4
x *= 3 # x = x * 3 --> 12
x /= 2 # x = x / 2 --> 6
print(x)
```

Tous les opérateurs de la table précédente se combinent ainsi : `-=` et `%=` existent autant que `+=`.

> ⚠️ Contrairement à beaucoup d'autres langages de programmation, Python
> n'autorise pas l'incrémentation d'une variable `x` avec la syntaxe `x++`.
> On écrit `x += 1`.

---

## IV. Les opérateurs de comparaison

Utilisés dans les [structures conditionnelles](11-les-structures-conditionnelles.md).

| Opérateur | Opération |
| --- | --- |
| `>` | supérieur à |
| `<` | inférieur à |
| `>=` | supérieur ou égal à |
| `<=` | inférieur ou égal à |
| `==` | égalité |
| `!=` | inégalité |
| `is` | même adresse en mémoire |

Chacun renvoie un booléen : `True` ou `False`. C'est ce résultat qui nourrira une condition.

> ⚠️ Ne pas confondre l'opérateur d'assignation `=` avec l'opérateur d'égalité
> `==`. Le premier range une valeur dans une variable, le second compare.

> 📌 **Opérateur d'égalité.** Il existe certains langages comme le JavaScript qui
> utilisent aussi le `===` pour vérifier plus de conditions que le `==`, qui est
> plus léger. Python n'a pas cette double forme : `==` compare la valeur, `is`
> compare l'identité de l'objet en mémoire.

---

## V. L'opérateur d'appartenance `in`

L'opérateur `in` permet de déterminer si oui ou non un élément est présent dans une collection d'objets. Son contraire s'écrit `not in`.

```python
phrase = "Le python c'est trop cool"

print('x' in phrase)    # False
print("trop" in phrase) # True

ma_liste = [1, 2, 3, 4]

print(1 not in ma_liste)      # False
print("test" not in ma_liste) # True
```

Sur une chaîne de caractères, `in` cherche donc une **sous-chaîne** : `"trop"` est bien dans la phrase, alors qu'une lettre isolée comme `'x'` n'y figure pas.

---

### Exercice 1 — Calculs de base (~4 min)

```python
# 1. Calculez la somme de 15 et 23

# 2. Soustrayez 42 de 57

# 3. Multipliez 6 par 9

# 4. Divisez 100 par 25

# 5. Trouvez le reste de la division de 29 par 5

# 6. Effectuez une division entière de 29 par 5

# 7. Calculez 2 à la puissance de 10
```

**Avant d'ouvrir le corrigé**, vérifiez que :

- [ ] Chaque question tient en une ligne d'affectation et un `print()`.
- [ ] Vous avez employé `%`, `//` et `/` dans trois lignes distinctes, sans les mélanger.

<details>
<summary>Corrigé</summary>

```python
# 1. Calculez la somme de 15 et 23
somme = 15 + 23
print("La somme de 15 et 23 est :", somme)

# 2. Soustrayez 42 de 57
difference = 57 - 42
print("La différence entre 57 et 42 est :", difference)

# 3. Multipliez 6 par 9
produit = 6 * 9
print("Le produit de 6 et 9 est :", produit)

# 4. Divisez 100 par 25
quotient = 100 / 25
print("Le quotient de 100 par 25 est :", quotient)

# 5. Trouvez le reste de la division de 29 par 5
reste = 29 % 5
print("Le reste de la division de 29 par 5 est :", reste)

# 6. Effectuez une division entière de 29 par 5
division_entiere = 29 // 5
print("La division entière de 29 par 5 est :", division_entiere)

# 7. Calculez 2 à la puissance de 10
puissance = 2 ** 10
print("2 à la puissance de 10 est :", puissance)
```

`print()` accepte plusieurs arguments séparés par des virgules : il les affiche dans l'ordre, espacés d'un blanc. C'est ce qui permet d'écrire `print("Libellé :", valeur)` sans passer par une concaténation.

</details>

---

### Exercice 2 — Fonctions de la bibliothèque `math` (~3 min)

```python
import math

# 1. Calculez la racine carrée de 81

# 2. Arrondissez 7.8 à l'entier inférieur

# 3. Arrondissez 7.2 à l'entier supérieur
```

<details>
<summary>Corrigé</summary>

```python
import math

# 1. Calculez la racine carrée de 81
racine_carree = math.sqrt(81)
print("La racine carrée de 81 est :", racine_carree)

# 2. Arrondissez 7.8 à l'entier inférieur
arrondi_inferieur = math.floor(7.8)
print("7.8 arrondi à l'entier inférieur est :", arrondi_inferieur)

# 3. Arrondissez 7.2 à l'entier supérieur
arrondi_superieur = math.ceil(7.2)
print("7.2 arrondi à l'entier supérieur est :", arrondi_superieur)
```

Notez la syntaxe `math.sqrt()` : le point signifie « la fonction `sqrt` **du module** `math` ».

</details>

---

### Exercice 3 — Assignations composées (~4 min)

```python
# 1. Initialisez la variable a avec la valeur 10, puis ajoutez 5 à a

# 2. Initialisez la variable b avec la valeur 20, puis soustrayez 7 de b

# 3. Initialisez la variable c avec la valeur 3, puis multipliez c par 4

# 4. Initialisez la variable d avec la valeur 50, puis divisez d par 2

# 5. Initialisez la variable e avec la valeur 9, puis calculez le reste de la division de e par 4
```

<details>
<summary>Corrigé</summary>

```python
# 1. Initialisez la variable a avec la valeur 10, puis ajoutez 5 à a
a = 10
a += 5
print("a après addition de 5 :", a)

# 2. Initialisez la variable b avec la valeur 20, puis soustrayez 7 de b
b = 20
b -= 7
print("b après soustraction de 7 :", b)

# 3. Initialisez la variable c avec la valeur 3, puis multipliez c par 4
c = 3
c *= 4
print("c après multiplication par 4 :", c)

# 4. Initialisez la variable d avec la valeur 50, puis divisez d par 2
d = 50
d /= 2
print("d après division par 2 :", d)

# 5. Initialisez la variable e avec la valeur 9, puis calculez le reste de la division de e par 4
e = 9
e %= 4
print("e après calcul du reste de la division par 4 :", e)
```

</details>

---

### Exercice 4 — Opérateurs de comparaison (~3 min)

```python
# 1. Vérifiez si 15 est supérieur à 10

# 2. Vérifiez si 8 est inférieur ou égal à 8

# 3. Vérifiez si 20 est égal à 25

# 4. Vérifiez si 30 est différent de 30

# 5. Vérifiez si "Bonjour" est identique à "bonjour"
```

<details>
<summary>Corrigé</summary>

```python
# 1. Vérifiez si 15 est supérieur à 10
print(15 > 10)  # True

# 2. Vérifiez si 8 est inférieur ou égal à 8
print(8 <= 8)  # True

# 3. Vérifiez si 20 est égal à 25
print(20 == 25)  # False

# 4. Vérifiez si 30 est différent de 30
print(30 != 30)  # False

# 5. Vérifiez si "Bonjour" est identique à "bonjour"
print("Bonjour" is "bonjour")  # False
```

Pour la question 5, `is` teste l'identité (même objet en mémoire), pas l'égalité des caractères. Ici, les deux chaînes sont différentes **et** distinctes en mémoire : le résultat est `False` dans les deux cas. Pour comparer le contenu, on écrirait `"Bonjour" == "bonjour"`, qui renvoie déjà `False` — la casse entre en jeu.

</details>

---

### Exercice 5 — Opérateur d'appartenance (~3 min)

```python
# 1. Vérifiez si le caractère 'a' est présent dans la chaîne "programmation"

# 2. Vérifiez si le mot "Python" est présent dans la phrase "Le Python est un langage génial"

# 3. Vérifiez si le nombre 5 est présent dans la liste [1, 2, 3, 4, 6]

# 4. Vérifiez si la lettre 'z' est absente de la chaîne "éducation"

# 5. Vérifiez si le nombre 10 n'est pas dans la liste [2, 4, 6, 8]
```

**Avant d'ouvrir le corrigé**, vérifiez que :

- [ ] Vos questions « est absent », « n'est pas » sont écrites avec `not in` et non avec `not ... in`.
- [ ] Vous avez prévu que la recherche dans une chaîne porte sur une sous-chaîne, casse comprise.

<details>
<summary>Corrigé</summary>

```python
# 1. Vérifiez si le caractère 'a' est présent dans la chaîne "programmation"
print('a' in "programmation")  # True

# 2. Vérifiez si le mot "Python" est présent dans la phrase "Le Python est un langage génial"
print("Python" in "Le Python est un langage génial")  # True

# 3. Vérifiez si le nombre 5 est présent dans la liste [1, 2, 3, 4, 6]
print(5 in [1, 2, 3, 4, 6])  # False

# 4. Vérifiez si la lettre 'z' est absente de la chaîne "éducation"
print('z' not in "éducation")  # True

# 5. Vérifiez si le nombre 10 n'est pas dans la liste [2, 4, 6, 8]
print(10 not in [2, 4, 6, 8])  # True
```

</details>

---

## Points clés

- Sept opérateurs arithmétiques : `+` `-` `/` `*` `%` `//` `**` — dont deux posent des questions différentes d'une simple division.
- Une bibliothèque standard comme `math` s'importe puis s'appelle avec un point : `math.sqrt()`.
- Les assignations composées (`+=`, `-=`, `*=`, `/=`, `%=`) mettent une variable à jour à partir d'elle-même ; `x++` n'existe pas en Python.
- Comparer s'écrit `==`, assigner s'écrit `=`, et `is` ne compare pas la valeur mais l'objet.
- `in` / `not in` testent l'appartenance d'un élément à une chaîne ou à une collection.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Quelle expression demande « ce qu'il reste » de la division de 29 par 5 ?

- A. `29 / 5`
- B. `29 // 5`
- C. `29 % 5`
- D. `29 ** 5`

**2.** Après `x = 3` puis `x *= 3`, qu'a-t-on réellement écrit ?

- A. `x = 3`, une seule fois, sans que la valeur de `x` change ensuite
- B. `x = x * 3`, c'est-à-dire une mise à jour de `x` à partir de lui-même
- C. `x == x * 3`, donc une comparaison dont le résultat est un booléen
- D. `x + 3`, car l'astérisque se lit comme une addition dans ce contexte

**3.** Pourquoi l'instruction `x++` provoque-t-elle une erreur en Python ?

- A. Parce que Python n'autorise pas l'incrémentation avec cette syntaxe : il faut écrire `x += 1`
- B. Parce que le symbole `+` est réservé à l'addition de deux chaînes de caractères
- C. Parce que la variable doit d'abord être déclarée avec un mot-clé dédié avant tout calcul
- D. Parce que Python refuse toute modification de la valeur d'une variable après son affectation

**4.** Que teste l'opérateur `is` ?

- A. Que deux valeurs numériques sont égales, arrondies à l'entier le plus proche
- B. Qu'une valeur est bien absente d'une collection d'objets
- C. Que deux variables désignent le même objet, à la même adresse en mémoire
- D. Que deux chaînes de caractères ont le même contenu, en ignorant la casse

**5.** *Question ouverte (2-3 lignes).* Avec `x = 29` et `y = 5`, dites à quoi servent respectivement `x / y`, `x // y` et `x % y`, et donnez un usage concret du troisième.

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. C.** `%` est le modulo : il renvoie le reste de la division.
**Pourquoi :** `/` est la division classique, `//` la division entière (le quotient sans décimales), `**` la puissance. Les trois travaillent sur la même division mais répondent à trois questions différentes.

**2. B.** `x *= 3` est la forme courte de `x = x * 3`.
**Pourquoi :** un opérateur mathématique collé à `=` met la variable à jour à partir d'elle-même. `==` aurait été une comparaison, et aurait laissé `x` intact.

**3. A.** Python ne connaît pas `++`.
**Pourquoi :** le langage ne prévoit pas cette syntaxe d'incrémentation, héritée d'autres langages. `x += 1` fait exactement le travail attendu, et `x = x + 1` est la forme équivalente que tout le monde comprend.

**4. C.** `is` compare l'identité des objets, donc leur adresse en mémoire.
**Pourquoi :** `==` compare le contenu, `is` compare l'objet. La confusion entre les deux est une source classique de bugs, d'autant qu'elle donne parfois le bon résultat par hasard.

**5.** Attendu : `x / y` est la division (résultat à virgule), `x // y` la division entière (combien de fois 5 entre dans 29), `x % y` le reste. Usage concret du modulo : tester la parité (`x % 2 == 0` pour un nombre pair), numéroter des places par rangées de 5, faire tourner un cycle de couleurs.
**Pourquoi :** ces trois écritures se lisent sur une seule division euclidienne, et le modulo est celui qui sert le plus souvent dès qu'on doit regrouper, alterner ou tester une divisibilité.

</details>

---

[← Chapitre précédent](08-les-methodes-de-chaines-de-caracteres.md) · [Sommaire](Readme.md) · [Chapitre suivant →](10-formatter-les-chaines-de-caracteres.md)
