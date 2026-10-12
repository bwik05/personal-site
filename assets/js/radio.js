(() => {
  const audio = document.getElementById("radio-audio");
  const buttons = [...document.querySelectorAll(".radio-track")];
  const title = document.getElementById("now-playing-title");
  const artist = document.getElementById("now-playing-artist");
  if (!audio || !buttons.length) return;

  function select(index, play = false) {
    const button = buttons[index];
    if (!button) return;
    buttons.forEach((item, itemIndex) => {
      const current = itemIndex === index;
      item.classList.toggle("is-current", current);
      item.setAttribute("aria-current", String(current));
    });
    if (audio.getAttribute("src") !== button.dataset.src)
      audio.src = button.dataset.src;
    title.textContent = button.dataset.title;
    artist.textContent = button.dataset.artist;
    if (play) audio.play().catch(() => {});
  }

  buttons.forEach((button, index) =>
    button.addEventListener("click", () => select(index, true)),
  );
  audio.addEventListener("ended", () => {
    const current = buttons.findIndex((button) =>
      button.classList.contains("is-current"),
    );
    select((current + 1) % buttons.length, true);
  });
})();
