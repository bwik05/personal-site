#!/usr/bin/env python3
"""Copy original audio into the site's Radio playlist.

Usage: python3 scripts/import_music.py ~/Downloads/my-song.m4a
"""

import argparse
import hashlib
import json
import re
import shutil
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIO_DIR = ROOT / "assets" / "audio"
PLAYLIST = ROOT / "_data" / "radio.yml"
SUPPORTED = {".m4a", ".mp3", ".ogg", ".wav"}


def digest(path):
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.digest()


def slugify(value):
    normalized = unicodedata.normalize("NFKD", value)
    ascii_name = normalized.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "-", ascii_name).strip("-") or "morceau"


def main():
    parser = argparse.ArgumentParser(description="Ajouter des morceaux à la Radio de RHYZOM lab")
    parser.add_argument("files", nargs="+", type=Path, help="Fichiers audio à importer")
    parser.add_argument("--artist", default="hearty solo", help="Nom d’artiste affiché")
    args = parser.parse_args()

    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    PLAYLIST.parent.mkdir(parents=True, exist_ok=True)
    if not PLAYLIST.exists():
        PLAYLIST.write_text("tracks:\n", encoding="utf-8")
    playlist_text = PLAYLIST.read_text(encoding="utf-8")
    if playlist_text.strip() == "tracks: []":
        playlist_text = "tracks:\n"
        PLAYLIST.write_text(playlist_text, encoding="utf-8")
    if not playlist_text.startswith("tracks:"):
        parser.error("_data/radio.yml doit commencer par tracks:")

    sources = [path.expanduser().resolve() for path in args.files]
    for source in sources:
        if not source.is_file():
            parser.error(f"Fichier introuvable : {source}")
        if source.suffix.lower() not in SUPPORTED:
            parser.error(f"Format non pris en charge : {source.name}")

    imported_hashes = {
        digest(path)
        for path in AUDIO_DIR.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED
    }
    additions = []
    for source in sources:
        extension = source.suffix.lower()
        source_hash = digest(source)
        if source_hash in imported_hashes:
            print(f"Déjà importé : {source.name}")
            continue
        base = slugify(source.stem)
        suffix = 1
        while True:
            filename = f"{base}{f'-{suffix}' if suffix > 1 else ''}{extension}"
            target = AUDIO_DIR / filename
            if not target.exists():
                break
            if digest(target) == source_hash:
                print(f"Déjà importé : {source.name}")
                target = None
                break
            suffix += 1
        if target is None:
            continue

        shutil.copy2(source, target)
        imported_hashes.add(source_hash)
        title = source.stem.replace("_", " ").strip()
        additions.append(
            "  - title: " + json.dumps(title, ensure_ascii=False) + "\n"
            "    artist: " + json.dumps(args.artist, ensure_ascii=False) + "\n"
            "    file: /assets/audio/" + filename + "\n"
        )
        print(f"Ajouté : {title} → {target.relative_to(ROOT)}")

    if additions:
        with PLAYLIST.open("a", encoding="utf-8") as stream:
            if not playlist_text.endswith("\n"):
                stream.write("\n")
            stream.writelines(additions)
        print(f"{len(additions)} morceau(x) ajouté(s) à la sélection.")


if __name__ == "__main__":
    main()
