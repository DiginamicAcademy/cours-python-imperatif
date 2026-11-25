[← Chapitre précédent](16-les-boucles.md) · [Sommaire](Readme.md) · [Chapitre suivant →](18-les-sets.md)

# 17 - Les dictionnaires

> Une liste range des valeurs dans un ordre : on demande « le troisième élément ».
> Un dictionnaire range des valeurs derrière des noms : on demande « le nom ».
> C'est la structure que l'on retrouve derrière une réponse de web service, un
> enregistrement chargé en mémoire ou un fichier de configuration.

**Durée :** ≈ 35 min (lecture ≈ 12 min + atelier 20 min + réflexion) · **Prérequis :** [Les listes](14-les-listes.md) et [Les boucles](16-les-boucles.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Décrire** ce qu'est un dictionnaire Python et ce que l'on y associe.
- **Consulter** une valeur avec `dict[clé]` ou avec `dict.get()`, et dire lequel employer quand la clé peut manquer.
- **Modifier**, **ajouter** et **supprimer** une clé.
- **Parcourir** un dictionnaire en clés, en valeurs ou en paires `(clé, valeur)`.
- **Trier** les éléments d'un dictionnaire d'après leurs valeurs.

---

## I. Définition et création

Le dictionnaire Python est une structure de donnée régie par l'association clé - valeur. Il est l'équivalent du tableau associatif en PHP, ou de la Map en JavaScript. Il peut avoir une syntaxe proche du JSON lorsque ses clés sont des strings, ce qui le rend très adapté pour le web.

Le dictionnaire est un objet **ordonné** et [muable](13-les-objets-muables-et-immuables.md) qui possède des clés qui doivent être uniques.

```python
mon_dict = {
    "nom"   : "Bouchard",
    "prenom": "Gérard"
}
```

---

## II. Accéder aux valeurs d'un dictionnaire

2 méthodes s'offrent à nous. Nous pouvons utiliser l'opérateur d'accès `[]`, ou la méthode `get()`.

### A. `dict[clé]`

Accède à la valeur du dictionnaire située à la clé donnée. Soulève une erreur si la clé n'existe pas.

```python
from datetime import date

mon_dict = {
    "nom"           : "Bouchard",
    "prenom"        : "Gérard",
    "admin"         : True,
    "date_naissance": date(1982, 5, 26),
    "nombre_adonnes": 123627,
    "enfants"       : [
        {
            "nom"   : "Bouchard",
            "prenom": "Timothée"
        }
    ]
}

print(mon_dict["admin"])                # True
print(mon_dict["enfants"][0]["prenom"]) # Timothée
```

### B. `dict.get(clé, message)`

Accède à la valeur du dictionnaire à la clé donnée. Renvoie `None` si la clé n'existe pas. Si une string est initialisée en second paramètre, renvoie cette dernière en cas de clé introuvable.

```python
mon_dict = {
    0: "titi",
    1: "tata",
    2: "toto"
}

print(mon_dict.get(2, "La clé demandée n'existe pas !")) 
print(mon_dict.get(3, "La clé demandée n'existe pas !"))
```

> 📓 Conseil d'utilisation
>
> Utiliser `dict.get(clé)` au lieu de `dict[clé]` permet de boucler sur une liste de dictionnaires aux données incomplètes sans risquer de planter la boucle si une clé n'existe pas dans l'un d'entre eux.

---

## III. Modifier, ajouter ou supprimer une clé

### A. Modifier une valeur

On utilise la même syntaxe que pour accéder à la valeur, c'est-à-dire via l'opérateur `[clé]`. Comme les dictionnaires sont des objets [muables](13-les-objets-muables-et-immuables.md), la modification des clés est persistante.

```python
mon_dict = {
    "a": True,
    "b": True,
    "c": False
}

mon_dict["a"] = False

print(mon_dict)
```

### B. Ajouter une clé

On procède aussi simplement que lorsqu'on veut modifier la valeur d'une clé préexistante. Ici, la clé n'existe pas mais sera créée à la volée.

```python
mon_dict = {
    "test": [1, 2, 3],
    "dev" : [4, 5, 6]
}

mon_dict["prod"] = [7, 8, 9]
print(mon_dict)
```

> ⚠️ Vous ne pouvez pas utiliser la méthode `dict.get(clé)` pour modifier la valeur d'une clé ou pour ajouter une nouvelle clé.

### C. Supprimer une clé

Pour supprimer une clé, on utilise le mot clé `del`.

```python
mon_dict = {
    1: {"nom": "Chahiri", "prenom": "Hamza"},
    2: {"nom": "Martin", "prenom": "Etienne"}
}

if 2 in mon_dict: # contrôler la présence de la clé pour éviter de soulever une erreur 
    del mon_dict[2]

print(mon_dict)
```

---

## IV. Boucler sur un dictionnaire

Il est possible de boucler sur un dictionnaire directement avec une boucle `for`, et cela va, par défaut, **boucler sur les clés**.

```python
mon_dict = {
    "a": True,
    "b": True,
    "c": False
}

for cle in mon_dict: # boucle sur les clés
    print(cle) # affiche la clé
    print(mon_dict[cle]) # affiche le contenu de la clé
```

L'objet dictionnaire propose deux méthodes pour retourner une liste de ses clés, et une liste de ses valeurs : `dict.keys()` et `dict.values()`.

```python
mon_dict = {
    "a": True,
    "b": True,
    "c": False
}

for key in mon_dict.keys(): # boucle sur les clés
    print(key)

for value in mon_dict.values(): # boucle sur les résultats
    print(value)
```

Enfin, la méthode `dict.items()` retourne une liste de tuples contenant la clé et la valeur pour chaque élément.

```python
mon_dict = {
    "a": True,
    "b": True,
    "c": False
}

for item in mon_dict.items(): # récupère les données en tuples (key, value)
    print(item)

for key, value in mon_dict.items(): # Séparation de la clé et la valeur en 2 variables
    print(f"la clé {key} a pour valeur {value}")
```

---

## V. Trier un dictionnaire

On peut utiliser les méthodes `sort()` et `sorted()` en passant en paramètre la liste de tuples obtenue à partir de la méthode `dict.items()`, et utiliser le paramètre `key` pour utiliser une fonction `lambda` de tri (nous verrons les fonctions lambda dans le [chapitre consacré aux fonctions](19-les-fonctions.md)). Enfin, la liste de tuples triée obtenue peut être reconvertie en dictionnaire.

```python
mon_dict = {
    "stat_1": 23423,
    "stat_2": 432,
    "stat_3": 7823,
    "stat_4": 212310,
    "stat_5": 70,
    "stat_6": 6439267
}

# Tri par défaut par ordre croissant
# x[1]: on trie par les valeurs car dans la liste de tuples obtenue avec dict.items(), les valeur sont à l'indice 1 de chaque tuple
sorted_dict = sorted(mon_dict.items(), key=lambda x: x[1])
print(dict(sorted_dict))
```

---

## VI. Exercices

Les quatre exercices ci-dessous partagent le même jeu de données. La contrainte est la même pour tous : **les codes proposés doivent fonctionner quel que soit le nombre de sites et d'utilisateurs dans le dictionnaire**.

```python
from pprint import pprint

mes_sites = {
    0: {
        "nom": "Mon super site",
        "url": "https://monsupersite.com",
        "utilisateurs": [
            {
                "nom": "Germain",
                "prenom": "Philibert",
                "date_naissance": "1984-12-12",
                "nombre_abonnes": 87621
            },
            {
                "nom": "Kaas",
                "prenom": "Patricia",
                "date_naissance": "1978-03-26",
                "nombre_abonnes": 124
            },
            {
                "nom": "Pipoude",
                "prenom": "Serges",
                "date_naissance": "1999-01-03",
                "nombre_abonnes": 7761287
            }
        ]
    },
    1: {
        "nom": "Mon site génial",
        "url": "https://monsitegenial.com",
        "utilisateurs": [
            {
                "nom": "Sbai",
                "prenom": "Nadia",
                "date_naissance": "1978-04-01",
                "nombre_abonnes": 7627
            },
            {
                "nom": "Koch",
                "prenom": "Christine",
                "date_naissance": "2001-12-07",
                "nombre_abonnes": 8727193
            }
        ]
    }
}
```

> 📌 [Documentation de pprint](https://docs.python.org/fr/3/library/pprint.html)

### Exercice 1 — Ajouter un utilisateur (~4 min)

```python
# Ajouter un nouvel utilisateur à "Mon super site" avec le nom, prénom, date de naissance et nombre d'abonnés de votre choix et printer le dictionnaire obtenu avec pprint pour obtenir un résultat plus lisible
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] J'ai ajouté l'utilisateur **dans la liste** `utilisateurs` du bon site, et pas à côté.
- [ ] Mon utilisateur possède bien les **quatre mêmes clés** que les autres.
- [ ] Mon code ne dépend pas du nombre déjà présents d'utilisateurs.

<details>
<summary>Voir la correction</summary>

```python
# Ajouter un nouvel utilisateur à "Mon super site" avec le nom, prénom, date de naissance et nombre d'abonnés de votre choix et printer le dictionnaire obtenu avec pprint pour obtenir un résultat plus lisible

mes_sites[0]["utilisateurs"].append(
    {
        "nom": "Test",
        "prenom": "Test",
        "date_naissance": "1997-12-28",
        "nombre_abonnes": 872619
    }
)

pprint(mes_sites)
```

</details>

---

### Exercice 2 — Supprimer une abonnée (~4 min)

```python
# Supprimer l'abonnée Patricia Kaas et printer le dictionnaire obtenu avec pprint
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] J'ai supprimé un **élément de la liste** des utilisateurs, pas une clé du site.
- [ ] Je sais que la suppression d'un élément d'une liste **décale** les indices suivants.

<details>
<summary>Voir la correction</summary>

```python
# Supprimer l'abonnée Patricia Kaas et printer le dictionnaire obtenu avec pprint

del mes_sites[0]["utilisateurs"][1]

pprint(mes_sites)
```

</details>

---

### Exercice 3 — Somme des abonnés de tous les sites (~6 min)

```python
# Retourner la somme du nombre d'abonnés de tous les utilisateurs de tous les sites à l'aide d'une boucle
# Printer le résultat (16583728 sans votre utilisateur créé)
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Ma boucle externe parcourt les **sites** et ma boucle interne les **utilisateurs**.
- [ ] Mon accumulateur est initialisé **avant** les boucles, pas dedans.
- [ ] Le résultat attendu est bien **16583728** après la suppression de l'exercice 2 (et sans l'utilisateur de l'exercice 1).

<details>
<summary>Voir la correction</summary>

```python
# Retourner la somme du nombre d'abonnés de tous les utilisateurs de tous les sites à l'aide d'une boucle
# Printer le résultat

total = 0
for site in mes_sites.values():
    for utilisateur in site["utilisateurs"]:
        total += utilisateur["nombre_abonnes"]

print("nombre total d'abonné de tous les utilisateurs:", total)
```

</details>

---

### Exercice 4 — Moyenne d'âge des utilisateurs (~6 min)

```python
# Retourner la moyenne des âges en années des utilisateurs
# Printer le résultat (~32.5 sans votre utilisateur créé)
```

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Je convertis la chaîne `date_naissance` en un véritable objet de date avant de calculer.
- [ ] Je compte les utilisateurs **autrement** que par la somme des âges.
- [ ] Le résultat attendu est d'environ **32,5** après les deux exercices précédents.

<details>
<summary>Voir la correction</summary>

```python
# Retourner la moyenne des âges en années des utilisateurs
# Printer le résultat

from datetime import datetime

now = datetime.now() # objet datetime décrivant maintenant (date et heure)
compteur = total = 0

for value in mes_sites.values():
    for utilisateur in value["utilisateurs"]:
        # formattage de la date en objet datetime
        formatted_date = datetime.fromisoformat(utilisateur["date_naissance"])

        # objet timedelta à partir de la soustraction de 2 objets datetime
        time_diff = now - formatted_date

        # conversion des secondes obtenues en années
        total += time_diff.days//365.25

        # incrémentation du compteur pour faire la moyenne plus tard
        compteur += 1

print("moyenne d'âge des utilisateurs:", total / compteur)
```

</details>

---

## VII. Aller plus loin

> ⏭️ Facultatif — pas exigé pour la suite du cours.

- Les dictionnaires sont la représentation naturelle d'une réponse de web service en JSON (JavaScript Object Notation) : les exercices de ce chapitre s'enchaînent exactement comme se lit un fichier de données réelles.
- La méthode `sorted()` avec `key=lambda` est revue en détail dans le [chapitre consacré aux fonctions](19-les-fonctions.md) : c'est le moment d'y revenir si le tri vous a semblé magique.

---

## Points clés

- Un dictionnaire associe des **clés uniques** à des valeurs ; il est ordonné et muable.
- `dict[clé]` soulève une erreur si la clé manque, `dict.get(clé)` renvoie `None` (ou la valeur de secours passée en second paramètre) : `get()` protège les boucles sur des données irrégulières.
- Affecter `mon_dict[clé] = valeur` **modifie** une clé existante ou en **crée** une nouvelle ; `del mon_dict[clé]` la supprime.
- Une boucle `for` parcourt les **clés** par défaut ; `keys()`, `values()` et `items()` donnent les trois autres lectures, et `items()` permet de séparer clé et valeur en deux variables.
- On trie un dictionnaire en triant la liste de tuples rendue par `items()`, puis en reconvertissant le résultat avec `dict()`.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Quelle proposition décrit le mieux un dictionnaire Python ?

- A. Une collection ordonnée d'éléments accessibles par leur position, où les valeurs peuvent se répéter
- B. Une structure régie par l'association clé - valeur, ordonnée et muable, dont les clés doivent être uniques
- C. Une collection non ordonnée qui refuse les doublons et s'initialise avec des accolades
- D. Une fonction qui retourne simultanément les clés et les valeurs d'un objet

**2.** `mon_dict` contient les clés `0`, `1` et `2`. Que renvoie `mon_dict.get(3, "La clé demandée n'existe pas !")` ?

- A. `None`, puisque la clé 3 n'existe pas et que second paramètre ne change rien au comportement de la méthode
- B. Une erreur, car contrairement à `dict[clé]` la méthode exige que la clé soit présente
- C. `"toto"`, car la méthode renvoie la dernière valeur du dictionnaire quand la clé demandée manque
- D. `"La clé demandée n'existe pas !"`, la chaîne passée en second paramètre servant de valeur de secours

**3.** On veut ajouter la clé `"prod"` à un dictionnaire qui ne la contient pas encore. Quelle écriture y parvient ?

- A. `mon_dict["prod"] = [7, 8, 9]`, la clé étant créée à la volée par l'affectation
- B. `mon_dict.get("prod", [7, 8, 9])`, la méthode acceptant une valeur par défaut à enregistrer
- C. `del mon_dict["prod"]`, qui libère l'emplacement puis y écrit la nouvelle valeur
- D. `mon_dict.keys() = [7, 8, 9]`, la liste des clés étant le seul endroit où déclarer une clé

**4.** Que parcourt par défaut une boucle `for cle in mon_dict:` ?

- A. Les valeurs du dictionnaire, dans l'ordre de leur insertion
- B. Les paires `(clé, valeur)` du dictionnaire, une seule variable ne pouvant rien contenir d'autre
- C. Les clés du dictionnaire ; on obtient la valeur correspondante avec `mon_dict[cle]`
- D. Les tuples rendus par `dict.items()`, que la boucle dépile toute seule

**5.** *Question ouverte (2-3 lignes).* Vous bouclez sur une liste de dictionnaires venant d'un web service et certains enregistrements n'ont pas la clé `"ville"`. Quelle méthode de lecture choisissez-vous et pourquoi ?

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. B.** Le chapitre définit le dictionnaire par l'association clé - valeur, et précise qu'il est ordonné, muable, à clés uniques.
**Pourquoi :** c'est ce qui le distingue d'une liste (accès par position, doublons autorisés) et d'un set (non ordonné, doublons interdits) ; la comparaison avec le tableau associatif PHP et la Map JavaScript va dans le même sens.

**2. D.** La chaîne passée en second paramètre est renvoyée quand la clé est introuvable.
**Pourquoi :** sans ce second paramètre, `get()` renverrait `None` ; c'est `dict[clé]` qui soulève une erreur. La méthode est justement conseillée pour boucler sur des données incomplètes sans planter.

**3. A.** L'affectation via `[clé]` modifie une clé existante ou en crée une nouvelle à la volée.
**Pourquoi :** le chapitre met explicitement en garde : `dict.get()` ne permet ni de modifier une valeur ni d'ajouter une clé.

**4. C.** `for cle in mon_dict:` boucle par défaut sur les clés.
**Pourquoi :** c'est pour cela que l'on écrive `mon_dict[cle]` pour afficher le contenu ; `keys()`, `values()` et `items()` sont les trois autres manières de parcourir l'objet.

**5.** Attendu : on choisit `dict.get("ville")` (éventuellement avec une valeur de secours en second paramètre), parce qu'il renvoie `None` ou la valeur de secours au lieu de soulever une erreur quand la clé manque.
**Pourquoi :** avec `mon_dict["ville"]`, l'enregistrement le plus mal fichu de la liste interromprait toute la boucle ; `get()` rend le parcours robuste à des données irrégulières.

</details>

---

[← Chapitre précédent](16-les-boucles.md) · [Sommaire](Readme.md) · [Chapitre suivant →](18-les-sets.md)
