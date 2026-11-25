[← Chapitre précédent](07-interaction-avec-lutilisateur.md) · [Sommaire](Readme.md) · [Chapitre suivant →](09-les-operateurs-mathematiques.md)

# 08 - Les méthodes de chaînes de caractères

> Une chaîne sait faire beaucoup plus que se laisser afficher : elle se met en casse,
> se découpe, se cherche, se compte. C'est votre premier contact avec les méthodes
> portées par un objet — et l'atelier qui suit va vous le faire prendre aux doigts.

**Durée :** ≈ 35 min (lecture ≈ 18 min + atelier ≈ 17 min) · **Prérequis :** [Les chaînes de caractères](02-les-chaines-de-caracteres.md), [Les variables, notions plus avancées](05-variables-notions-plus-avancees.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Transformer** la casse d'une chaîne avec `upper()`, `lower()`, `capitalize()`, `title()`.
- **Remplacer** et **nettoyer** une chaîne avec `replace()`, `strip()`, `rstrip()`, `lstrip()`.
- **Découper** une chaîne avec `split()` et **reconstruire** une chaîne avec `join()`.
- **Contrôler** le contenu d'une chaîne avec `islower()`, `isupper()`, `isdigit()`, `startswith()`, `endswith()`.
- **Chercher** et **compter** des occurrences avec `find()`, `rfind()`, `index()`, `count()`.
- **Consulter** l'aide en ligne d'une méthode avec `help()`.

---

## I. Les méthodes liées à la casse

La **casse** — *case* en anglais — décrit ce qui a trait aux lettres majuscules et
minuscules. Python propose plusieurs méthodes pour transformer une chaîne et modifier
sa casse.

### A. `upper()` et `lower()`

```python
minuscule = "minuscule"
majuscule = minuscule.upper()

print(majuscule) # "MINUSCULE"

crier  = "PAS LA PEINE DE CRIER!"
parler = crier.lower()

print(parler) # "pas la peine de crier!"
```

Remarquez la forme : on n'appelle pas une fonction isolée, on appelle une méthode
**sur la chaîne** (`crier.lower()`). La chaîne d'origine n'est pas modifiée : la
méthode **renvoie une nouvelle chaîne**. C'est pourquoi on l'affecte à une variable
si l'on veut la garder.

### B. `capitalize()` et `title()`

```python
phrase = "bonjour tout le monde"

print(phrase.capitalize()) # "Bonjour tout le monde"
print(phrase.title())      # "Bonjour Tout Le Monde"
```

`capitalize()` met une majuscule au **début de la chaîne** et ramène le reste en
minuscules ; `title()` en met une à **chaque mot**.

> 🧪 **Atelier rapide (3 min)**
>
> Besoin concret : afficher l'identité des utilisateurs d'un site selon la norme
> `NOM Prénom`. Avec ce que vous savez déjà, quelles méthodes appliquez-vous à la
> chaîne saisie, et dans quel ordre ? Testez votre réponse sur `"jean dupont"`.

---

## II. Remplacer et nettoyer

### A. `replace()`

`replace()` remplace un morceau de chaîne par un autre, si le premier est présent.

```python
bonjour = "Bonjour"

print(bonjour.replace("jour", "soir")) # "Bonsoir"
```

Si le morceau cherché n'apparaît pas, la chaîne est rendue inchangée : aucune erreur
n'est levée.

### B. `strip()`, `rstrip()`, `lstrip()`

`strip()` retire les espaces et les caractères spéciaux **en début et en fin de
chaîne** quand aucun caractère n'est passé en paramètre.

```python
plein_d_espaces     = " Coucou "
caracteres_speciaux = "\tj'adore faire des tabs\t"

print(plein_d_espaces.strip())     # "Coucou"
print(caracteres_speciaux.strip()) # "j'adore faire des tabs"
```

Si des caractères sont passés en paramètre, ce sont **eux** qui sont retirés des deux
extrémités, indépendamment de leur ordre dans la chaîne :

```python
print(plein_d_espaces.strip("uco ")) # 'C'
```

Passez cette ligne dans votre interpréteur et regardez ce qui reste : l'espace de
gauche est retiré, puis le `C` s'arrête là (il n'est pas dans le jeu demandé) ; à
droite, `oucou` puis l'espace disparaissent l'un après l'autre, puisque chacun de ces
caractères figure dans le jeu. Il ne subsiste que le `C` de tête, que rien ne
concerne.

`rstrip()` et `lstrip()` ont le même comportement que `strip()`, sauf que l'on choisit
de l'appliquer uniquement à **droite** (*right*) ou à **gauche** (*left*) de la chaîne.

---

## III. Séparer et joindre

