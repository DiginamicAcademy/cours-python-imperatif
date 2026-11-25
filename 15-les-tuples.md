[← Chapitre précédent](14-les-listes.md) · [Sommaire](Readme.md) · [Chapitre suivant →](16-les-boucles.md)

# 15 - Les tuples

> Une liste qui refuse qu'on la modifie, cela paraît inutile. C'est au contraire
> la structure la plus sûre du langage : impossible d'ajouter, d'oublier, de
> trier de travers. Et Python la récompense — un tuple va plus vite qu'une liste à
> contenu identique.

**Durée :** ≈ 20 min (lecture ≈ 8 min + atelier 8 min + réflexion 4 min) · + 6 min facultatif · **Prérequis :** [Les listes](14-les-listes.md), [Les objets muables et immuables](13-les-objets-muables-et-immuables.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Déclarer** un tuple et **dire** ce qui le distingue d'une liste.
- **Convertir** une liste en tuple et un tuple en liste.
- **Distinguer** le tuple, immuable, des objets muables qu'il contient.
- **Choisir** entre liste et tuple selon la taille de la collection et les opérations prévues.

---

## I. Définir un tuple

Les tuples sont des collections comme [les listes](14-les-listes.md) à l'exception qu'ils sont [immuables](13-les-objets-muables-et-immuables.md), et qu'**on ne peut plus modifier leur contenu une fois initialisé**.

```python
# Les tuples s'initialisent comme des listes mais en utilisant les parenthèses (optionnelles mais fortement conseillées pour la lisibilité)
mon_tuple = (1, 2, 3)
mon_tuple_mix = ("coucou", True, 45, [1, 2, 3])
```

Comme une liste, un tuple accepte des types différents et peut contenir une autre collection. Comme une liste aussi, il est **ordonné** : `mon_tuple[0]` vaut `1`, `mon_tuple[-1]` vaut `3`. Ce qui change, c'est ce que vous avez le droit de faire **après**.

---

## II. Convertir entre liste et tuple

On peut convertir un tuple en une liste avec la fonction `list()`, et inversement avec la fonction `tuple()`.

```python
mon_tuple = (1, 2, 3)

print(list(mon_tuple))  # [1, 2, 3]
print(tuple([1, 2, 3])) # (1, 2, 3)
```

Ces deux allers-retours sont le moyen le plus simple de travailler sur un tuple : on le convertit en liste, on modifie, on reconvertit. Vous ferez exactement cela dans l'exercice 1.

---

## III. Immuable, mais pas blindé

On ne peut certes pas modifier un tuple, mais on peut modifier les **objets muables** qui appartiennent au tuple.

```python
mon_tuple_mix = ("coucou", True, 45, [1, 2, 3])

mon_tuple_mix[3][0] = 42 # Pour rappel une liste est un objet muable
print(mon_tuple_mix)     # ('coucou', True, 45, [42, 2, 3])
```

Lisons la ligne de droite à gauche : `mon_tuple_mix[3]` désigne la liste `[1, 2, 3]` — le tuple, lui, ne bouge pas, on ne remplace aucun de ses éléments — puis `[0] = 42` modifie **cette liste**, qui est muable. Ce que le tuple garantit, c'est la stabilité de **ses références** : ni ajout, ni retrait, ni remplacement d'un élément (`mon_tuple_mix[1] = 200` lève une `TypeError`). Ce qu'il ne garantit pas, c'est le contenu des objets muables qu'il héberge.

---

## IV. Quel intérêt ?

Les tuples proposent moins de fonctionnalités mais apportent de **meilleures performances**. C'est une structure de données à privilégier lorsque l'on sait d'avance le nombre d'éléments qu'il y aura dans notre collection et qu'on n'a pas besoin d'y faire des opérations d'ajout, de modification ou de suppression.

Trois situations où le tuple est le bon choix :

- une **collection à taille fixe** : les coordonnées d'un point, un couple `(clé, valeur)`, les composantes RGB d'une couleur ;
- une donnée que l'on veut **protéger contre la modification** — y compris par son propre code plus bas dans le fichier ;
- un **retour multiple** depuis une fonction, comme le renvoie `enumerate()` vu au chapitre suivant.

Le réflexe inverse est tout aussi simple : dès qu'il faut ajouter, retirer ou trier, on prend une liste.

---

### Exercice 1 — Créer, convertir, reconvertir (~4 min)

```python
# 1. Créez un tuple avec les éléments suivants : 10, 20, 30, 40. Affichez ce tuple.

# 2. Convertissez ce tuple en une liste, puis affichez cette liste.

# 3. Modifiez le premier élément de la liste pour qu'il soit égal à 15, puis affichez la liste.

# 4. Convertissez la liste modifiée en un nouveau tuple, puis affichez ce nouveau tuple.
```

**Avant d'ouvrir le corrigé**, vérifiez que :

- [ ] À l'étape 3, vous modifiez la **liste**, pas le tuple.
- [ ] Le tuple final est bien reconstruit avec `tuple()`, et non laissé en liste.

<details>
<summary>Corrigé</summary>

```python
# 1. Créez un tuple avec les éléments suivants : 10, 20, 30, 40. Affichez ce tuple.
mon_tuple = (10, 20, 30, 40)
print("Tuple d'origine :", mon_tuple)

# 2. Convertissez ce tuple en une liste, puis affichez cette liste.
ma_liste = list(mon_tuple)
print("Liste convertie :", ma_liste)

# 3. Modifiez le premier élément de la liste pour qu'il soit égal à 15, puis affichez la liste.
ma_liste[0] = 15
print("Liste modifiée :", ma_liste)

# 4. Convertissez la liste modifiée en un nouveau tuple, puis affichez ce nouveau tuple.
nouveau_tuple = tuple(ma_liste)
print("Nouveau tuple :", nouveau_tuple)
```

Essayez, pour voir, d'écrire `mon_tuple[0] = 15` à la place de l'étape 2 : Python répond `TypeError: 'tuple' object does not support item assignment`. C'est le message que vous chercherez un jour sans le comprendre — autant le croiser maintenant, dans un exercice où il n'a rien de grave.

</details>

---

### Exercice 2 — Modifier sans modifier (~4 min)

```python
# 1. Créez un tuple contenant une chaîne de caractères, un nombre, et une liste. Affichez ce tuple.

# 2. Accédez au troisième élément du tuple (la liste) et modifiez son premier élément pour qu'il soit égal à 10. Affichez le tuple.

# 3. Essayez de modifier le deuxième élément du tuple directement pour qu'il soit égal à 200. Que se passe-t-il ?
```

<details>
<summary>Corrigé</summary>

```python
# 1. Créez un tuple contenant une chaîne de caractères, un nombre, et une liste. Affichez ce tuple.
mon_tuple_mix = ("bonjour", 100, [1, 2, 3])
print("Tuple d'origine :", mon_tuple_mix)

# 2. Accédez au troisième élément du tuple (la liste) et modifiez son premier élément pour qu'il soit égal à 10. Affichez le tuple.
mon_tuple_mix[2][0] = 10
print("Tuple après modification indirecte :", mon_tuple_mix)

# 3. Essayez de modifier le deuxième élément du tuple directement pour qu'il soit égal à 200. Que se passe-t-il ?
# mon_tuple_mix[1] = 200  # Cette ligne doit être commentée pour éviter une erreur
# La ligne ci-dessus lève une erreur car les tuples sont immuables
```

**Réponse à la question 3.** La ligne décommentée lève une `TypeError`, exactement comme à l'exercice précédent. La nuance est là, et c'est tout l'enjeu de l'exercice : l'étape 2 **passe**, alors qu'elle change ce qui s'affiche. Le tuple n'a pas été touché — ses trois références sont les mêmes — c'est la liste qu'il désigne qui a changé de contenu. Immuable veut dire « ses éléments ne bougent pas », pas « rien de ce qu'il montre ne bouge ».

</details>

---

### Exercice 3 — Tuple ou liste, la course (~6 min, facultatif)

```python
# 1. Créez un tuple contenant les nombres de 1 à 1000. Utilisez la fonction range() pour vous aider.

# 2. DEFI : Comparez le temps de création d'un tuple et d'une liste contenant les mêmes éléments en utilisant la fonction time de la bibliothèque time.
# Note: Les résultats de temps peuvent varier en fonction de l'environnement d'exécution
import time
```

> 📌 La consigne d'origine portait sur un million d'éléments ; le corrigé travaille
> sur 1000 pour rester rapide à exécuter en salle. Gardez la même écriture avec
> `range(1, 1_000_001)` si vous voulez une mesure plus nette.

<details>
<summary>Corrigé</summary>

```python
# 1. Créez un tuple contenant les nombres de 1 à 1000. Utilisez la fonction range() pour vous aider.
grand_tuple = tuple(range(1, 1001))
print("Premier élément du grand tuple :", grand_tuple[0])
print("Dernier élément du grand tuple :", grand_tuple[-1])

# 2. DEFI : Comparez le temps de création d'un tuple et d'une liste contenant les mêmes éléments en utilisant la fonction time de la bibliothèque time.
# Note: Les résultats de temps peuvent varier en fonction de l'environnement d'exécution
import time

debut_liste = time.time()
grande_liste = list(range(1, 1001))
fin_liste = time.time()
temps_liste = fin_liste - debut_liste

debut_tuple = time.time()
grand_tuple = tuple(range(1, 1001))
fin_tuple = time.time()
temps_tuple = fin_tuple - debut_tuple

print("Temps de création de la liste :", temps_liste)
print("Temps de création du tuple :", temps_tuple)
```

**Lisez le résultat avec honnêteté.** À 1000 éléments, les deux durées se chiffrent en millionièmes de seconde : le premier tour peut très bien donner la liste plus rapide, le second le tuple, sans que cela veuille dire quoi que ce soit. La machine est occupée, le premier appel prépare aussi le terrain. Ce n'est pas un échec de l'exercice, c'est une leçon sur les mesures : avant de conclure, montez à un million d'éléments et relancez plusieurs fois.

Ce que l'on vérifie alors, et qui est stable, c'est l'affirmation du chapitre : à contenu égal, un tuple se crée plus vite et occupe moins de mémoire qu'une liste — Python n'a pas à prévoir de place pour des ajouts futurs.

</details>

---

## Points clés

- Un tuple est une collection ordonnée **immuable** : ni ajout, ni retrait, ni remplacement d'élément.
- `list()` et `tuple()` convertissent dans un sens comme dans l'autre ; c'est la façon propre de faire évoluer un tuple.
- L'immuabilité porte sur les **références** du tuple : une liste qu'il contient reste modifiable.
- Moins de méthodes, mais de meilleures performances : le tuple est le choix par défaut quand la taille est connue.
- `TypeError: 'tuple' object does not support item assignment` = on a essayé d'écrire dans un tuple.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Quelle ligne lève une erreur ?

- A. `point = (3, 4)` puis `print(point[1])`
- B. `point = (3, 4)` puis `point = (5, 6)`
- C. `point = (3, 4)` puis `point[1] = 9`
- D. `point = (3, 4)` puis `autre = tuple(list(point))`

**2.** Un tuple contient une liste. Que se passe-t-il si l'on modifie cette liste ?

- A. Rien : l'immuabilité du tuple protège tout ce qu'il contient
- B. Le tuple se convertit automatiquement en liste pour permettre l'opération
- C. La modification réussit : le tuple reste immuable, c'est la liste hébergée qui change
- D. Python remplace l'ancienne liste par la nouvelle, ce qui casse l'immuabilité du tuple

**3.** Pourquoi écrire `mon_tuple = (1, 2, 3)` plutôt que `mon_tuple = 1, 2, 3` ?

- A. Parce que sans parenthèses, Python crée trois variables distinctes et non un tuple
- B. Parce que les parenthèses sont optionnelles mais rendent l'intention lisible à la relecture
- C. Parce que les parenthèses sont obligatoires et la seconde écriture est une erreur
- D. Parce que les parenthèses améliorent les performances à la création du tuple

**4.** Vous stockez les quatre composantes d'une couleur RGBa et ne les modifierez jamais. Pourquoi le tuple plutôt que la liste ?

- A. Parce qu'il est plus rapide, plus léger, et qu'une écriture par erreur devient impossible
- B. Parce qu'une liste ne peut pas contenir quatre éléments de type entier
- C. Parce qu'un tuple autorise des méthodes de tri que la liste n'a pas
- D. Parce qu'un tuple peut être affiché alors qu'une liste doit être convertie

**5.** *Question ouverte (2-3 lignes).* Vous recevez un tuple de notes et devez en retrancher la plus basse, donc modifier le contenu. Décrivez les trois étapes, sans jamais écrire dans le tuple.

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. C.** Écrire dans un tuple est interdit.
**Pourquoi :** `point[1] = 9` demande le remplacement d'une référence, ce qu'un tuple refuse. En revanche, lire (`point[1]`) est libre, et **réaffecter la variable** à un autre tuple (réponse B) ne modifie rien : c'est une nouvelle liaison, pas une modification de l'objet.

**2. C.** La liste modifiable reste modifiable.
**Pourquoi :** c'est l'exemple `mon_tuple_mix[3][0] = 42` du chapitre. Le tuple garantit ses références, pas le contenu des objets muables qu'il pointe. À retenir, car cette nuance explique des comportements qui semblent d'abord illogiques.

**3. B.** Les parenthèses sont optionnelles, mais fortement conseillées.
**Pourquoi :** la seconde écriture produit bien un tuple — mais à la relecture, rien ne le dit. Dans une affectation multiple, l'absence de parenthèses devient même source de confusion de sens.

**4. A.** Taille connue, aucune modification prévue : le tuple gagne sur les trois plans.
**Pourquoi :** performances et mémoire sont l'argument du chapitre ; la sûreté vient avec. Un `couleur[3] = 0` oublié se signalera de lui-même par une erreur, au lieu de passer inaperçu dans une liste.

**5.** Attendu : `notes_liste = list(notes)` pour convertir en liste ; on repère la plus basse — par exemple avec `notes_liste.sort()`, qui la place en index 0 (chapitre des listes) — puis `notes_liste.remove(notes_liste[0])` ; enfin `resultat = tuple(notes_liste)` si la valeur finale doit être un tuple.
**Pourquoi :** c'est le détour enseigné à l'exercice 1 : on ne lutte pas contre l'immuabilité, on la contourne par une conversion aller-retour. Une variante équivalente — reconstruire un tuple par compréhension en excluant le minimum — est également juste, puisqu'elle ne touche pas le tuple d'origine.

</details>

---

[← Chapitre précédent](14-les-listes.md) · [Sommaire](Readme.md) · [Chapitre suivant →](16-les-boucles.md)
