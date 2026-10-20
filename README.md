# frostforge-legal

Public pages for the Frostforge game (privacy policy, account deletion), served by GitHub Pages
at https://agspf94.github.io/frostforge-legal/ in English, Portuguese (Brazil) and Spanish (Latin America).

## Sources

- English and Portuguese: `docs/legal/privacy-policy.md` in the private game repo.
- Spanish (es-419): `src/privacy-policy.es.md` in this repo. The account-deletion and index texts for all
  three languages live in `build_legal.py`.

Edit the sources, never the generated HTML.

## Rebuild

Needs Python 3 and `pip install markdown`. From this repo, with the game repo checked out next to it:

```sh
python3 build_legal.py ../frostforge . "the Frostforge developer, Anderson Fantin" "YYYY-MM-DD"
```

An optional fifth argument sets the controller name in Spanish (default: derived from the English one).
The build fails if any `[PLACEHOLDER]` is left unfilled. Commit and push to `main`; GitHub Pages redeploys.

## Languages

Each page shows one language at a time, chosen by `#en` / `#pt-br` / `#es` (or `?lang=`), then the saved
choice, then the browser language. Without JavaScript all languages are shown.
