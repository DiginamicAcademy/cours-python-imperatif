[← Chapitre précédent](03-les-nombres.md) · [Sommaire](Readme.md) · [Chapitre suivant →](05-variables-notions-plus-avancees.md)

# 04 - Les booléens

> Une valeur qui ne peut être que vraie ou fausse semble trop simple pour être
> utile. En réalité, tout le programme en dépend : ce sont les booléens qui
> décident, et ils se cachent dans des endroits surprenants.

**Durée :** ≈ 10 min (lecture ≈ 7 min + réflexion) · **Prérequis :** [Les variables](01-les-variables.md), [Les nombres](03-les-nombres.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Écrire** les deux seules valeurs booléennes de Python.
- **Expliquer** pourquoi `bool` est une sous-classe de `int` et ce que ça implique.
- **Utiliser** la fonction `bool()` pour déterminer la « véracité » d'une valeur.
- **Retenir** quelles valeurs sont considérées fausses dans chaque type.

---

## I. Deux valeurs, et pas une de plus

Un **booléen** (type `bool`) ne peut avoir que deux valeurs, **vraie** ou
**fausse** :

```python
bool_true = True
bool_false = False
```

Attention à l'écriture : `True` et `False` prennent une majuscule initiale, et ce
sont des mots réservés du langage — vous ne pouvez pas les utiliser comme noms de
variables. `true`, `TRUE` ou `vrai` soulèveraient une erreur.

---

## II. Le booléen, un entier qui s'ignore

### A. `bool` est une sous-classe de `int`

Les booléens sont une **sous-classe des nombres entiers** : `True` est équivalent
à `1` et `False` à `0`. Pour s'en convaincre, l'interpréteur Python nous retourne
`True` à la question :

```python
true_or_false = issubclass(bool, int)

print(true_or_false) # True
```

### B. On peut additionner un booléen et un entier

Grâce aux fonctionnalités de **transtypage implicite** de Python — la conversion
faite automatiquement par le langage, sans que vous l'écriviez — on peut additionner
des `bool` avec des `int` :

```python
print(True + 3) # 4
```

Ce n'est pas une coquetterie : vous manipulerez cette propriété sans le savoir
quand vous compterez des éléments valides — chaque valeur vraie comptant pour 1.
Le chapitre 11, sur les conditions, rendra ce réflexe utile.

---

## III. La fonction `bool()` : une valeur est-elle « vraie » ?

La fonction `bool()` permet de savoir si une valeur est vraie ou fausse, quel que
soit son type. Chaque type a sa manière de considérer une valeur comme **fausse** :

```python
print(bool(""))       # False
print(bool("Python")) # True pour n'importe quelle string non vide

print(bool(0))        # False
print(bool(12))       # True pour n'importe quel int différent de 0

print(bool(0.0))      # False
print(bool(-1.2))     # True pour n'importe quel float différent de 0.0

print(bool([]))       # False
print(bool([0]))      # True pour n'importe quelle liste non vide

print(bool({}))       # False
print(bool({0:0}))    # True pour n'importe quel dictionnaire non vide
```

Le motif se répète d'un type à l'autre : **le vide et le zéro sont faux, tout le
reste est vrai**. Un point de détail qui a son importance : `[0]` est **vraie**,
alors que `0` est fausse — c'est la liste qui est pleine, pas la valeur qu'elle
contient qui compte.

Retenez cette table, car elle commande les conditions : une chaîne lue au clavier
vide, une liste sans élément et un zéro se testeront tous les trois de la même
façon.

---

## Points clés

- Un booléen vaut `True` ou `False`, **avec une majuscule** ; ce sont des mots réservés.
- `bool` est une **sous-classe de `int`** : `True` vaut `1`, `False` vaut `0`.
- Le transtypage implicite autorise `True + 3`, qui donne `4`.
- `bool(valeur)` répond vrai ou faux : **le vide et le zéro sont faux**, tout le
  reste est vrai.
- `bool([0])` est `True` : c'est le **contenant** qui est jugé, pas le contenu.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Quelles sont les valeurs booléennes de Python ?

- A. `True` et `False`, avec une majuscule initiale, toutes deux réservées au langage
- B. `true` et `false`, en minuscules, comme dans la plupart des langages dérivés du C
- C. `vrai` et `faux`, puisque l'interpréteur accepte les mots français
- D. `1` et `0` uniquement, le type booléen n'existant pas en Python

**2.** Ce que `issubclass(bool, int)` renvoie nous apprend que :

- A. Tout entier est aussi un booléen, et peut donc servir de drapeau vrai ou faux
- B. Le type booléen hérite du type entier, `True` valant 1 et `False` valant 0
- C. Les booléens et les entiers sont deux types sans aucun rapport entre eux
- D. Le type booléen est plus vaste que le type entier, puisqu'il accepte ses valeurs

**3.** Que vaut `True + 3` ?

- A. Une erreur, puisque l'on n'additionne pas un booléen avec un entier
- B. `4`, grâce au transtypage implicite qui lit `True` comme l'entier 1
- C. `True3`, le résultat étant alors une chaîne de caractères
- D. `3`, le booléen étant ignoré dans une addition avec un entier

**4.** Parmi ces valeurs, laquelle est considérée **vraie** par `bool()` ?

- A. `""`, puisqu'une chaîne existe même sans contenu
- B. `[0]`, puisque la liste n'est pas vide
- C. `0`, puisque zéro est un nombre à part entière
- D. `{}`, puisque le dictionnaire est bien un conteneur

**5.** *Question ouverte (2-3 lignes).* Vous lisez une réponse au clavier (chapitre 07) et vous voulez savoir si l'utilisateur a réellement tapé quelque chose. Sans condition encore vue, quelle fonction vous renseigne, et que renvoie-t-elle sur une entrée vide ?

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. A.** Seuls `True` et `False`, majuscule comprise, sont des booléens ; ce sont d'ailleurs des mots réservés.
**Pourquoi :** le chapitre signale explicitement l'écriture, car les minuscules — réflexe venu d'autres langages — soulèvent une erreur.

**2. B.** `bool` hérite de `int` : c'est le sens de `issubclass(bool, int)`, qui renvoie `True`.
**Pourquoi :** la conséquence directe est que `True` équivaut à `1` et `False` à `0`. L'inverse serait faux : tous les entiers ne sont pas des booléens.

**3. B.** `True` devient `1` et l'addition donne `4`.
**Pourquoi :** le chapitre donne cet exemple exact pour illustrer le transtypage implicite, et annonce qu'on réutilisera cette propriété en comptant des valeurs vraies.

**4. B.** `[0]` est une liste non vide, donc vraie ; le `0` qu'elle contient n'est pas jugé.
**Pourquoi :** la table du chapitre oppose précisément `bool([])` faux et `bool([0])` vrai, et c'est l'exception piège à retenir.

**5.** Attendu : la fonction `bool()`, qui renvoie `False` sur une chaîne vide — donc sur une entrée où l'utilisateur n'a rien tapé — et `True` dès qu'un caractère est présent.
**Pourquoi :** c'est la règle du chapitre (le vide et le zéro sont faux) appliquée au cas concret d'une saisie clavier, que nous formaliserons avec les conditions au chapitre 11.

</details>

---

[← Chapitre précédent](03-les-nombres.md) · [Sommaire](Readme.md) · [Chapitre suivant →](05-variables-notions-plus-avancees.md)
