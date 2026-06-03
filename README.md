# Dofus Rétro API — API JSON communautaire (monstres, objets, recettes) 🐉⚔️

**🌐 Langues / Languages / Idiomas : [🇫🇷 Français](README.md) · [🇬🇧 English](README.en.md) · [🇪🇸 Español](README.es.md)**

> **API publique, gratuite et sans clé** pour les données de **Dofus Rétro** : monstres, objets, recettes de craft, statistiques, résistances et zones.
> Propulsée par le **[Wiki Dofus Rétro communautaire](https://wiki.moon-bot.io/)** — données extraites du client, au format **JSON statique** avec **CORS** ouvert.

[![API Dofus Rétro](https://img.shields.io/badge/API-Dofus%20R%C3%A9tro-5865f2?style=for-the-badge)](https://wiki.moon-bot.io/api/)
[![Wiki](https://img.shields.io/badge/Wiki-moon--bot.io-5865f2?style=for-the-badge)](https://wiki.moon-bot.io/)
[![Sans clé](https://img.shields.io/badge/Auth-aucune%20cl%C3%A9-46c97e?style=for-the-badge)]()
[![CORS](https://img.shields.io/badge/CORS-*-46c97e?style=for-the-badge)]()
[![Licence MIT](https://img.shields.io/badge/Licence-MIT-green?style=for-the-badge)](LICENSE)

---

## 🐉 C'est quoi cette API ?

La **Dofus Rétro API** expose les **données de jeu de Dofus Rétro** (version 1.29) sous forme de **fichiers JSON statiques**, servis par le **[Wiki Dofus Rétro](https://wiki.moon-bot.io/)**, un projet **communautaire et non officiel**.

- ✅ **1 471 monstres** — niveaux, points de vie, PA/PM, **résistances élémentaires**, points faibles, paliers (grades).
- ✅ **11 716 objets** — type, niveau, poids, prix, caractéristiques et **recettes de craft**.
- ✅ **Index de recherche** global (monstres + objets) avec icônes.
- ✅ **Aucune authentification**, **aucune clé**, **gratuit**.
- ✅ **CORS** activé (`Access-Control-Allow-Origin: *`) → utilisable directement depuis un navigateur.
- ✅ Réponses mises en cache (`Cache-Control: public, max-age=3600`).

> 🌙 Ces données alimentent l'écosystème **[Moonbot Rétro](https://moon-bot.io/)** et sont mises à disposition de toute la communauté Dofus Rétro : développeurs d'outils, calculateurs, overlays, bots, sites de craft…

**Base URL :** `https://wiki.moon-bot.io/api`

---

## 🚀 Démarrage rapide

```bash
# Liste de tous les monstres
curl https://wiki.moon-bot.io/api/monsters.json

# Détail d'un monstre (37 = Craqueleur) → points faibles, résistances, paliers
curl https://wiki.moon-bot.io/api/monster/37.json

# Détail d'un objet (39 = Petite Amulette du Hibou) → stats + recette
curl https://wiki.moon-bot.io/api/item/39.json
```

```javascript
// JavaScript (navigateur ou Node 18+) — grâce au CORS, ça marche directement dans le front
const monstre = await fetch("https://wiki.moon-bot.io/api/monster/37.json").then(r => r.json());
console.log(monstre.name, "→ point faible :", monstre.weakness); // Craqueleur → point faible : Feu
```

➡️ Plus d'exemples (curl, JavaScript, Python, Lua) dans [`examples/`](examples/).

---

## 📚 Endpoints

| Méthode | Route | Description |
|--------|-------|-------------|
| `GET` | [`/api/monsters.json`](https://wiki.moon-bot.io/api/monsters.json) | Liste de tous les monstres (id, nom, tranche de niveau, url) |
| `GET` | [`/api/monster/{id}.json`](https://wiki.moon-bot.io/api/monster/37.json) | Détail d'un monstre : niveaux, paliers, PV/PA/PM, **résistances**, point faible |
| `GET` | [`/api/items.json`](https://wiki.moon-bot.io/api/items.json) | Liste de tous les objets (id, nom, type, niveau, url) |
| `GET` | [`/api/item/{id}.json`](https://wiki.moon-bot.io/api/item/39.json) | Détail d'un objet : caractéristiques, **recette de craft**, type, niveau, prix |
| `GET` | [`/api/search-index.json`](https://wiki.moon-bot.io/api/search-index.json) | Index de recherche global (nom, url, catégorie, icône) |

📖 Documentation détaillée par endpoint dans [`docs/`](docs/) · Spécification **OpenAPI 3.0** : [`openapi.yaml`](openapi.yaml).

---

## 🧬 Exemples de réponses

### `GET /api/monster/37.json` — Craqueleur
```json
{
  "id": 37,
  "name": "Craqueleur",
  "boss": false,
  "url": "https://wiki.moon-bot.io/monstres/craqueleur/",
  "level_min": 1,
  "level_max": 6,
  "weakness": "Feu",
  "grades": [
    { "grade": 1, "level": 1, "hp": 100, "ap": 5, "mp": 2,
      "resist": { "neutral": 0, "earth": 25, "fire": -50, "water": 6, "air": -12 } }
  ],
  "locations": []
}
```

### `GET /api/item/39.json` — Petite Amulette du Hibou
```json
{
  "id": 39,
  "name": "Petite Amulette du Hibou",
  "type": "Amulette",
  "level": 1,
  "weight": 4,
  "price": 100,
  "description": "Cette amulette augmente l'intelligence de son porteur.",
  "stats": ["+2 en intelligence"],
  "recipe": [
    { "item_id": 441, "name": "Cuivre", "qty": 1 },
    { "item_id": 473, "name": "Bois de Châtaignier", "qty": 1 }
  ],
  "url": "https://wiki.moon-bot.io/items/petite-amulette-du-hibou/"
}
```

### `GET /api/search-index.json` — entrée d'index
```json
{ "n": "Craqueleur", "u": "/monstres/craqueleur/", "c": "Monstre", "i": "/icons/sprite_1156.png" }
```

---

## 💡 Idées d'utilisation communautaire

- 🔮 **Calculateurs de craft** et de rentabilité (recettes → prix HDV).
- 🗺️ **Overlays / outils de chasse** affichant le point faible élémentaire d'un monstre.
- 🤖 **Scripts & bots** ([Moonbot Rétro](https://moon-bot.io/)) qui choisissent l'élément optimal selon les **résistances**.
- 📊 **Bestiaires, wikis et apps mobiles** alimentés par des données à jour.
- 🔎 **Barres de recherche** instantanées via `search-index.json`.

---

## ⚙️ Bonnes pratiques

- **Cachez** les réponses côté client (les fichiers sont déjà servis avec `max-age=3600`).
- Pour parcourir tout le bestiaire/les objets, téléchargez **une fois** `monsters.json` / `items.json`, puis tapez les `monster/{id}.json` au besoin.
- **Ne surchargez pas** le serveur communautaire : évitez les milliers de requêtes en rafale, ajoutez un petit délai dans vos boucles.
- Les données sont **non officielles** et peuvent évoluer ; signalez les erreurs sur le [Discord communautaire](https://wiki.moon-bot.io/).

---

## 🤝 Contribuer

Ce dépôt documente l'API et fournit des exemples pour toute la communauté Dofus Rétro. Exemples dans un nouveau langage, corrections de doc, schémas, wrappers… tout est bienvenu : voir [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## 🔗 Liens

- 📖 **Wiki Dofus Rétro (source des données)** → **[wiki.moon-bot.io](https://wiki.moon-bot.io/)**
- 📡 **Documentation API** → [wiki.moon-bot.io/api](https://wiki.moon-bot.io/api/)
- 🌙 **Moonbot Rétro (bot Dofus Rétro)** → **[moon-bot.io](https://moon-bot.io/)**

---

## 🔖 Mots-clés

`dofus rétro api` · `dofus retro json` · `api dofus` · `dofus 1.29 api` · `bestiaire dofus rétro` · `recettes craft dofus` · `monstres dofus retro` · `objets dofus retro` · `dofus retro data` · `wiki dofus rétro` · `moonbot`

---

<sub>API et données fournies par le Wiki Dofus Rétro communautaire (wiki.moon-bot.io). Projet non officiel — Dofus et Dofus Rétro sont des marques d'Ankama Games. Non affilié à Ankama.</sub>
