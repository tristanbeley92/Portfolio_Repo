# Tristan Beley - portfolio

A static, multi-page portfolio. No runtime packages, client framework, web-font requests, or build service required.

## Preview

Run `python -m http.server 4173` and open http://localhost:4173. Deploy the repository root to any static host. Generated HTML is checked in and supports subdirectory hosting.

## Edit

- `tools/build.py`: shared templates, biography, experience, toolkit, and six project write-ups. Run `python tools/build.py` after editing.
- `style.css`: responsive layouts, colors, motion, and component styles.
- `script.js`: mobile navigation, project filtering, preview switching, copy email, and Ctrl/Cmd+K search.
- `assets/`: compressed WebP derivatives and favicon. Originals remain in `Images/`.

About, Experience, Skills, and Projects are separate pages. Contact stays a section on every page. Each project has a standalone write-up with a problem, implementation, technical detail, and reflection.

## Validate

```sh
python tools/build.py
python tools/check.py
node --check script.js
```

Browser checks: desktop and mobile navigation, project previews, category filters, command search, keyboard behavior, image loading, and horizontal overflow. CSS honors reduced motion. Cross-document view transitions enhance supported browsers and fall back to ordinary navigation elsewhere. No continuous JavaScript animation loops.

## Content provenance

Biography, work history, project details, awards, and external destinations come from the original portfolio. Both ConvergentIS roles and the current skills list are sourced from WorthTheCall_TristanBeley_Resume.pdf. Existing PDFs are preserved. The original Unity video link pointed to a missing file and is omitted. Role titles, dates, and engineering scope are taken from the supplied resume.

## Design references

Original HTML/CSS implementations informed by 21st.dev's [cards and grids](https://21st.dev/community/components/s/card) and [navigation patterns](https://21st.dev/community/components/s/navigation-menu): composed project cards, a switchable preview, compact command menu, subtle hover motion, and grid-backed hero. No third-party component code or animation packages were copied into the site.

## Performance

HTML contains page content before JavaScript runs. Images use WebP, explicit dimensions, and lazy loading below the fold. The portrait is eager-loaded. The original 12.7 MB hockey image is served as a compressed derivative. Shared assets are cacheable by the host. Actual load times depend on hosting, connection, and device; no production Lighthouse score is claimed.

The skills wheel and directory share their content in `tools/skills_data.py`. Each category can be selected by mouse, touch, or keyboard. Wheel motion runs only after interaction. The original archive remains untouched.
