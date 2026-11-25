[← Chapitre précédent](00-01-deux-paradigmes-programmation.md) · [Sommaire](Readme.md) · [Chapitre suivant →](00-03-installation-du-poste-de-travail.md)

# 00.2 - Introduction à Python

> Avant d'écrire la première ligne, savoir ce qu'on manipule : un langage
> interprété, lu par un humain avant de l'être par la machine. Ce chapitre ne
> contient aucun exercice : lisez-le, et installez votre poste de travail dans le
> chapitre suivant.

**Durée :** ≈ 10 min (lecture) · **Prérequis :** aucun

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Expliquer** ce que signifie « langage interprété » et ce qui le distingue d'un langage compilé.
- **Citer** les atouts de Python qui en font un langage adapté aux débutants.
- **Situer** les domaines d'utilisation de Python et les bibliothèques associées.

---

## I. Un langage interprété

Python a été créé par **Guido van Rossum**, et une version 1.0 est publiée en
**1991**. C'est un langage **interprété** : le code source est exécuté ligne par
ligne par un **interpréteur**. À la différence des langages compilés, il n'y a pas
de phase préalable de traduction du code source en code machine.

Concrètement, cela change deux choses dans votre quotidien de débutant :

- vous écrivez un fichier `.py` et vous le lancez directement, sans étape de
  compilation ;
- l'interpréteur s'arrête au moment où il rencontre le problème et affiche un
  message d'erreur — souvent bavard, toujours lisible — qui dit où chercher.

Le prix de ce confort : un programme interprété s'exécute généralement moins vite
qu'un programme compilé. Pour l'immense majorité des scripts d'entreprise, la
différence est imperceptible — et le temps gagné à écrire le code est bien
supérieur au temps perdu à l'exécuter.

---

## II. Ce qui fait la force de Python

- **Syntaxe lisible.** Python se caractérise par une syntaxe claire, proche de
  l'anglais, ce qui le rend idéal pour débuter en programmation.
- **Polyvalence.** On l'utilise dans une grande variété de domaines : développement
  web, analyse de données, automatisation de tâches, tests, administration système.
- **Grande communauté.** Python s'appuie sur une communauté de développeurs active
  et engagée, qui facilite l'apprentissage et l'entraide.
- **Bibliothèques puissantes.** L'écosystème est riche : **NumPy** pour le calcul
  scientifique, **Django** pour le développement web, **TensorFlow** pour l'apprentissage
  automatique. Vous n'aurez presque jamais à réécrire ce qui a déjà été écrit.
- **Multiplateforme.** Le même code fonctionne sur Windows, macOS et Linux, ce qui
  permet de travailler sur n'importe quel système d'exploitation.

Python est un langage populaire qui a su gagner en polyvalence. Il continue de
gagner en popularité au fil des années, notamment dans la **science des données**
(*data science*), les mathématiques et l'**intelligence artificielle** (**IA**).
Son essor récent vient surtout de ces trois domaines.

---

## III. Ce que vous allez faire de ces deux jours

Ce cours ne cherche pas à couvrir tout Python : il couvre la **programmation
impérative**, c'est-à-dire les briques que vous retrouverez dans tous les langages
et dans tous les projets.

- La première partie du parcours pose les fondations : variables, types, chaînes de
  caractères, interaction avec l'utilisateur, opérateurs, conditions, modules.
- Les conteneurs (listes, tuples, dictionnaires, ensembles), les boucles et les
  fonctions viennent dans un second temps.
- La fin du parcours vous donne les réflexes professionnels : documenter son code,
  découper un projet en modules, isoler un projet dans un **environnement virtuel**.

Un travail pratique clos le cours : il mobilise l'ensemble de ces briques sur un
jeu de données réel. Il est noté, son corrigé n'est donc pas publié avec le support.

---

## Points clés

