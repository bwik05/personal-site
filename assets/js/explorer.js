(() => {
  const buttons = [...document.querySelectorAll('.topic-button')];
  const cards = [...document.querySelectorAll('.filterable')];
  const empty = document.getElementById('filter-empty');
  const sections = [...document.querySelectorAll('#notes, #articles')];
  if (!buttons.length) return;

  function choose(topic, updateUrl = true) {
    const normalized = topic.toLocaleLowerCase('fr');
    let visible = 0;
    buttons.forEach(button => {
      const active = button.dataset.topic === normalized;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    cards.forEach(card => {
      const match = !normalized || card.dataset.tags.includes(`|${normalized}|`);
      card.hidden = !match;
      if (match) visible += 1;
    });
    sections.forEach(section => {
      const hasVisible = [...section.querySelectorAll('.filterable')].some(card => !card.hidden);
      section.classList.toggle('section-filtered-empty', Boolean(normalized) && !hasVisible);
    });
    empty.hidden = visible !== 0;
    if (updateUrl) {
      const url = new URL(window.location.href);
      if (topic) url.searchParams.set('sujet', topic);
      else url.searchParams.delete('sujet');
      history.replaceState(null, '', url);
    }
  }

  buttons.forEach(button => button.addEventListener('click', () => choose(button.dataset.topic)));
  const requested = new URLSearchParams(window.location.search).get('sujet');
  if (requested) {
    const matching = buttons.find(button => button.dataset.topic === requested.toLocaleLowerCase('fr'));
    if (matching) choose(matching.dataset.topic, false);
  }
})();
