---
layout: page
title: Explorer le jardin
description: Parcourir les notes, les articles et les sujets de ce jardin numérique.
permalink: /explorer/
---

{% assign all_entries = site.notes | concat: site.posts %}
{% capture raw_tags %}{% for entry in all_entries %}{% for tag in entry.tags %}{{ tag }}|{% endfor %}{% endfor %}{% endcapture %}
{% assign topics = raw_tags | split: '|' | uniq | sort %}

<div class="explorer-intro"><p>Pas besoin de commencer par le plus récent. Choisissez un sujet, ouvrez une note ou suivez simplement votre curiosité.</p></div>

<section id="sujets" class="explorer-section" aria-labelledby="topics-title">
  <div class="section-heading"><div><p class="eyebrow">Les fils conducteurs</p><h2 id="topics-title">Explorer par sujet</h2></div><span>{{ topics.size }} {% if topics.size == 1 %}sujet{% else %}sujets{% endif %}</span></div>
  {% if topics.size > 0 %}<div class="topic-filters" role="group" aria-label="Filtrer par sujet"><button class="topic-button is-active" type="button" data-topic="" aria-pressed="true">Tout voir</button>{% for topic in topics %}<button class="topic-button" type="button" data-topic="{{ topic | downcase | escape }}" aria-pressed="false">{{ topic | escape }}</button>{% endfor %}</div>{% else %}<p class="empty-state">Les sujets apparaîtront ici avec les prochaines notes.</p>{% endif %}
</section>

<section id="notes" class="explorer-section" aria-labelledby="notes-title"><div class="section-heading"><div><p class="eyebrow">Idées en mouvement</p><h2 id="notes-title">Notes</h2></div><span>{{ site.notes.size }} {% if site.notes.size == 1 %}note{% else %}notes{% endif %}</span></div><div class="entry-grid explorer-grid">{% assign sorted_notes = site.notes | sort: 'date' | reverse %}{% for note in sorted_notes %}<a class="entry-card filterable" data-tags="{% for tag in note.tags %}|{{ tag | downcase | escape }}{% endfor %}|" href="{{ note.url | relative_url }}"><span class="entry-type">✳ Note {% if note.status %}· {{ note.status | escape }}{% endif %}</span><h3>{{ note.title | escape }}</h3><p>{{ note.description | default: note.excerpt | strip_html | truncate: 130 | escape }}</p><span class="entry-bottom">Ouvrir la note <span aria-hidden="true">↗</span></span></a>{% endfor %}</div>{% if site.notes.size == 0 %}<p class="empty-state">Les premières notes arrivent bientôt. En attendant, explorez les articles plus bas.</p>{% endif %}</section>

<section id="articles" class="explorer-section" aria-labelledby="articles-title"><div class="section-heading"><div><p class="eyebrow">Chemins plus longs</p><h2 id="articles-title">Articles</h2></div><span>{{ site.posts.size }} {% if site.posts.size == 1 %}article{% else %}articles{% endif %}</span></div><div class="entry-grid explorer-grid">{% for post in site.posts %}<a class="entry-card filterable" data-tags="{% for tag in post.tags %}|{{ tag | downcase | escape }}{% endfor %}|" href="{{ post.url | relative_url }}"><span class="entry-type">↗ Article · <time datetime="{{ post.date | date: '%Y-%m-%d' }}">{{ post.date | date: '%d.%m.%Y' }}</time></span><h3>{{ post.title | escape }}</h3><p>{{ post.description | default: post.excerpt | strip_html | truncate: 130 | escape }}</p><span class="entry-bottom">Lire l’article <span aria-hidden="true">↗</span></span></a>{% endfor %}</div>{% if site.posts.size == 0 %}<p class="empty-state">Les articles pousseront ici.</p>{% endif %}</section>
<p id="filter-empty" class="filter-empty" hidden>Aucune page pour ce sujet pour le moment. Choisissez un autre sujet.</p>
<script src="{{ '/assets/js/explorer.js' | relative_url }}" defer></script>
