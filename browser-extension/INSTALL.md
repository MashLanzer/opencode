# INSTALL.md

# OpenCode Web Clipper - Installation Guide

## How to Install (Chrome/Edge)

### Option 1: Developer Mode (Recommended)

1. Open Chrome/Edge and navigate to `chrome://extensions`

2. Enable **Developer mode** (toggle in top right)

3. Click **Load unpacked**

4. Select the `browser-extension` folder

5. The extension will appear as "OpenCode Web Clipper"

### Option 2: Packaged

1. Create a zip of the `browser-extension` folder

2. Go to `chrome://extensions`

3. Click **Pack extension**

4. Select the folder

5. Upload the `.crx` file

## How to Use

1. Click the extension icon in Chrome/Edge

2. Add notes and tags

3. Click "Save to Obsidian"

4. The note will appear in `Notas/lectura/`

## Configuration

Edit `popup.html` to change:
- OBSIDIAN_URL (default: http://127.0.0.1:27123)
- API_KEY (your API key)

## Notes Created

Location: `Notas/lectura/YYYY-MM-dd-title.md`

Format:
```markdown
---
tags: [web-clip, tags]
creado: YYYY-MM-DD
source: web
---

# Title

## Notes
Your notes

## URL
{{url}}
```

## Requirements

- Obsidian running with Local REST API
- Network access to Obsidian (same network or localhost)