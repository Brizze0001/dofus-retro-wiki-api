# 🐉 Monstres — Dofus Rétro API

Base URL : `https://wiki.moon-bot.io/api`

---

## `GET /api/monsters.json` — Liste des monstres

Retourne un **tableau** de tous les monstres (≈ 1 471 entrées).

### Champs

| Champ | Type | Description |
|-------|------|-------------|
| `id` | `integer` | Identifiant de liste. ⚠️ **Peut ne pas être unique** d'une entrée à l'autre — utilisez `url` comme clé canonique. |
| `name` | `string` | Nom du monstre. |
| `level_min` | `string` | Tranche de niveau, au format texte (ex. `"1 à 6"`). |
| `url` | `string (uri)` | URL de la fiche sur le wiki. |

### Exemple

```json
[
  { "id": 1, "name": "Arakne", "level_min": "1 à 3", "url": "https://wiki.moon-bot.io/monstres/arakne/" },
  { "id": 1, "name": "Bouftou", "level_min": "1 à 6", "url": "https://wiki.moon-bot.io/monstres/bouftou/" }
]
```

> 💡 Pour obtenir les statistiques détaillées, appelez `/api/monster/{id}.json` avec l'**id numérique du détail** (ex. `37` pour le Craqueleur). Le slug de `url` est l'identifiant humain fiable.

---

## `GET /api/monster/{id}.json` — Détail d'un monstre

Retourne le détail complet : niveaux, **point faible élémentaire**, et **paliers** (grades) avec PV/PA/PM et résistances.

### Paramètres

| Paramètre | Type | Exemple | Description |
|-----------|------|---------|-------------|
| `id` | `integer` (path) | `37` | Identifiant numérique du monstre. |

### Champs

| Champ | Type | Description |
|-------|------|-------------|
| `id` | `integer` | Identifiant du monstre. |
| `name` | `string` | Nom. |
| `boss` | `boolean` | `true` si c'est un boss. |
| `url` | `string (uri)` | Fiche wiki. |
| `level_min` / `level_max` | `integer` | Niveaux min et max. |
| `weakness` | `string` | Point faible élémentaire (ex. `"Feu"`). |
| `grades` | `array<Grade>` | Un objet par palier (voir ci-dessous). |
| `locations` | `array` | Localisations (peut être vide). |

**Objet `Grade` :**

| Champ | Type | Description |
|-------|------|-------------|
| `grade` | `integer` | Numéro du palier. |
| `level` | `integer` | Niveau à ce palier. |
| `hp` | `integer` | Points de vie. |
| `ap` | `integer` | Points d'action (PA). |
| `mp` | `integer` | Points de mouvement (PM). |
| `resist` | `object` | Résistances % : `neutral`, `earth`, `fire`, `water`, `air`. |

### Exemple — `GET /api/monster/37.json`

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
      "resist": { "neutral": 0, "earth": 25, "fire": -50, "water": 6, "air": -12 } },
    { "grade": 6, "level": 6, "hp": 250, "ap": 5, "mp": 4,
      "resist": { "neutral": 25, "earth": 50, "fire": -25, "water": 12, "air": -6 } }
  ],
  "locations": []
}
```

> 🔥 Astuce : une **résistance négative** indique une faiblesse à cet élément (ici `fire: -50` → frapper **Feu**). Idéal pour qu'un bot/outil choisisse l'élément optimal.

### Erreurs

- `404` : id inexistant → le serveur renvoie une **page HTML** (et non du JSON). Vérifiez le `Content-Type` avant de parser.

---

⬅️ [Retour à la doc](../README.md) · 📡 [API en ligne](https://wiki.moon-bot.io/api/) · 🌙 [moon-bot.io](https://moon-bot.io/)
