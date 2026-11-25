# TP - Analyser deux jeux de données

> **Nature :** TP de fin de cours, **noté** · **Durée :** ≈ 2 h (exercices 1 et 2) + ≈ 45 min d'approfondissement · **Prérequis :** les 24 chapitres du cours

---

## En bref

| Rubrique | Détail |
| --- | --- |
| Nature | TP de fin de cours — tout le programme appliqué sur deux jeux de données réels |
| Durée | ≈ 2 h pour les exercices exigés, + ≈ 45 min pour l'approfondissement |
| Travail | individuel |
| Livrables | `citations.py`, `titanic.py`, et `auteurs.py` + `classement_the.csv` si vous faites l'approfondissement |
| Notation | rendu pour notation, une note pour l'ensemble du TP ; l'approfondissement n'est pas exigé |

---

## Contexte

Vous récupérez deux jeux de données que personne n'a jamais ouverts.

D'un côté, un **corpus de citations littéraires** servi par une petite bibliothèque que l'on installe avec `pip` : on lui demande un auteur, elle rend des citations avec le livre d'origine. De l'autre, la **liste des passagers du Titanic** : 14 colonnes, un siècle, et tout ce que les archives ont laissé de trous.

Deux formats différents, un seul métier : récupérer, découper, compter, trier, et rendre un résultat lisible. C'est exactement le programme du cours, réuni dans trois programmes courts.

---

## Objectifs

À l'issue de ce TP, vous serez capable de :

- **Installer** un paquet tiers et l'utiliser dans un projet isolé.
- **Écrire** au moins deux fonctions paramétrées, documentées, qui renvoient une valeur.
- **Découper** un texte en mots et **compter** des occurrences.
- **Trier** un classement par fréquence décroissante et **filtrer** par seuil.
- **Lire** un fichier CSV (Comma-Separated Values) avec le seul module standard `csv`, en traitant les valeurs manquantes.
- **Croiser** des ensembles (`set`) et des dictionnaires pour comparer plusieurs sources.
- **Écrire** un CSV de sortie avec les colonnes demandées.

---

## Matériel

| Élément | Où |
| --- | --- |
| L'énoncé que vous lisez | `tp/TP-01-analyse-donnees.md` |
| Les données du Titanic | `tp/data/titanic_survival.csv` |
| Le repli hors-ligne des citations | `tp/citations-hors-ligne/` — son [README](citations-hors-ligne/README.md) explique le mécanisme |

Le reste s'installe.

---

## Préparatifs

1. Créez un environnement virtuel pour ce TP et activez-le (chapitre 24).
2. Installez le module de citations et ses certificats :

   ```shell
   pip install quote certifi
   ```

