# Notes de code

Jardin numérique en Markdown, publié avec Jekyll et GitHub Pages à l’adresse **https://bwik05.github.io/personal-site/**.

## Ajouter une note

Créer un fichier dans [`_notes`](https://github.com/bwik05/personal-site/tree/main/_notes), par exemple `ma-decouverte.md` :

```markdown
---
title: Ma découverte
description: Une phrase pour présenter cette idée.
date: 2026-10-12
status: en croissance
tags:
  - développement
  - outils
---

Une idée, une question ou un lien utile.

Voir aussi [une autre note]({{ '/notes/autre-note/' | relative_url }}).
```

Une note n’a pas besoin d’être définitive. Les pages qui partagent un sujet dans `tags` sont proposées comme connexions au bas de la page. La date est facultative ; elle sert seulement à ordonner les notes sur l’accueil et dans l’explorateur.

## Publier un article

Créer `AAAA-MM-JJ-mon-titre.md` dans [`_posts`](https://github.com/bwik05/personal-site/tree/main/_posts) :

```markdown
---
layout: post
title: Mon titre
description: Une phrase qui résume l'article.
tags:
  - développement
---

Mon premier paragraphe.
```

Les articles restent accessibles par `/articles/mon-titre/`. Les sujets relient notes et articles. Utiliser toujours le même libellé pour un même sujet.

## Modifier le site

- Apparence : `assets/css/style.css`
- Accueil : `_layouts/home.html`
- Page Explorer : `explorer.md`
- Liens entre pages : `_includes/related.html`
- Titre, adresse et collections : `_config.yml`

Les liens internes utilisent `relative_url` pour fonctionner sous `/personal-site/`. Le flux RSS des articles est disponible dans `feed.xml`.