- Python est **interprété** : le code est exécuté ligne par ligne, sans compilation préalable.
- Sa **syntaxe lisible** et sa communauté en font un langage adapté aux débutants.
- Il est **polyvalent** et **multiplateforme**, avec un écosystème de bibliothèques très riche.
- Son essai récent vient surtout de la donnée et de l'IA, mais son usage courant reste le script et l'automatisation.
- Le programme de ces deux jours : les briques impératives universelles, puis les réflexes de professionnalisation.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Que signifie « Python est un langage interprété » ?

- A. Que le code source est traduit une seule fois en code machine avant d'être exécuté
- B. Que le code source est exécuté ligne par ligne par un interpréteur, sans phase de traduction préalable
- C. Que le code doit être relu par un humain avant d'être confié à la machine
- D. Que le code est exécuté uniquement dans le navigateur internet de l'utilisateur

**2.** Pourquoi la syntaxe de Python est-elle jugée favorable aux débutants ?

- A. Parce qu'elle est claire et lisible, ce qui limite le temps passé à déchiffrer ce qui est écrit
- B. Parce qu'elle interdit d'écrire du code erroné, donc décourage la débroussaille
- C. Parce qu'elle impose un seul fichier pour tout le programme du débutant
- D. Parce qu'elle est identique à celle du langage C, que la plupart connaissent déjà

**3.** Quelle bibliothèque est associée au développement web dans le chapitre ?

- A. NumPy
- B. TensorFlow
- C. Django
- D. Python Enhancement Proposal

**4.** Quel est le compromis assumé de l'interprétation ?

- A. Une exécution généralement moins rapide, contre un confort d'écriture et de débuggage supérieur
- B. Une exécution plus rapide, contre une communauté beaucoup plus réduite
- C. Un programme réservé à Windows, contre une syntaxe plus courte
- D. Une obligation de compiler avant chaque exécution, contre un code mieux vérifié

**5.** *Question ouverte (2-3 lignes).* Citez un domaine d'utilisation de Python et expliquez, avec vos mots, ce que l'expression « langage multiplateforme » change pour une équipe qui travaille sur des postes variés.

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. B.** Interprété veut dire exécution ligne par ligne par un interpréteur, sans phase de traduction en code machine avant le lancement.
**Pourquoi :** c'est précisément ce qui oppose Python d'un langage compilé, et ce qui permet de lancer un fichier `.py` tel quel.

**2. A.** C'est la lisibilité de la syntaxe, proche de l'anglais, qui rend Python accessible à qui apprend à programmer.
**Pourquoi :** le chapitre range la syntaxe lisible en premier des atouts de Python ; elle ne rend pas le code correct pour autant, elle rend le code lisible.

**3. C.** Django est la bibliothèque de développement web citée ; NumPy relève du calcul, TensorFlow de l'apprentissage automatique.
**Pourquoi :** le chapitre associe explicitement une bibliothèque à un domaine, et **PEP** (**Python Enhancement Proposal**) désigne les documents de référence du langage, pas une bibliothèque.

**4. A.** Un programme interprété s'exécute généralement moins vite qu'un programme compilé : c'est le prix d'un confort d'écriture et d'erreur parlante.
**Pourquoi :** le chapitre conclut que pour l'immense majorité des scripts, la différence est imperceptible face au temps gagné à écrire le code.

**5.** Attendu : un domaine parmi le développement web, l'analyse de données, l'automatisation de tâches ou l'IA ; et pour le multiplateforme, l'idée qu'un même code s'exécute sur Windows, macOS et Linux, donc sans réécriture ni système imposé selon les postes.
**Pourquoi :** la polyvalence et la portabilité sont deux des atouts listés par le chapitre, et ce sont celles qui comptent le plus dans une entreprise équipée de postes hétérogènes.

</details>

---

[← Chapitre précédent](00-01-deux-paradigmes-programmation.md) · [Sommaire](Readme.md) · [Chapitre suivant →](00-03-installation-du-poste-de-travail.md)
