[← Chapitre précédent](06-les-constructeurs-de-types.md) · [Sommaire](Readme.md) · [Chapitre suivant →](08-les-methodes-de-chaines-de-caracteres.md)

# 07 - Intéragir avec l'utilisateur

> Jusqu'ici vos programmes ne savaient que réciter. Avec `input()`, ils posent une
> question. Et avec cette question arrive le premier piège du parcours : tout ce
> que tape l'utilisateur est du texte.

**Durée :** ≈ 10 min (lecture ≈ 5 min + atelier ≈ 5 min) · **Prérequis :** [Les constructeurs de types](06-les-constructeurs-de-types.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Récupérer** une saisie clavier dans une variable avec `input()`.
- **Afficher** une invite explicite avant la saisie.
- **Convertir** une saisie vers le type réellement nécessaire.
- **Expliquer** pourquoi une saisie numérique doit être convertie avant calcul.

---

## I. La fonction `input()`

### A. Poser une question, stocker la réponse

La fonction `input()` permet de stocker dans une variable le contenu de la chaîne de
caractères **saisie par l'utilisateur dans le terminal**.

```python
nombre = input("Veuillez taper un nombre : ")
# une fois que l'utilisateur a appuyé sur Entrée, nombre contient ce qu'il a écrit
print(nombre)
```

Le texte passé en argument est l'**invite** : il s'affiche sur la même ligne, pendant
que l'utilisateur tape. Le programme **s'arrête** là : il attend qu'Entrée soit
appuyée pour reprendre.

Sans argument, `input()` attend silencieusement, sans rien afficher — ce qui
déroute souvent l'utilisateur, qui ne sait pas qu'on l'interroge. Écrivez toujours
une invite.

### B. Le piège : une saisie est toujours une chaîne

> ⚠️ **La fonction `input()` retourne toujours une chaîne de caractères.**

Même si l'utilisateur tape `42`, votre variable contient `"42"`, du texte. Vous
voulez un nombre ? Vous le convertissez **explicitement**, avec ce que le chapitre
précédent vous a donné :

```python
nombre = int(input("Veuillez taper un nombre entier : "))
```

L'écriture est emboîtée : `input()` lit le texte, `int()` le convertit, l'affectation
range le résultat. C'est la forme que vous écrirez couramment. Tant que vous ne
maîtrisez pas les conditions (chapitre 11), cette conversion peut échouer si
l'utilisateur tape autre chose qu'un nombre : le programme s'arrête sur une erreur,
et c'est acceptable à ce stade.

---

### Exercice 1 — Recueillir une fiche (≈ 4 min)

Complétez le script : demandez le nom, le prénom et l'âge de l'utilisateur, puis
affichez toutes les informations à la fin du script.

```python
# Utiliser la fonction input pour recueillir le nom, le prénom et l'âge

# Afficher toutes les informations à la fin du script
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Chaque saisie affiche une invite différente et explicite.
- [ ] Les trois variables sont nommées clairement.
- [ ] Les trois valeurs sont réaffichées à la fin, et pas seulement pendant la saisie.

<details>
<summary>Corrigé</summary>

```python
nom     = input("Insérez votre nom : ")
prenom  = input("Insérez votre prénom : ")
age     = input("Insérez votre âge : ")

print(nom)
print(prenom)
print(age)
```

On peut aussi tout afficher en une ligne : `print(nom, prenom, age)`. Remarquez
qu'`age` reste une **chaîne** : elle ne permet aucun calcul tant qu'elle n'est pas
convertis en `int`.

</details>

### Exercice 2 — Calculer à partir d'une saisie (≈ 5 min)

Complétez le script : demandez à l'utilisateur un nombre entier, puis affichez ce
nombre auquel vous aurez préalablement ajouté `3.14`.

```python
# Utiliser la fonction input pour demander à l'utilisateur de donner un nombre entier

# Afficher le nombre donné auquel on a préalablement ajouté 3.14
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Votre script additionne un **nombre**, pas deux textes collés bout à bout.
- [ ] Vous avez compris ce que donnerait `input(...) + 3.14` sans conversion.
- [ ] Le résultat affiché est bien un nombre à virgule.

<details>
<summary>Corrigé</summary>

```python
nombre = input("Donnez un nombre entier : ")
print(int(nombre) + 3.14)
```

Sans le `int(...)`, l'interpréteur tenterait `"25" + 3.14` et lèverait une erreur de
types : on ne additionne pas une chaîne et un flottant. Notez aussi le résultat : un
`int` additionné à un `float` donne un `float`.

Pour s'en convaincre, remplacez un instant `print(int(nombre) + 3.14)` par
`print(type(int(nombre) + 3.14))`.

</details>

---

## Points clés

- `input()` **lit une ligne du terminal** et rend son contenu ; le texte en argument
  sert d'invite.
- Le retour d'`input()` est **toujours une chaîne**, même pour `42`.
- Une conversion explicite — `int()`, `float()` — précède tout calcul sur une saisie.
- La forme courante est emboîtée : `int(input("... : "))`.
- Sans conversion, une saisie non numérique fait échouer le programme : c'est le
  comportement attendu à ce stade, et le chapitre 11 permettra de s'en prémunir.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** L'utilisateur tape `7` puis Entrée. Que contient la variable ayant reçu `input()` ?

- A. L'entier 7, l'interpréteur devinant la nature de ce qui a été tapé
- B. La chaîne `"7"`, car `input()` retourne toujours du texte
- C. Le caractère 7, puisque le terminal ne transmet qu'un seul symbole
- D. Une valeur indéterminée, tant que le programme n'a pas affiché la variable

**2.** À quoi sert la chaîne passée en argument de `input("Votre âge : ")` ?

- A. À servir d'invite affichée sur la ligne où l'utilisateur tape sa réponse
- B. À définir la valeur par défaut utilisée si l'utilisateur ne tape rien
- C. À contrôler que la saisie commence bien par ce texte
- D. À nommer la variable dans laquelle la réponse sera rangée

**3.** Que faut-il écrire pour obtenir un entier utilisable dans un calcul ?

- A. `age = input("Âge : ")`, l'interpréteur convertissant la saisie numérique
- B. `age = int(input("Âge : "))`, la conversion étant explicite après la lecture
- C. `age = number(input("Âge : "))`, la fonction dédiée aux nombres faisant le travail
- D. `age = input(int, "Âge : ")`, le type étant passé comme premier argument

**4.** Que se passerait-il avec `"25" + 3.14` ?

- A. Le texte serait converti automatiquement et le résultat s'afficherait normalement
- B. Une erreur de types serait levée, chaîne et flottant n'étant pas additionnables
- C. Le texte serait collé au nombre, donnant la chaîne de caractères attendue
- D. La valeur 3.14 serait perdue, seul le texte étant conservé par l'opération

**5.** *Question ouverte (2-3 lignes).* Écrivez, sans l'exécuter, la ligne qui demande le prix d'un article et range un **flottant** dans la variable `prix`. Quelle saisie ferait échouer cette ligne ?

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. B.** `input()` retourne toujours une chaîne : la variable contient `"7"`, pas `7`.
**Pourquoi :** c'est l'avertissement central du chapitre, et la source de la plupart des erreurs de débutants sur les saisies numériques.

**2. A.** L'argument s'affiche comme invite, sur la ligne même de saisie ; il ne fournit aucune valeur par défaut et ne vérifie rien.
**Pourquoi :** le chapitre note qu'une saisie sans invite laisse l'utilisateur sans repère, d'où la règle « écrivez toujours une invite ».

**3. B.** On lit avec `input()`, puis on convertit avec `int()` — les deux emboîtés en une ligne.
**Pourquoi :** le chapitre présente exactement cette forme comme la forme courante ; aucune fonction `number()` n'existe, et `input()` ne prend pas de type en argument.

**4. B.** L'addition d'une chaîne et d'un flottant lève une erreur : Python ne convertit pas ces deux types entre eux automatiquement.
**Pourquoi :** c'est le correctif même de l'exercice 2 — sans le `int(...)`, l'interpréuteur tente `"25" + 3.14` et refuse.

**5.** Attendu : `prix = float(input("Prix de l'article : "))` ; la ligne échoue si l'utilisateur tape autre chose qu'un nombre au format reconnu par `float()` — par exemple du texte, une virgule à la place du point, ou rien du tout.
**Pourquoi :** le type voulu décide de la fonction de conversion, et tant que les conditions ne sont pas en place, une saisie invalide interrompt le programme au lieu d'être rattrapée.

</details>

---

[← Chapitre précédent](06-les-constructeurs-de-types.md) · [Sommaire](Readme.md) · [Chapitre suivant →](08-les-methodes-de-chaines-de-caracteres.md)
