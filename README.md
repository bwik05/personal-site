# Notes de code

Blog minimaliste en Markdown, publié par GitHub Pages à l’adresse **https://bwik05.github.io/personal-site/**. Jekyll transforme les fichiers Markdown en pages ; il n’y a ni base de données ni interface d’administration à maintenir.

## Publier un article depuis GitHub

1. Ouvrir le dossier [`_posts`](https://github.com/bwik05/personal-site/tree/main/_posts) et cliquer sur **Add file → Create new file**.
2. Nommer le fichier `AAAA-MM-JJ-mon-titre.md`, avec la date du jour et un titre court sans accents ni espaces.
3. Coller ce modèle et écrire sous la deuxième ligne `---` :

   ```markdown
   ---
   layout: post
   title: Mon titre
   description: Une phrase qui résume l'article.
   ---

   Mon premier paragraphe.

   ## Un intertitre

   La suite de mon article.
   ```

4. Cliquer sur **Commit changes**. Le site se met à jour automatiquement, généralement en quelques minutes.

Le fichier `2026-10-11-bienvenue.md` est un exemple publiable : modifie-le ou supprime-le quand ton premier vrai article est prêt.

## Ajouter une image

Déposer l’image dans `assets/images/`, puis l’insérer dans l’article :

```markdown
![Description de l'image]({{ '/assets/images/mon-image.webp' | relative_url }})
```

La description entre crochets aide les lecteurs qui utilisent un lecteur d’écran. Un fichier WebP ou JPEG optimisé garde la page rapide.

## Ajouter une page

Créer `ma-page.md` à la racine :

```markdown
---
layout: page
title: Ma page
permalink: /ma-page/
---

Contenu de la page.
```

La page À propos est dans `a-propos.md`. Pour l’ajouter au menu, modifier `_layouts/default.html`.

## Modifier l’apparence

- Titre, description et adresse : `_config.yml`
- Couleurs, typographie et espacements : `assets/css/style.css`
- Structure de la page d’accueil : `_layouts/home.html`

Les liens internes utilisent `relative_url`, ce qui garde les images et les pages correctes sous `/personal-site/`. Le flux d’articles est disponible dans `feed.xml`.
