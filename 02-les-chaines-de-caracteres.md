[Sommaire](Readme.md) · [Chapitre précédent →](01-les-variables.md) · [Chapitre suivant →](03-les-nombres.md)

# 02 - Les chaînes de caractères

> Écrire du texte en code, c'est choisir comment on le délimite, comment on passe à
> la ligne et comment on écrit un anti-slash sans que le langage y voie un ordre.

**Durée :** ≈ 15 min (lecture ≈ 10 min + réflexion) · **Prérequis :** [Les variables](01-les-variables.md)

> 📖 Vocabulaire et acronymes : [glossaire du cours](A-Glossaire-et-ressources.md).

---

## Objectifs

À l'issue de ce chapitre, vous serez capable de :

- **Écrire** une chaîne de caractères en simple ou en double quote, et **justifier** ce choix.
- **Échapper** un caractère qui autrement aurait une signification pour le langage.
- **Écrire** une chaîne s'étendant sur plusieurs lignes.
- **Utiliser** les caractères spéciaux `\n`, `\t` et `\b`.
- **Neutraliser** les anti-slashs d'un chemin Windows avec une chaîne brute (*raw string*).

---

## I. Délimiter une chaîne

### A. Simple quote ou double quote

Une **chaîne de caractères** — *string* — peut être initialisée avec des simples
guillemets `''` (simple quote) ou avec des doubles guillemets `""` (double quote).
Les deux écrivent la même chose.

```python
simple_quote = 'En simple quote, on doit échapper l\'apostrophe'
double_quote = "En double quote, l'apostrophe est conservée tel quel"
print(simple_quote)
```

### B. Pourquoi on conseille les doubles quotes

En Python, les deux notations sont équivalentes. Mais dès qu'une apostrophe
apparaît dans votre texte, une chaîne en simple quote **oblige à l'échapper** avec
un anti-slash `\`, ce qui alourdit la lecture.

Prenez donc l'habitude des doubles quotes : une phrase comme `L'élève a rendu son
devoir` s'écrira sans échappement. Et dans d'autres langages, cette habitude n'est
pas une question de goût : C, C++, Java et C# **distinguent** la simple quote,
réservée à un caractère isolé, de la double quote, réservée au texte.

```java
String simpleQuote = 'Ça ne compilerait pas ici : simple quote = un seul caractère';
String doubleQuote = "Ok, là j'accepte.";
```

Autant prendre la bonne habitude dès le premier langage.

---

## II. Les chaînes multilignes

Une chaîne ordinaire ne peut pas s'étendre sur plusieurs lignes du fichier source.
Python propose pour cela les **triples quotes** — trois simples `'''` ou trois
doubles `"""` — qui permettent d'initialiser de longues chaînes **en conservant la
mise en forme**, sauts de ligne et indentations compris.

```python
simple_quote = 'Avec une simple quote, je ne peux pas passer à la ligne \n sauf à échapper n...'

double_quote = """Je suis une chaine
mais je peux m'étendre sur plusieurs lignes"""


simple_quote_triple = '''Même chose, et le truc cool
c'est que je n'ai plus besoin
d'échapper les apostrophes!'''

