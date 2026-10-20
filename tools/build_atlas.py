#!/usr/bin/env python3
"""Rebuild the native v2 atlas from the repository's editable RGBA frames."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
CELL = (192, 208)
ROWS = [
    ("idle", 6), ("running-right", 8), ("running-left", 8),
    ("waving", 4), ("jumping", 5), ("failed", 8),
    ("waiting", 6), ("running", 6), ("review", 6),
]
LOOK = ["000", "022.5", "045", "067.5", "090", "112.5", "135", "157.5",
        "180", "202.5", "225", "247.5", "270", "292.5", "315", "337.5"]


def load_frame(path: Path) -> Image.Image:
    with Image.open(path) as opened:
        frame = opened.convert("RGBA")
    if frame.size != CELL:
        raise ValueError(f"{path}: expected {CELL}, got {frame.size}")
    if frame.getchannel("A").getbbox() is None:
        raise ValueError(f"{path}: required frame is empty")
    return frame


def build(frames_root: Path, output: Path) -> None:
    atlas = Image.new("RGBA", (1536, 2288), (0, 0, 0, 0))
    for row, (state, count) in enumerate(ROWS):
        for col in range(count):
            frame = load_frame(frames_root / state / f"{col:02d}.png")
            atlas.paste(frame, (col * CELL[0], row * CELL[1]))
    for index, label in enumerate(LOOK):
        frame = load_frame(frames_root / "look" / f"{label}.png")
        atlas.paste(frame, ((index % 8) * CELL[0], (9 + index // 8) * CELL[1]))
    output.mkdir(parents=True, exist_ok=True)
    atlas.save(output / "spritesheet.png")
    atlas.save(output / "spritesheet.webp", format="WEBP", lossless=True,
               quality=100, method=6, exact=True)
    metadata = json.loads((ROOT / "pets/deepseek-basin-whale/pet.json").read_text(encoding="utf-8-sig"))
    (output / "pet.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(output), "size": list(atlas.size),
                      "required_frames": 73, "sprite_version": 2}, ensure_ascii=False))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--frames", type=Path, default=ROOT / "artwork/frames")
    parser.add_argument("--output", type=Path, default=ROOT / "build")
    args = parser.parse_args()
    build(args.frames.resolve(), args.output.resolve())


if __name__ == "__main__":
    main()
