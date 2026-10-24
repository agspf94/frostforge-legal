# frostforge-legal

Public pages for the Frostforge game (privacy policy, account deletion), served by GitHub Pages
at https://agspf94.github.io/frostforge-legal/ in English, Portuguese (Brazil) and Spanish (Latin America).

## Sources

- English, Portuguese and Spanish: `docs/legal/privacy-policy.md` in the private game repo (the build copies the Spanish section into `src/privacy-policy.es.md`).
- Account deletion: `docs/legal/web/delete-account.html` and its `delete-account-config.json` in the game repo, published as-is
  once the config holds the prod values; otherwise a static page whose texts live in `scripts/legal/build_legal.py`, like the index texts.

**Generated: do not edit this repo by hand.** Edit the sources in the game repo; every merge to its `main` that touches
`docs/legal/` or `scripts/legal/` runs the "Publish legal pages" workflow, which rebuilds and pushes here, and GitHub Pages redeploys.

## Languages

Each page shows one language at a time, chosen by `#en` / `#pt-br` / `#es` (or `?lang=`), then the saved
choice, then the browser language. Without JavaScript all languages are shown.
