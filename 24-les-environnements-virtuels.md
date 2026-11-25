[← Chapitre précédent](23-les-modules.md) · [Sommaire](Readme.md) · [Chapitre suivant →](A-Glossaire-et-ressources.md)

# 24 - Les environnements virtuels

> `pip install` écrit quelque part. Ce chapitre dit où, et comment faire que ce
> soit ailleurs pour chaque projet. C'est la dernière pierre du cours, et la
> première de tout ce qui suivra.

**Durée :** ≈ 30 min (lecture ≈ 8 min + atelier 20 min) · **Prérequis :** [Les modules](23-les-modules.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Décrire** ce qu'est un environnement virtuel et ce qu'il contient.
- **Créer** un environnement virtuel, avec ou sans version de Python précisée.
- **Activer** et **désactiver** un environnement selon le système d'exploitation.
- **Vérifier** que l'on travaille bien avec l'interpréteur de cet environnement.
- **Installer** des packages dans l'environnement, et constater qu'ils n'existent pas en dehors.

---

## I. Définition

Un environnement virtuel est une version de python indépendante de la version installée sur le système d'exploitation. Il contiendra également des librairies différentes que le python natif, en fonction des besoin du projet.

![Deux sorties de `pip list` côte à côte : à gauche, un interpréteur déjà chargé de bibliothèques de données ; à droite, un environnement neuf où ne figurent que `pip`, `setuptools` et `wheel`](assets/venv-pip-list.png)

---

## II. Création d'un environnement Python

### A. Création du dossier de l'environnement et des fichiers

```shell
# py <version:optionnel> -m venv <nom_environnement>
py -3.11 -m venv env
py -m venv C:\venv\mon_env
```

La version est optionnelle : sans elle, l'environnement est créé avec le Python par défaut. Le nom de l'environnement peut être un simple dossier relatif, comme `env`, ou un chemin complet.

### B. Activation de l'environnement virtuel

```shell
env/Scripts/activate # windows
source env/bin/activate # linux et mac
```

Si le terminal vous empêche d'exécuter le script sur windows, vous pouvez rentrer la commande suivante.

```shell
Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force
```

### C. Vérifier que l'on est dans le bon environnement

Pour connaître la version de python sur laquelle on est sur le dossier courant on peut utiliser `which python` afin de s'assurer qu'on est bien sous la version Python de notre environnement virtuel. Vous pouvez également ouvrir un interpréteur python après avoir activé votre environnement avec `python`, et de taper les instruction suivantes.

```python
import sys
sys.executable
```

Vous devriez voir le chemin de dossier de l'interpréteur courant, et il devrait se situer dans le dossier `Scripts` de votre environnement virtuel.

### D. Désactivation de l'environnement

```shell
deactivate
```

---

## III. Exercices

### Exercice 1 — Création et activation d'un environnement virtuel (~7 min)

1. Ouvrez un terminal.
2. Créez un environnement virtuel nommé `myenv` en utilisant Python 3.11.
3. Activez cet environnement virtuel.
4. Vérifiez que l'environnement virtuel est activé en affichant le chemin de l'interpréteur Python.

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] J'ai bien précisé la **version** de Python dans la commande de création.
- [ ] J'ai employé la commande d'activation de **mon** système d'exploitation.
- [ ] Le chemin affiché par la vérification se trouve **dans le dossier de l'environnement**.

<details>
<summary>Voir la correction</summary>

```shell
py -3.11 -m venv myenv

# Windows
myenv\Scripts\activate
# Linux et Mac
source myenv/bin/activate
```

```shell
# Pour vérifier l'interpréteur Python
which python

# Ou en utilisant Python
python -c "import sys; print(sys.executable)"
```

</details>

---

### Exercice 2 — Installation de packages dans l'environnement virtuel (~7 min)

1. Assurez-vous que l'environnement virtuel `myenv` est activé.
2. Installez les packages `requests` et `flask`.
3. Vérifiez que les packages sont installés en listant les packages de l'environnement.

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Mon terminal indique l'environnement **activé** avant d'installer quoi que ce soit.
- [ ] J'ai installé les deux packages en **une seule** commande `pip install`.
- [ ] Les deux packages apparaissent bien dans la liste obtenue.

<details>
<summary>Voir la correction</summary>

```shell
pip install requests flask
```

```shell
pip list
```

</details>

---

### Exercice 3 — Désactivation de l'environnement virtuel (~6 min)

1. Avec l'environnement virtuel `myenv` activé, désactivez l'environnement.
2. Vérifiez que l'environnement virtuel est désactivé et afficher de nouveau la liste des packages qui sont installés.

**Avant d'ouvrir la correction**, vérifiez que :

- [ ] Ma liste de packages ne contient **plus** `requests` ni `flask`.
- [ ] Cette comparaison se fait avec la **même commande** que dans l'exercice 2.
- [ ] J'ai compris que les packages installés dans l'environnement n'existent **pas** dans le Python du système.

<details>
<summary>Voir la correction</summary>

```shell
deactivate
```

```shell
pip list
```

