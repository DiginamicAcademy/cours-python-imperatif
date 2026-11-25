[Sommaire](Readme.md) · [Chapitre précédent →](02-les-chaines-de-caracteres.md) · [Chapitre suivant →](04-les-booleens.md)

# 03 - Les nombres

> Deux types suffisent pour commencer à compter : les entiers et les nombres à
> virgule. Les pièges ne sont pas dans l'écriture, mais dans ce que le second ne
> sait pas faire.

**Durée :** ≈ 10 min (lecture ≈ 7 min + réflexion) · **Prérequis :** [Les variables](01-les-variables.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Écrire** un entier positif ou négatif, et **utiliser** les `_` comme séparateurs de lisibilité.
- **Écrire** un nombre décimal (*flottant*) avec un point.
- **Distinguer** `int` et `float`, et savoir laquelle des deux écritures votre programme a retenue.

---

## I. Les nombres entiers — `int`

### A. Écrire un entier

Un **entier** — *integer*, type `int` — s'initialise simplement. Sa longueur ne se
limite pas à ce que peut contenir un registre du processeur : elle dépend de la
mémoire disponible sur votre machine. Vous pouvez écrire des entiers **positifs**
comme **négatifs**, aussi grands que nécessaire.

```python
nombre_entier_positif = 68373433
print(nombre_entier_positif)
```

### B. Les underscores, pour l'œil

Vous pouvez séparer par des underscores `_` les chiffres qui constituent un nombre,
pour le rendre plus lisible :

```python
nombre_entier_positif = 68_373_433 # population de la France au 1er janvier 2024 (INSEE)
print(nombre_entier_positif)
```

Il s'agit bien de la **même valeur** : les underscores sont ignorés par
l'interpréteur, ils n'apparaissent pas à l'affichage. C'est un commentaire écrit
dans le nombre.

Les négatifs se comportent identiquement — y compris avec des séparateurs absurdes,
que l'on évite en pratique :

```python
nombre_entier_negatif = -1_000_000
nombre_entier_negatif_simplifie = -1_0_0_0_0_0_0 # à éviter, mais possible
print(nombre_entier_negatif, nombre_entier_negatif_simplifie)
```

---

## II. Les nombres décimaux — `float`

### A. Écrire un flottant

Les nombres **décimaux**, dits « flottants » (type `float`), s'écrivent avec un
**point** et non une virgule : la virgule, en Python, sert à autre chose (elle
sépare des valeurs, comme vous le verrez au chapitre 05 avec les affectations
parallèles).

```python
pi = 3.141592653
print(pi)
```

### B. Lisibilité et négatifs

Les underscores fonctionnent aussi pour les flottants, des deux côtés du point :

```python
pi_simplifie = 3.141_592_653

flottant_negatif = -23.0
flottant_negatif_simplifie = -1_000.000_1

print(pi_simplifie)
print(flottant_negatif, flottant_negatif_simplifie)
```

Notez l'écriture `-23.0` : un `.` suivi d'un `0` suffit à faire de `-23` un
flottant et non un entier. C'est le type, pas la valeur, qui change — et le type
déterminera ce que vous pourrez faire du nombre.

> ⚠️ **Un flottant n'est pas une décimale exacte**
>
> Un `float` est stocké en binaire, avec un nombre fini de chiffres. Certaines
> opérations décimales simples donnent donc des résultats inattendus en fin de
> nombre. Ce n'est pas un bug de Python : c'est la représentation elle-même. On ne
> compare donc pas deux flottants avec un `==` sans précaution.

---

## Points clés

- Deux types pour les nombres : **`int`** pour les entiers, **`float`** pour les
  décimaux.
- La taille d'un `int` en Python dépend de la **mémoire disponible**, pas d'une
  limite de 32 ou 64 bits.
- Les **underscores** `_` dans un nombre sont ignorés : ils servent uniquement à
  l'œil.
- Un flottant s'écrit avec un **point** ; `-23.0` est un `float`, `-23` est un `int`.
- Un `float` est une approximation binaire : on ne le compare pas à l'égalité stricte.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** À quoi servent les underscores écrits dans un nombre, comme `68_373_433` ?

- A. À rendre le nombre plus lisible à la lecture du code, sans changer sa valeur
- B. À marquer que le nombre est un flottant plutôt qu'un entier ordinaire
- C. À séparer la partie entière de la partie décimale d'un nombre à virgule
- D. À indiquer à l'interpréteur que le nombre doit être arrondi à l'affichage

**2.** Quelle écriture obtient un nombre de type `float` ?

- A. `-23`, puisque tout nombre signé est un décimal
- B. `-23.0`, puisque le point suivi d'un chiffre fait basculer la valeur en flottant
- C. `-23_0`, puisque l'underscore sert de séparateur décimal
- D. `-23f`, puisque le suffixe explicite demande un flottant au compilateur

**3.** Quelle est la limite de grandeur d'un entier en Python ?

- A. Elle dépend de la mémoire disponible sur la machine, pas d'une largeur fixe de registre
- B. Elle est fixée à dix chiffres, comme dans la plupart des tableurs
- C. Elle est plafonnée à deux milliards, comme dans les langages compilés
- D. Elle dépend du nombre de variables déjà déclarées dans le script

**4.** Pourquoi écrit-on `3.14` et non `3,14` ?

- A. Parce que la virgule est réservée aux nombres négatifs en Python
- B. Parce que la virgule sert à séparer plusieurs valeurs, et non à écrire un décimal
- C. Parce que la virgule obligerait à convertir le nombre avant chaque affichage
- D. Parce que la virgule n'appartient pas au jeu de caractères autorisé dans un fichier source

**5.** *Question ouverte (2-3 lignes).* On vous donne `1_000_000`, `1000000` et `1.000_000`. Donnez le type et la valeur de chacun.

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. A.** Les underscores sont ignorés par l'interpréteur : ils n'existent que pour l'œil de celui qui lit le code.
**Pourquoi :** le chapitre les compare à « un commentaire écrit dans le nombre » ; la valeur affichée reste la même.

**2. B.** `-23.0` est un `float` parce qu'un point et au moins un chiffre en font un décimal ; `-23` reste un `int`.
**Pourquoi :** c'est un exemple direct du chapitre : c'est le type, pas la valeur, qui change — et le type décide des opérations possibles.

**3. A.** Un `int` Python n'a pas de largeur fixe : sa taille dépend de la mémoire disponible.
**Pourquoi :** le chapitre l'énonce explicitement, ce qui permet d'écrire des entiers bien plus grands que deux milliards sans rien configurer.

**4. B.** Le point écrit la partie décimale ; la virgule, elle, sépare plusieurs valeurs dans une même ligne de code.
**Pourquoi :** le chapitre annonce ce double usage de la virgule, qui apparaîtra avec les affectations parallèles du chapitre 05.

**5.** Attendu : `1_000_000` et `1000000` sont tous deux des `int` valant un million ; `1.000_000` est un `float` valant un entier approché, c'est-à-dire `1.0`.
**Pourquoi :** les underscores ne changent rien et n'obligent pas à être groupés par trois ; le point, lui, place la valeur côté décimal, et les chiffres qui suivent ne pèsent plus que par leur position.

</details>

---

[Sommaire](Readme.md) · [Chapitre précédent →](02-les-chaines-de-caracteres.md) · [Chapitre suivant →](04-les-booleens.md)
