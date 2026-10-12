# RHYZOM lab

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

## Ajouter un morceau à la Radio

Le répertoire d’import est [`assets/audio/`](assets/audio/). Sur ce Mac, placer les nouveaux morceaux dans `Téléchargements`, puis lancer à la racine du dépôt :

```bash
python3 scripts/import_music.py ~/Downloads/*.m4a
```

La commande copie les nouveaux fichiers dans `assets/audio/`, ignore les morceaux déjà importés et ajoute leurs titres dans `_data/radio.yml` avec l’artiste **hearty solo**. Pour un `.mp3`, `.ogg` ou `.wav`, passer son chemin à la commande à la place du motif `*.m4a`.

Publier ensuite les changements du dépôt sur GitHub. Il est aussi possible d’ajouter un fichier directement dans le répertoire sur GitHub, puis d’inscrire son titre, son artiste et son chemin dans `_data/radio.yml`.

La page `/radio/` affiche les titres dans l’ordre du fichier YAML. Le lecteur démarre uniquement après un clic et s’arrête lorsqu’on quitte la page.
