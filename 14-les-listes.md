[← Chapitre précédent](13-les-objets-muables-et-immuables.md) · [Sommaire](Readme.md) · [Chapitre suivant →](15-les-tuples.md)

# 14 - Les listes

> Une variable ne peut ranger qu'une valeur. Dès qu'un programme doit tenir une
> commande, une liste de notes ou un panier, il lui faut un contenant : la liste.
> Vous en avez déjà écrit sans le savoir — `"coucou".split()` en produit une. Ici,
> on apprend à la remplir, la vider, la découper, sans se faire surprendre par
> les index.

**Durée :** ≈ 45 min (lecture ≈ 15 min + atelier 27 min + réflexion) · **Prérequis :** [Les objets muables et immuables](13-les-objets-muables-et-immuables.md), [Les méthodes de chaînes de caractères](08-les-methodes-de-chaines-de-caracteres.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Déclarer** une liste et **accéder** à un élément par son index, y compris négatif.
- **Ajouter** et **retirer** des éléments avec `append()`, `extend()`, `insert()`, `remove()`, `pop()`.
- **Découper** une liste avec une slice, bornes omises et pas compris.
- **Exploiter** une liste avec `len()`, `index()`, `count()`, `sort()`, `filter()` et une `range`.

---

## I. Ce qu'est une liste

Les listes permettent de **représenter des collections d'objets** dans Python. Elles sont appelées `array` ou tableau dans PHP ou JavaScript. Elles vont pouvoir contenir des types d'objets différents ou non, et on va pouvoir faire des opérations d'ajout, de suppression, de modification.

```python
liste_vide    = []
liste_ints    = [1, 2, 3, 4, 5]
liste_strings = ["coucou", "ca", "va", '?']
liste_mix     = [1, "Super", True, [1, 2, "Bonjour"]]
```

Les listes reposent sur un système d'index, ce qui en fait des objets **ordonnés**. Les fonctions qui sont appliquées à une liste vont changer la valeur de la liste en mémoire : c'est un objet [muable](13-les-objets-muables-et-immuables.md).

Ce dernier point est le plus important du chapitre. `liste_mix` contient un nombre, une chaîne, un booléen **et une autre liste** : une liste n'est pas une « ligne de cases », c'est une suite de références vers des objets, de n'importe quel type.

---

## II. Ajouter ou retirer des éléments

### A. `append()` et `extend()`

`append()` permet d'ajouter un élément à la fin d'une liste, alors qu'`extend()` permet d'en ajouter plusieurs.

```python
ma_liste = [1, 2, 3]

ma_liste.append(4)
print(ma_liste) #  [1, 2, 3, 4]

ma_liste.extend([5, 6, 7])
print(ma_liste) #  [1, 2, 3, 4, 5, 6, 7]
```

La différence se voit sur un seul argument : `append([5, 6, 7])` aurait ajouté **une liste** à la fin (la liste aurait alors quatre éléments, dont une sous-liste), `extend([5, 6, 7])` ajoute les trois éléments un par un.

### B. `insert()`

Pour placer un élément ailleurs qu'en bout de liste, on donne sa **position** à `insert()`.

```python
ma_liste = [1, 2, 3]

ma_liste.insert(0, "début")
print(ma_liste) #  ['début', 1, 2, 3]
```

Le premier argument est l'index où l'élément est placé, le second l'élément lui-même. Les éléments déjà présents décalent d'une case vers la droite.

### C. `remove()`

Supprime la **première occurrence** d'un élément d'une liste.

```python
ma_liste = [1, 2, 3, 4, 3]

ma_liste.remove(3)
print(ma_liste) # [1, 2, 4, 3]
```

Le `3` de la fin est encore là : `remove()` travaille sur la valeur, pas sur une position, et s'arrête après le premier trouvé. Si la valeur n'existe pas, la méthode lève une erreur au lieu de ne rien faire.

### D. `pop()`

Enlève l'élément à un index donné. Elle permet aussi de supprimer le dernier élément si aucun index n'est fourni.

```python
liste = [1, 2, 3, 4, 3]

liste.pop(2) # Suppression de l'élément à l'index 2
print(liste) # [1, 2, 4, 3]

liste.pop() # Suppression du dernier élément
print(liste) # [1, 2, 4]
```

`pop()` se distingue de `remove()` sur deux points : elle travaille par **index**, et elle **retourne** l'élément retiré — `x = liste.pop()` retire et récupère en même temps.

---

## III. Récupérer les éléments d'une liste

Pour accéder à un élément d'une liste, on utilise des index qui représentent l'ordre dans lequel l'élément est disposé.

```python
ma_liste = [1, 2, 3, 4, 5, [10, 11]]

print(ma_liste[3])     # 4
print(ma_liste[5][1])  # 11
print(ma_liste[-1])    # Retourne le dernier élément de la liste
print(ma_liste[-2])    # Retourne l'avant-dernier élément de la liste
```

`ma_liste[5][1]` se lit de gauche à droite : le sixième élément de la grande liste est `[10, 11]`, et `[1]` va chercher le `11` à l'intérieur. On enchaîne les crochets autant de niveaux que nécessaire.

> ⚠️ **Index.** L'indice du premier élément d'une liste est toujours `0`. Le
> deuxième est `1`. Et `ma_liste[-1]` est le dernier, sans avoir à connaître la
> longueur de la liste.

---

## IV. Les slices

### A. Sélectionner une sous-partie

Les slices permettent de sélectionner une sous-partie d'une liste. Celle-ci peut être vide. Il est composé de deux index, le premier inclusif qui définit le début, le second exclusif qui définit le premier élément à ne pas prendre. Ces index sont séparés par des `:`.

```python
ma_liste = [1, 2, 3, 4, 5, 6]
print(ma_liste[3:5])   # [4, 5] - exclusion de l'index 5
```

Retenez **« début inclus, fin exclue »** : `[3:5]` prend les cases 3 et 4. C'est la convention de Python partout où l'on découpe — chaînes incluses.

### B. Omettre une borne

Pour nous faciliter l'écriture, les slices permettent d'omettre les index :

- de début, pour récupérer tout jusqu'à l'index de fin ;
- de fin, pour récupérer toute la fin de la liste après l'index de début.

```python
print(ma_liste[:2])    # [1, 2] - depuis le début jusqu'à l'index 2 exclu
print(ma_liste[2:])    # [3, 4, 5, 6] - depuis l'index 2 jusqu'à la fin
print(ma_liste[:])     # [1, 2, 3, 4, 5, 6] - toute la liste ce qui est équivalent à afficher la liste sans slicer
```

### C. Des index négatifs

Pour accroître encore cette facilité d'écriture, on a accès aux chiffres négatifs. Cela permet facilement d'écarter N éléments sans devoir écrire `len(ma_liste) - N`.

```python
print(ma_liste[2:-1])  # [3, 4, 5] - depuis l'index 2 jusqu'au dernier élément exclu (-1 représente le dernier élément)
print(ma_liste[-5:5])  # [2, 3, 4, 5] - depuis l'index -5 jusqu'à l'index 5
```

### D. Le troisième index : le pas

Il existe un troisième index qui permet de définir le pas. Cet index est optionnel et est défini à 1 par défaut.

```python
ma_liste = [1, 2, 3, 4, 5, 6]

print(ma_liste[::1])   # [1, 2, 3, 4, 5, 6] - entièreté de la liste avec un pas de 1, donc affichage normal
print(ma_liste[::2])   # [1, 3, 5] - entièreté de la liste avec un pas de 2 (1 chiffre sur 2)
print(ma_liste[2:5:2]) # [3, 5] depuis l'index 2 jusqu'à l'index 5 avec un pas de 2
print(ma_liste[::-1])  # [6, 5, 4, 3, 2, 1] - entièreté de la liste en sens inverse
```

`[::-1]` — pas de -1, donc parcours à l'envers — est le réflexe le plus utile de toute cette section : il retourne une liste en trois caractères, sans tri et sans copie manuelle.

---

## V. Diverses méthodes de liste

### A. `len()`

Retourne la longueur d'une liste ou d'une chaîne de caractères.

```python
longueur = len([1, 2, 3, 4, 5])
print(longueur) # 5
```

### B. `index()`

Retourne l'index d'un élément dans une liste.

```python
liste = [1, 2, 3]
print(liste.index(2)) # 1
```

### C. `count()`

Retourne le nombre de fois qu'un élément est présent dans une liste.

```python
liste = ["coucou", "pepito", "coucou"]
print(liste.count("coucou")) # 2
```

Les deux méthodes cherchent une **valeur** : `index()` lève une erreur si l'élément manque, `count()` retourne simplement `0`.

### D. `sort()`

Trie une liste en fonction du type d'éléments.

```python
liste_str = ['a', 'b', 'z', 'c', 'r', 'm', 'y']
liste_int = [23, 1, 2, 75, 54, 2, 42]
liste_str.sort()
liste_int.sort()

print(liste_str) # ['a', 'b', 'c', 'm', 'r', 'y', 'z']
print(liste_int) # [1, 2, 2, 23, 42, 54, 75]
```

> 📌 **Fonctionnement de la fonction.** La fonction `sort()` ne retourne rien :
> quand elle est appelée, elle va trier la liste « in place ». Pour stocker le
> résultat d'un tri d'une liste, utiliser la fonction `sorted()`.

C'est le cas d'école de l'objet [muable](13-les-objets-muables-et-immuables.md) : `sort()` modifie la liste et renvoie `None`. Écrire `ma_liste = ma_liste.sort()` détruit donc la liste en la remplaçant par `None`.

### E. `filter()`

Filtre une liste en utilisant une fonction.

```python
ma_liste = [1, 2, 33, 477, 5, 61, 73, 8]

# Filtre de la liste en ne gardant que les valeurs supérieures à 100
filtre = filter(lambda x: x > 100, ma_liste)

# Retourne un objet filter, doit être reconverti en liste
print(list(filtre))
```

Le `lambda x: x > 100` est une **fonction écrite en ligne**, sans nom : « prends `x`, renvoie vrai si `x` est plus grand que 100 ». Vous apprendrez à écrire de vraies fonctions au chapitre [Les fonctions](19-les-fonctions.md) ; pour l'instant, sachez que `filter()` en exige une et retourne un objet à reconvertir avec `list()`.

### F. `join()` et `split()`

`join()` permet de joindre les éléments d'une liste dans une même chaîne, tandis que `split()` permet de séparer une chaîne en une liste (voir [Les méthodes de chaînes de caractères](08-les-methodes-de-chaines-de-caracteres.md)).

---

## VI. Les ranges

Retourne un objet de type `range` qui, converti en liste, vous donne une suite de nombres avec un incrément de 1, commençant à la valeur `x` jusqu'à la valeur `y` exclue. Un troisième paramètre peut être ajouté pour paramétrer le pas.

```python
range_pas_1 = range(1, 10)
print(list(range_pas_1)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

range_pas_2 = range(1, 10, 2)
print(list(range_pas_2)) # [1, 3, 5, 7, 9]
```

Retrouvez la convention des slices : la borne de fin est exclue. `range(1, 10)` s'arrête donc à 9.

> ⚠️ Il faut transformer le résultat de `range` en liste avec la fonction
> `list()`, sinon l'affichage vous surprendra ! Sans conversion, on affiche
> l'objet `range` lui-même, et son nom — pas les nombres qu'il contient.

---

### Exercice 1 — Plonger dans une liste (~5 min)

```python
# Printer le nombre 5 à partir de la liste suivante
liste = [1, 2, [3, 4, [5, 6, 7]]]

# A l'aide d'une slice, extrayez une liste contenant 3 et 4
```

**Avant d'ouvrir le corrigé**, vérifiez que :

- [ ] Vous comptez les index depuis `0`, à chaque niveau de crochets.
- [ ] Votre slice utilise une borne de fin **exclue**.

<details>
<summary>Corrigé</summary>

```python
# Printer le nombre 5 à partir de la liste suivante

liste = [1, 2, [3, 4, [5, 6, 7]]]
print(liste[2][2][0])

# A l'aide d'une slice, extrayez une liste contenant 3 et 4

print(liste[2][:2])
```

`liste[2]` est `[3, 4, [5, 6, 7]]`, donc `liste[2][2]` est `[5, 6, 7]` et `liste[2][2][0]` est `5`. Chaque crochet descend d'un niveau, et l'index `2` de la liste d'origine correspond bien au **troisième** élément.

</details>

---

### Exercice 2 — Un texte, des phrases, un ordre inverse (~12 min)

```python
# A partir du texte suivant, créer une liste contenant chacune des phrases
# Créer une slice regroupant les phrases du texte en inversant leur ordre d'apparition
# Joindre la slice avec un antislash pour séparateur et printer le résultat

texte = "Les Cucurbitaceae (Cucurbitacées) sont une famille de plantes dicotylédones de l'ordre des Cucurbitales, originaires pour la plupart des régions tropicales et subtropicales, qui comprend environ 800 espèces réparties en 180 genres. Ce sont généralement des plantes herbacées, annuelles ou vivaces, à port rampant ou grimpant, aux tiges munies de vrilles, et plus rarement des arbustes. Ces plantes sont sensibles au gel. Les fleurs sont unisexuées, portées parfois par les mêmes plantes (monoïques), parfois par des plantes différentes (dioïques). Les fruits sont le plus souvent des baies modifiées appelées péponides, plus rarement des fruits secs (capsules, samares). De nombreuses espèces sont cultivées pour leur fruits comestibles (courges, courgettes, concombres, cornichons, doubeurres, melons, pastèques, chayotes, etc.) et parfois pour leurs graines (courge à huile, pistache africaine). Leur domestication est très ancienne et remonte à plusieurs milliers d'années, tant dans le Nouveau Monde (Cucurbita, Sechium) que dans l'Ancien (Citrullus, Cucumis, Lagenaria, Luffa, Albanus Quénetus)."
```

**Avant d'ouvrir le corrigé**, vérifiez que :

- [ ] Vous découpez sur `". "` (point **et** espace), pas sur `"."` seul — sinon chaque phrase garderait sa ponctuation et une chaîne vide apparaîtrait.
- [ ] L'inversion passe par une slice à pas négatif, pas par un tri.
- [ ] L'antislash est écrit `'\\'` dans le code.

*Pour aller plus loin (facultatif).* Comptez le nombre de phrases obtenues avec `len()`, puis vérifiez que le dernier élément de la liste inversée est bien la première phrase du texte.

<details>
<summary>Corrigé</summary>

```python
texte = "Les Cucurbitaceae (Cucurbitacées) sont une famille de plantes dicotylédones de l'ordre des Cucurbitales, originaires pour la plupart des régions tropicales et subtropicales, qui comprend environ 800 espèces réparties en 180 genres. Ce sont généralement des plantes herbacées, annuelles ou vivaces, à port rampant ou grimpant, aux tiges munies de vrilles, et plus rarement des arbustes. Ces plantes sont sensibles au gel. Les fleurs sont unisexuées, portées parfois par les mêmes plantes (monoïques), parfois par des plantes différentes (dioïques). Les fruits sont le plus souvent des baies modifiées appelées péponides, plus rarement des fruits secs (capsules, samares). De nombreuses espèces sont cultivées pour leur fruits comestibles (courges, courgettes, concombres, cornichons, doubeurres, melons, pastèques, chayotes, etc.) et parfois pour leurs graines (courge à huile, pistache africaine). Leur domestication est très ancienne et remonte à plusieurs milliers d'années, tant dans le Nouveau Monde (Cucurbita, Sechium) que dans l'Ancien (Citrullus, Cucumis, Lagenaria, Luffa, Albanus Quénetus)."

phrases = texte.split('. ')       # split de chaque phrase du texte dans une liste
first_last = phrases[::-1]        # pas de -1 = à l'envers
join_list = '\\'.join(first_last) # on échappe le \ pour joindre avec

print(join_list)
```

Les trois gestes du chapitre, alignés :

- `split('. ')` transforme la chaîne en liste (chapitre précédent) ;
- `[::-1]` retourne la liste sans la trier — un tri aurait classé les phrases alphabétiquement, ce n'est pas la consigne ;
- `'\\'.join(...)` recolle les morceaux. Un antislash seul dans une chaîne d'échappe lui-même, d'où les deux.

Dernier détail : la **dernière** phrase du texte se termine par `."` sans espace derrière, donc `split('. ')` ne la coupe pas et elle garde son point final. C'est visible à l'affichage, et ce n'est pas une erreur.

</details>

---

### Exercice 3 — Insérer, trier… et filtrer (~10 min)

```python
# Ajouter/insérer 2 en dernier élément de la liste
# Ajouter/insérer 31 en premier élément de la liste
# Ajouter/insérer 100 au milieu de la liste (doit fonctionner quelle que soit la longueur de la liste)
# Printer la liste obtenue
# Créer un objet filter, qui ne retient de la liste que les éléments inférieurs ou égaux à 30
# Printer l'objet sous forme d'une liste

li = [23, 12, 7, 38, 90, 9, 1, 0]
```

**Avant d'ouvrir le corrigé**, vérifiez que :

- [ ] Le « milieu » est calculé à partir de `len()`, et non écrit en dur.
- [ ] La position centrale est un **entier** : une division `/` donnerait un `float` que `insert()` refuse.
- [ ] Votre objet `filter` est reconstruit en liste avant l'affichage.

<details>
<summary>Corrigé</summary>

```python
li = [23, 12, 7, 38, 90, 9, 1, 0]
li.append(2)
li.insert(0, 31)
li.insert(len(li) // 2, 100)
print(li)
filtre = filter(lambda x: x <= 30, li)
print(list(filtre))
```

Quatre méthodes du chapitre travaillent ici :

- `append(2)` pour la fin, `insert(0, 31)` pour le début ;
- `len(li) // 2` pour le milieu : **division entière**, comme au chapitre des opérateurs. Écrire `len(li) / 2` donnerait un nombre à virgule et `insert()` refuserait l'index ;
- `filter()` avec un `lambda`, puis `list()` pour rendre le résultat lisible.

**Note sur le nom de la variable.** La correction d'origine écrivait `filter = filter(...)`. Cela fonctionne, mais **écrase** la fonction `filter()` pour tout le reste du script : un second filtrage plus bas échouerait sans raison apparente. C'est exactement le piège signalé au chapitre des modules à propos des imports — on nomme la variable `filtre`.

</details>

---

## Points clés

- Une liste est **ordonnée** (index de `0` au dernier) et **muable** : les méthodes la modifient en place.
- Ajouter : `append()` en fin, `extend()` plusieurs d'un coup, `insert(index, valeur)` à une position précise.
- Retirer : `remove(valeur)` sur la première occurrence trouvée, `pop(index)` par position — et `pop()` retourne ce qu'il retire.
- Une slice est `début inclus, fin exclue` ; les bornes peuvent être omises, négatives, et un troisième index donne le pas (`[::-1]` retourne).
- `sort()` trie sur place et retourne `None` ; `sorted()` retourne une nouvelle liste.
- `range()` et les slices partagent la même convention de borne exclue, et `range()` s'affiche avec `list()`.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Que renvoie `ma_liste[1:3]` sur la liste `[10, 20, 30, 40, 50]` ?

- A. `[10, 20, 30]`, les index 1 à 3 étant pris des deux côtés inclusivement
- B. `[20, 30]`, la borne de début étant incluse et celle de fin exclue
- C. `[30, 40]`, les index étant décalés d'une case après le premier élément
- D. `[20, 30, 40]`, Python incluant toujours un élément de marge au-delà de la borne

**2.** Quelle différence entre `append([5, 6])` et `extend([5, 6])` sur une liste de trois éléments ?

- A. Aucune, les deux ajoutent deux éléments et la liste passe à cinq
- B. `append` ajoute une sous-liste (la liste passe à quatre éléments), `extend` ajoute 5 puis 6 (cinq éléments)
- C. `append` fonctionne en fin de liste, `extend` uniquement en début de liste
- D. `append` refuse les listes en argument et lève une erreur, `extend` les accepte

**3.** Après `notes = [3, 1, 2]` puis `notes = notes.sort()`, que vaut `notes` ?

- A. `[1, 2, 3]`, la liste étant triée puis réaffectée
- B. `[3, 1, 2]`, la méthode n'ayant aucun effet sur une liste de nombres
- C. `None`, car `sort()` trie sur place et ne retourne rien
- D. Une erreur, le tri d'une liste ne pouvant pas être réaffecté à la même variable

**4.** Pourquoi écrire `li.insert(len(li) // 2, 100)` plutôt que `li.insert(len(li) / 2, 100)` ?

- A. Parce que `//` renvoie un entier, seule valeur qu'un index accepte
- B. Parce que `/` est plus lent que `//` sur un grand nombre d'éléments
- C. Parce que `//` arrondit systématiquement au-dessus, ce qui convient mieux
- D. Parce que `/` ne fonctionne pas sur le résultat de la fonction `len()`

**5.** *Question ouverte (2-3 lignes).* À partir de `notes = [12, 8, 15, 6, 20]`, écrivez une ligne qui retourne les notes supérieures ou égales à 10 sous forme de liste, puis expliquez pourquoi `list()` est nécessaire.

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. B.** `[20, 30]`.
**Pourquoi :** index 1 → 20, index 2 → 30, index 3 exclu. La même règle s'applique aux chaînes et à `range()` : c'est la convention de découpe de Python, pas une exception de ce type.

**2. B.** C'est la question la plus fréquente sur ces deux méthodes.
**Pourquoi :** `extend()` itère sur l'argument et ajoute chaque élément un par un ; `append()` traite l'argument comme **un seul objet**. Une sous-liste dans une liste est licite (`liste_mix` en donnait un exemple), donc rien n'erre — la liste est simplement différente de ce qu'on voulait.

**3. C.** `sort()` retourne `None`.
**Pourquoi :** elle trie la liste en place, puis ne rend rien. L'affectation écrase donc la liste triée par la valeur `None`. Écrire `notes.sort()` seul, ou `notes = sorted(notes)` si l'on veut vraiment une affectation.

**4. A.** Un index doit être un entier.
**Pourquoi :** `/` produit toujours un `float` en Python 3 — `4.0` ici — et `insert()` refuse. `//` est la division entière du chapitre des opérateurs. Et non, `//` n'arrondit pas au-dessus : il tronque vers le bas.

**5.** Attendu :

```python
print(list(filter(lambda x: x >= 10, notes)))
```

`filter()` ne retourne pas une liste mais un **objet `filter`**, un itérable paresseux : tant qu'on ne le parcourt pas, il n'a rien produit. `list()` le parcourt et materialise le résultat, seul moyen de l'afficher correctement ou de lui demander sa longueur.
**Pourquoi :** c'est le comportement annoncé dans le chapitre — « retourne un objet filter, doit être reconverti en liste ». Sans `list()`, l'affichage montre un objet `filter` sans rapport avec les notes.

</details>

---

[← Chapitre précédent](13-les-objets-muables-et-immuables.md) · [Sommaire](Readme.md) · [Chapitre suivant →](15-les-tuples.md)