### A. `split()`

`split()` transforme une chaîne de caractères en **liste**, en coupant sur le
séparateur passé en paramètre.

```python
string = "1, 2, 3, 4, 5"
liste  = string.split(", ")

print(liste) # ['1', '2', '3', '4', '5']
```

Sans paramètre, `split()` coupe sur les blancs. C'est la porte d'entrée de tout
traitement de fichier : une ligne de **CSV** (*Comma Separated Values*, valeurs
séparées par des virgules) devient une liste de champs.

### B. `join()`

`join()` fait l'opération inverse : elle transforme une **liste** en chaîne de
caractères, en intercalant le séparateur sur lequel on l'appelle.

```python
liste = ['1', '2', '3', '4', '5']
join  = ", ".join(liste)

print(join) # "1, 2, 3, 4, 5"
```

> ⚠️ `join()` n'accepte que des **listes de chaînes de caractères**.

```python
liste = [1, 2, 3, 4, 5]
join  = "|".join(liste) # soulève une erreur
```

La liste contenait des entiers, pas des chaînes : la méthode refuse. Vous verrez au
chapitre 14 comment transformer tous les éléments d'une liste d'un coup.

---

## IV. Contrôler une chaîne

### A. `islower()` et `isupper()`

Vérifient si la chaîne est entièrement en minuscules ou en majuscules, et renvoient
`True` ou `False`.

```python
print("Bonjour".islower()) # False
print("BONJOUR".isupper()) # True
```

### B. `isdigit()`

Vérifie si la chaîne est entièrement composée de chiffres, et renvoie `True` ou
`False`.

```python
print("2 et 2 font 4".isdigit()) # False
print("12345".isdigit())         # True
```

C'est le contrôle réflexe avant une conversion : plutôt que de tenter `int()` à
l'aveugle, on vérifie d'abord que la saisie ne contient que des chiffres. Le
chapitre 11 l'utilisera dans une condition.

---

## V. Compter

### `count()`

Compte le nombre d'occurrences d'un morceau dans une chaîne.

```python
print("coucou".count("cou"))  # 2
print("coucou".count("Cou"))  # 0, car la méthode respecte la casse
print("coucou".count("cou ")) # 0, car il n'y a pas d'espace après 'cou' dans 'coucou'
```

