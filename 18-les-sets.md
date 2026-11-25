[← Chapitre précédent](17-les-dictionnaires.md) · [Sommaire](Readme.md) · [Chapitre suivant →](19-les-fonctions.md)

# 18 - Les sets

> Un set répond à une question très concrète : « qu'est-ce que j'ai, enlevant les
> doublons ? ». Ni ordre, ni répétition : juste une collection de valeurs
> différentes, et des opérations pour les comparer entre elles.

**Durée :** ≈ 15 min (lecture ≈ 7 min + atelier 7 min + réflexion) · **Prérequis :** [Les listes](14-les-listes.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Décrire** un set et les deux propriétés qui le distinguent d'une liste.
- **Convertir** une collection en set pour éliminer ses doublons.
- **Comparer** deux sets avec `difference()`, `intersection()` et `union()`.

---

## I. Définition

Le set est un type de Collection dans Python. Il n'est **pas ordonné**, c'est-à-dire que l'ordre des éléments n'est pas préservé, et **non modifiable**. On ne peut ni ajouter, ni enlever des éléments après son initialisation. Il s'initialise avec des accolades. Il peut contenir tout type de données primitives (les collections sont exclues).

```python
mon_set = {"mon", "super", "set"}
```

---

## II. Valeurs identiques interdites

La grande force du set, c'est que les valeurs identiques y sont interdites ; on peut ainsi s'assurer qu'une collection ne contient aucun doublon en l'initialisant ou en la convertissant en set.

```python
duplicats_interdit = {1, 2, 3, 1}
print(duplicats_interdit) # {1, 2, 3}
```

```python
my_list = [1, 2, 3, 1]
print(set(my_list)) # {1, 2, 3}
```

---

## III. Méthodes de sets entre eux

### A. `set.difference`

Retourne la différence du `set` devant la fonction avec un « . » par rapport aux `set` dans les parenthèses.

```python
set_1 = {'a', 'b', 'c', 'd', 'e', 'f'}
set_2 = {'d', 'e'}
set_3 = {'c', 'd'}

diff = set_1.difference(set_2, set_3)
print(diff) # {'a', 'b', 'f'}
```

### B. `set.intersection`

Retourne les éléments communs entre le `set` devant la fonction avec un « . » et plusieurs `set` passés dans les parenthèses.

```python
set_1 = {5, 10, 15, 20}
set_2 = {5, 35, 40}
set_3 = {5, 50, 15}

intersect = set_1.intersection(set_2, set_3)
print(intersect) # {5}
```

### C. `set_1.union(set_2)`

Retourne la réunion des deux sets sans doublons.

```python
set_1 = {"banane", "kaki", "pomme", "poire"}
set_2 = {"pomme", "orange", "rhubarbe"}

union = set_1.union(set_2)
print(union) # {'rhubarbe', 'kaki', 'orange', 'banane', 'poire', 'pomme'}
```

> 📌 [Liste exhaustive des méthodes de set](https://www.w3schools.com/python/python_sets_methods.asp).

---

## IV. Exercices

### Exercice 1 — Union, éléments communs, éléments distincts (~7 min)

```python
# A l'aide d'une méthode de set
# Extraire une union des 2 sets
# Extraire les éléments communs aux 2 sets
# Extraire les éléments qui ne sont pas en commun entre les 2 sets
# Printer les résultats au fur et à mesure

set_1 = {"coucou", True, 2, 't', 76, False, "test"}
set_2 = {"python", 2.2, 'x', False, "test", 76, "la réponse D"}
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] J'ai utilisé **une méthode de set** par question, et pas une boucle.
- [ ] Ma troisième réponse s'appuie sur une méthode qui écarte bien les éléments **communs** : la liste exhaustive des méthodes de set est liée plus haut.
- [ ] J'ai printer les trois résultats **au fur et à mesure**, dans l'ordre des questions.

<details>
<summary>Voir la correction</summary>

```python
# A l'aide d'une méthode de set
# Extraire une union des 2 sets
# Extraire les éléments communs aux 2 sets
# Extraire les éléments qui ne sont pas en commun entre les 2 sets
# Printer les résultats au fur et à mesure

set_1 = {"coucou", True, 2, 't', 76, False, "test"}
set_2 = {"python", 2.2, 'x', False, "test", 76, "la réponse D"}

print(set_1.union(set_2))
print(set_1.intersection(set_2))
print(set_1.symmetric_difference(set_2))
```

Deux particularités de ce jeu de données méritent un arrêt : `True` et `1` d'une part, `False` et `0` d'autre part, se valent en Python — un set contenant `True` et `1` ne garderait qu'une de ces deux valeurs. Et `2` (entier) comme `2.2` (flottant) sont deux valeurs différentes, toutes deux conservées.

</details>

---

## V. Aller plus loin

> ⏭️ Facultatif — pas exigé pour la suite du cours.

- La liste exhaustive des méthodes de set ([w3schools](https://www.w3schools.com/python/python_sets_methods.asp)) couvre notamment `symmetric_difference()`, `isdisjoint()` et `issubset()` : la correction de l'exercice 1 en utilise une que le chapitre ne détaille pas.

---

## Points clés

- Un set est **non ordonné** et **refuse les doublons** : c'est l'outil tout désigné pour purger une collection de ses répétitions.
- `set(ma_liste)` convertit une liste en set et élimine les doublons d'un coup.
- Les collections (listes, dictionnaires, autres sets) ne peuvent pas être membres d'un set : seules les données primitives y entrent.
- `difference()`, `intersection()` et `union()` comparent des sets entre eux et retournent un nouveau set.
- L'ordre d'affichage d'un set n'étant pas garanti, on ne s'appuie jamais dessus pour relire un résultat.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** On exécute `print({1, 2, 3, 1})`. Que s'affiche-t-il ?

- A. `{1, 2, 3, 1}`, l'ordre d'écriture étant toujours préservé dans une collection Python
- B. `{1, 2, 3}`, les valeurs identiques étant interdites dans un set
- C. `{1}`, la première valeur servant de référence et les suivantes étant ignorées
- D. Une erreur, la répétition d'une valeur étant refusée à l'écriture d'un set

**2.** Pourquoi convertit-on une liste en set avec `set(my_list)` ?

- A. Pour obtenir la même collection débarrassée de ses doublons
- B. Pour classer les éléments de la liste par ordre croissant avant de les afficher
- C. Pour rendre la liste modifiable, le set autorisant l'ajout d'éléments
- D. Pour pouvoir y ranger des listes et des dictionnaires en plus des valeurs simples

**3.** `set_1 = {'a', 'b', 'c', 'd', 'e', 'f'}`, `set_2 = {'d', 'e'}`, `set_3 = {'c', 'd'}`. Que retourne `set_1.difference(set_2, set_3)` ?

- A. `{'d'}`, l'unique valeur que partagent les trois sets
- B. `{'a', 'b', 'f'}`, c'est-à-dire les éléments de `set_1` restants une fois retirés ceux des deux autres
- C. `{'c', 'd', 'e'}`, la réunion des éléments que `set_2` et `set_3` ont en commun
- D. `{'a', 'b', 'c', 'd', 'e', 'f'}`, la différence laissant passer la totalité du premier set

**4.** Avec `set_1 = {"banane", "kaki", "pomme", "poire"}` et `set_2 = {"pomme", "orange", "rhubarbe"}`, combien de valeurs contient `set_1.union(set_2)` ?

- A. 4, la méthode retournant le set qui contient le plus d'éléments
- B. 6, chaque valeur n'étant présente qu'une seule fois dans la réunion
- C. 7, les deux sets étant mis bout à bout avec leurs doublons
- D. 1, seule la valeur commune aux deux sets étant conservée

**5.** *Question ouverte (2-3 lignes).* Vous relevez les prénoms saisis dans un formulaire d'inscription et voulez savoir combien de personnes différentes se sont inscrites. Pourquoi le set est-il le bon outil, et quelle limite devez-vous garder en tête sur l'affichage du résultat ?

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. B.** Le doublon est éliminé à la création : le set n'en garde qu'une occurrence.
**Pourquoi :** « les valeurs identiques y sont interdites » est la grande force du set, et c'est ce qui permet de purger une collection d'un seul coup.

**2. A.** La conversion en set retire les doublons, puis on peut reconvertir le résultat si besoin.
**Pourquoi :** le chapitre l'illustre avec `my_list = [1, 2, 3, 1]` qui devient `{1, 2, 3}`. Attention : un set reste non ordonné et n'accepte pas les collections en son sein.

**3. B.** `difference()` retire du set devant le point tous les éléments passés en paramètres, ici ceux de `set_2` et de `set_3`.
**Pourquoi :** `'c'`, `'d'` et `'e'` disparaissent, il reste `{'a', 'b', 'f'}` ; la méthode peut encaisser plusieurs sets dans les parenthèses.

**4. B.** La réunion réunit les deux collections **sans doublons** : 4 + 4 éléments, moins `pomme` compté une seule fois.
**Pourquoi :** c'est la définition de `union()`, illustrée par les fruits où `pomme` apparaît dans les deux sets.

**5.** Attendu : on place les prénoms dans un set, qui efface les doublons, puis on compte avec `len()` ; la limite est que le set n'est pas ordonné, donc l'affichage ne retrouve pas l'ordre de saisie et peut varier.
**Pourquoi :** le set n'est pas ordonné et refuse les valeurs identiques — exactement ce qu'il faut pour dénombrer des inscrits distincts, mais pas pour rejouer l'ordre d'arrivée.

</details>

---

[← Chapitre précédent](17-les-dictionnaires.md) · [Sommaire](Readme.md) · [Chapitre suivant →](19-les-fonctions.md)