3. Vérifiez que la récupération fonctionne :

   ```python
   import os
   import certifi
   from quote import quote

   os.environ["SSL_CERT_FILE"] = certifi.where()

   print(quote("Edgar Allan Poe", limit=2))
   ```

   Vous devez obtenir une liste de dictionnaires, chacun avec trois clés : `quote` (le texte), `book` (le livre d'origine, parfois vide) et `author`.

### Si rien ne revient

Deux causes, deux remèdes.

- **Erreur de certificat** (`ssl.SSLCertVerificationError`) : les deux lignes sur `certifi` doivent précéder le premier appel.
- **Pas d'accès réseau** (proxy, poste fermé, site injoignable) : la fonction renvoie `None`. On bascule alors sur le **repli hors-ligne** : copiez `quote_offline.py` (il est dans `citations-hors-ligne/`) à côté de vos programmes, et changez une seule ligne d'import.

  | Votre code | Source des citations |
  | --- | --- |
  | `from quote import quote` | en ligne, le paquet installé par `pip` |
  | `from quote_offline import quote` | hors-ligne, le corpus livré avec le TP |

  Le repli expose la **même fonction** `quote(auteur, limit=...)` et rend les **mêmes dictionnaires** `quote`, `book`, `author`. Tout le reste de votre code est inchangé.

---

## Aide-mémoire : deux choses que ce cours n'a pas faites

Ce TP vous demande d'ouvrir un fichier et de lire du CSV. Vous ne l'avez pas fait en cours — le cours consacré à la programmation orientée objet y passe deux chapitres ; pour aujourd'hui, ces lignes suffisent.

```python
import csv

with open("data/titanic_survival.csv", encoding="utf-8", newline="") as fichier:
    for ligne in csv.DictReader(fichier):
        print(ligne["name"], ligne["age"])
```

- `with open(...)` : la fermeture du fichier se fait toute seule à la sortie du bloc.
- `csv.DictReader` : la première ligne du fichier fournit les clés, chaque autre ligne devient un dictionnaire. On écrit `ligne["age"]` au lieu de compter les colonnes.
- **Tout ce que `csv` lit est une chaîne de caractères** : `"29"`, et non `29` ; `""` quand la valeur manque, et non `0` ni `None`. C'est la source de la moitié des erreurs de ce TP.

Pour découper un texte en mots, avec `re` (chapitre 23) : `re.findall(r"\w+", texte.lower())` rend la liste des mots, ponctuation retirée.

---

## Exercice 1 - Trente citations d'un auteur (≈ 45 min)

Récupérez **30 citations d'Edgar Allan Poe** avec le module `quote` (ou son repli hors-ligne), puis répondez aux deux questions ci-dessous dans un fichier `citations.py`.

**Contraintes :**

- au moins **deux fonctions**, chacune avec des paramètres, un `return` et une docstring ;
- les deux inventaires attendus sont **décroissants** ;
- le programme s'exécute d'une traite, sans erreur, depuis le dossier `tp/`.

**Questions :**

1. Dressez l'inventaire des **titres de livres** classés par fréquence d'apparition dans le résultat, en ordre décroissant.
2. Dressez l'inventaire des **mots** classés par ordre décroissant de présence dans ces citations. N'affichez pas les mots présents moins de 5 fois.

Le contenu exact de ces deux inventaires n'est pas attendu tel quel : le corpus de citations bouge d'une exécution à l'autre, et il arrive de recevoir moins de 30 citations. Ce qui est regardé, c'est la méthode et la forme du résultat : ordre décroissant réel, seuil appliqué, découpage en mots propre.

---

## Exercice 2 - Le Titanic, avec le seul module `csv` (≈ 50 min)

Le fichier `data/titanic_survival.csv` décrit les passagers. Colonnes utiles :

| Colonne | Contenu |
| --- | --- |
| `pclass` | classe du passager : `1`, `2` ou `3` |
| `survived` | `1` s'il a survécu, `0` sinon |
| `age` | âge en années — vide quand l'âge est inconnu |
| `boat` | canot de sauvetage qui l'a recueilli — vide quand il n'y en a pas eu |

Les autres (`name`, `sex`, `sibsp`, `parch`, `ticket`, `fare`, `cabin`, `embarked`, `body`, `home.dest`) ne servent pas ici.

**Contraintes :**

- le module `csv` **uniquement** : ni `pandas`, ni aucun autre paquet installé par `pip` ;
- avant les questions, affichez **combien de passagers vous retenez**, et écartez ce qui n'est pas un passager ;
- rendez le tout dans un fichier `titanic.py`.

**Questions :**

1. Quelle est l'**âge moyen** des passagers dont l'âge est connu ? *(ordre de grandeur attendu : ~30 ans)*
2. Quel est le **pourcentage de survie par classe** de passager ? *(~62 % en première, ~43 % en deuxième, ~26 % en troisième)*
3. Quel **canot de sauvetage** a recueilli le plus de passagers, et **combien** ? *(le canot « 13 », avec 39 passagers)* Comptez la valeur du champ `boat` **telle qu'elle est écrite dans le fichier**.

**Données sales (au choix, quelques lignes de commentaire suffisent) :** dix lignes du fichier portent deux canots dans la même case (`13 15`, `5 7`, `C D`...). Recomptez en découpant ces cases sur les espaces : le total du canot 13 change. Expliquez en deux lignes pourquoi les deux décomptes diffèrent, et lequel vous rendez à la question 3. Le décompte attendu reste celui demandé ci-dessus.

---

## Exercice 1 bis - Approfondissement : seize auteurs (≈ 45 min, non exigé)

| | |
| --- | --- |
| Edgar Allan Poe | Victor Hugo |
| Gustave Flaubert | Ernest Hemingway |
| Agatha Christie | Friedrich Nietzsche |
| Arthur Schopenhauer | Simone De Beauvoir |
| Guy De Maupassant | Voltaire |
| Emile Zola | Georges Orwell |
| Frank Herbert | Isaac Asimov |
| Tolkien | William Shakespeare |

Récupérez **30 citations pour chacun de ces 16 auteurs**, puis répondez aux trois questions dans un fichier `auteurs.py`. Le seul paquet que vous utilisez reste le module de citations, en ligne ou hors-ligne : pour le reste, uniquement ce que le cours vous a donné — listes, dictionnaires, sets, boucles, fonctions.

1. Générez l'**ensemble des mots communs à tous ces auteurs**. *Exemple : si « concombre » apparaît dans une citation de Victor Hugo, il ne figure dans ce set que s'il apparaît aussi chez TOUS les autres auteurs.*
2. Établissez le **classement décroissant des auteurs** par le nombre de fois qu'ils utilisent le mot « the » dans leurs 30 citations, en affichant l'auteur et le nombre.
3. Écrivez ce classement dans un fichier `classement_the.csv` portant exactement deux colonnes : `auteur` et `nombre d'occurrences du mot 'the'`.

Un ensemble commun tout petit — parfois vide — est un résultat normal : 16 auteurs, 30 citations chacun, une seule intersection. Pour vous rassurer, refaites le calcul sur deux auteurs seulement, où le résultat se contrôle à l'œil.

---

## Livrables attendus

| Fichier | Contenu | Exigé |
| --- | --- | --- |
| `citations.py` | exercice 1 | oui |
| `titanic.py` | exercice 2 | oui |
| `auteurs.py` | exercice 1 bis | non |
| `classement_the.csv` | sortie de la question 3 de l'approfondissement | non |

Vos programmes doivent s'exécuter depuis le dossier `tp/`, là où se trouvent `data/` et `citations-hors-ligne/`.

---

## Rendu

Rendez les fichiers du tableau ci-dessus **sans archive et sans dossier supplémentaire**, sur le canal de rendu indiqué en séance. Le TP est noté : une note pour l'ensemble, pas une note par question.

Un programme qui ne s'exécute pas rend le reste inexploitable : faites tourner vos fichiers une dernière fois avant de les déposer.

---

## ✅ Auto-évaluation

Avant de rendre, vérifiez que :

- [ ] Mes programmes s'exécutent de bout en bout, sans erreur, depuis le dossier `tp/`.
- [ ] J'ai écrit au moins deux fonctions avec paramètres, `return` et docstring à l'exercice 1.
- [ ] Mes deux inventaires sont réellement décroissants, et le seuil de 5 occurrences est appliqué.
- [ ] J'ai lu le fichier avec le module `csv` uniquement, sans aucun paquet installé par `pip`.
- [ ] J'affiche le nombre de passagers retenus, et ce nombre n'inclut pas la ligne vide du fichier.
- [ ] Je traite l'âge manquant et le canot manquant sans lever d'erreur.
- [ ] Ma question 3 compte la valeur du champ `boat` telle qu'elle est écrite : j'obtiens 39 pour le canot 13.
- [ ] Mes arrondis sont expliqués, et mes résultats sont comparés aux ordres de grandeur annoncés.
- [ ] (Approfondissement) Mon `classement_the.csv` porte exactement les deux colonnes demandées, et s'ouvre sans tableur.
- [ ] Aucun test de débogage ne traîne dans le code rendu, et mes noms de variables restent compréhensibles.

---

## Où puiser dans le cours

| Besoin | Chapitre |
| --- | --- |
| Installer un paquet avec `pip` | [23 - Les modules](../23-les-modules.md) |
| Isoler le projet dans un environnement virtuel | [24 - Les environnements virtuels](../24-les-environnements-virtuels.md) |
| Importer un module, ou une seule de ses fonctions | [23 - Les modules](../23-les-modules.md) |
| Découper un texte avec `re.findall` | [23 - Les modules](../23-les-modules.md) |
| Compter dans un dictionnaire | [17 - Les dictionnaires](../17-les-dictionnaires.md) |
| Intersection de sets | [18 - Les sets](../18-les-sets.md) |
| Trier, en ordre décroissant | [14 - Les listes](../14-les-listes.md) |
| Parcourir | [16 - Les boucles](../16-les-boucles.md) |
| Partager le travail entre deux fonctions | [19 - Les fonctions](../19-les-fonctions.md) |
| Tester une valeur manquante | [11 - Les structures conditionnelles](../11-les-structures-conditionnelles.md) |
| Aligner une sortie lisible | [10 - Formater les chaînes de caractères](../10-formatter-les-chaines-de-caracteres.md) |
