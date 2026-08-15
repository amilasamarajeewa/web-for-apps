# AS TechnoArt Landing Page

Free GitHub Pages landing page with an automated Google Play catalogue updater.

## Deploy

1. Create a public GitHub repository, e.g. `as-technoart-site`.
2. Upload the contents of this folder to the repository.
3. Open **Settings → Pages**.
4. Select **Deploy from a branch**, choose `main` and `/ (root)`.
5. Save.

Your URL will be:
`https://YOUR-GITHUB-USERNAME.github.io/as-technoart-site/`

## Automatic updates

`.github/workflows/update-apps.yml` runs daily and can also be started manually from **Actions**.

It reads the public AS TechnoArt Google Play developer page and regenerates `data/apps.json`. GitHub Pages then serves the updated catalogue.

Google may change the HTML structure of Play Store pages. The updater preserves the previous catalogue if parsing fails, so a temporary Google change will not erase the live app list.

Developer page:
https://play.google.com/store/apps/dev?id=6407847081352449241
