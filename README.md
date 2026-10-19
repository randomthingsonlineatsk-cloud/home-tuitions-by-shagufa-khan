# Home Tuitions by Shagufa Khan

Free notes, solutions and video lessons — Class 1 to NEET, JEE, B.Sc & M.Sc.

Live site: `https://randomthingsonlineatsk-cloud.github.io/home-tutions-by-shagufa-khan/`
(takes 1-2 minutes to go live after the very first push, and after each update)

---

## How to upload a new PDF (no coding needed)

You never need to touch code to add a new note. Everything happens through
GitHub's normal website.

1. Go to the repo on github.com and open the `content` folder.
2. Open (or create) the folder for the right **level**, e.g. `content/class-10/`.
   Level folder names must be exactly one of:
   `class-1` `class-2` `class-3` `class-4` `class-5` `class-6` `class-7`
   `class-8` `class-9` `class-10` `class-11` `class-12` `neet` `jee` `bsc` `msc`
3. Inside it, open (or create) a folder for the **subject**, e.g. `biology`.
4. Inside that, create a **new folder** named after the topic, e.g. `photosynthesis`
   (use lowercase and hyphens instead of spaces).
5. Click **"Add file" → "Upload files"** and upload two files into that topic folder:
   - `notes.pdf` — the actual PDF (must be named exactly `notes.pdf`)
   - `meta.json` — a small text file with the topic's details (copy the template below)
6. Commit the changes (the green "Commit changes" button).
7. Wait 1-2 minutes — the site rebuilds and updates itself automatically. That's it.

### `meta.json` template

Copy this, fill in your details, and upload it alongside `notes.pdf`:

```json
{
  "title": "Photosynthesis",
  "level": "class-10",
  "levelLabel": "Class 10",
  "subject": "Biology",
  "description": "Light and dark reactions, factors affecting the rate, and a labelled diagram.",
  "video_url": "https://www.youtube.com/@hometuitionsbyshagufakhan/your-video-link",
  "date": "2026-10-25"
}
```

- `video_url` is optional — leave it as `""` if there's no matching video yet.
- `date` controls sort order on the "Latest uploads" section — use today's date.
- For `bsc` / `msc`, put the actual specialization in `subject`, e.g. `"Organic Chemistry"` or `"Microbiology"`.

### To edit or remove a note later

Just open that topic's folder in GitHub, edit `meta.json` or replace `notes.pdf`
directly on the website (pencil/upload icon), or delete the whole folder to
remove it from the site. The site re-rebuilds automatically either way.

---

## Editing the YouTube / Instagram links, email, or site text

Open `assets/js/config.js` in the GitHub web editor and change the values —
no coding knowledge needed, just edit the text between the quotes. Commit, and
it updates in 1-2 minutes.

---

## How this is hosted (for your own reference)

- **Code + PDFs**: this GitHub repository (free, unlimited for a site this size)
- **Hosting**: GitHub Pages (free, no credit system, no monthly limit at this scale)
- **"Rebuild"**: a GitHub Action (`.github/workflows/deploy.yml`) runs automatically
  on every push — it scans the `content/` folder and regenerates the site's data
  file, then publishes it. You never run anything yourself.

There is no database, no third-party app, and no account other than GitHub itself
— so there's nothing to upgrade or hit a limit on for normal use.

## One-time setup still needed

GitHub Pages needs to be turned on once for this repo:
**Settings → Pages → Build and deployment → Source → "GitHub Actions"**.
After that, every push publishes automatically.
