# The original portfolio

This is an exact snapshot of Tristan's handmade portfolio before the multi-page redesign.

Source commit: `4d7585e150fd63b66c2af8631725b8a066563908`.

All tracked code, original images, resumes, and project files are preserved in `original-portfolio/`. The files have not been rewritten or modernized.

## Run the original

From the repository root:

```sh
python -m http.server 4174 --directory archive/original-portfolio
```

Open http://localhost:4174. Serve this folder as the web root because the original code includes absolute `/Images/` links. Any missing external resources or original bugs remain as they were in the snapshot.

The current website lives at the repository root. This archive is a separate copy and can be copied elsewhere whenever you want to revisit it.