Deux détails à retenir : la recherche **respecte la casse** (un `C` majuscule n'est
pas un `c`), et elle est **littérale** (l'espace fait partie du morceau cherché).

---

## VI. Chercher

### A. `find()` et `rfind()`

`find()` cherche une occurrence dans une chaîne et renvoie l'**index** du premier
caractère à partir duquel l'occurrence est présente. Elle renvoie `-1` si l'occurrence
est introuvable. `rfind()` fait la même chose en partant de la **droite** de la chaîne.

```python
phrase = "Le Python, c'est cool. Python est puissant."
print(phrase.find("Python"))  # 3
print(phrase.find("python"))  # -1, respect de la casse
print(phrase.rfind("Python")) # 23
```

L'index compte les caractères depuis **0**, espaces et ponctuation compris.

### B. `index()`

Fonctionne comme `find()`, à cette exception près que si l'occurrence n'est pas
présente, la méthode **lève une erreur** au lieu de renvoyer `-1`.

```python
phrase = "Le Python, c'est cool. Python est puissant."
print(phrase.index("python")) # erreur
```

Retenez la règle générale du parcours : quand une méthode peut échouer, il existe
souvent une variante qui renvoie une valeur témoin (`-1`, `False`, `None`). À ce stade
du cours, préférez la variante tolérante.

### C. `startswith()` et `endswith()`

Déterminent si la chaîne **commence** ou **se termine** par la sous-chaîne passée en
paramètre, et renvoient `True` ou `False`.

```python
je = "Je commence par je".startswith("je")
print(je) # False

je = "Je commence par je".endswith("je")
print(je) # True
```

Le premier résultat est attendu : la chaîne commence par un `J` majuscule, et la
comparaison respecte la casse.

> 💡 **Usage concret** : déterminer si un fichier reçu est bien une image, c'est-à-dire
> si son nom se termine par `.png`, `.jpg` ou `.gif` — avec `endswith()`.

---

## VII. La fonction `help()`

Il existe énormément de fonctions et de méthodes en Python, rien que pour les chaînes.
Il est impossible de toutes les retenir. Quand vous avez un doute sur le
fonctionnement d'une méthode, utilisez la fonction `help()` plutôt que d'aller chercher
sur un moteur de recherche : vous gagnerez du temps, et votre source d'information sera
sûre.

```python
help('str.join')
```

La liste complète des méthodes de chaîne est rappelée dans l'annexe
[Vocabulaire et ressources](A-Glossaire-et-ressources.md).

---

### Exercice 1 — Chaîner les remplacements (≈ 4 min)

En chaînant la méthode `replace()`, transformez la phrase suivante en
`Au clair du soleil`, puis affichez le résultat.

```python
base = "Au clair de la lune"
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Vous n'avez écrit qu'une seule ligne de transformation.
- [ ] Vous avez vérifié le résultat caractère par caractère, espaces compris.
- [ ] Le mot `soleil` est apparu une seule fois dans la phrase finale.

<details>
<summary>Corrigé</summary>

```python
base = "Au clair de la lune"
repl = base.replace("lune", "soleil").replace("de", "du").replace(" la", "")

print(repl)
```

Un chaînage se lit comme un **pipeline** : chaque méthode reçoit le résultat de la
précédente. Ici les trois remplacements ne se gênent pas, mais l'ordre devient vite
déterminant : si l'on remplaçait `de` par `lunde` à un autre moment, le `lune` créé
en cours de route serait ou non attrapé par le remplacement suivant. Écrivez donc
vos chaînages dans l'ordre où les opérations ont du sens, et vérifiez le résultat.

</details>

### Exercice 2 — Compter une lettre (≈ 3 min)

Comptez le nombre de `e` dans la phrase suivante, puis affichez le résultat.

```python
phrase = "J'aime bien le python même si le snake case, ça fait bizarre au début"
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Vous avez utilisé une méthode de chaîne, pas une boucle.
- [ ] Votre compte porte sur le caractère `e` minuscule, et vous le savez.

<details>
<summary>Corrigé</summary>

```python
phrase = "J'aime bien le python même si le snake case, ça fait bizarre au début"

print(phrase.count('e'))
```

`count()` compte les occurrences **sans chevauchement** et **respecte la casse**. Si
l'on voulait compter les `e` quelle que soit leur casse, il aurait fallu normaliser
d'abord : `phrase.lower().count('e')`.

</details>

### Exercice 3 — Nettoyer une chaîne (≈ 6 min)

Transformez la phrase suivante pour qu'elle devienne exactement `Python c'est trop
cool`. **Une seule ligne de code** est autorisée pour la transformation, puis affichez
le résultat.

```python
phrase = " python\tc'est\ntrop cool   xx"
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Les tabulations et les sauts de ligne ont été remplacés par des espaces.
- [ ] Le suffixe `xx` et les espaces traîneurs ont disparu.
- [ ] La majuscule initiale est là, et elle seule.

<details>
<summary>Corrigé</summary>

```python
phrase = " python\tc'est\ntrop cool   xx"

phrase = phrase.replace("\t", " ").replace("\n", " ").replace("xx", "").strip().capitalize()
print(phrase)
```

Quatre opérations, dans cet ordre :

1. `replace("\t", " ")` puis `replace("\n", " ")` : les blancs invisibles deviennent
   des espaces normaux ;
2. `replace("xx", "")` : le résidu disparaît ;
3. `strip()` : les espaces devenus superflus aux deux extrémités sont retirés ;
4. `capitalize()` : la majuscule initiale, et rien d'autre.

Sans le `strip()` final, le résultat garderait des espaces de fin — invisibles à
l'écran, bien présents dans une comparaison. C'est le piège classique de tout nettoyage
de saisie.

</details>

### Exercice 4 — Compter des phrases (≈ 4 min)

Comptez le nombre de phrases dans ce texte, puis affichez le résultat.

```python
texte_super_interessant = """L'ornithorynque ne peut être confondu avec aucun autre animal. C'est un petit mammifère – il dépasse rarement 2 kg – vraiment original, à la fourrure courte et dense et au large bec de canard.

Son pelage est typique d'une espèce aquatique. La peau est protégée par une dense couche de poils de bourre, qui maintiennent une pellicule d'air tempéré entre elle et l'eau. Les poils de jarre, plus longs, protègent l'ensemble. La fourrure est presque aussi dense sur le ventre que sur le dos. Seule la couleur change.
"""
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Votre compte s'appuie sur le point final, et l'assume comme une hypothèse.
- [ ] Vous avez repéré au moins un cas où ce critère tromperait.

<details>
<summary>Corrigé</summary>

```python
print(texte_super_interessant.count('.'))
```

C'est la réponse attendue à ce stade du cours : compter les points. Mais regardez ce
que compte vraiment cette ligne — elle ne compte pas des phrases, elle compte des
points. Un texte contenant des abréviations (`M. Dupont`, `etc.`), des initiales ou des
nombres décimaux fausserait le résultat.

Compter correctement demanderait de découper avec `split()` et de tenir compte aussi
des `!` et des `?`. Ces limites sont normales : elles se règlent avec les conditions et
les boucles des chapitres suivants.

</details>

---

## Points clés

- Les méthodes de chaîne s'écrivent `chaine.methode()` et **renvoient une nouvelle
  chaîne** : l'originale n'est jamais modifiée.
- Casse : `upper()`, `lower()`, `capitalize()`, `title()`.
- Nettoyage : `replace()`, `strip()`, `lstrip()`, `rstrip()`.
- Découpage : `split()` chaîne → liste ; `join()` liste de chaînes → chaîne.
- Contrôle : `islower()`, `isupper()`, `isdigit()`, `startswith()`, `endswith()`.
- Recherche et comptage : `count()`, `find()` / `rfind()` (renvoient `-1`), `index()`
  (lève une erreur).
- Presque toutes **respectent la casse** : c'est la source n° 1 des « ça marche pas ».
- `help('str.nom_de_methode')` répond plus vite et mieux qu'un moteur de recherche.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Après `nom = "dupont"` puis `nom.upper()` (sans affectation), que contient `nom` ?

- A. `DUPONT`, la méthode ayant modifié la chaîne en place
- B. `dupont`, la méthode a renvoyé une nouvelle chaîne que personne n'a rangée
- C. Une valeur indéterminée, la méthode ne renvoyant rien d'exploitable
- D. `Dupont`, la méthode ne capitalisant que la première lettre du mot

**2.** Quelle méthode transforme une chaîne en liste de champs ?

- A. `split()`, qui découpe la chaîne sur le séparateur passé en paramètre
- B. `join()`, qui assemble les morceaux reconnus à l'intérieur de la chaîne
- C. `strip()`, qui retire les séparateurs situés aux deux extrémités
- D. `find()`, qui localise chaque séparateur pour le compte de l'appelant

**3.** Pourquoi `"|".join([1, 2, 3])` lève-t-il une erreur ?

- A. Parce que la liste ne contient aucun séparateur, ce qui bloque la jointure
- B. Parce que la méthode n'accepte que des éléments de type chaîne de caractères
- C. Parce que le séparateur doit être passé en argument et non avant la méthode
- D. Parce qu'une liste de nombres ne se joint qu'après une boucle explicite

**4.** Que renvoie `"Le Python".find("python")` ?

- A. `0`, la recherche ignorant la casse par défaut
- B. `-1`, la recherche respectant la casse et l'occurrence étant absente
- C. Une erreur, la sous-chaîne n'ayant pas été trouvée
- D. `3`, l'index de la majuscule la plus proche de la recherche

**5.** *Question ouverte (2-3 lignes).* Vous devez savoir si un nom de fichier se termine bien par `.png` pour décider d'afficher ou non un message d'erreur. Quelle méthode utilisez-vous, et que renvoie-t-elle ? (Le « décider d'afficher » vient au chapitre 11.)

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. B.** `nom` vaut toujours `"dupont"` : `upper()` a renvoyé une nouvelle chaîne restée sans nom.
**Pourquoi :** toutes les méthodes de chaîne du chapitre fonctionnent ainsi, et cela rejoint la règle du chapitre 05 — une affectation déplace un nom, elle ne modifie pas l'objet visé.

**2. A.** `split()` découpe la chaîne et rend une liste ; `join()` fait exactement l'inverse.
**Pourquoi :** le chapitre présente les deux comme un couple aller-retour, et signale que `split()` est la porte d'entrée du traitement de fichiers.

**3. B.** `join()` n'accepte que des éléments de type chaîne ; une liste d'entiers la fait échouer.
**Pourquoi :** c'est l'avertissement du chapitre, illustré par `"|".join([1, 2, 3, 4, 5])`. La conversion de tous les éléments d'une liste se voit au chapitre 14.

**4. B.** `-1` : la recherche est littérale et respecte la casse, or `"python"` en minuscules n'apparaît pas dans `"Le Python"`.
**Pourquoi :** c'est l'exemple du chapitre ; `find()` rend une valeur témoin en cas d'absence, contrairement à `index()` qui lève une erreur.

**5.** Attendu : la méthode `endswith(".png")`, qui renvoie `True` ou `False` ; c'est ce booléen que la condition du chapitre 11 testera pour décider du message.
**Pourquoi :** le chapitre donne cet usage concret, et toute méthode de contrôle renvoie un booléen — ce qui relie directement ce chapitre au suivant.

</details>

---

[← Chapitre précédent](07-interaction-avec-lutilisateur.md) · [Sommaire](Readme.md) · [Chapitre suivant →](09-les-operateurs-mathematiques.md)
