#!/usr/bin/env python3
"""
Scans content/<level>/<subject>/<topic>/ for a meta.json + notes.pdf pair and
writes assets/data/index.json for the site to read.

This is the ONLY "build step". It runs automatically via the GitHub Action
on every push, so uploading a new folder through the GitHub website is all
that's needed to publish a new resource -- no app, no login, no coding.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
OUT_DIR = os.path.join(ROOT, "assets", "data")
OUT_FILE = os.path.join(OUT_DIR, "index.json")

LEVEL_LABELS = {
    "class-1": "Class 1", "class-2": "Class 2", "class-3": "Class 3",
    "class-4": "Class 4", "class-5": "Class 5", "class-6": "Class 6",
    "class-7": "Class 7", "class-8": "Class 8", "class-9": "Class 9",
    "class-10": "Class 10", "class-11": "Class 11", "class-12": "Class 12",
    "neet": "NEET", "jee": "JEE", "bsc": "B.Sc", "msc": "M.Sc",
}

LEVEL_BANDS = [
    ("primary", "Class 1-5 (Primary)", ["class-1", "class-2", "class-3", "class-4", "class-5"]),
    ("middle", "Class 6-8 (Middle)", ["class-6", "class-7", "class-8"]),
    ("secondary", "Class 9-10 (Secondary)", ["class-9", "class-10"]),
    ("senior", "Class 11-12 (Senior Secondary)", ["class-11", "class-12"]),
    ("neet", "NEET", ["neet"]),
    ("jee", "JEE (Main & Advanced)", ["jee"]),
    ("bsc", "B.Sc", ["bsc"]),
    ("msc", "M.Sc", ["msc"]),
]


def human_size(num_bytes):
    for unit in ("B", "KB", "MB"):
        if num_bytes < 1024:
            return f"{num_bytes:.0f} {unit}" if unit == "B" else f"{num_bytes:.1f} {unit}"
        num_bytes /= 1024
    return f"{num_bytes:.1f} GB"


def main():
    resources = []
    errors = []
    if os.path.isdir(CONTENT):
        for level in sorted(os.listdir(CONTENT)):
            level_dir = os.path.join(CONTENT, level)
            if not os.path.isdir(level_dir) or level.startswith("."):
                continue
            for subject in sorted(os.listdir(level_dir)):
                subject_dir = os.path.join(level_dir, subject)
                if not os.path.isdir(subject_dir):
                    continue
                for topic in sorted(os.listdir(subject_dir)):
                    topic_dir = os.path.join(subject_dir, topic)
                    if not os.path.isdir(topic_dir):
                        continue
                    meta_path = os.path.join(topic_dir, "meta.json")
                    pdf_path = os.path.join(topic_dir, "notes.pdf")
                    rel_pdf = os.path.relpath(pdf_path, ROOT).replace(os.sep, "/")
                    if not os.path.isfile(pdf_path):
                        errors.append(f"{level}/{subject}/{topic}: missing notes.pdf")
                        continue
                    if not os.path.isfile(meta_path):
                        errors.append(f"{level}/{subject}/{topic}: missing meta.json")
                        continue
                    try:
                        with open(meta_path, encoding="utf-8") as f:
                            meta = json.load(f)
                    except Exception as e:
                        errors.append(f"{level}/{subject}/{topic}: bad meta.json ({e})")
                        continue
                    size_bytes = os.path.getsize(pdf_path)
                    resources.append({
                        "title": meta.get("title", topic.replace("-", " ").title()),
                        "level": meta.get("level", level),
                        "levelLabel": meta.get("levelLabel", LEVEL_LABELS.get(level, level)),
                        "subject": meta.get("subject", subject.replace("-", " ").title()),
                        "description": meta.get("description", ""),
                        "video_url": meta.get("video_url", ""),
                        "date": meta.get("date", ""),
                        "file": rel_pdf,
                        "size": human_size(size_bytes),
                        "slug": f"{level}/{subject}/{topic}",
                    })

    resources.sort(key=lambda r: r.get("date", ""), reverse=True)

    counts = {}
    for r in resources:
        counts[r["level"]] = counts.get(r["level"], 0) + 1

    bands = []
    for band_id, band_label, levels in LEVEL_BANDS:
        bands.append({
            "id": band_id,
            "label": band_label,
            "levels": levels,
            "count": sum(counts.get(lv, 0) for lv in levels),
        })

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "resources": resources,
            "bands": bands,
            "levelLabels": LEVEL_LABELS,
        }, f, indent=2)

    print(f"Indexed {len(resources)} resource(s) across {len(counts)} level(s).")
    if errors:
        print("Warnings (skipped):")
        for e in errors:
            print(f"  - {e}")


if __name__ == "__main__":
    main()
