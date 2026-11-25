[← Chapitre précédent](11-les-structures-conditionnelles.md) · [Sommaire](Readme.md) · [Chapitre suivant →](13-les-objets-muables-et-immuables.md)

# 12 - Les modules standards de Python

> Vous avez déjà appelé `math.sqrt()` et `input()` sans jamais écrire ces
> fonctions. Elles vivent dans des **modules** : des fichiers Python que l'on
> importe au lieu de les réécrire. Ce chapitre ouvre la bibliothèque livrée avec
> Python — celle qu'on télécharge jamais, mais qu'on oublie souvent d'aller
> regarder.

**Durée :** ≈ 30 min (lecture ≈ 15 min + atelier 11 min + réflexion 4 min) · + 8 min facultatif · **Prérequis :** [Les opérateurs mathématiques](09-les-operateurs-mathematiques.md) (pour `import math`), [Les structures conditionnelles](11-les-structures-conditionnelles.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Définir** ce qu'est un module et d'où viennent les fonctions déjà disponibles.
- **Importer** un module de plusieurs façons et **choisir** la bonne.
- **Manipuler** l'arborescence et les fichiers avec `os` puis `pathlib`.
- **Explorer** un module inconnu avec `dir()`, et **créer** son propre module.

---

## I. Ce qu'est un module

Les modules sont des **fichiers Python contenant des fonctions**. Certains modules sont inclus de base avec Python, d'autres peuvent être téléchargés depuis internet. Ces derniers relèvent des *paquets* installés avec `pip` : c'est le sujet du chapitre [Les modules](23-les-modules.md), plus loin dans le cours.

---

## II. Les modules de la bibliothèque standard

Ces modules sont inclus avec Python lors de son installation dans votre système. Pour les utiliser, vous n'avez rien à télécharger, mais vous devrez les **inclure** dans votre fichier Python avec le mot-clé `import`.

### A. Le module `random`

Permet de générer des données aléatoires.

```python
import random as rd

print(rd.randint(1, 5))         # génère un entier aléatoire entre 1 et 5 inclus
print(rd.uniform(0, 1))         # génère un float aléatoire entre 0 et 1 inclus
print(rd.randrange(0, 101, 10)) # génère un entier aléatoire entre 0 et 101 exclus avec un pas de 10
```

Ici, `import random as rd` renomme le module : on écrit `rd.randint()` au lieu de `random.randint()`. Court, mais moins lisible à la relecture.

On remarque que l'opérateur `.` signifie dans `random.randint()` que l'on utilise la fonction `randint` du module `random`. On peut se passer de cette syntaxe de la manière suivante.

```python
from random import randint

print(randint(0, 5))
```

> ⚠️ **Syntaxe déconseillée.**
>
> Sauf circonstance exceptionnelle, cette dernière syntaxe est à éviter pour deux
> raisons. Si vous créez une variable portant le même nom que la fonction
> importée, vous allez écraser cette fonction. En second lieu, les bonnes
> pratiques Python précisées dans [The Zen of Python](https://peps.python.org/pep-0020/)
> établissent qu'il faut toujours privilégier l'explicite à l'implicite, quitte à
> écrire plus de code. Ici, en précisant à chaque fois le nom du module quand on
> utilise une de ses fonctions, on est plus explicite, et notre code Python est de
> meilleure qualité.

### B. Le module `os`

Permet d'accéder aux ressources du système d'exploitation.

```python
import os

chemin = "/home/digi/Documents"

# Création d'un nouveau dossier dans mes Documents
# Documents/nouveau_dossier/os
# La fonction join gère les '\' sous windows ou les '/' sous linux et mac
dossier = os.path.join(chemin, "nouveau_dossier", "os") # "/home/digi/Documents/nouveau_dossier/os"
if not os.path.exists(dossier):
    os.makedirs(dossier)

# Suppression de l'architecture de dossier nouvellement créée
if os.path.exists(dossier):
    os.removedirs(dossier)
```

Retrouvez le `if not …` du chapitre précédent : on ne crée pas ce qui existe déjà, on ne supprime pas ce qui n'existe pas.

### C. Le module `pathlib`

Disponible depuis la version 3.6, il propose une modernisation du module `os` avec une meilleure syntaxe.

```python
from pathlib import Path

chemin  = "/home/user/Documents/doc.txt"

p = Path(chemin)         # Création d'un objet Path
p.touch(exist_ok=True)   # Création du fichier txt dans le dossier Documents
p.write_text("Coucou !") # Écrit du texte dans le fichier
print(p.read_text())     # Lecture du contenu du fichier

print(p.name)            # Print le nom du fichier
print(p.suffix)          # Print l'extension du fichier
```

Un `Path` est un **objet** qui connaît son nom, son extension, son contenu : on manipule un chemin au lieu de bricoler une chaîne de caractères. C'est l'écriture à préférer aujourd'hui. Notez que l'exemple suppose que le dossier `Documents` existe déjà : `touch()` crée un fichier, pas les dossiers qui le précèdent.

---

## III. La fonction `dir()`

Permet de dresser une liste des fonctions disponibles dans un module. Utile pour savoir quelles fonctionnalités offre un module.

```python
import random

print(dir(random)) # Les fonctions avec des underscores _ ne sont pas utilisables
```

Les noms entourés de doubles underscores (`__name__`, `__doc__`, …) appartiennent au fonctionnement interne du module : ce sont les noms « publics », sans underscore, que vous pouvez appeler.

> 📌 Je vous renvoie à [la fonction `help`](08-les-methodes-de-chaines-de-caracteres.md) pour obtenir une aide sur la fonction particulière d'un module : `help(random.randint)` affiche la documentation de cette seule fonction.

---

## IV. Créer son propre module

Pour créer son propre module il suffit de créer un nouveau fichier Python. Dans le fichier où l'on veut importer ce module, un simple `import nom_du_fichier` suffit à importer tout son contenu.

Concrètement : vous écrivez vos fonctions dans `outils.py`, et n'importe quel autre script du même dossier fait `import outils` puis `outils.ma_fonction()`. Vous pratiquez ce mécanisme dès que vous découpez un exercice en deux fichiers.

> ⚠️ **Nommage du fichier.** Attention à ne pas nommer votre fichier avec le même
> nom qu'un module standard de Python comme `random.py` ou `math.py`, sous peine
> d'écraser tout leur contenu : c'est votre fichier qui serait importé à la place
> du vrai module, et l'erreur se propage loin de sa cause.

---

### Exercice 1 — Cinq nombres dans un fichier (~6 min)

```python
# Créer un script python écrivant 5 entiers aléatoires entre 0 et 100 dans un fichier .txt dans votre dossier 'Documents'
# Le résultat doit apparaître comme ceci: "Voici mes 5 nombres aléatoires: X, X, X, X et X"

# Afficher le contenu du document

# Supprimer le fichier
```

📌 [Documentation pathlib](https://docs.python.org/fr/3/library/pathlib.html)

**Avant d'ouvrir le corrigé**, vérifiez que :

- [ ] Vos cinq tirages sont bien compris entre 0 et 100 **inclus**.
- [ ] Le chemin du fichier fonctionne aussi bien sous Windows que sous Linux (pas de `C:\` recopié à la main).
- [ ] La suppression du fichier est faite **après** son affichage.

<details>
<summary>Corrigé</summary>

```python
import random
import pathlib

random_1 = random.randint(0, 100)
random_2 = random.randint(0, 100)
random_3 = random.randint(0, 100)
random_4 = random.randint(0, 100)
random_5 = random.randint(0, 100)

path = pathlib.Path.home() / "Documents" / "doc.txt"
path.write_text(f"Voici mes 5 nombres aléatoires: {random_1}, {random_2}, {random_3}, {random_4} et {random_5}")

# Afficher le contenu du document
print(path.read_text())

# Supprimer le fichier
path.unlink()
```

Trois remarques :

- `Path.home() / "Documents" / "doc.txt"` construit le chemin **selon le système** : pas besoin de savoir si le séparateur est `\` ou `/`, et le script reste valable où qu'il soit rendu. Si votre dossier personnel ne s'appelle pas `Documents` (langue ou configuration différente), adaptez simplement ce segment.
- `randint(a, b)` inclut **les deux** bornes : `randint(0, 100)` peut donc tomber sur 0 comme sur 100.
- `unlink()` supprime le fichier. Sans argument, elle échoue si le fichier n'existe pas.

*Cette version diffère volontairement de la correction d'origine*, qui écrivait un chemin Windows en dur (`C:\Users\Digivic\Documents\doc.txt`) et utilisait `randint(0, 101)` — soit un tirage possible jusqu'à 101, hors de l'intervalle demandé.

</details>

---

### Exercice 2 — Un âge avec `datetime` (~5 min)

```python
# Avec l'aide du module datetime, afficher l'âge de la personne possédant la date de naissance suivante

date_naissance = "1998-04-23"
```

📌 [Documentation datetime](https://docs.python.org/fr/3/library/datetime.html)

<details>
<summary>Corrigé</summary>

```python
# Avec l'aide du module datetime, printer l'âge en années de la personne possédant la date de naissance suivante

date_naissance = "1998-04-23"
import datetime

time_delta = datetime.datetime.now() - datetime.datetime.fromisoformat(date_naissance)

print(time_delta.days//365)
```

La date est une **chaîne** au format ISO (`AAAA-MM-JJ`) : `fromisoformat()` la convertit en objet `datetime`. La soustraction de deux dates renvoie un `timedelta`, dont on lit le nombre de jours, qu'on divise par 365 en **division entière**.

Le résultat arrondit l'année bissextile au plus juste sur de longues périodes : la valeur exacte dépend du jour où vous lancez le script, puisque `now()` change à chaque exécution.

</details>

---

### Exercice 3 — Un trieur de fichiers (~8 min, facultatif)

```python
# A l'aide du module zipfile, extraire l'archive sources.zip
# A l'aide du module pathlib, ou os, et d'une boucle, créer un trieur de fichier qui va répartir les fichiers extraits en 5 dossiers (Musique, Videos, Images, Documents, Divers) selon les règles suivantes
# 1.  mp3, wav, flac : Musique
# 2.  avi, mp4, gif : Videos
# 3.  bmp, png, jpg : Images
# 4.  txt, pptx, csv, xls, odp, pages : Documents
# 5.  autres : Divers
```

**Préparation.** L'archive n'étant pas fournie avec le cours, fabriquez-la vous-mêmes avec ce script : il crée douze fichiers vides dans un dossier `data/`, puis les range dans `sources.zip`.

```python
import pathlib
import zipfile

racine = pathlib.Path("data")
racine.mkdir(exist_ok=True)

for index, extension in enumerate([".mp3", ".wav", ".flac", ".avi", ".mp4", ".gif",
                                   ".bmp", ".png", ".jpg", ".txt", ".csv", ".xyz"]):
    racine.joinpath(f"fichier-{index}{extension}").touch()

with zipfile.ZipFile("sources.zip", "w") as archive:
    for fichier in racine.iterdir():
        archive.write(fichier, arcname=f"data/{fichier.name}")
```

📌 [Documentation ZipFile](https://docs.python.org/fr/3/library/zipfile.html)

<details>
<summary>Corrigé</summary>

```python
import zipfile  
import pathlib  
# Extraction des fichiers contenus dans l'archive
root = zipfile.ZipFile("sources.zip", "r")  
root.extractall()  

# Instanciation d'un objet path sur la racine
root = pathlib.Path("data")  
# Création d'un objet path pour chacun des futurs dossiers
musique   = root.joinpath("Musique")  
videos    = root.joinpath("Videos")  
images    = root.joinpath("Images")  
documents = root.joinpath("Documents")  
divers    = root.joinpath("Divers")  

# Itération sur tous les éléments contenus dans la racine
for file in root.iterdir():
    # iterdir() retient aussi les dossiers, on ne veut que les fichiers
    if file.is_file():  
        match file.suffix:  
            case ".mp3" | ".wav" | ".flac":
                musique.mkdir(exist_ok=True)  
                file.rename(musique / file.name)  
            case ".avi" | ".mp4" | ".gif": 
                videos.mkdir(exist_ok=True) 
                file.rename(videos / file.name)  
            case ".bmp" | ".png" | ".jpg":  
                images.mkdir(exist_ok=True)  
                file.rename(images / file.name)  
            case ".txt" | ".pptx" | ".csv" | ".xls" | ".odp" | ".pages":
                documents.mkdir(exist_ok=True)   
                file.rename(documents / file.name)  
            case _:  
                divers.mkdir(exist_ok=True) 
                file.rename(divers / file.name)
```

Ce corrigé réunit trois chapitres :

- `match case` du chapitre précédent, avec l'alternative `|` qui regroupe plusieurs valeurs dans un seul cas, et `case _` qui joue le rôle du `default` ;
- `Path.suffix` (vu plus haut) qui donne l'extension, avec le point ;
- `iterdir()` qui parcourt le dossier, filtré par `is_file()` — sinon le trieur tenterait de déplacer les dossiers qu'il vient de créer.

Les fichiers de préparation portent l'extension `.xyz` pour l'un d'eux : il doit terminer dans `Divers`, ce qui prouve que le `case _` travaille.

</details>

---

## Points clés

- Un module est un fichier Python contenant des fonctions ; la bibliothèque standard est installée avec Python, rien à télécharger.
- `import random as rd` renomme, `from random import randint` isole une fonction — et expose à l'écraser par une variable du même nom. La forme explicite `random.randint()` reste la bonne pratique.
- `pathlib.Path` remplace avantageusement `os.path` : un chemin est un objet, pas une chaîne, et `/` construit les chemins sur tous les systèmes.
- `dir()` liste ce qu'un module contient, `help()` documente une fonction précise.
- Un simple `.py` devient un module importable — à condition de ne pas lui donner le nom d'un module standard.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Quelle écriture importer est considérée comme la meilleure pratique dans ce cours ?

- A. `from random import *`, car elle évite d'écrire le nom du module à chaque ligne
- B. `from random import randint`, car une fonction importée seule est plus légère à charger
- C. `import random`, puis `random.randint()`, car l'appel dit d'où vient la fonction
- D. `import random as r`, car un nom court se retient mieux dans un long fichier

**2.** Que risque-t-on à nommer son propre fichier `random.py` ?

- A. Rien tant qu'on n'importe pas ce module dans le même projet
- B. Que son fichier soit importé à la place du module standard, et que `randint` disparaisse
- C. Que Python refuse le fichier au moment de l'exécution, avec une erreur de syntaxe
- D. Que les deux modules coexistent et que Python tire au sort celui qui répond à l'appel

**3.** Pourquoi préférer `Path.home() / "Documents" / "doc.txt"` à `"C:\\Users\\you\\Documents\\doc.txt"` ?

- A. Parce que le premier s'adapte au système et à l'utilisateur qui exécute le script
- B. Parce que le second est illisible par Python, qui n'accepte que des chemins relatifs
- C. Parce que le premier crée automatiquement tous les dossiers qui manquent sur le trajet
- D. Parce que le second ne fonctionne que si le fichier a déjà été ouvert une fois

**4.** À quoi sert la fonction `dir()` ?

- A. À créer un dossier portant le nom passé en argument
- B. À lister les noms disponibles dans un module ou un objet
- C. À afficher le code source complet d'une fonction importée
- D. À renommer un module importé sous un nom plus court

**5.** *Question ouverte (2-3 lignes).* Vous devez écrire un programme qui crée un dossier de rapport, y dépose un fichier, puis lit ce fichier. Citez deux raisons pour lesquelles `pathlib` est plus confortable qu'une chaîne de caractères que l'on assemble avec `+`.

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. C.** L'explicite bat l'implicite : `random.randint()` dit d'où vient la fonction.
**Pourquoi :** c'est le Zen of Python. En plus, une fonction importée directement dans l'espace de noms peut être écrasée par une variable du même nom, et `import *` rend le fichier illisible : on ne sait plus quel module fournit quoi.

**2. B.** Votre fichier gagne la compétition.
**Pourquoi :** Python cherche les modules dans le dossier courant avant les modules standard. `import random` chargerait alors votre fichier, et l'erreur se manifesterait bien loin de sa cause — d'où la règle de nommage.

**3. A.** Le chemin se construit selon le système et l'utilisateur.
**Pourquoi :** `Path.home()` renvoie le dossier personnel de **celui qui lance le script**, et l'opérateur `/` place le bon séparateur. Un chemin en dur ne fonctionne que sur la machine où il a été écrit — piège classique d'un exercice rendu sur un autre poste. En revanche, non : `pathlib` ne crée pas les dossiers manquants, c'est `mkdir()` qui le fait.

**4. B.** `dir()` dresse la liste des noms accessibles.
**Pourquoi :** c'est le premier réflexe face à un module inconnu, suivi de `help()` sur le nom qui semble correspondre au besoin. Les noms entourés d'underscores sont internes et ne s'appellent pas.

**5.** Attendu, deux raisons parmi : les segments se joignent avec `/` au lieu d'assembler des séparateurs à la main (et le bon séparateur est choisi selon le système) ; l'objet expose déjà ce dont on a besoin (`name`, `suffix`, `parent`) sans découper une chaîne ; les opérations sur le fichier sont des méthodes de l'objet (`touch()`, `write_text()`, `read_text()`, `unlink()`) ; un objet ne se casse pas silencieusement en deux comme une chaîne mal coupée.
**Pourquoi :** `os.path` manipule des chaînes et empile les fonctions (`os.path.join`, `os.path.exists`, `os.path.basename`) ; `pathlib` rassemble tout cela sur un seul objet, ce qui est plus lisible et plus court.

</details>

---

[← Chapitre précédent](11-les-structures-conditionnelles.md) · [Sommaire](Readme.md) · [Chapitre suivant →](13-les-objets-muables-et-immuables.md)
