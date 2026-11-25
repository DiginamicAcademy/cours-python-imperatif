[← Chapitre précédent](24-les-environnements-virtuels.md) · [Sommaire](Readme.md)

# A - Glossaire et ressources

> **Nature :** annexe de référence · **Usage :** tout au long du cours

Cette page rassemble les sigles et les termes employés dans les chapitres, avec
leur définition, puis les ressources de référence — la documentation officielle
en tête. Chaque terme se travaille dans le chapitre indiqué entre parenthèses :
c'est là qu'il est manipulé, pas ici.

---

## Acronymes

| Sigle | Signification | En clair |
| --- | --- | --- |
| **CSV** | Comma Separated Values | un fichier où chaque ligne est un enregistrement et chaque valeur est séparée par une virgule |
| **IA** | intelligence artificielle | le domaine qui a fait la fortune de Python ces dix dernières années, sans être l'objet de ce cours |
| **IDE** | Integrated Development Environment | un logiciel qui réunit éditeur, exécution et débogage ; VS Code en tient le rôle ici |
| **ISO** | International Organization for Standardization | l'organisme de normalisation ; le cours rencontre sa norme de date, `AAAA-MM-JJ` |
| **JSON** | JavaScript Object Notation | un format texte de données structurées, que Python sait lire et écrire |
| **PEP** | Python Enhancement Proposal | les documents officiels qui décrivent le langage et ses usages ; la PEP 8 fixe le style du code |
| **PATH** | (nom de variable, pas un sigle) | la variable d'environnement qui liste les dossiers où le système cherche une commande |
| **pip** | (nom d'outil, qui ne se développe pas) | la commande qui installe, liste et désinstalle les paquets Python |
| **POO** | programmation orientée objet | l'autre paradigme : des objets portant à la fois des données et des comportements |
| **PyPI** | Python Package Index | le catalogue en ligne des paquets publiés par la communauté Python |
| **RGB / RGBA** | Red Green Blue (Alpha) | une couleur à trois composantes, plus une quatrième de transparence ; un exercice du cours les démêle |
| **SQL** | Structured Query Language | le langage avec lequel on interroge une base de données relationnelle |
| **UTF-8** | Unicode Transformation Format, 8 bits | l'encodage de texte qui fait passer les accents et les guillemets dans un fichier |
| **URL** | Uniform Resource Locator | l'adresse complète d'une page ou d'un fichier sur le web |
| **venv** | virtual environment | le module qui crée un environnement virtuel, c'est-à-dire un Python isolé pour un projet |
| **VS Code** | Visual Studio Code | l'éditeur installé au chapitre d'ouverture : gratuit, multiplateforme, extensible |
| **XOR** | eXclusive OR | le « ou » exclusif : vrai quand un seul des deux opérandes est vrai |

---

## Termes techniques clés

- **Affectation** — l'opération `nom = valeur`, qui associe un nom à un objet ; elle se lit de droite à gauche (chap. 01).
- **Annotation de type** — l'écriture `def aire(longueur: float) -> float:`, qui annonce les types attendus : elle documente le code et se laisse lire par les outils, sans changer l'exécution (chap. 21).
- **Argument** — la valeur effectivement transmise au moment de l'appel d'une fonction (chap. 19).
- **Bloc** — l'ensemble des instructions regroupées sous une même indentation, sous un `if`, une boucle ou une fonction (chap. 11).
- **Booléen** — la valeur `True` ou `False`, sur laquelle repose toute condition (chap. 04).
- **Boucle** — l'instruction qui répète un bloc : `for` parcourt une collection, `while` tourne tant qu'une condition tient (chap. 16).
- **Chaîne de caractères** — une suite de caractères entre guillemets : `'12'` y reste du texte, pas un nombre (chap. 02).
- **Clé** — l'étiquette à laquelle une valeur est associée dans un dictionnaire ; elle doit y être unique (chap. 17).
- **Compréhension de liste** — l'écriture `[x * 2 for x in nombres]`, qui fabrique une liste à partir d'une autre en une ligne (chap. 16).
- **Condition** — le test `if` / `elif` / `else`, qui choisit quelle branche s'exécute (chap. 11).
- **Constructeur de type** — l'appel `int()`, `float()`, `str()`, `bool()`, `list()`, qui fabrique un objet de ce type ou convertit une valeur dans ce type (chap. 06).
- **Débogage** — l'exécution pas à pas, arrêtée sur un point d'arrêt, pour regarder l'état du programme pendant qu'il vit (chap. 00.3).
- **Docstring** — la chaîne placée en tête d'un module ou d'une fonction : la documentation lisible par `help()` et par l'éditeur, à la différence du commentaire (chap. 22).
- **Ensemble (set)** — une collection non ordonnée qui refuse les doublons (chap. 18).
- **Environnement virtuel** — un interpréteur et ses paquets, isolés dans un dossier, propres à un projet (chap. 24).
- **Échappement** — la séquence `\n`, `\t` ou `\\`, qui donne au caractère suivant un sens spécial dans une chaîne (chap. 02).
- **Formateur automatique** — l'extension qui réécrit le code selon un style régulier sans toucher à son comportement ; le cours emploie Black Formatter (chap. 00.3).
- **f-string** — la chaîne écrite `f"{prenom} a {age} ans"`, où ce qui est entre accolades est évalué puis injecté (chap. 10).
- **Fonction** — un bloc de code nommé, défini une fois avec `def` et appelé autant de fois que nécessaire (chap. 19).
- **Immuable** — se dit d'un objet qu'on ne peut pas modifier après sa création : `int`, `float`, `bool`, chaîne, tuple (chap. 13).
- **Index** — la position d'un élément dans une liste ou une chaîne, en comptant à partir de 0 (chap. 14).
- **Interpréteur** — le programme qui lit et exécute le code ligne à ligne, sans étape de compilation préalable (chap. 00.2).
- **Itérable** — ce qu'une boucle `for` peut parcourir élément par élément : liste, chaîne, dictionnaire, `range()` (chap. 16).
- **Liste** — une collection ordonnée et modifiable, `[1, 2, 3]` (chap. 14).
- **Match-case** — l'aiguillage `match valeur:` suivi de `case …:`, qui compare une valeur à plusieurs formes attendues (chap. 11).
- **Module** — un fichier Python contenant du code réutilisable ; la bibliothèque standard est installée avec Python, les modules tiers s'ajoutent (chap. 12 et 23).
- **Muable (mutable)** — se dit d'un objet qu'on modifie sur place : liste, dictionnaire, ensemble (chap. 13).
- **Opérateur arithmétique** — `+`, `-`, `*`, `/`, puis `//` pour la division entière, `%` pour le reste et `**` pour la puissance (chap. 09).
- **Opérateur de comparaison** — `==`, `!=`, `<`, `<=`, `>`, `>=` : le résultat est un booléen (chap. 09).
- **Opérateur logique** — `and`, `or`, `not`, qui combinent ou inversent des booléens (chap. 11).
- **Opérateur ternaire** — l'écriture `vrai_si_vrai if condition else vrai_si_faux`, qui tient une décision sur une ligne (chap. 11).
- **Paquet (package)** — un module publié par la communauté et installé avec `pip install` (chap. 23).
- **Paramètre** — la variable inscrite dans la signature de la fonction, qui recevra l'argument à l'appel (chap. 19).
- **Paradigme** — une manière d'organiser un programme ; celui de ce cours est impératif, et le chapitre d'ouverture pose les mots de l'autre, la POO, sans la pratiquer (chap. 00.1).
- **Portée** — la zone du code où un nom est visible : locale dans la fonction, globale hors d'elle (chap. 19).
- **`range()`** — la séquence d'entiers produite par `range(10)`, employée pour faire tourner une boucle un nombre fixé de fois (chap. 14).
- **Récursivité** — une fonction qui s'appelle elle-même pour traiter un problème plus petit à chaque tour (chap. 19).
- **Référence** — ce que contient une variable : un accès à l'objet en mémoire, pas la valeur copiée ; deux variables peuvent viser le même objet (chap. 05 et 13).
- **Slice (tranche)** — le morceau extrait par `collection[début:fin]`, la borne de fin restant exclue (chap. 14).
- **Tuple** — une collection ordonnée immuable, `(1, 2, 3)` (chap. 15).
- **Type** — la nature d'un objet : `int`, `float`, `str`, `bool`, `list`… Python le détermine à l'exécution, et une même variable peut changer de type (chap. 01).
- **`*args` et `**kwargs`** — les deux écritures qui laissent une fonction accepter autant d'arguments positionnels ou nommés qu'on lui en passe (chap. 20).
- **Valeur de retour** — ce qu'une fonction rend par `return` ; sans `return`, elle rend quand même `None`, la valeur du rien (chap. 19).

---

## Ressources utiles

### La documentation du langage

- **Documentation officielle, Python 3.11** — <https://docs.python.org/3.11/> — la référence, en anglais ; le tutoriel et la bibliothèque y sont complets.
- **Le tutoriel officiel** — <https://docs.python.org/3.11/tutorial/index.html> — le parcours guidé, du premier `print()` aux structures de données.
- **Fonctions intégrées** — <https://docs.python.org/3.11/library/functions.html> — `len()`, `print()`, `input()`, `dir()`, `help()`… : tout ce qui est disponible sans rien importer.
- **Types standards, dont les méthodes de chaînes** — <https://docs.python.org/3.11/library/stdtypes.html#string-methods> — la liste complète des méthodes vues au chapitre 08, avec leur signature exacte.
- **PEP 8, le style officiel du code Python** — <https://peps.python.org/pep-0008/> — ce que la communauté attend d'un code lisible.

### Le poste de travail

- **VS Code, la documentation** — <https://code.visualstudio.com/docs> — installation, extensions Python, débogueur.
- **Installer Python sous Windows** — <https://docs.python.org/3.11/using/windows.html> — l'installeur, l'option `PATH`, les versions côte à côte.

### Les paquets et les environnements

- **PyPI** — <https://pypi.org/> — le catalogue des paquets publiés par la communauté.
- **pip** — <https://pypi.org/project/pip/> — l'outil derrière `pip install`, `pip list`, `pip uninstall`.
- **Le module `venv`** — <https://docs.python.org/3.11/library/venv.html> — la création et l'activation d'un environnement virtuel.
- **quote** — <https://pypi.org/project/quote/> — le paquet de citations employé par le travail pratique de fin de cours.

---

## Dans ce cours

- La plupart des chapitres proposent un ou plusieurs exercices, avec leur correction à déplier juste après : ils servent à s'exercer, pas à être notés.
- Chaque chapitre se referme par « Vérifiez vos acquis » : cinq questions dont les réponses expliquent le pourquoi.
- Le travail pratique de fin de parcours mobilise tout le cours sur un seul livrable ; son énoncé et ses données sont fournis dans le dossier `tp/` du dépôt.
- Les deux références qui resservent vraiment : la [documentation officielle](https://docs.python.org/3.11/), citée plus haut, et les chapitres eux-mêmes — ils renvoient à la documentation plutôt que de recopier une liste de méthodes.

---

[← Chapitre précédent](24-les-environnements-virtuels.md) · [Sommaire](Readme.md)
