[← Chapitre précédent](00-03-installation-du-poste-de-travail.md) · [Sommaire](Readme.md) · [Chapitre suivant →](02-les-chaines-de-caracteres.md)

# 01 - Les variables

> Une variable, c'est une étiquette collée sur une valeur. Toute la programmation
> tient presque dans cette image : on range, on retrouve, on remplace.

**Durée :** ≈ 20 min (lecture ≈ 10 min + atelier ≈ 10 min) · **Prérequis :** Python installé et un premier script exécuté ([chapitre 00.3](00-03-installation-du-poste-de-travail.md))

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Créer** une variable et **réutiliser** sa valeur dans une expression.
- **Décrire** les quatre étapes du cycle de vie d'une variable en Python.
- **Appliquer** les règles de nommage imposées par le langage et la convention `snake_case`.
- **Vérifier** qu'un nom n'est pas réservé par le langage avec le module `keyword`.
- **Reconnaître** qu'une variable Python est un objet, et le voir dans le code.

---

## I. Ce que fait une variable

### A. Stocker pour réutiliser

Les variables permettent de **stocker des données** pour les réutiliser plus tard.

```python
ma_variable = 4
print(ma_variable + 3) # 7
```

Le nom `ma_variable` désigne la valeur `4`. Partout ailleurs dans le programme,
`ma_variable + 3` vaut donc `7`. Écrire `4 + 3` fonctionnerait aussi ; la variable
devient indispensable dès que la valeur arrive d'un calcul, d'un fichier ou du
clavier de l'utilisateur, ou dès qu'elle sert plusieurs fois.

### B. Le cycle de vie d'une variable

Les grandes étapes du cycle de vie d'une variable en Python sont les suivantes :

1. **Déclaration** de son nom. L'interpréteur Python se charge alors de lui donner
   un type : c'est le **typage dynamique**, vous n'écrivez jamais le type.
2. **Affectation** (ou **assignation**) d'une valeur. Le nom pointe vers une zone
   mémoire qui stocke cette valeur. Réaffecter la variable modifie son contenu.
3. **Lecture** de la variable, autant de fois que nécessaire.
4. **Suppression** automatique, gérée par Python dès qu'elle n'est plus utilisée.

Python libère ainsi toutes les variables dont on ne se sert plus, grâce au
**ramasse-miettes** (*garbage collector*).

Cette facilité d'utilisation et ce travail réalisé dans l'ombre donnent à Python un
confort de développement certain, en contrepartie d'une perte de performance :
vous ne gérez jamais la mémoire vous-même, et vous payez ce service en vitesse
d'exécution.

---

## II. Des noms de variables valides

### A. Les règles imposées par le langage

Python n'est **pas entièrement permissif** sur le nommage des variables. Certains
noms soulèvent une erreur :

- un nom ne peut pas commencer par un chiffre ;
- un nom ne peut pas contenir d'espaces ;
- un nom ne peut contenir que des caractères alphanumériques (`A-z`, `0-9`) et le
  caractère `_` ;
- certains mots sont **réservés** par le langage, comme `print`, `bool`, `break`.

Pour obtenir la liste complète des mots réservés, on utilise le module `keyword` :

```python
import keyword
print(keyword.kwlist)
```

### B. Les conventions choisies par les développeurs

