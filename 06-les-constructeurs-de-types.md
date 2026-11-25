[Sommaire](Readme.md) · [Chapitre précédent →](05-variables-notions-plus-avancees.md) · [Chapitre suivant →](07-interaction-avec-lutilisateur.md)

# 06 - Les constructeurs de types

> Écrire `12`, c'est déjà fabriquer un objet de type `int`. Voir les types comme
> des fabriques d'objets, c'est se donner le moyen de les converter sans deviner.

**Durée :** ≈ 15 min (lecture ≈ 8 min + atelier ≈ 7 min) · **Prérequis :** [Les variables](01-les-variables.md), [Les booléens](04-les-booleens.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Dire** ce que fait Python quand il rencontre une valeur littérale.
- **Écrire** une instanciation explicite avec le constructeur d'un type.
- **Converter** une valeur d'un type à un autre avec `str()`, `int()`, `float()`, `bool()`.
- **Prévoir** qu'une conversion peut échouer, et lire le message d'erreur.
- **Consulter** le type d'une valeur avec `type()`.

---

## I. Un type est une classe

### A. Déclarer une variable, c'est instancier

Chaque **type** en Python est en fait une **classe**. À ce stade du parcours, vous
ne savez sans doute pas ce qu'est une classe : la notion est étudiée en détail dans
le cours consacré à la programmation orientée objet.

Sachez cependant que chaque fois que l'on déclare une variable et qu'on lui assigne
une valeur, on **instancie un nouvel objet** de la classe « type » correspondante :

```python
number = 12
number = int(12) # ceci est une instanciation explicite de la classe int
```

### B. Les deux écritures, et celle qu'on garde

Ces notations sont **équivalentes**, mais on préférera la **première** car elle est
plus lisible : l'**interpréteur** Python devine le type de la variable lorsqu'il
analyse la valeur écrite à droite du signe égal.

Gardez pourtant la seconde en tête : elle devient indispensable quand le type n'est
pas devinable, c'est-à-dire quand la valeur arrive d'une conversion.

---

## II. Converter d'un type à un autre

### A. Les fonctions de conversion

Les noms de types sont aussi des **fonctions** : on peut les utiliser pour
**convertir** des valeurs d'un type à un autre.

```python
int_to_str = str(5)   # nous donnera "5"
str_to_int = int("2") # nous donnera 2

print(int_to_str, type(int_to_str)) # 5 <class 'str'>
print(str_to_int, type(str_to_int)) # 2 <class 'int'>
```

La fonction `type()` renvoie la classe de la valeur qu'on lui passe : c'est votre
instrument de contrôle permanent. En cas de doute sur ce que contient une variable,
affichez `type(ma_variable)`.

### B. Une conversion peut échouer

Ces fonctions de conversion sont évidemment à utiliser dans la limite du raisonnable
— et elles ne conversionnent que ce qui est convertible :

```python
error = int("Python") # lève une erreur
```

Le message qui s'affiche alors est de la forme `ValueError: invalid literal for
int() with base 10: 'Python'`. Lisez-le jusqu'au bout : il dit **quelle** erreur
s'est produite et **sur quelle valeur**. C'est le fonctionnement normal du
langage : une chaîne qui ne décrit pas un nombre ne devient pas un nombre.

Vous verrez au chapitre 07 pourquoi ce détail est capital : tout ce que saisit un
utilisateur arrive sous forme de chaîne, et se convertit donc **explicitement**.

---

### Exercice 1 — Types et conversions (≈ 7 min)

Complétez les trois `print()` du script ci-dessous, sans modifier les variables déjà
déclarées.

```python
boolean = True
nombre_entier = 12

# Vérifier si le type bool est bien une sous-classe du type int, et afficher le résultat
print()

# Converter nombre_entier en string sans le stocker, et afficher le résultat
print()

# Afficher le type de nombre_entier dans la console
print()
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Vos trois réponses tiennent chacune dans un seul `print()`.
- [ ] Aucune variable n'est modifiée ni recréée.
- [ ] Le troisième affichage montre bien `<class 'int'>`.

<details>
<summary>Corrigé</summary>

```python
boolean = True
nombre_entier = 12

# Le type bool est-il une sous-classe du type int ?
print(issubclass(bool, int))    # True
print(issubclass(int, bool))    # False : l'hérédité ne se lit pas en sens inverse

# Convertir sans stocker
print(str(nombre_entier))

# Afficher le type
print(type(nombre_entier))
```

On pouvait aussi interroger les variables plutôt que les types écrits en dur :
`issubclass(boolean.__class__, nombre_entier.__class__)` pose la même question à
partir des objets eux-mêmes. Les deux écritures se rencontrent ; la première est
plus directe.

</details>

---

## III. Aller plus loin

> ⏭️ **Facultatif — pas exigé pour finir la journée.**

- `float("3.14")` fonctionne, `int("3.14")` échoue : un nombre à virgule écrit en
  texte ne devient pas un entier directement. Essayez les deux.
- `bool("")` et `bool("0")` ne se ressemblent pas autant qu'il y paraît :
  retrouvez la règle du chapitre 04, puis vérifiez-la avec `print()`.

---

## Points clés

- Chaque type Python est une **classe** ; une valeur littérale instancie un objet.
- `12` et `int(12)` sont équivalents ; on écrit `12`, plus lisible.
- Les noms de types servent aussi de **fonctions de conversion** : `str()`, `int()`,
  `float()`, `bool()`.
- Une conversion impossible lève une **erreur explicite** — `int("Python")` — qu'il
  faut lire, pas redouter.
- `type(valeur)` est le réflexe de contrôle : dans le doute, affichez le type.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Que se passe-t-il quand on écrit `number = 12` ?

- A. Un nouvel objet de la classe `int` est instancié, que le nom `number` désigne
- B. La valeur 12 est écrite dans un fichier de configuration lu par l'interpréteur
- C. Le nom `number` est réservé, mais reste vide tant qu'on ne l'affiche pas
- D. Une conversion implicite transforme 12 en chaîne de caractères prête à l'emploi

**2.** Pourquoi écrit-on `12` plutôt que `int(12)` ?

- A. Parce que la seconde écriture instancie deux objets au lieu d'un seul
- B. Parce que la première est plus lisible et que l'interpréteur déduit le type de la valeur
- C. Parce que la seconde n'est valable qu'à l'intérieur d'une définition de classe
- D. Parce que la première occupe moins de mémoire à l'exécution que la seconde

**3.** Que produit `int("Python")` ?

- A. La valeur 0, par défaut, la chaîne étant impossible à interpréter
- B. Une erreur, explicitant la valeur concernée, qu'il faut lire en entier
- C. Le caractère P, première lettre de la chaîne passée en argument
- D. Une chaîne vide, le type int acceptant n'importe quelle entrée textuelle

**4.** À quoi sert la fonction `type()` ?

- A. À renvoyer la classe de la valeur passée en argument, pour vérifier ce qu'on manipule
- B. À converter une valeur vers le type indiqué par son argument
- C. À déclarer le type d'une variable avant sa première affectation
- D. À interdire l'affectation d'une valeur d'un autre type à la variable testée

**5.** *Question ouverte (2-3 lignes).* Vous lisez la chaîne `"25"` et vous voulez additionner 3 au nombre qu'elle représente. Décrivez les deux opérations nécessaires, dans l'ordre, et le type de chaque résultat.

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. A.** L'écriture de la valeur instancie un objet de la classe `int`, et le nom `number` vient s'y attacher.
**Pourquoi :** le chapitre présente chaque type comme une classe, et l'écriture littérale comme une instanciation dont l'interpréteur se charge.

**2. B.** Les deux sont équivalentes ; la forme littérale est retenue pour la lisibilité, le type étant deviné à la lecture de la valeur.
**Pourquoi :** c'est la conclusion explicite du chapitre, qui garde la seconde écriture pour les cas où le type n'est pas devinable : les conversions.

**3. B.** Une conversion impossible lève une erreur nommant la valeur en cause ; le langage ne remplace pas silencieusement par zéro.
**Pourquoi :** le chapitre cite le message `ValueError: invalid literal for int() with base 10` et insiste : le lire en entier est le bon réflexe.

**4. A.** `type()` renvoie la classe de la valeur, donc ce qu'elle est réellement — pas ce qu'on croyait.
**Pourquoi :** le chapitre en fait l'instrument de contrôle permanent à utiliser dans le doute, réflexe que la suite du parcours ne démentira pas.

**5.** Attendu : on convertit `"25"` en `int` avec `int("25")` (type `int`), puis on additionne 3, ce qui donne `28`, de type `int` également.
**Pourquoi :** sans conversion explicite, `"25" + 3` serait une erreur de types — la saisie textuelle reste une chaîne jusqu'à ce qu'on la convertisse, comme l'annonce le chapitre en lien avec le chapitre 07.

</details>

---

[Sommaire](Readme.md) · [Chapitre précédent →](05-variables-notions-plus-avancees.md) · [Chapitre suivant →](07-interaction-avec-lutilisateur.md)
