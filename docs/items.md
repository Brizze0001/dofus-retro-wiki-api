# ⚔️ Objets — Dofus Rétro API

Base URL : `https://wiki.moon-bot.io/api`

---

## `GET /api/items.json` — Liste des objets

Retourne un **tableau** de tous les objets (≈ 11 716 entrées).

### Champs

| Champ | Type | Description |
|-------|------|-------------|
| `id` | `integer` | Identifiant de l'objet (à utiliser dans `/api/item/{id}.json`). |
| `name` | `string` | Nom de l'objet. |
| `type` | `string` | Type (ex. `Amulette`, `Epée`, `Potion`…). |
| `level` | `integer` | Niveau de l'objet. |
| `url` | `string (uri)` | Fiche wiki. |

### Exemple

```json
[
  { "id": 39, "name": "Petite Amulette du Hibou", "type": "Amulette", "level": 1, "url": "https://wiki.moon-bot.io/items/petite-amulette-du-hibou/" },
  { "id": 42, "name": "Épée de Boisaille", "type": "Epée", "level": 3, "url": "https://wiki.moon-bot.io/items/epee-de-boisaille/" }
]
```

---

## `GET /api/item/{id}.json` — Détail d'un objet

Retourne le détail complet : caractéristiques (`stats`) et **recette de craft** (`recipe`).

### Paramètres

| Paramètre | Type | Exemple | Description |
|-----------|------|---------|-------------|
| `id` | `integer` (path) | `39` | Identifiant numérique de l'objet. |

### Champs

| Champ | Type | Description |
|-------|------|-------------|
| `id` | `integer` | Identifiant. |
| `name` | `string` | Nom. |
| `type` | `string` | Type. |
| `level` | `integer` | Niveau. |
| `weight` | `integer` | Poids (pods). |
| `price` | `integer` | Prix indicatif (PNJ). |
| `description` | `string` | Description en jeu. |
| `stats` | `array<string>` | Caractéristiques en texte (ex. `"+2 en intelligence"`, `"Dommages : 2 à 8 (neutre)"`). |
| `recipe` | `array<RecipeIngredient>` | Ingrédients de craft. |
| `url` | `string (uri)` | Fiche wiki. |

**Objet `RecipeIngredient` :**

| Champ | Type | Description |
|-------|------|-------------|
| `item_id` | `integer` | Id de l'ingrédient (appelable via `/api/item/{item_id}.json`). |
| `name` | `string` | Nom de l'ingrédient. |
| `qty` | `integer` | Quantité requise. |

### Exemple — `GET /api/item/42.json`

```json
{
  "id": 42,
  "name": "Épée de Boisaille",
  "type": "Epée",
  "level": 3,
  "weight": 20,
  "price": 250,
  "description": "Epée de simple facture, elle ne fera pas de votre héros une légende.",
  "stats": ["Dommages : 2 à 8 (neutre)", "+1 en force"],
  "recipe": [
    { "item_id": 473, "name": "Bois de Châtaignier", "qty": 3 },
    { "item_id": 303, "name": "Bois de Frêne", "qty": 2 }
  ],
  "url": "https://wiki.moon-bot.io/items/epee-de-boisaille/"
}
```

> 🛠️ La présence de `recipe` permet de construire un **calculateur de craft** : descendez récursivement sur chaque `item_id` pour calculer le coût total en ressources.

### Erreurs

- `404` : id inexistant → page **HTML** renvoyée (pas de JSON). Vérifiez le `Content-Type`.

---

⬅️ [Retour à la doc](../README.md) · 📡 [API en ligne](https://wiki.moon-bot.io/api/) · 🌙 [moon-bot.io](https://moon-bot.io/)
