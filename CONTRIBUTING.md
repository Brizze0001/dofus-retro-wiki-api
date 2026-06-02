# Contribuer — Dofus Rétro API 🐉

Merci de vouloir améliorer la documentation et les outils autour de l'**[API Dofus Rétro](https://wiki.moon-bot.io/api/)** ! Ce dépôt est **communautaire** : toute contribution utile à l'écosystème Dofus Rétro est bienvenue.

## Ce que vous pouvez apporter

- 📝 **Documentation** : corrections, précisions sur les champs, nouveaux exemples de réponses.
- 💻 **Exemples de code** : nouveaux langages (PHP, Go, C#, Rust, Kotlin…), notebooks, snippets front-end.
- 📦 **Wrappers / mini-SDK** : petites bibliothèques pour appeler l'API facilement.
- 🧪 **Schémas & validation** : amélioration des schémas JSON / de la spec OpenAPI.
- 🛠️ **Outils** : démos (calculateur de craft, recherche, overlay de point faible…).

## Comment proposer une contribution

1. **Forkez** le dépôt et créez une branche : `git checkout -b mon-exemple-go`.
2. Ajoutez vos fichiers au bon endroit :
   - exemples de code → `examples/<langage>/`
   - documentation d'endpoint → `docs/`
   - schémas → `schemas/`
3. Vérifiez que vos exemples **tournent réellement** contre `https://wiki.moon-bot.io/api`.
4. Ouvrez une **Pull Request** en décrivant votre ajout.

## Règles de bon voisinage avec l'API

- L'API est servie par un **serveur communautaire** : vos exemples doivent **mettre en cache** et **ne pas marteler** le serveur (ajoutez un délai dans les boucles).
- Préférez télécharger `monsters.json` / `items.json` **une fois** plutôt que de boucler sur des milliers de `monster/{id}.json`.
- Signalez les **erreurs de données** directement sur le [Discord communautaire](https://wiki.moon-bot.io/) (ce dépôt documente l'API, il n'héberge pas les données).

## Rappel

Projet **non officiel**. Dofus et Dofus Rétro sont des marques d'**Ankama Games**. Les données restent la propriété d'Ankama. Ce dépôt est sous licence **MIT** (voir [`LICENSE`](LICENSE)).

Bon code, et longue vie à la communauté Dofus Rétro ! 🌙
