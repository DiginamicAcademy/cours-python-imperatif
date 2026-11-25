[← Chapitre précédent](19-les-fonctions.md) · [Sommaire](Readme.md) · [Chapitre suivant →](21-les-annotations-de-type.md)

# 20 - Les arguments flexibles

> Vous savez écrire `add(2, 3)`. Mais que fait-on quand on ne sait pas combien
> de valeurs l'appelant va transmettre, ou quand on veut accepter des options
> nommées sans multiplier les paramètres ? Deux écritures règlent ça, et vous les
> croiserez dans presque toute la documentation de Python.

**Durée :** ≈ 25 min (lecture ≈ 10 min + atelier 15 min) · **Prérequis :** [Les fonctions](19-les-fonctions.md) et [Les dictionnaires](17-les-dictionnaires.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Collecter** un nombre variable d'arguments positionnels avec `*args`.
- **Collecter** un nombre variable d'arguments par mot-clé avec `**kwargs`.
- **Combiner** les deux dans une même signature, dans le bon ordre.
- **Reconnaître** les situations où cette souplesse est utile.

---

## I. Introduction

En Python, `*args` et `**kwargs` sont des concepts puissants pour gérer les arguments de fonction de manière flexible. Ils permettent de traiter un nombre variable d'arguments positionnels (`*args`) et d'arguments par mot-clé (`**kwargs`) dans une fonction.

---

## II. `*args` : arguments de fonction positionnels

`*args` permet de passer un nombre variable d'arguments positionnels à une fonction. Lorsque vous utilisez `*args`, vous permettez à une fonction de recevoir un nombre arbitraire d'arguments, qui seront rassemblés dans un **tuple**.

```python
def ma_fonction(*args):
    for argument in args:
        print(argument)

ma_fonction(1, 2, 3, 4, 5)
```

Dans cet exemple, la fonction `ma_fonction` accepte un nombre variable d'arguments positionnels, puis les affiche un par un.

---

## III. `**kwargs` : arguments de fonction par mot-clé

`**kwargs` permet de passer un nombre variable d'arguments par mot-clé à une fonction. Lorsque vous utilisez `**kwargs`, vous permettez à une fonction de recevoir un nombre arbitraire d'arguments sous forme de **dictionnaire**.

Voici comment vous pouvez utiliser `**kwargs` :

```python
def ma_fonction(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle}: {valeur}")

ma_fonction(nom="Alice", age=30, ville="Paris")
```

Dans cet exemple, la fonction `ma_fonction` accepte un nombre variable d'arguments par mot-clé, puis les affiche avec leur nom et leur valeur.

---

## IV. Combinaison de `*args` et `**kwargs`

Il est possible d'utiliser à la fois `*args` et `**kwargs` dans une même fonction pour gérer à la fois les arguments positionnels et les arguments par mot-clé :

```python
def ma_fonction(arg1, *args, **kwargs):
    print(f"arg1: {arg1}")
    for argument in args:
        print(argument)
    for cle, valeur in kwargs.items():
        print(f"{cle}: {valeur}")

ma_fonction("Premier", 2, 3, nom="Alice", age=30, ville="Paris")
```

Dans cet exemple, `arg1` est un argument positionnel, `*args` reçoit les arguments positionnels supplémentaires, et `**kwargs` reçoit les arguments par mot-clé.

---

## V. Utilisations courantes

`*args` et `**kwargs` sont couramment utilisés pour créer des fonctions flexibles qui peuvent traiter un nombre variable d'arguments. Voici quelques utilisations courantes :

- Créer des wrappers de fonctions pour ajouter des fonctionnalités supplémentaires sans connaître à l'avance le nombre d'arguments que la fonction d'origine peut recevoir.
- Créer des fonctions de log pour enregistrer des informations sur les appels de fonctions, notamment les arguments et les valeurs de retour.
- Créer des fonctions utilitaires qui doivent interagir avec un grand nombre d'arguments.

---

## VI. Exercices

### Exercice 1 — Somme et affichage avec `*args` (~5 min)

```python
# 1. Créez une fonction `addition` qui prend un nombre variable d'arguments et retourne leur somme. Testez la fonction.

# 2. Créez une fonction `liste_arguments` qui prend un nombre variable d'arguments et les affiche. Testez la fonction.
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] `addition` **retourne** la somme et ne l'affiche pas seulement.
- [ ] `liste_arguments` affiche **un argument par ligne**.
- [ ] J'ai testé chaque fonction avec **plusieurs séries** d'arguments de longueurs différentes.

<details>
<summary>Voir la correction</summary>

```python
# 1. Créez une fonction `addition` qui prend un nombre variable d'arguments et retourne leur somme.
def addition(*args):
    somme = sum(args)
    return somme

# Testez la fonction avec différentes séries d'arguments.
print(addition(1, 2, 3))           # Devrait afficher 6
print(addition(4, 5))              # Devrait afficher 9
print(addition(1, 2, 3, 4, 5, 6))  # Devrait afficher 21

# 2. Créez une fonction `liste_arguments` qui prend un nombre variable d'arguments et les affiche.
def liste_arguments(*args):
    for arg in args:
        print(arg)

# Testez la fonction avec différentes séries d'arguments.
liste_arguments('a', 'b', 'c')  # Devrait afficher chaque caractère sur une nouvelle ligne
liste_arguments(1, 2, 3, 4)     # Devrait afficher chaque nombre sur une nouvelle ligne
```

</details>

---

### Exercice 2 — Informations et produit avec `**kwargs` (~7 min)

```python
# 1. Créez une fonction `infos_personnelles` qui prend un nombre variable d'arguments par mot-clé et affiche ces informations. Testez la fonction.

# 2. Créez une fonction `multiplication_kwargs` qui multiplie les valeurs des arguments par mot-clé qui sont des nombres. Testez la fonction.

# Exemple :
print(multiplication_kwargs(a=2, b=3, c=4)) # 2 * 3 * 4 => 24
print(multiplication_kwargs(a=2, b="toto", c=4)) # 2 * 4 => 8
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Je parcours `kwargs` avec `.items()` pour récupérer **le nom et la valeur**.
- [ ] Dans la seconde fonction, je **teste le type** de chaque valeur avant de la multiplier.
- [ ] Mon accumulateur de produit démarre à **1**, pas à 0.
- [ ] `multiplication_kwargs(a=2, b="toto", c=4)` renvoie bien **8**.

<details>
<summary>Voir la correction</summary>

```python
# 1. Créez une fonction `infos_personnelles` qui prend un nombre variable d'arguments par mot-clé et affiche ces informations.
def infos_personnelles(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle}: {valeur}")

# Testez la fonction avec différentes séries d'arguments.
infos_personnelles(nom="Alice", age=30, ville="Paris")
# Devrait afficher :
# nom: Alice
# age: 30
# ville: Paris

infos_personnelles(prenom="Bob", profession="Ingénieur")
# Devrait afficher :
# prenom: Bob
# profession: Ingénieur

# 2. Créez une fonction `multiplication_kwargs` qui multiplie les valeurs des arguments par mot-clé qui sont des nombres.
def multiplication_kwargs(**kwargs):
    resultat = 1
    for cle, valeur in kwargs.items():
        if isinstance(valeur, (int, float)):
            resultat *= valeur
    return resultat

# Testez la fonction avec différentes séries d'arguments.
print(multiplication_kwargs(a=2, b=3, c=4))  # Devrait afficher 24
print(multiplication_kwargs(x=1, y=10, z=0.5))  # Devrait afficher 5.0
```

`isinstance(valeur, (int, float))` est la pièce maîtresse de la seconde fonction : c'est le test qui écarte `"toto"` sans émettre la moindre erreur.

</details>

---

### Exercice 3 — Tout combiner (~3 min)

```python
# 1. Créez une fonction `affiche_details` qui accepte un argument positionnel, un nombre variable d'arguments positionnels et un nombre variable d'arguments par mot-clé. Testez la fonction.
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Ma signature respecte l'ordre : argument normal, puis `*args`, puis `**kwargs`.
- [ ] J'affiche les trois sortes de données distinctement.
- [ ] Mon appel de test mélange les trois.

<details>
<summary>Voir la correction</summary>

```python
# 1. Créez une fonction `affiche_details` qui accepte un argument positionnel, un nombre variable d'arguments positionnels et un nombre variable d'arguments par mot-clé.
def affiche_details(arg1, *args, **kwargs):
    print(f"arg1: {arg1}")
    for argument in args:
        print(f"Argument supplémentaire: {argument}")
    for cle, valeur in kwargs.items():
        print(f"{cle}: {valeur}")

# Testez la fonction avec différentes combinaisons d'arguments.
affiche_details("Principal", 1, 2, 3, nom="Alice", age=30)
# Devrait afficher :
# arg1: Principal
# Argument supplémentaire: 1
# Argument supplémentaire: 2
# Argument supplémentaire: 3
# nom: Alice
# age: 30

affiche_details("Test", a=10, b=20)
# Devrait afficher :
# arg1: Test
# a: 10
# b: 20
```

Le second appel, `affiche_details("Test", a=10, b=20)`, montre que `*args` peut fort bien ne rien recevoir du tout : le tuple est simplement vide.

</details>

---

## VII. Aller plus loin

> ⏭️ Facultatif — pas exigé pour la suite du cours.

- `sum()` employée dans la correction de l'exercice 1 est une fonction intégrée qui additionne les éléments d'une séquence : elle remplace avantageusement l'accumulateur écrit à la main dans un `for`.
- Les wrappers et les fonctions de log évoqués plus haut deviennent concrets quand on découvre les décorateurs, dans le cours consacré à la programmation orientée objet.

---

## Points clés

- `*args` rassemble les arguments positionnels supplémentaires dans un **tuple** ; `**kwargs` rassemble les arguments par mot-clé dans un **dictionnaire**.
- Dans une signature, l'ordre est figé : arguments normaux, puis `*args`, puis `**kwargs`.
- Les deux peuvent rester vides : rien n'oblige l'appelant à fournir quelque chose.
- `**kwargs` se parcourt avec `.items()`, comme n'importe quel dictionnaire.
- Cette souplesse sert aux wrappers, aux fonctions de log et aux fonctions utilitaires — pas à masquer une signature mal pensée.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Dans `def ma_fonction(*args):`, que devient `args` à l'intérieur de la fonction ?

- A. Un dictionnaire dont les clés sont les positions occupées par chaque argument reçu
- B. Un tuple regroupant les arguments positionnels reçus, éventuellement vide
- C. Une liste muable dans laquelle la fonction peut ajouter de nouveaux arguments
- D. Une chaîne de caractères contenant tous les arguments séparés par des espaces

**2.** `ma_fonction(nom="Alice", age=30)` est appelée avec `def ma_fonction(**kwargs):`. Comment lire le nom et la valeur de chaque argument reçu ?

- A. En parcourant `kwargs` avec `.items()`, comme n'importe quel dictionnaire
- B. En parcourant `kwargs` en indexant par position, comme une liste
- C. En appelant `args`, qui récupère de toute façon les arguments nommés
- D. En convertissant `kwargs` en tuple, puis en prenant les éléments deux par deux

**3.** Quelle signature est correcte pour accepter un argument obligatoire, puis le reste des arguments positionnels, puis des options nommées ?

- A. `def f(**kwargs, *args, arg1):`
- B. `def f(*args, arg1, **kwargs):`
- C. `def f(arg1, *args, **kwargs):`
- D. `def f(*args, **kwargs, arg1):`

**4.** D'après le chapitre, dans quel cas cette souplesse est-elle réellement utile ?

- A. Partout, une signature à deux paramètres devant être évitée par principe
- B. Dans un wrapper, qui ajoute des fonctionnalités sans connaître à l'avance les arguments de la fonction d'origine
- C. Uniquement dans les fonctions du module `math` de la bibliothèque standard
- D. Pour remplacer les paramètres par défaut, devenus inutiles dès lors que `**kwargs` existe

**5.** *Question ouverte (2-3 lignes).* Une fonction `multiplication_kwargs(**kwargs)` doit ignorer les valeurs qui ne sont pas des nombres. Quel mécanisme permet ce tri, et pourquoi le total partiel démarre-t-il à 1 ?

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. B.** `*args` rassemble les arguments positionnels dans un tuple, qui peut être vide si l'appelant n'en passe pas.
**Pourquoi :** le chapitre écrit « rassemblés dans un tuple », et la boucle `for argument in args:` de l'exemple ne fait que parcourir ce tuple.

**2. A.** `**kwargs` est un dictionnaire, il se parcourt donc avec `.items()`.
**Pourquoi :** c'est exactement l'écriture de l'exemple `ma_fonction(nom="Alice", age=30, ville="Paris")`, qui affiche chaque nom avec sa valeur.

**3. C.** L'ordre est arguments normaux, puis `*args`, puis `**kwargs` — c'est la signature donnée en exemple dans le chapitre.
**Pourquoi :** les trois autres placeraient un paramètre obligatoire après un ramasse-tout, ce qui rendrait l'appel indécodable.

**4. B.** Le chapitre cite d'abord les wrappers : ajouter des fonctionnalités sans connaître à l'avance le nombre d'arguments de la fonction d'origine.
**Pourquoi :** les deux autres usages cités sont les fonctions de log et les fonctions utilitaires ; il ne s'agit pas d'une règle générale appliquée à toute fonction.

**5.** Attendu : on teste le type de chaque valeur avec `isinstance(valeur, (int, float))` avant de la multiplier ; l'accumulateur démarre à 1 parce que 1 est l'élément neutre de la multiplication.
**Pourquoi :** partir de 0 donnerait 0 quel que soit le produit ; la correction de l'exercice 2 commence donc à 1, et le test de type écarte `"toto"` sans lever d'erreur.

</details>

---

[← Chapitre précédent](19-les-fonctions.md) · [Sommaire](Readme.md) · [Chapitre suivant →](21-les-annotations-de-type.md)