print(simple_quote)
print(double_quote)
print(simple_quote_triple)
```

Notez le troisième exemple : en plus de passer à la ligne, les triples quotes
laissent les apostrophes tranquilles. C'est ce qui en fait l'outil naturel pour les
blocages de documentation de fonction, que vous croiserez au chapitre 22.

---

## III. Caractères spéciaux et échappement

### A. Faire venir le texte à la ligne

En incorporant des **caractères spéciaux**, vous pouvez mettre en forme le contenu
d'une chaîne :

```python
print("passement\nde ligne!")
```

Liste non exhaustive des caractères spéciaux fréquemment utilisés en développement :

- `\n` passage à la ligne
- `\t` tabulation
- `\b` retour arrière

Le point commun de ces séquences : un caractère ordinaire, le `\`, signale à
l'interpréteur « le caractère qui suit ne se lit pas littéralement ». C'est
l'**échappement**.

### B. Les chaînes brutes (raw strings)

En Python, une chaîne **brute** (*raw string*) est préfixée par un `r` ou un `R`.
Les anti-slashs y sont traités comme des caractères **littéraux** et non comme des
caractères d'échappement. C'est utile avec les expressions régulières, les chemins
de fichiers, et plus généralement partout où des barres obliques inverses font partie
du texte.

```python
raw_string = r"Je suis une raw string,\nsans passage à la ligne!"
print(raw_string)
```

> ⚠️ **Anti-slashs et chemins Windows**
>
> Les chemins Windows en comportent une multitude. Deux écritures vous donneront
> le même résultat affiché : doubler chaque anti-slash, ou préfixer la chaîne par
> un `r`.

```python
path = "C:\\User\\Bob"
pathraw = r"C:\User\Bob"
print(path)
print(pathraw)
```

La première ligne est l'écriture classique : chaque `\` doit être échappé par un
`\`. La seconde, plus lisible, est la chaîne brute : le texte est écrit tel quel.

---

## Points clés

- `''` et `""` décrivent la même chose : préférez les **doubles quotes**, qui
  évitent d'échapper les apostrophes.
- Les **triples quotes** `"""…"""` ou `'''…'''` écrivent une chaîne multilignes en
  conservant la mise en forme.
- `\n`, `\t`, `\b` sont des caractères spéciaux : le `\` **échappe** le caractère
  suivant.
- Un `r"…"` rend les anti-slashs **littéraux** : c'est la chaîne brute, précieuse
  pour les chemins Windows et les expressions régulières.
- Pour écrire un anti-slash dans une chaîne normale, on écrit `\\`.

---

## 🧠 Vérifiez vos acquis

*Formatif, jamais noté. Répondez sans relire le chapitre. Les réponses se déplient juste après le séparateur : ce qui compte est de repérer où vous vacillez, pas de faire 5 sur 5.*

**1.** Pourquoi le chapitre conseille-t-il les doubles quotes en Python ?

- A. Parce qu'elles sont les seules à accepter les accents dans une chaîne de caractères
- B. Parce qu'elles évitent d'échapper une apostrophe, et correspondent à l'usage des autres langages
- C. Parce qu'elles seules permettent d'écrire une chaîne sur plusieurs lignes
- D. Parce qu'elles rendent l'interpréteur plus rapide à la lecture du fichier source

**2.** Quelle notation permet d'écrire une chaîne étalée sur plusieurs lignes en conservant les sauts de ligne ?

- A. Un anti-slash final à la fin de chaque ligne, qui signale la continuation de la chaîne
- B. Des triples quotes, `"""` ou `'''`, qui englobent tout le texte avec sa mise en forme
- C. Une succession de petites chaînes séparées par des virgules, collées par l'interpréteur
- D. Le caractère `\n` placé seul entre deux guillemets, qui allonge la ligne affichée

**3.** Que fait le préfixe `r` dans `r"C:\User\Bob"` ?

- A. Il convertit la chaîne en chemin absolu pointant vers le disque système
- B. Il traite les anti-slashs comme des caractères littéraux plutôt que comme des échappements
- C. Il affiche la chaîne en supprimant tous les anti-slashs qu'elle contient
- D. Il recherche le chemin sur le disque avant de l'affecter à la variable

**4.** Comment écrire, dans une chaîne classique, un anti-slash suivi du mot `n` sans déclencher le passage à la ligne ?

- A. `"\\n"`, puisque doubler l'anti-slash l'empêche d'échapper le caractère suivant
- B. `"\n"`, puisque deux caractères suffisent toujours à neutraliser un échappement
- C. `"/n"`, puisque la barre oblique remplace l'anti-slash dans les chaînes classiques
- D. "`n`" entre guillemets inversés, qui court-circuite l'échappement de la chaîne

**5.** *Question ouverte (2-3 lignes).* Vous devez affecter le chemin `D:\notes\2026\cours.txt` à une variable. Écrivez les deux façons vues dans le chapitre, et dites laquelle vous retenez.

---

<details>
<summary>Vérifier ses réponses</summary>

### Réponses

**1. B.** Les deux notations sont équivalentes en Python, mais les doubles quotes évitent d'échapper les apostrophes et correspondent à l'usage des autres langages.
**Pourquoi :** le chapitre ajoute que C, C++, Java et C# distinguent la simple quote (un caractère) de la double quote (du texte) : prendre la bonne habitude dès le premier langage évite une erreur de réflexe ailleurs.

**2. B.** Les triples quotes englobent le texte avec ses sauts de ligne et son indentation.
**Pourquoi :** c'est leur usage dans le chapitre, et elles ont en bonus de laisser les apostrophes sans échappement — ce qui servira pour les blocs de documentation.

**3. B.** Le préfixe `r` déclare une chaîne brute : les anti-slashs cessent d'être des échappements et deviennent du texte.
**Pourquoi :** c'est ce qui rend cette notation précieuse pour les chemins Windows et les expressions régulières, où les `\` sont nombreux et doivent rester visibles.

**4. A.** `"\\n"` : le premier anti-slash échappe le second, qui devient un anti-slash imprimable, et le `n` qui suit reste un `n` ordinaire.
**Pourquoi :** c'est exactement la première écriture de l'exemple `path = "C:\\User\\Bob"` ; l'autre solution eût été la chaîne brute, mais elle n'est pas une chaîne classique.

**5.** Attendu : `chemin = "D:\\notes\\2026\\cours.txt"` et `chemin = r"D:\notes\2026\cours.txt"` ; la seconde est habituellement retenue comme plus lisible, la première restant obligatoire quand la chaîne est construite dynamiquement.
**Pourquoi :** ce sont les deux écritures données par le chapitre pour un chemin Windows ; les anti-slashs y sont nombreux, donc l'échappement systématique y est vite illisible.

</details>

---

[Sommaire](Readme.md) · [Chapitre précédent →](01-les-variables.md) · [Chapitre suivant →](03-les-nombres.md)
