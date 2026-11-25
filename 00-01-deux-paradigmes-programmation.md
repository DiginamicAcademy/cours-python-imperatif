[Sommaire](Readme.md) · [Chapitre suivant →](00-02-introduction-a-python.md)

# 00.1 - Deux paradigmes : impératif et objet

> Ce cours enseigne la programmation impérative en Python. Et pourtant, il est
> question d'« objet » dès la première page. Pourquoi ? Parce qu'en Python, tout
> — ou presque — est objet. Pas de panique : on pose ici seulement les mots,
> les concepts reviendront pas à pas.

**Durée :** ≈ 15 min (lecture ≈ 10 min + réflexion) · **Prérequis :** aucun, aucune ligne de code écrite auparavant

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Définir** la programmation impérative et ce qu'on entend par « état d'un programme ».
- **Opposer** programmation impérative et programmation déclarative.
- **Expliquer** ce qu'est un objet et ce qu'il apporte par rapport à une simple suite d'instructions.
- **Justifier** pourquoi un cours de Python « impératif » parle quand même d'objets.

---

## I. La programmation impérative

### A. Décrire des étapes

La **programmation impérative** est un paradigme de programmation qui utilise des
instructions pour modifier l'**état** d'un programme. Le programmeur décrit
explicitement les étapes que l'ordinateur doit suivre pour obtenir le résultat
souhaité : il écrit une séquence de commandes que la machine exécute dans l'ordre.

On fait souvent la comparaison avec une **recette de cuisine** : pour fabriquer une
pizza, on écrit toutes les étapes, dans l'ordre, du préchauffage du four à la
sortie du four. L'ordinateur est un cuisinier très obéissant et très littéral :
il fait exactement ce qui est écrit, dans l'ordre où c'est écrit.

C'est le paradigme de ce cours. Vous allez écrire des instructions, les unes après
les autres, et observer l'état du programme changer à chaque ligne.

### B. Ce à quoi elle s'oppose

La programmation impérative s'oppose à la **programmation déclarative**, dans
laquelle le programmeur spécifie **quel** résultat il veut, et laisse la machine
déterminer **comment** y parvenir.

Toujours la métaphore de la pizza : en déclaratif, vous appelez une pizzeria et
vous déclarez que vous souhaitez une 4 fromages. Vous n'avez pas dit comment la
faire ; vous avez dit ce que vous vouliez obtenir.

Les deux approches coexistent et se complètent. En SQL (le langage des bases de
données), on déclare ce qu'on veut récupérer ; en Python, on écrit le comment.
Retenez simplement cette distinction : **impératif = les étapes, déclaratif = le
résultat attendu**.

---

## II. La programmation orientée objet

### A. Une autre manière d'organiser le code

La **programmation orientée objet** — **POO** — correspond à une autre manière
d'imaginer, de construire et d'organiser son code. Elle repose sur le concept
d'**objets** : des entités qui possèdent leurs propres variables et leurs propres
fonctions.

Ses objectifs principaux : rendre le code plus clair, mieux structuré, plus
modulable, plus facile à maintenir et à déboguer. Quand un programme grossit, une
simple suite d'instructions devient difficile à suivre ; l'objet est une manière de
ranger le code en boîtes cohérentes.

C'est un passage obligé dans de nombreux langages, et un sujet réputé ardu quand
on le rencontre pour la première fois. Il est normal de ne pas tout comprendre
d'un coup : suivez ce cours à votre rythme, une bonne partie de ce qui vous
échappe ici s'éclairera en écrivant du code. Les concepts objet sont repris en
détail dans le cours consacré à la programmation orientée objet.

### B. Un objet, dans la vie réelle puis en code

Dans la vie réelle, un objet possède des caractéristiques et permet de réaliser
des actions. Un crayon a une taille, une couleur, une forme ; il sert à écrire ou
à dessiner.

Le concept informatique s'inspire directement de cette définition :

- les **caractéristiques** deviennent des variables portées par l'objet (on les
  appelle des attributs) ;
- les **actions** deviennent des fonctions portées par l'objet (on les appelle des
  méthodes) ;
- l'ensemble forme un **bloc de code cohérent**.

Comme les objets de la vie courante, les objets informatiques peuvent être très
simples ou très complexes.

### C. Python, langage orienté objet

Python est un langage résolument orienté objet : le langage tout entier est
construit autour de la notion d'objet. En pratique, quasiment tout en Python est
un objet, et vous allez manipuler des objets dès le premier chapitre.

Une chaîne de caractères, un nombre, une liste sont des objets : ils possèdent
des caractéristiques et savent faire des choses. C'est exactement ce que vous
utiliserez en appelant des méthodes sur des chaînes de caractères plus loin dans
ce cours. Pas besoin de savoir *construire* un objet pour commencer : il faut
surtout accepter que **votre variable est un objet**.

---