C'est la seconde liste qui porte tout l'enjeu de ce chapitre : `requests` et `flask` y ont disparu. Ils avaient été installés dans l'environnement virtuel, et l'installation partagée du système, elle, est restée intacte.

</details>

---

## IV. Aller plus loin

> ⏭️ Facultatif — pas exigé pour la suite du cours.

- Tenez la main sur un cas concret : créez un environnement pour un dossier de travaux dirigés, activez-le, installez-y un package, puis désactivez-le et constatez avec `pip list` que le Python natif est resté intact.
- Les environnements virtuels ne sont pas une fin en soi : ils deviennent un prérequis dès qu'un projet s'appuie sur des bibliothèques. C'est le cas du cours consacré à la programmation orientée objet, qui reprend celui-ci et suppose que l'on sait isoler un projet de l'installation partagée avant d'y installer quoi que ce soit. Ce chapitre clôt le cours impératif ; gardez-le sous la main, vous le rouvrirez au premier `pip install` du cours suivant.

---

## Points clés

- Un environnement virtuel est un Python **indépendant** de celui du système, avec ses propres bibliothèques, choisies selon le projet.
- `py -3.11 -m venv env` crée l'environnement ; la version est optionnelle, le nom peut être un chemin complet.
- On l'active avec `env/Scripts/activate` sous Windows, `source env/bin/activate` sous Linux et macOS ; `deactivate` le quitte.
- `sys.executable`, ou `which python`, disent quel interpréteur répond — donc si vous êtes bien dans l'environnement.
- Sous Windows, un terminal qui refuse le script d'activation se débloque avec `Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force`.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Qu'est-ce qu'un environnement virtuel ?

- A. Une version de Python indépendante de celle du système, avec ses propres bibliothèques selon le projet
- B. Un dossier de sauvegarde qui permet de retrouver les fichiers d'un projet supprimé
- C. Une copie de l'installation Python du système, conservée identique à l'original
- D. Un module intégré qui affiche la liste des bibliothèques installées

**2.** Comment créer un environnement virtuel fondé sur Python 3.11 dans un dossier nommé `env` ?

- A. `py -m venv <version:optionnel>`
- B. `env/Scripts/activate 3.11`
- C. `py -3.11 -m venv env`
- D. `import sys; sys.executable`

**3.** Sur quel chemin vous attendez-vous en tapant `sys.executable` une fois l'environnement activé ?

- A. Sur le dossier de l'installation Python du système, l'environnement n'étant qu'un alias
- B. Sur le dossier `Scripts` de votre environnement virtuel
- C. Sur le dossier courant du projet, là où vous avez tapé la commande
- D. Sur le répertoire des modules intégrés, commun à tous les projets

**4.** Comment quitter un environnement virtuel ?

- A. En tapant `deactivate`
- B. En tapant `pip uninstall env`
- C. En fermant l'interpréteur avec `import sys`
- D. En relançant `env/Scripts/activate` sans argument

**5.** *Question ouverte (2-3 lignes).* Votre terminal Windows refuse d'exécuter le script d'activation. Que faites-vous, et comment contrôlez-vous ensuite que l'environnement est bien actif ?

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. A.** C'est la définition du chapitre : une version de Python indépendante de celle du système d'exploitation, avec des librairies différentes du Python natif selon les besoins du projet.
**Pourquoi :** la capture d'écran du chapitre montre l'écart : un interpréteur chargé de bibliothèques de données d'un côté, un environnement neuf réduit à `pip`, `setuptools` et `wheel` de l'autre.

**2. C.** `py -3.11 -m venv env` : le mot-clé `venv` avec le module `venv`, la version devant, le nom de l'environnement après.
**Pourquoi :** c'est le modèle commenté du chapitre, `py <version:optionnel> -m venv <nom_environnement>` ; la version peut être omise, et le nom peut être un chemin complet comme `C:\venv\mon_env`.

**3. B.** `sys.executable` renvoie le chemin de l'interpréteur courant, qui doit se situer dans le dossier `Scripts` de l'environnement virtuel.
**Pourquoi :** c'est le contrôle proposé par le chapitre, `which python` jouant le même rôle depuis le terminal.

**4. A.** `deactivate` quitte l'environnement et rend le Python natif au terminal.
**Pourquoi :** c'est la dernière commande de la section, après l'activation qui se fait avec `env/Scripts/activate` sous Windows ou `source env/bin/activate` sous Linux et macOS.

**5.** Attendu : on autorise l'exécution des scripts pour l'utilisateur courant avec `Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force`, puis on réactive et on vérifie avec `which python` ou `sys.executable` que l'interpréteur indiqué est bien dans le dossier `Scripts` de l'environnement.
**Pourquoi :** le chapitre donne cette commande pour le cas précis où le terminal refuse le script d'activation, et le contrôle par le chemin de l'interpréteur est la preuve que l'on travaille bien dans l'environnement.

</details>

---

[← Chapitre précédent](23-les-modules.md) · [Sommaire](Readme.md) · [Chapitre suivant →](A-Glossaire-et-ressources.md)
