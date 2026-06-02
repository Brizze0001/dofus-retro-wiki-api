# 🔎 Index de recherche — Dofus Rétro API

Base URL : `https://wiki.moon-bot.io/api`

---

## `GET /api/search-index.json` — Index global

Retourne un **tableau léger** regroupant monstres et objets, optimisé pour une **barre de recherche instantanée** (clés courtes pour réduire le poids).

### Champs

| Champ | Type | Description |
|-------|------|-------------|
| `n` | `string` | **N**om de l'entrée. |
| `u` | `string` | **U**RL relative de la fiche (ex. `/monstres/craqueleur/`). |
| `c` | `string` | **C**atégorie (`Monstre`, `Objet`, …). |
| `i` | `string` | **I**cône (chemin relatif, ex. `/icons/sprite_1156.png`). |

### Exemple

```json
[
  { "n": "Bouftou",    "u": "/monstres/bouftou/",    "c": "Monstre", "i": "/icons/sprite_1566.png" },
  { "n": "Craqueleur", "u": "/monstres/craqueleur/", "c": "Monstre", "i": "/icons/sprite_1156.png" }
]
```

### Bon usage

- Téléchargez l'index **une seule fois** au chargement, puis filtrez **côté client** (recherche instantanée, autocomplétion).
- Préfixez `u` et `i` par `https://wiki.moon-bot.io` pour obtenir des URLs absolues.

---

⬅️ [Retour à la doc](../README.md) · 📡 [API en ligne](https://wiki.moon-bot.io/api/) · 🌙 [moon-bot.io](https://moon-bot.io/)
