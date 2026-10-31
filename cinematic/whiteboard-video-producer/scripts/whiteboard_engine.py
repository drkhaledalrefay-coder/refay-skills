#!/usr/bin/env python3
"""Assemble pre-rendered whiteboard boards and a narration track with FFmpeg.

Timeline JSON format:
{
  "width": 1920, "height": 1080, "fps": 30,
  "scenes": [
    {"start": 0.0, "end": 8.0, "image": "boards/scene_01.png"},
    {"start": 8.0, "end": 17.5, "image": "boards/scene_02.png"}
  ]
}

The scene images should already contain the desired board artwork. This helper
does not generate drawings, animate a hand, or infer scene boundaries.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def load_timeline(path: Path) -> tuple[int, int, int, list[dict]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    width = int(data.get("width", 1920))
    height = int(data.get("height", 1080))
    fps = int(data.get("fps", 30))
    scenes = data.get("scenes")
    if width <= 0 or height <= 0 or fps <= 0 or not isinstance(scenes, list) or not scenes:
        raise ValueError("Timeline needs positive width/height/fps and at least one scene.")
    previous_end = 0.0
    base = path.parent
    normalized = []
    for number, scene in enumerate(scenes, start=1):
        start, end = float(scene["start"]), float(scene["end"])
        image = (base / scene["image"]).resolve()
        if start < 0 or end <= start:
            raise ValueError(f"Scene {number} has an invalid time range.")
        if number == 1 and start != 0:
            raise ValueError("The first scene must start at 0 seconds.")
        if abs(start - previous_end) > 0.001:
            raise ValueError(f"Scene {number} must start where the previous scene ends.")
        if not image.is_file():
            raise FileNotFoundError(f"Scene image not found: {image}")
        normalized.append({"duration": end - start, "image": image})
        previous_end = end
    return width, height, fps, normalized


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timeline", required=True, type=Path, help="Scene timing JSON.")
    parser.add_argument("--audio", required=True, type=Path, help="Narration audio file.")
    parser.add_argument("--output", required=True, type=Path, help="Output MP4 path.")
    parser.add_argument("--ffmpeg", default="ffmpeg", help="FFmpeg executable or full path.")
    args = parser.parse_args()

    ffmpeg = shutil.which(args.ffmpeg) if not Path(args.ffmpeg).is_file() else args.ffmpeg
    if not ffmpeg:
        parser.error("FFmpeg was not found. Install it or pass --ffmpeg with its full path.")
    audio = args.audio.resolve()
    if not audio.is_file():
        parser.error(f"Audio file not found: {audio}")

    try:
        width, height, fps, scenes = load_timeline(args.timeline.resolve())
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    cmd = [str(ffmpeg), "-y"]
    for scene in scenes:
        cmd += ["-loop", "1", "-framerate", str(fps), "-t",
                f"{scene['duration']:.3f}", "-i", str(scene["image"])]
    cmd += ["-i", str(audio)]

    filters = []
    labels = []
    for index in range(len(scenes)):
        label = f"v{index}"
        filters.append(
            f"[{index}:v]scale={width}:{height}:force_original_aspect_ratio=decrease,"
            f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:color=white,"
            f"fps={fps},setsar=1,format=yuv420p[{label}]"
        )
        labels.append(f"[{label}]")
    filters.append("".join(labels) + f"concat=n={len(scenes)}:v=1:a=0[vout]")

    cmd += ["-filter_complex", ";".join(filters), "-map", "[vout]",
            "-map", f"{len(scenes)}:a:0", "-c:v", "libx264",
            "-profile:v", "main", "-pix_fmt", "yuv420p", "-r", str(fps),
            "-c:a", "aac", "-b:a", "192k", "-shortest",
            "-movflags", "+faststart", str(output)]
    print("Running:", subprocess.list2cmdline(cmd))
    result = subprocess.run(cmd, check=False)
    if result.returncode:
        print(f"FFmpeg exited with status {result.returncode}.", file=sys.stderr)
        return result.returncode
    print(f"Created: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