## III. Les standards de code

Écrire du code qui fonctionne ne suffit pas : il faut écrire du code que quelqu'un
d'autre — ou vous dans six mois — peut lire.

La référence en la matière est la **PEP 8** (**Python Enhancement Proposal** n° 8,
le document qui fixe les conventions d'écriture du code Python) :
<https://peps.python.org/pep-0008/>. Vous n'avez pas à la mémoriser. Gardez
seulement l'idée qu'il existe une manière attendue d'écrire du Python, et que les
outils de l'écosystème la vérifient pour vous.

---

## Points clés

- **Impératif = les étapes.** On décrit une séquence d'instructions qui modifie
  l'état du programme, dans l'ordre.
- **Déclaratif = le résultat.** On dit ce qu'on veut obtenir, la machine choisit
  comment.
- Un **objet** rassemble des variables (caractéristiques) et des fonctions
  (actions) dans un même bloc cohérent.
- En Python, **tout est objet** : on manipule des objets dès la première variable.
- Il existe une manière attendue d'écrire du Python : la **PEP 8**.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Comment définit-on la programmation impérative ?

- A. Une manière de programmer où l'on décrit explicitement les étapes, dans l'ordre, qui modifient l'état du programme
- B. Une manière de programmer où l'on décrit le résultat voulu et où l'interpréteur choisit lui-même les étapes à exécuter
- C. Une manière de programmer qui consiste à écrire des objets isolés les uns des autres, sans suite d'instructions
- D. Une manière de programmer réservée aux langages compilés, qui interdit de modifier l'état d'un programme

**2.** On appelle une pizzeria et l'on commande une 4 fromages, sans dire comment la fabriquer. À quel paradigme cette situation correspond-elle ?

- A. À l'impératif, puisque l'on passe une commande qui va déclencher des étapes
- B. À la programmation déclarative : on spécifie le résultat attendu et quelqu'un d'autre détermine comment l'obtenir
- C. À la programmation orientée objet, puisque la pizza est un objet possédant des caractéristiques
- D. À aucun des deux, la métaphore de la pizza n'illustrant que la programmation impérative

**3.** Qu'est-ce qu'un objet en programmation ?

- A. Un bloc de code cohérent qui regroupe ses propres variables et ses propres fonctions
- B. Une variable particulière qui accepte à la fois des nombres et du texte
- C. Un fichier source que l'on importe depuis la bibliothèque standard de Python
- D. Une instruction qui modifie l'état du programme à un instant donné

**4.** Pourquoi un cours de Python « impératif » parle-t-il d'objets dès le premier chapitre ?

- A. Parce que la syntaxe impérative de Python est identique à celle des langages objet
- B. Parce qu'il faut savoir fabriquer une classe avant d'écrire la première ligne de code
- C. Parce que presque tout y est déjà un objet : ce que l'on manipule dès la première variable
- D. Parce que les programmes impératifs deviennent plus courts que les programmes objet

**5.** *Question ouverte (2-3 lignes).* Décrivez une tâche de votre quotidien une fois en mode « étapes » et une fois en mode « résultat attendu ». Qu'est-ce qui change dans ce que vous avez à dire ?

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. A.** L'impératif décrit explicitement les étapes que l'ordinateur suit, dans l'ordre, et chacune modifie l'état du programme.
**Pourquoi :** c'est la définition donnée par le chapitre, et la recette de cuisine n'est qu'une image de cette séquence d'instructions.

**2. B.** Commander sans décrire la fabrication, c'est déclarer un résultat : c'est la programmation déclarative.
**Pourquoi :** le chapitre oppose précisément les deux : en impératif on écrit les étapes de la pizza, en déclaratif on appelle la pizzeria.

**3. A.** Un objet est un bloc de code cohérent possédant ses propres variables (ses caractéristiques) et ses propres fonctions (ses actions).
**Pourquoi :** c'est la transposition directe de l'objet de la vie réelle : le crayon a une couleur et sert à écrire.

**4. C.** Python est construit autour de la notion d'objet : une chaîne, un nombre, une liste sont des objets, donc on en manipule immédiatement.
**Pourquoi :** le chapitre insiste : il n'est pas nécessaire de savoir construire un objet pour commencer, mais il faut accepter que chaque variable en est un.

**5.** Attendu : la version « étapes » énumère une succession d'actions ordonnées (prendre les clés, marcher jusqu'à l'arrêt, attendre, monter…), la version « résultat » énonce l'état final voulu (« être arrivé au travail à 8 h 45 ») sans dire comment.
**Pourquoi :** c'est exactement la distinction impératif/déclaratif : dans le premier cas on décrit le *comment*, dans le second le *quoi*, et l'exécution est laissée à d'autres (ou à la machine).

</details>

---

[Sommaire](Readme.md) · [Chapitre suivant →](00-02-introduction-a-python.md)
