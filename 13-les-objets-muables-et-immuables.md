[← Chapitre précédent](12-les-modules-standards-de-python.md) · [Sommaire](Readme.md) · [Chapitre suivant →](14-les-listes.md)

# 13 - Les objets muables et immuables

> Deux lignes qui se ressemblent, deux résultats différents : `ma_string.upper()`
> ne change rien à `ma_string`, alors que `ma_liste.sort()` la change pour
> toujours. Ce n'est pas un caprice de Python, c'est une propriété des objets :
> certains se laissent modifier sur place, d'autres non.

**Durée :** ≈ 15 min (lecture ≈ 10 min + réflexion) · **Prérequis :** [Les variables](01-les-variables.md), [Les chaînes de caractères](02-les-chaines-de-caracteres.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Classer** les types que vous connaissez en objets muables et immuables.
- **Prévoir** si une méthode modifie l'objet ou en retourne un nouveau.
- **Écrire** la ligne d'affectation qu'exige une méthode appliquée à un objet immuable.
- **Expliquer** une valeur « inchangée » qui surprend dans un débogage.

---

## I. Les objets muables

> ⚠️ *Python fait une distinction entre les objets muables et immuables.*

Les objets **muables** sont **modifiés en mémoire** à chaque fonction qu'on leur applique. On dit qu'ils sont passés par **référence**.

Exemples d'objets muables :

- listes
- dictionnaires
- sets

Concrètement : l'objet est modifié **là où il est**. Partout où il est déjà référencé, on voit le changement — inutile de réaffecter la variable.

---

## II. Les objets immuables

Les objets immuables ne sont pas modifiés, et **les fonctions qu'on leur applique retournent une copie modifiée de l'objet tandis que l'objet de base reste inchangé**. On dit qu'ils sont passés par **valeur**. Le résultat de l'opération va devoir être affecté à une variable pour être utilisé.

Exemples d'objets immuables :

- chaîne de caractères
- nombres
- tuples

> 📌 **Formulation à connaître, nuance à garder.** Dire qu'un objet immuable est
> « passé par valeur » est une simplification commode, et c'est le vocabulaire de
> ce cours. Python, lui, passe toujours l'objet ; simplement, un objet immuable ne
> peut pas être modifié sur place, donc on repart toujours d'un nouvel objet. Ce
> qui compte opérationnellement : **le résultat se récupère**, il ne se devine pas.

---

## III. Ce que ça change dans votre code

```python
string_immuable = "coucou ca va ?"
string_immuable.upper()

print(string_immuable) # La string demeure inchangée car elle est immuable

liste_muable = [1, 4, 3, 2]
liste_muable.sort()

print(liste_muable) # La liste sera triée en mémoire et changée pour toujours car elle est muable
```

La première ligne qui « n'a rien fait » est en réalité une ligne qui a **produit une nouvelle chaîne, puis l'a jetée** : personne n'a rangeé le résultat. Le `print()` affiche donc l'originale.

Pour corriger notre `.upper()`, il va nous falloir stocker le résultat dans une variable — qui peut être la même.

```python
string_immuable = "coucou ca va ?"
nouvelle_string = string_immuable.upper()
string_immuable = string_immuable.upper()

print(nouvelle_string, string_immuable) # La string a enfin changé
```

Les deux écritures sont valides : l'une garde l'originale intacte à côté du résultat, l'autre remplace la valeur dans la même variable. C'est le même choix qu'entre `sorted()` (retourne une nouvelle liste triée) et `liste.sort()` (trie sur place), que vous verrez au chapitre suivant.

Le réflexe à prendre, pour chaque méthode d'un objet que vous manipulez : **modifie-t-elle sur place, ou retourne-t-elle un nouvel objet ?** La documentation officielle le dit toujours, mais tant que vous ne l'avez pas lu, le test est simple : appelez la méthode, puis affichez l'objet. S'il a changé, il est muable.

---

## Points clés

- Muables : listes, dictionnaires, sets — modifiés **en mémoire**, visibles partout où l'objet circule.
- Immuables : chaînes, nombres, tuples — l'original reste intact, le résultat **se récupère** dans une variable.
- Une méthode appelée sans affectation sur un objet immuable n'est pas perdue : elle est exécutée, puis son résultat est jeté.
- Réaffecter la même variable (`x = x.upper()`) est équivalent à créer `nouvelle_x` : c'est une question de lisibilité, pas de fonctionnement.
- En cas de doute sur une méthode, on affiche l'objet après l'appel : la muabilité se vérifie en deux lignes.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Après ces trois lignes, que contient `texte` ?

```python
texte = "bonjour"
texte.upper()
```

- A. `"bonjour"`, parce que la chaîne est immuable et que le résultat n'a nulle part où aller
- B. `"BONJOUR"`, parce que la méthode modifie l'objet sur lequel elle est appelée
- C. Une chaîne vide, la méthode ayant consommé la valeur d'origine pour la convertir
- D. Une erreur : appeler une méthode sans ranger son résultat est interdit

**2.** Lequel de ces types est muable ?

- A. Le tuple
- B. La liste
- C. La chaîne de caractères
- D. Le nombre entier

**3.** Un collègue écrit `notes.sort()` puis `print(sorted(notes))` et s'étonne du résultat affiché. Que lui répondez-vous ?

- A. Que `sorted()` trie la liste à l'envers, ce qui explique l'écart constaté
- B. Que les deux fonctions trient, mais que `sort()` retourne une nouvelle liste sans toucher à l'ancienne
- C. Que la liste avait déjà été triée sur place par `sort()` : `sorted()` ne peut que la retrouver triée
- D. Que `sort()` ne fonctionne que sur des chaînes de caractères, pas sur des nombres

**4.** Pourquoi dit-on qu'un objet muable est « passé par référence » ?

- A. Parce qu'il ne peut être utilisé qu'à l'intérieur du fichier où il a été créé
- B. Parce qu'il est recopié à chaque appel, ce qui protège la valeur d'origine
- C. Parce que son nom doit être écrit entre guillemets pour être transmis à une fonction
- D. Parce qu'il est modifié là où il se trouve : les autres accès voient le changement

**5.** *Question ouverte (2-3 lignes).* Vous relevez le texte d'une saisie utilisateur et voulez afficher la version en majuscules **sans** perdre la saisie d'origine, pour la comparer plus tard. Écrivez les deux lignes qui font cela, et dites laquelle des deux écritures serait inutile si la valeur était une liste.

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. A.** Le résultat de `.upper()` est une **nouvelle** chaîne, jamais rangée.
**Pourquoi :** la ligne s'exécute bien, puis son résultat est jeté. Il faut écrire `texte = texte.upper()` ou `maj = texte.upper()`. C'est le débogage classique : la méthode « ne marche pas », alors qu'elle a parfaitement travaillé.

**2. B.** La liste est muable ; tuple, chaîne et nombre sont immuables.
**Pourquoi :** c'est la classification du chapitre, et elle explique pourquoi `append()`, `sort()`, `remove()` modifient réellement la liste, tandis que `upper()`, `replace()` ou une opération arithmétique produisent une valeur à récupérer.

**3. C.** `sort()` a déjà trié la liste en mémoire.
**Pourquoi :** les deux fonctions existent justement pour les deux besoins : `sort()` trie **sur place** et ne retourne rien, `sorted()` retourne une **nouvelle** liste triée. Après un `sort()`, `sorted()` ne peut que reconstituer le même ordre.

**4. D.** L'objet est touché là où il est.
**Pourquoi :** c'est tout l'intérêt — et tout le danger — des objets muables : une fonction qui reçoit une liste peut la modifier, et l'appelant constate le changement sans qu'on lui ait rien rendu. Une recopie, elle, protégerait l'original : ce n'est pas ce qui se passe ici.

**5.** Attendu :

```python
saisie = input("Votre réponse")
majuscules = saisie.upper()
```

Si la valeur avait été une liste, l'écriture `autre = ma_liste.sort()` aurait été inutile : `sort()` retourne `None` et trie sur place. Il aurait fallu `autre = sorted(ma_liste)` pour obtenir une copie triée en gardant l'originale.
**Pourquoi :** la question n'est pas « comment obtenir des majuscules » mais « où va le résultat ». Sur un objet immuable, il faut le ranger ; sur un objet muable qui trie sur place, il faut changer de fonction.

</details>

---

[← Chapitre précédent](12-les-modules-standards-de-python.md) · [Sommaire](Readme.md) · [Chapitre suivant →](14-les-listes.md)
