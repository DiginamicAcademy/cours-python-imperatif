[← Chapitre précédent](15-les-tuples.md) · [Sommaire](Readme.md) · [Chapitre suivant →](17-les-dictionnaires.md)

# 16 - Les boucles

> « Printer chaque élément d'une liste » ne s'écrit pas en huit `print()`. Une
> boucle, c'est un ordre qu'on donne une fois et que Python répète — et tout
> l'enjeu est de savoir **quand il s'arrête**. Vous verrez ici les deux formes de
> boucles, les deux mots-clés qui les commandent, et une écriture compacte qu'il
> faut savoir lire plus que produire.

**Durée :** ≈ 55 min (lecture ≈ 18 min + atelier 29 min + réflexion 8 min) · + 8 min facultatif · **Prérequis :** [Les listes](14-les-listes.md), [Les structures conditionnelles](11-les-structures-conditionnelles.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Parcourir** une collection, une chaîne ou un `range` avec `for`, et retrouver les index avec `enumerate()`.
- **Répéter** une action avec `while` et **garantir** la condition de sortie.
- **Interrompre** une itération avec `continue` ou une boucle avec `break`, et comprendre le `else` d'une boucle.
- **Reconnaître** une compréhension de liste et utiliser `any()` / `all()` dans une condition.

---

## I. La boucle `for`

La boucle `for` est très pratique pour **boucler sur les éléments d'une collection**.

Les chaînes de caractères sont en quelque sorte une **collection** de caractères et on peut à ce titre boucler dessus de la même façon. Enfin les [ranges](14-les-listes.md) vus précédemment peuvent être parcourus sans avoir à les convertir en liste.

```python
ma_liste = [1, 2, 3, 4]
for nb in ma_liste:
    print(nb + 2) # Nous printons chaque chiffre dans ma_liste en ajoutant 2

ma_string = "python"
for char in ma_string:
    print(f"la lettre {char} !")

for x in range(5):
    print(x)
```

Les trois boucles ont la même forme : `for <élément> in <collection>:`. Python prend le premier élément, exécute le bloc indenté, passe au suivant, et s'arrête quand la collection est épuisée. Il n'y a **aucun compteur à écrire** : c'est ce qui distingue `for` de `while`.

Notez au passage que le nom de la variable d'itération est libre : `nb`, `char`, `x`, `element`… mais qu'elle garde sa **dernière valeur** après la boucle.

### A. Retrouver les index avec `enumerate()`

Pour accéder aux **index** des éléments lorsqu'on boucle sur une liste, il est pertinent d'utiliser `enumerate()`.

```python
ma_liste = ['a', 'b', 'c', 'd', 'e']
for index, char in enumerate(ma_liste):
    print(f"la lettre {char} est à l'index {index}.")
```

> 📌 Vous remarquerez que la fonction `enumerate` permet à la fois d'obtenir la
> valeur de chaque élément de la liste mais également son index.

C'est l'`enumerate()` du chapitre sur les tuples, retrouvé ici dans une boucle : deux variables après le `for`, parce que `enumerate()` fournit un couple `(index, valeur)` à chaque tour — on le « déballle » directement.

---

## II. La boucle `for… else`

Cette boucle se comporte comme une boucle `for` à l'exception qu'une branche `else` est placée **au niveau du `for`** (et non dans le `if` de l'intérieur) : elle s'exécute si la boucle s'est terminée normalement, c'est-à-dire si aucun `break` n'a été rencontré.

```python
ma_liste = [False, False, False, False, False]

for booleen in ma_liste:
    if booleen is True:
        print("élément vrai trouvé!")
        break
else:
    print("Tous les éléments de la liste sont faux 🥲")
```

Lisons le parcours : aucun élément n'est `True`, donc aucun `break` n'est exécuté, la boucle va jusqu'au bout, et le `else` s'affiche. Si un seul `True` s'était trouvé, le `break` aurait coupé la boucle **et** sauté le `else`.

C'est une particularité de Python, qui surprend même des développeurs expérimentés : le `else` d'une boucle répond à « **est-ce que je suis allé au bout ?** », pas à « est-ce que le test a échoué ? ». Il est à son place quand on cherche quelque chose : `else` = « je ne l'ai pas trouvé ».

---

## III. La boucle `while`

La boucle `while` va répéter des instructions **tant que** sa condition n'est pas remplie.

```python
total = 20
x = 0

while x < total:
    print(x)
    x += 1 # on n'oublie pas d'incrémenter x à chaque itération
```

> 📌 La notation `x++` n'existe pas en Python — vous l'avez déjà vu au chapitre
> des opérateurs.

> ⚠️ **Boucle infinie.**
>
> Attention à garantir une condition de sortie à votre boucle sous peine de créer
> une boucle infinie. Dans l'exemple précédent, si je n'incrémente pas `x` à
> chaque itération, il sera toujours inférieur à `total` et on ne sortira jamais
> de la boucle.

Le choix entre les deux boucles se pose dès qu'on écrit : avec un **nombre d'éléments à parcourir**, prenez `for` ; avec une **condition à attendre** — une saisie valide, une valeur atteinte, un fichier à lire — prenez `while`. Si vous vous surprenez à écrire un compteur et à l'incrémenter vous-même dans un `while`, c'est généralement un `for` qui demande à sortir.

---

## IV. `continue` et `break`

Ces mots-clés permettent de réagir **en cours d'itération** : `continue` abandonne le tour en cours, `break` quitte la boucle entière.

### A. `continue`

Permet d'empêcher la continuation de l'itération en cours et va passer à la suivante sans effectuer le reste du code de la boucle.

```python
ma_liste = ["COUCOU", "PYTHON", "lowercase"]

# Chaque fois qu'on croise une string en uppercase on passe à l'itération suivante sans exécuter le reste du code
for string in ma_liste:
    if string.isupper():
        continue
    print(string) # nous ne printons que "lowercase"
```

La suite de lignes après le `continue` est simplement **sautée** pour ce tour-là : la boucle, elle, continue.

### B. `break`

Permet de complètement sortir de la boucle courante.

```python
ma_liste = [1, 2, 3, 4, 5]

for x in ma_liste:
    if x >= 4:
        print("C'en est trop pour moi, je m'en vais!")
        break
    print(x)
```

À comparer avec `continue` : ici le `4` et le `5` ne seront jamais traités, la boucle est terminée. `break` est le geste naturel dès qu'on a **trouvé ce qu'on cherchait** — continuer à chercher coûte du temps pour rien.

---

## V. Les compréhensions de listes

📚 <https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions>

Fonctionnalité exclusive de Python, elles permettent de boucler sur une liste et d'effectuer des opérations en utilisant une syntaxe plus compacte. **Cela nous retourne une nouvelle liste**.

Les applications courantes des compréhensions consistent à créer de nouvelles listes dans lesquelles chaque élément est le résultat de certaines opérations appliquées à chaque membre d'une autre séquence ou itérable, ou à créer une sous-séquence de ces éléments qui satisfont à une certaine condition.

Sans compréhension de liste, si nous voulons extraire les chiffres pairs d'une liste et les multiplier par 2, notre code pourrait ressembler à ceci.

```python
ma_liste = [1, 2, 3, 4, 5]
liste_paire = []

for x in ma_liste:
    if x % 2 == 0: # modulo, permet de calculer le reste de la division euclidienne entre x et 2
        liste_paire.append(x*2)

print(liste_paire) # [4, 8]
```

Avec une compréhension de liste, le code nécessaire est plus compact.

```python
ma_liste = [1, 2, 3, 4, 5]

# structure : [<ACTION TRUE> for <ELEMENT> in <LISTE> if <CONDITION>]
liste_paire = [x*2 for x in ma_liste if x % 2 == 0]

print(liste_paire) # [4, 8]
```

Les deux blocs font la même chose. Pour lire une compréhension, retrouvez l'ordre du `for` d'origine : « pour chaque `x` de `ma_liste`, **si** la condition, alors `x*2` ».

> ⚠️ **Compact ne rime pas avec qualité.**
>
> Les compréhensions de liste proposent une fonctionnalité intéressante pour faire
> des opérations sur des listes, mais comme pour les [assignations parallèles et
> multiples de variables](05-variables-notions-plus-avancees.md) ou [l'opérateur
> ternaire](11-les-structures-conditionnelles.md), elles sont à utiliser avec
> mesure et doivent être évitées lorsque cela met en péril la lisibilité de votre
> code.
>
> ```python
> sorted_datas = [data.strip(' ').split('/') for data in message.content.split(':')[1].split(',')]
> ```
>
> Cette ligne est un cas d'école : elle fonctionne, et personne ne la relit sans
> la dérouler dans sa tête. Un `for` explicite sur six lignes aurait été plus
> clair — et c'est l'exemple à éviter, pas à copier.

---

## VI. `any()` et `all()`

Ces deux fonctions vont permettre de boucler sur une liste de conditions et de retourner `True` ou `False` selon que **au moins une** condition, ou **la totalité**, est vraie.

```python
any_true  = any([True, True, True, False])
all_true  = all([True, True, True])

print(any_true) # True car au moins une condition est True
print(all_true) # True car toutes les conditions sont True
```

> 📌 **Nommage.** La version d'origine de cet exemple nommait la première variable
> `any_false`, ce qui laissait croire qu'elle valait `False` : `any()` ne retourne
> `False` que si **tous** les éléments sont faux. Retenez plutôt les deux règles,
> et nommez la variable d'après le résultat attendu.
>
> - `any([...])` → `True` dès qu'**un** élément est `True`.
> - `all([...])` → `True` seulement si **aucun** élément n'est `False`.

Elles sont particulièrement utiles lorsqu'on a beaucoup de conditions à vérifier dans le même `if`.

### A. Exemple avec `any()`

```python
phone = "06 56 26 37 28"

if phone.startswith("06") or phone.startswith("07") or phone.startswith("04"):
    print("Numéro de téléphone valide")

# En utilisant any()
if any([phone.startswith("06"), phone.startswith("07"), phone.startswith("04")]):
    print("Numéro de téléphone valide")
```

### B. Exemple avec `all()`

```python
mail = "mail@gmail.com"

if len(mail) > 8 and '@' in mail and mail.endswith(".com"):
    print("Mail valide")

# En utilisant all()
if all([len(mail) > 8, '@' in mail, mail.endswith(".com")]):
    print("Mail valide")
```

Les deux écritures sont équivalentes. L'avantage d'`any()` / `all()` apparaît quand la liste des cas s'allonge ou vient d'une variable : on ajoute un élément à la liste au lieu d'ajouter un `or` à la ligne.

### C. Avec une compréhension de liste

`any()` et `all()` peuvent être particulièrement puissants dans le cadre d'une compréhension de liste.

```python
ma_liste = [1, 3, 5, 7, 9, 11, 13, 16]
print(all([x%2 != 0 for x in ma_liste])) # False : le 16 est pair

notes = [12, 13, 8, 18, 20]
if any([x < 10 for x in notes]):
    print("un cancre est parmi nous!") # Au moins une des notes est en dessous de 10
```

**Une précision utile.** Le deuxième exemple de la version d'origine testait `x >= 10`, ce qui est vrai pour presque toutes les notes : le message s'affichait donc quoi qu'il arrive, pour une raison inverse de celle annoncée. Pour repérer une note sous 10, la condition est `x < 10` — c'est ce que montre le code ci-dessus, et c'est ce que vous écrirez à l'exercice 7.

---

### Exercice 1 — L'intrus (~3 min)

```python
# A l'aide d'une boucle, parcourir la liste suivante à la recherche de l'intrus
# Une fois l'intrus trouvé, printer "intrus trouvé!" et sortir de la boucle

liste = ["bernard", "gérard", "gontran", "jacqueline", "intrus", "nadia", "jack"]
```

**Avant d'ouvrir le corrigé**, vérifiez que :

- [ ] Vous sortez de la boucle (`break`), et non pas seulement « passez à la suite ».
- [ ] Les noms qui suivent l'intrus ne sont jamais testés.

<details>
<summary>Corrigé</summary>

```python
# A l'aide d'une boucle, parcourir la liste suivante à la recherche de l'intrus
# Une fois l'intrus trouvé, printer "intrus trouvé!" et sortir de la boucle

liste = ["bernard", "gérard", "gontran", "jacqueline", "intrus", "nadia", "jack"]

for name in liste:
    if name == "intrus":
        print("intrus trouvé!")
        break
```

`nadia` et `jack` ne sont jamais regardés : le `break` quitte la boucle. On pourrait ajouter un `else` aligné sur le `for` pour signaler qu'aucun intrus n'a été trouvé — c'est exactement la structure vue en II.

*Le corrigé d'origine oubliait les deux-points de la ligne `if`* : Python refuse alors le bloc entier avec une `SyntaxError`, et l'indentation par tabulations n'arrangeait rien.

</details>

---

### Exercice 2 — La somme, sans `sum()` (~4 min)

```python
# Sans utiliser la fonction sum(), retourner la somme de la liste suivante à l'aide d'une boucle

liste_somme = [12.3, 34, 1, 0.4, 23, -17, 76, -300.2]
```

<details>
<summary>Corrigé</summary>

```python
# Sans utiliser la fonction sum(), retourner la somme de la liste suivante à l'aide d'une boucle

liste_somme = [12.3, 34, 1, 0.4, 23, -17, 76, -300.2]

total = 0
for nombre in liste_somme:
    total += nombre

print(total)
```

Le patron à retenir est celui d'un **accumulateur** : une variable initialisée avant la boucle (`total = 0`), mise à jour à chaque tour (`total += nombre`), lue après la boucle. Le `+=` vient du chapitre des opérateurs.

Attention tout de même au résultat affiché : le calcul fait intervenir des nombres à virgule, et l'addition de flottants n'est pas exacte comme celle des décimaux — le total peut s'afficher avec quelques décimales de bruit en plus de `-170.5`. Ce n'est pas votre boucle qui dérive, c'est la façon dont la machine range les virgules.

</details>

---

### Exercice 3 — Le factoriel de 10 (~4 min)

```python
# A l'aide d'une boucle et d'une range, calculer le factoriel de 10 (Résultat: 3 628 800) (1*2*3*4*5*6*7*8*9*10)
# Le factoriel d'un entier n est le produit des nombres entiers strictement positifs inférieurs ou égaux à n
# Printer le résultat
```

<details>
<summary>Corrigé</summary>

```python
# A l'aide d'une boucle et d'une range, calculer le factoriel de 10 (3628800)
# Le factoriel d'un entier n est le produit des nombres entiers strictement positifs inférieurs ou égaux à n
# Printer le résultat

total = 1
for x in range(1, 11):
    total *= x

print(total)
```

Même patron que l'exercice 2, en multiplication cette fois — d'où `total = 1` et non `0` : partir de `0` donnerait `0` à chaque tour, et le factoriel de 10 vaudrait `0`.

Le `range(1, 11)` mérite un arrêt sur image : la borne de fin est **exclue**, donc s'arrêter à `11` est ce qui fait monter le produit jusqu'à `10`. Écrire `range(1, 10)` oublierait le dernier facteur et donnerait 362 880.

</details>

---

### Exercice 4 — Oui, ou non (~5 min)

```python
# A l'aide d'une boucle while, demander à l'utilisateur de "Taper oui, ou non.", et tant que ce dernier n'a pas tapé "non", continuer de lui demander "Taper oui, ou non."
# Si l'utilisateur ne tape ni "oui", ni "non", continuer la boucle en lui mettant un message d'erreur car l'input est invalide
```

<details>
<summary>Corrigé</summary>

```python
# A l'aide d'une boucle while, demander à l'utilisateur de "Taper oui, ou non.", et tant que ce dernier n'a pas tapé "non", continuer de lui demander "Taper oui, ou non."
# Si l'utilisateur ne tape ni "oui", ni "non", continuer de lui demander "Taper oui, ou non."

question = input("Taper oui, ou non.")

while(question != "non"):
    question = input("Taper oui, ou non.")
    if question != "oui" and question != "non":
        print("Erreur dans la requête, vous devez taper 'oui' ou 'non' !")
```

Lisez le déroulé, c'est le cœur de l'exercice : la première saisie sert de **garde** — si l'utilisateur tape `non` immédiatement, la boucle ne tourne pas une seule fois. Ensuite, chaque tour repose la question **puis** valide la réponse : un mot invalide affiche le message d'erreur et le `while` repart, parce que la question a déjà été reposée en haut du bloc.

Deux détails à repérer :

- le message d'erreur n'interrompt pas la boucle : c'est ce que demande la consigne (« continuer de lui demander ») ;
- la sortie est **garantie** parce que `question` est réaffectée dans le bloc. Sans cette réaffectation, la condition serait toujours la même et la boucle serait infinie — le piège signalé dans l'encadré de la III.

</details>

---

### Exercice 5 — Index et valeurs (~3 min)

```python
# A partir de la liste suivante printer le résultat suivant à l'aide d'une boucle :
# "L'élément à l'index 0 est a"
# "L'élément à l'index 1 est 3"
# "L'élément à l'index 2 est True"
# ...

ma_liste = ['a', 3, True, "coucou", 'r', 3.14, [1, 2, 3]]
```

<details>
<summary>Corrigé</summary>

```python
# A partir de la liste suivante printer le résultat suivant à l'aide d'une boucle :
# "L'élément à l'index 0 est a"
# "L'élément à l'index 1 est 3"
# "L'élément à l'index 2 est True"
# ...

ma_liste = ['a', 3, True, "coucou", 'r', 3.14, [1, 2, 3]]

for index, elem in enumerate(ma_liste):
    print(f"L'élément à l'index {index} est {elem}")
```

`enumerate()` fait exactement ce que l'énoncé réclame — l'index **et** la valeur dans le même tour. L'alternative sans `enumerate()` (`for i in range(len(ma_liste))` puis `ma_liste[i]`) fonctionne, mais dit la même chose en plus compliqué.

Le dernier élément est une **liste** : la f-string l'affiche `[1, 2, 3]` sans conversion manuelle, comme au chapitre des f-strings.

</details>

---

### Exercice 6 — Compréhension avec `else` (~5 min)

```python
# A l'aide d'une compréhension de liste générer une nouvelle liste suivant les règles suivante :
# Si le chiffre est un multiple de 5, le multiplier par 2
# Sinon, retourner sa division entière par 3
# Printer la nouvelle liste obtenue

liste_de_base = [23, 1, 27, 28, 3, 4, 763, 12, 90]
```

**Avant d'ouvrir le corrigé**, vérifiez que :

- [ ] Le `if / else` est placé **avant** le `for` dans la compréhension (ici ce n'est pas une condition de filtrage, c'est un choix de valeur).
- [ ] Vous utilisez `//`, pas `/` — sinon toute la liste se retrouve peuplée de flottants.

<details>
<summary>Corrigé</summary>

```python
# A l'aide d'une compréhension de liste générer une nouvelle liste suivant les règles suivante :
# Si le chiffre est un multiple de 5, le multiplier par 2
# Sinon, retourner sa division entière par 3
# Printer la nouvelle liste obtenue

liste_de_base = [23, 1, 27, 28, 3, 4, 763, 12, 90]
comp_liste = [x*2 if x%5 == 0 else x//3 for x in liste_de_base]

print(comp_liste)
```

Le modèle de la V change un peu ici : `[<VALEUR SI VRAI> if <CONDITION> else <VALEUR SINON> for x in <LISTE>]`. Le `if` n'élimine plus d'éléments, il **choisit** la valeur produite — c'est l'opérateur ternaire du chapitre des conditions, glissé dans la compréhension.

Un seul nombre de la liste est multiple de 5 : `90`, qui devient `180`. Les autres passent par la division entière par 3, ce qui donne `[7, 0, 9, 9, 1, 1, 254, 4, 180]`. Vérifiez-en deux ou trois à la main (`23 // 3` = 7, `1 // 3` = 0, `763 // 3` = 254) : c'est le meilleur contrôle à porter sur ce type d'exercice.

</details>

---

### Exercice 7 — Tous les palindromes sont-ils là ? (~5 min)

```python
# A l'aide d'une compréhension de liste et de all() printer une fois True ou False si toutes les chaînes de caractères contenues dans la liste sont des palindromes.

palindromes = ["kayak", "coloc", "malayalam", "pop", "erre"]
```

> 📌 Un palindrome est un mot qui se lit de la même manière de gauche à droite
> comme de droite à gauche.

<details>
<summary>Corrigé</summary>

```python
# A l'aide d'une compréhension de liste et de all() printer une fois True ou False si toutes les chaînes de caractères contenues dans la liste sont des palindromes.

palindromes = ["kayak", "coloc", "malayalam", "pop", "erre"]
all_condition = all([mot[:] == mot[::-1] for mot in palindromes])

print(all_condition)
```

Trois pièces du cours s'empilent ici :

- la slice `[::-1]`, qui retourne la chaîne (chapitre des listes) ;
- la compréhension, qui fabrique une liste de booléens, un par mot ;
- `all()`, qui ne rend `True` que si **aucun** booléen n'est `False`.

Ici, `"coloc"` retourné donne `"coloc"` ✓, `"kayak"`, `"malayalam"`, `"pop"`, `"erre"` se lisent aussi à l'envers de la même façon : la liste est pleine de `True` et l'affichage est `True`.

*Le `mot[:]` est une écriture redondante* — copier une chaîne slice complète ne sert à rien : `mot == mot[::-1]` compare la même chose, en plus clair. Gardez-la quand même en tête, vous la croiserez.

</details>

---

### Exercice 8 — Aplatir et trier (~8 min, facultatif)

```python
# A l'aide de boucles imbriquées, créer une nouvelle liste "flat", qui sera une liste aplatie de "liste", ayant les éléments classés dans l'ordre décroissant : [7, 6, 5, 4, 3, 2, 1]

liste = [1, 3, 7, [4, 6, [5, 2]]]
```

**Avant d'ouvrir le corrigé**, vérifiez que :

- [ ] Vous testez le **type** de l'élément avant de décider quoi en faire.
- [ ] Une sous-liste de niveau 2 est bien étendue (et pas ajoutée comme un bloc).

<details>
<summary>Corrigé</summary>

```python
# A l'aide de boucles imbriquées, créer une nouvelle liste "flat", qui sera une liste aplatie de "liste", ayant les éléments classés dans l'ordre décroissant : [7, 6, 5, 4, 3, 2, 1]

liste = [1, 3, 7, [4, 6, [5, 2]]]
flat = []
for root_element in liste:
    if isinstance(root_element, list):
        for elem in root_element:
            if isinstance(elem, list):
                flat.extend(elem)
            else:
                flat.append(elem)
    else:
        flat.append(root_element)

flat.sort(reverse=True)
print(flat)
```

Deux nouveautés apparaissent ici, et l'exercice est facultatif pour cette raison :

- `isinstance(objet, list)` demande « cet objet est-il une liste ? ». C'est le cousin de `type()` que vous manipulez depuis le premier jour, et c'est ce qui permet de séparer les nombres des sous-listes.
- `sort(reverse=True)` trie **à l'envers**. `sort()` seul trie dans l'ordre croissant ; `reverse=True` inverse le résultat.

Le reste est du déjà-vu : deux boucles **imbriquées** (une par niveau de profondeur), `append()` pour un élément, `extend()` pour une sous-liste entière — rappelez-vous la nuance du chapitre des listes, `append([5, 2])` aurait ajouté une sous-liste et le tri aurait échoué.

**Limite assumée, et intéressante à nommer.** Ce code gère **deux** niveaux d'imbrication, pas trois : il est écrit pour la liste de l'énoncé. Une liste `[1, [2, [3, [4]]]]` lui rendrait une sous-liste dans `flat`. La version générale passe par une **fonction qui s'appelle elle-même** — la récursivité — et ce sera disponible après le chapitre [Les fonctions](19-les-fonctions.md).

</details>

---

## Points clés

- `for` parcourt une collection (liste, chaîne, tuple, `range`) sans compteur ; `while` répète tant qu'une condition tient.
- `enumerate()` donne l'index et la valeur dans le même tour — c'est la bonne réponse à « j'ai besoin de la position ».
- Une boucle `while` doit **modifier** ce que teste sa condition, sinon elle ne s'arrête jamais.
- `continue` saute la fin du tour en cours, `break` quitte la boucle ; le `else` d'une boucle s'exécute si aucun `break` n'a eu lieu.
- Une compréhension de liste fabrique une **nouvelle** liste ; compacte n'est pas synonyme de lisible.
- `any()` = au moins un vrai, `all()` = tous vrais ; les deux se marient très bien aux compréhensions.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Combien de fois le bloc de `for x in range(3): print(x)` s'exécute-t-il ?

- A. Deux fois, la borne de fin étant exclue
- B. Trois fois, avec `x` valant 0, puis 1, puis 2
- C. Quatre fois, Python exécutant aussi un tour avec `x` égal à 3
- D. Trois fois, avec `x` valant 1, puis 2, puis 3

**2.** Un `while` dont on oublie d'incrémenter la variable de contrôle :

- A. S'arrête au premier tour, la condition devenant fausse
- B. Lève une erreur dès la deuxième itération
- C. Tourne sans fin, la condition restant vraie
- D. Est refusé par Python à l'exécution, qui exige un incrément

**3.** Quelle est la différence entre `continue` et `break` ?

- A. `continue` passe au tour suivant, `break` quitte définitivement la boucle
- B. `continue` sort de la boucle, `break` revient au début de la boucle
- C. Les deux se recouvrent, `break` étant seulement plus explicite
- D. `continue` fonctionne dans un `while`, `break` seulement dans un `for`

**4.** Dans une boucle `for… else`, quand le `else` s'exécute-t-il ?

- A. À chaque tour où la condition interne du `if` est fausse
- B. Seulement si la boucle s'est terminée sans rencontrer de `break`
- C. Toujours, une fois la dernière itération passée, `break` ou pas
- D. Jamais, le `else` d'une boucle n'est que de la syntaxe tolérée

**5.** *Question ouverte (2-3 lignes).* Vous devez afficher chaque mot d'une liste en indiquant sa position, et vous voulez repérer après la boucle si aucun mot ne commençait par « A ». Quelles structures utilisez-vous, et pourquoi pas un simple compteur ?

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. B.** Trois tours : 0, 1, 2.
**Pourquoi :** `range(3)` commence à 0 et s'arrête avant 3 — même convention que les slices. C'est la réponse A qui piège : « borne exclue » ne veut pas dire « un tour de moins que la valeur », cela veut dire que la valeur n'est pas atteinte.

**2. C.** Condition toujours vraie, boucle infinie.
**Pourquoi :** rien ne vient changer l'état testé. Le programme ne plante pas, il s'accroche : c'est pourquoi on garantit toujours une sortie — et pourquoi `for` est préférable quand on peut l'utiliser.

**3. A.** C'est la définition des deux mots-clés.
**Pourquoi :** `continue` laisse la boucle vivre (le bloc après lui est sauté pour ce tour), `break` la tue. Les deux s'utilisent dans `for` comme dans `while`.

**4. B.** Le `else` d'une boucle répond « je suis allé au bout ».
**Pourquoi :** un `break` est un chemin de sortie particulier, et le `else` signale justement qu'il n'a pas été pris. C'est le mode naturel d'une recherche : trouvé → `break` et pas de `else` ; pas trouvé → le `else` s'affiche.

**5.** Attendu : une boucle `for index, mot in enumerate(mots)` avec une f-string pour l'affichage ; pour le repérage, un `any([mot.startswith("A") for mot in mots])` — ou une variable booléenne passée à `True` dans la boucle, avec un `else` aligné sur le `for` si l'on veut un message « aucun ».
**Pourquoi :** `enumerate()` évite d'écrire à la main un compteur qu'il fournit déjà (et qu'on oublie parfois d'incrémenter) ; `any()` répond en une ligne à une question d'existence, sans accumuler de `or`. Le compteur manuel n'apporte ici qu'une occasion d'erreur de plus.

</details>

---

[← Chapitre précédent](15-les-tuples.md) · [Sommaire](Readme.md) · [Chapitre suivant →](17-les-dictionnaires.md)
