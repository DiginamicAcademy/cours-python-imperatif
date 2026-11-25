# Repli hors-ligne des citations

Le TP interroge un service en ligne par l'entremise du module `quote`, installé avec `pip`. Derrière un proxy, sur un poste fermé, ou quand le site ne répond plus : l'exercice devient impossible, alors que la donnée, elle, ne change pas. Ce dossier contient cette donnée, capturée une fois pour toutes.

## Basculer du module en ligne sur ce repli

Une seule ligne change dans vos programmes :

| Votre code | Source des citations |
| --- | --- |
| `from quote import quote` | en ligne — `pip install quote certifi`, accès réseau requis |
| `from quote_offline import quote` | ici — rien à installer, aucun réseau |

Copiez `quote_offline.py` à côté de votre programme (ou travaillez depuis ce dossier). La fonction rendue a la même forme que celle du paquet : `quote(auteur, limit=30)` renvoie une liste de dictionnaires à trois clés — `quote` (le texte), `book` (le livre d'origine, parfois vide), `author`. Tout le reste de votre code s'en moque : c'est tout l'intérêt du montage.

Deux différences à connaître, quand même :

- le corpus est figé : vous obtiendrez toujours les mêmes citations, ce qui rend l'exercice répétable ;
- si le fichier d'un auteur manque, le repli s'arrête immédiatement en le disant, là où le module en ligne renvoie simplement `None`.

## Contenu attendu

**Un fichier `.json` par auteur — seize fichiers**, un par auteur de l'approfondissement du TP :

| | |
| --- | --- |
| `Edgar_Allan_Poe.json` | `Victor_Hugo.json` |
| `Gustave_Flaubert.json` | `Ernest_Hemingway.json` |
| `Agatha_Christie.json` | `Friedrich_Nietzsche.json` |
| `Arthur_Schopenhauer.json` | `Simone_De_Beauvoir.json` |
| `Guy_De_Maupassant.json` | `Voltaire.json` |
| `Emile_Zola.json` | `Georges_Orwell.json` |
| `Frank_Herbert.json` | `Isaac_Asimov.json` |
| `Tolkien.json` | `William_Shakespeare.json` |

Nom normalisé comme à la capture : espaces remplacés par des tirets bas, points ôtés. Les autres séparateurs sont tolérés à la lecture (`edgar-allan-poe.json` fonctionne aussi) : la recherche se fait sur le nom normalisé.

Chaque fichier est une liste de dictionnaires à trois clés :

```json
[
  {
    "quote": "Texte de la citation.",
    "book": "Titre d'origine, parfois vide.",
    "author": "Edgar Allan Poe"
  }
]
```

Trente citations par auteur, ou moins : la source en ligne n'en donne pas toujours trente, et l'exercice s'en accommode.

## Les trois scripts du dossier

| Fichier | À quoi il sert |
| --- | --- |
| `quote_offline.py` | le module de repli, à importer à la place de `quote` |
| `lire_citations.py` | l'inventaire du corpus, à lancer avant de travailler : combien de citations par auteur |
| `capture_citations.py` | la reconstruction du corpus (une fois, avec réseau et les deux paquets installés) |
