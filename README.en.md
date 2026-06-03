# Dofus Retro API — Community JSON API (monsters, items, recipes) 🐉⚔️

**🌐 Langues / Languages / Idiomas: [🇫🇷 Français](README.md) · [🇬🇧 English](README.en.md) · [🇪🇸 Español](README.es.md)**

> **Public, free, key-less API** for **Dofus Retro** game data: monsters, items, craft recipes, stats, resistances and zones.
> Powered by the **[community Dofus Retro Wiki](https://wiki.moon-bot.io/)** — data extracted from the client, served as **static JSON** with open **CORS**.

[![Dofus Retro API](https://img.shields.io/badge/API-Dofus%20Retro-5865f2?style=for-the-badge)](https://wiki.moon-bot.io/api/)
[![Wiki](https://img.shields.io/badge/Wiki-moon--bot.io-5865f2?style=for-the-badge)](https://wiki.moon-bot.io/)
[![No key](https://img.shields.io/badge/Auth-no%20key-46c97e?style=for-the-badge)]()
[![CORS](https://img.shields.io/badge/CORS-*-46c97e?style=for-the-badge)]()
[![MIT License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## 🐉 What is this API?

The **Dofus Retro API** exposes **Dofus Retro (1.29) game data** as **static JSON files**, served by the **[Dofus Retro Wiki](https://wiki.moon-bot.io/)**, a **community, unofficial** project.

- ✅ **1,471 monsters** — levels, hit points, AP/MP, **elemental resistances**, weaknesses, grades.
- ✅ **11,716 items** — type, level, weight, price, characteristics and **craft recipes**.
- ✅ Global **search index** (monsters + items) with icons.
- ✅ **No authentication**, **no key**, **free**.
- ✅ **CORS** enabled (`Access-Control-Allow-Origin: *`) → usable straight from the browser.
- ✅ Cached responses (`Cache-Control: public, max-age=3600`).

> 🌙 This data powers the **[Moonbot Rétro](https://moon-bot.io/)** ecosystem and is shared with the whole Dofus Retro community: tool makers, calculators, overlays, bots, craft sites…

**Base URL:** `https://wiki.moon-bot.io/api`

---

## 🚀 Quick start

```bash
# List every monster
curl https://wiki.moon-bot.io/api/monsters.json

# Monster detail (37 = Craqueleur) → weaknesses, resistances, grades
curl https://wiki.moon-bot.io/api/monster/37.json

# Item detail (39 = Petite Amulette du Hibou) → stats + recipe
curl https://wiki.moon-bot.io/api/item/39.json
```

```javascript
// JavaScript (browser or Node 18+) — thanks to CORS it works straight from the front-end
const monster = await fetch("https://wiki.moon-bot.io/api/monster/37.json").then(r => r.json());
console.log(monster.name, "→ weakness:", monster.weakness); // Craqueleur → weakness: Feu
```

➡️ More examples (curl, JavaScript, Python, Lua) in [`examples/`](examples/).

---

## 📚 Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | [`/api/monsters.json`](https://wiki.moon-bot.io/api/monsters.json) | List of all monsters (id, name, level range, url) |
| `GET` | [`/api/monster/{id}.json`](https://wiki.moon-bot.io/api/monster/37.json) | Monster detail: levels, grades, HP/AP/MP, **resistances**, weakness |
| `GET` | [`/api/items.json`](https://wiki.moon-bot.io/api/items.json) | List of all items (id, name, type, level, url) |
| `GET` | [`/api/item/{id}.json`](https://wiki.moon-bot.io/api/item/39.json) | Item detail: characteristics, **craft recipe**, type, level, price |
| `GET` | [`/api/search-index.json`](https://wiki.moon-bot.io/api/search-index.json) | Global search index (name, url, category, icon) |

📖 Detailed per-endpoint docs in [`docs/`](docs/) · **OpenAPI 3.0** spec: [`openapi.yaml`](openapi.yaml).

---

## 🧬 Sample responses

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

### `GET /api/search-index.json` — index entry
```json
{ "n": "Craqueleur", "u": "/monstres/craqueleur/", "c": "Monstre", "i": "/icons/sprite_1156.png" }
```

---

## 💡 Community use cases

- 🔮 **Craft & profitability calculators** (recipes → market price).
- 🗺️ **Hunting tools / overlays** showing a monster's elemental weakness.
- 🤖 **Scripts & bots** ([Moonbot Rétro](https://moon-bot.io/)) picking the optimal element from **resistances**.
- 📊 **Bestiaries, wikis and mobile apps** powered by up-to-date data.
- 🔎 **Instant search bars** via `search-index.json`.

---

## ⚙️ Best practices

- **Cache** responses on the client (files are already served with `max-age=3600`).
- To browse the whole bestiary/items, download `monsters.json` / `items.json` **once**, then hit `monster/{id}.json` as needed.
- **Don't overload** the community server: avoid thousands of burst requests, add a small delay in your loops.
- Data is **unofficial** and may change; report errors on the [community Discord](https://wiki.moon-bot.io/).

---

## 🤝 Contributing

This repo documents the API and provides examples for the whole Dofus Retro community. Examples in a new language, doc fixes, schemas, wrappers… all welcome: see [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## 🔗 Links

- 📖 **Dofus Retro Wiki (data source)** → **[wiki.moon-bot.io](https://wiki.moon-bot.io/)**
- 📡 **API docs** → [wiki.moon-bot.io/api](https://wiki.moon-bot.io/api/)
- 🌙 **Moonbot Rétro (Dofus Retro bot)** → **[moon-bot.io](https://moon-bot.io/)**

---

## 🔖 Keywords

`dofus retro api` · `dofus retro json` · `dofus api` · `dofus 1.29 api` · `dofus retro bestiary` · `dofus craft recipes` · `dofus retro monsters` · `dofus retro items` · `dofus retro data` · `dofus retro wiki` · `moonbot`

---

<sub>API and data provided by the community Dofus Retro Wiki (wiki.moon-bot.io). Unofficial project — Dofus and Dofus Retro are trademarks of Ankama Games. Not affiliated with Ankama.</sub>