Au-delà de ce qui est légal, il existe ce qui est **attendu**. La convention
retenue par la communauté Python est le format
[snake case](https://fr.wikipedia.org/wiki/Snake_case) : des mots en minuscules
reliés par des `_`, comme `nombre_de_commandes`. D'autres langages préfèrent le
[camel case](https://fr.wikipedia.org/wiki/Camel_case) (`nombreDeCommandes`) ou
d'autres syntaxes. En Python, écrivez en `snake_case` : votre code deviendra
immédiatement reconnaissable comme du Python.

---

## III. Affecter, et voir ce qu'on manipule

### A. Les affectations simples

Python propose **plusieurs manières** d'affecter des valeurs à des variables. Ces
méthodes sont pertinentes quand elles sont utilisées avec bon sens, en privilégiant
toujours la lisibilité du code. La première d'entre elles, l'affectation simple :

```python
a = 2
b = 3
```

Les autres formes (affectations multiples et parallèles) sont étudiées au
chapitre 05, une fois que vous aurez rencontré les tuples et les dictionnaires.

### B. Votre variable est déjà un objet

**Toute variable en Python est un `objet`.** C'est pour cela que le code suivant
s'exécute sans erreur :

```python
hello = "Hello World"
print(hello.__len__())
```

On appelle une **méthode** — ici `__len__()`, qui renvoie la longueur de la chaîne —
directement sur la valeur. Vous avez rencontré ce vocabulaire au chapitre 00.1 :
une variable Python possède des caractéristiques et sait faire des choses. Nous
n'irons pas plus loin sur ce point dans ce cours, mais gardez-le en tête : quand
vous écrivez `ma_chaine.upper()`, vous utilisez exactement le même mécanisme.

---

### Exercice 1 — Créer ses premières variables (≈ 5 min)

Complétez le script suivant, puis exécutez-le.

```python
# Créer une variable prenom contenant votre prénom

# Créer une variable age contenant votre âge

# Créer une variable majeur contenant un booléen pour déterminer si oui ou non, vous êtes majeur(e)

# Créer une variable voie contenant le nombre à virgule (float) 9.75

# Afficher les variables
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Mes quatre variables portent exactement les noms demandés.
- [ ] Mon booléen est écrit `True` ou `False`, avec la majuscule initiale.
- [ ] Mon nombre à virgule utilise un point, pas une virgule.
- [ ] Le script s'exécute sans erreur et affiche les quatre valeurs.

<details>
<summary>Corrigé</summary>

```python
# Créer une variable prenom contenant votre prénom
prenom = "Victor"

# Créer une variable age contenant votre âge
age = 30

# Créer une variable majeur contenant un booléen pour déterminer si oui ou non, vous êtes majeur(e)
majeur = True

# Créer une variable voie contenant le nombre à virgule (float) 9.75
voie = 9.75

# Afficher les variables
print(prenom, age, majeur, voie)
```

Remarquez deux pièges : le booléen s'écrit `True` avec une majuscule (le `true` des
autres langages lèverait une erreur), et le nombre à virgule s'écrit avec un point —
`9,75` serait interprété comme deux valeurs séparées par une virgule.

</details>

### Exercice 2 — Repérer les noms invalides (≈ 5 min)

Le script ci-dessous ne s'exécute pas. Supprimez les variables dont le nom est
invalide, jusqu'à ce qu'il s'exécute sans erreur.

```python
break    = 3
_var     = "coucou"
123var_  = 123
%coucou% = 'ça marche là'
var_2    = 'toujours pas, non...'

print("Plus d'erreurs à signaler (ง ͠° ͟ل͜ ͡°)ง")
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Vous avez justifié chaque suppression par une règle du chapitre.
- [ ] Vous avez conservé les noms qui sont, eux, parfaitement valides.
- [ ] Le message final s'affiche dans le terminal.

<details>
<summary>Corrigé</summary>

```python
_var  = "coucou"
var_2 = 'toujours pas, non...'

print("Plus d'erreurs à signaler ദ്ദി(˵ •̀ ᴗ - ˵ )")
```

Trois lignes ont dû disparaître :

| Nom supprimé | Règle violée |
| --- | --- |
| `break` | mot réservé par le langage |
| `123var_` | commence par un chiffre |
| `%coucou%` | contient `%`, caractère non alphanumérique |

Les deux noms conservés sont parfaitement valides : un nom peut commencer par `_`,
et un chiffre en **deuxième** position ou plus est autorisé. Le contenu du texte
affecté à `var_2` n'a aucune incidence sur la validité du nom.

</details>

---

## IV. Aller plus loin

> ⏭️ **Facultatif — pas exigé pour finir la journée.**

- Référence sur les variables et les types en Python :
  <https://www.learnpython.org/en/Variables_and_Types>
- La liste des mots réservés change d'une version de Python à l'autre : comparez
  `print(keyword.kwlist)` sur votre machine avec la documentation officielle de
  votre version.

---

## Points clés

- Une variable **stocke une valeur pour la réutiliser** ; son nom est une
  étiquette, pas une boîte.
- Cycle de vie : **déclaration, affectation, lecture, suppression automatique**
  par le ramasse-miettes.
- Python pratique le **typage dynamique** : le type est déduit de la valeur, jamais
  écrit.
- Un nom de variable : pas de chiffre au départ, pas d'espace, que des caractères
  alphanumériques et `_`, et jamais un mot réservé (`keyword.kwlist` pour vérifier).
- Convention Python : **`snake_case`**.
- **Toute variable est un objet** : on peut lui appliquer des méthodes.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Que se passe-t-il quand on écrit `a = 2` ?

- A. Le nom `a` est créé, reçu le type déduit de la valeur, puis pointé vers la zone mémoire qui la stocke
- B. Une case mémoire de la taille d'un entier est réservée à l'avance, puis remplie avec la valeur demandée
- C. Le nom `a` est déclaré comme une constante, ce qui interdira de lui affecter une autre valeur
- D. Le nom `a` est enregistré dans un fichier de configuration que l'interpréteur relit à chaque exécution

**2.** Pourquoi n'a-t-on jamais à écrire le type d'une variable en Python ?

- A. Parce que l'interpréteur le déduit de la valeur assignée, ce qu'on appelle le typage dynamique
- B. Parce que toutes les variables Python partagent un unique type, quel que soit le contenu stocké
- C. Parce qu'un fichier de configuration global déclare les types utilisés par le programme entier
- D. Parce que le compilateur corrige rétroactivement le type de la variable après la première lecture

**3.** Lequel de ces noms de variables est valide ?

- A. `mon nom`, puisque deux mots séparés par un espace sont plus lisibles
- B. `2variable`, puisque le nom commence par un chiffre bien visible
- C. `_var`, puisque le underscore est autorisé et qu'un nom peut commencer par lui
- D. `break`, puisque c'est un mot court, clair et déjà connu du développeur

**4.** À quoi sert le module `keyword` ?

- A. À lister les mots réservés par Python, donc les noms interdits pour une variable
- B. À rechercher un mot de recherche dans la documentation officielle depuis le terminal
- C. À vérifier que le nom d'une variable respecte la convention `snake_case`
- D. À créer automatiquement un jeu de noms de variables valides pour un script

**5.** *Question ouverte (2-3 lignes).* En quoi l'exemple `print(hello.__len__())` montre-t-il qu'une variable Python est un objet ? Reformulez avec vos mots ce que l'on appelle.

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. A.** L'interpréteur crée le nom, lui donne un type déduit de la valeur, puis fait pointer le nom vers la zone mémoire qui stocke cette valeur.
**Pourquoi :** ce sont les étapes 1 et 2 du cycle de vie du chapitre ; la gestion de la mémoire est justement ce que Python fait « dans l'ombre » à notre place.

**2. A.** Le typage dynamique : le type est déduit de la valeur écrite à droite du `=`, il n'est jamais déclaré.
**Pourquoi :** le chapitre l'inscrit dans la première étape du cycle de vie, et en assume la contrepartie — du confort au prix de la performance.

**3. C.** `_var` est valide : le `_` fait partie des caractères autorisés et un nom peut commencer par lui.
**Pourquoi :** les trois autres violent une règle du chapitre — un espace, un chiffre en première position, et un mot réservé pour `break`.

**4. A.** `keyword.kwlist` renvoie la liste complète des mots réservés, donc la liste des noms qu'il ne faut pas donner à une variable.
**Pourquoi :** c'est l'usage indiqué par le chapitre, et cette liste évolue avec les versions de Python, d'où l'intérêt de la consulter plutôt que de la retenir.

**5.** Attendu : on n'appelle pas une fonction isolée, on appelle une méthode (`__len__()`, la longueur) **portée par la valeur** elle-même ; or c'est la définition même d'un objet que de posséder ses propres fonctions.
**Pourquoi :** le chapitre rattache ce point au chapitre 00.1 : une chaîne, comme tout objet, possède des caractéristiques et des actions, et `ma_chaine.upper()` fonctionnera de la même manière.

</details>

---

[← Chapitre précédent](00-03-installation-du-poste-de-travail.md) · [Sommaire](Readme.md) · [Chapitre suivant →](02-les-chaines-de-caracteres.md)
