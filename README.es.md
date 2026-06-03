# Dofus Retro API — API JSON comunitaria (monstruos, objetos, recetas) 🐉⚔️

**🌐 Langues / Languages / Idiomas: [🇫🇷 Français](README.md) · [🇬🇧 English](README.en.md) · [🇪🇸 Español](README.es.md)**

> **API pública, gratuita y sin clave** para los datos de **Dofus Retro**: monstruos, objetos, recetas de fabricación, estadísticas, resistencias y zonas.
> Impulsada por el **[Wiki comunitario de Dofus Retro](https://wiki.moon-bot.io/)** — datos extraídos del cliente, en formato **JSON estático** con **CORS** abierto.

[![Dofus Retro API](https://img.shields.io/badge/API-Dofus%20Retro-5865f2?style=for-the-badge)](https://wiki.moon-bot.io/api/)
[![Wiki](https://img.shields.io/badge/Wiki-moon--bot.io-5865f2?style=for-the-badge)](https://wiki.moon-bot.io/)
[![Sin clave](https://img.shields.io/badge/Auth-sin%20clave-46c97e?style=for-the-badge)]()
[![CORS](https://img.shields.io/badge/CORS-*-46c97e?style=for-the-badge)]()
[![Licencia MIT](https://img.shields.io/badge/Licencia-MIT-green?style=for-the-badge)](LICENSE)

---

## 🐉 ¿Qué es esta API?

La **Dofus Retro API** expone los **datos de juego de Dofus Retro (1.29)** como **ficheros JSON estáticos**, servidos por el **[Wiki de Dofus Retro](https://wiki.moon-bot.io/)**, un proyecto **comunitario y no oficial**.

- ✅ **1.471 monstruos** — niveles, puntos de vida, PA/PM, **resistencias elementales**, puntos débiles, grados.
- ✅ **11.716 objetos** — tipo, nivel, peso, precio, características y **recetas de fabricación**.
- ✅ **Índice de búsqueda** global (monstruos + objetos) con iconos.
- ✅ **Sin autenticación**, **sin clave**, **gratis**.
- ✅ **CORS** activado (`Access-Control-Allow-Origin: *`) → utilizable directamente desde el navegador.
- ✅ Respuestas en caché (`Cache-Control: public, max-age=3600`).

> 🌙 Estos datos alimentan el ecosistema **[Moonbot Rétro](https://moon-bot.io/)** y se comparten con toda la comunidad de Dofus Retro: creadores de herramientas, calculadoras, overlays, bots, webs de fabricación…

**URL base:** `https://wiki.moon-bot.io/api`

---

## 🚀 Inicio rápido

```bash
# Lista de todos los monstruos
curl https://wiki.moon-bot.io/api/monsters.json

# Detalle de un monstruo (37 = Craqueleur) → puntos débiles, resistencias, grados
curl https://wiki.moon-bot.io/api/monster/37.json

# Detalle de un objeto (39 = Petite Amulette du Hibou) → estadísticas + receta
curl https://wiki.moon-bot.io/api/item/39.json
```

```javascript
// JavaScript (navegador o Node 18+) — gracias al CORS funciona directamente en el front-end
const monstruo = await fetch("https://wiki.moon-bot.io/api/monster/37.json").then(r => r.json());
console.log(monstruo.name, "→ punto débil:", monstruo.weakness); // Craqueleur → punto débil: Feu
```

➡️ Más ejemplos (curl, JavaScript, Python, Lua) en [`examples/`](examples/).

---

## 📚 Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | [`/api/monsters.json`](https://wiki.moon-bot.io/api/monsters.json) | Lista de todos los monstruos (id, nombre, rango de nivel, url) |
| `GET` | [`/api/monster/{id}.json`](https://wiki.moon-bot.io/api/monster/37.json) | Detalle de un monstruo: niveles, grados, PV/PA/PM, **resistencias**, punto débil |
| `GET` | [`/api/items.json`](https://wiki.moon-bot.io/api/items.json) | Lista de todos los objetos (id, nombre, tipo, nivel, url) |
| `GET` | [`/api/item/{id}.json`](https://wiki.moon-bot.io/api/item/39.json) | Detalle de un objeto: características, **receta de fabricación**, tipo, nivel, precio |
| `GET` | [`/api/search-index.json`](https://wiki.moon-bot.io/api/search-index.json) | Índice de búsqueda global (nombre, url, categoría, icono) |

📖 Documentación detallada por endpoint en [`docs/`](docs/) · Especificación **OpenAPI 3.0**: [`openapi.yaml`](openapi.yaml).

---

## 🧬 Ejemplos de respuesta

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

### `GET /api/search-index.json` — entrada del índice
```json
{ "n": "Craqueleur", "u": "/monstres/craqueleur/", "c": "Monstre", "i": "/icons/sprite_1156.png" }
```

---

## 💡 Casos de uso comunitarios

- 🔮 **Calculadoras de fabricación** y de rentabilidad (recetas → precio del mercadillo).
- 🗺️ **Herramientas/overlays de caza** que muestran el punto débil elemental de un monstruo.
- 🤖 **Scripts y bots** ([Moonbot Rétro](https://moon-bot.io/)) que eligen el elemento óptimo según las **resistencias**.
- 📊 **Bestiarios, wikis y apps móviles** alimentados con datos actualizados.
- 🔎 **Barras de búsqueda** instantáneas con `search-index.json`.

---

## ⚙️ Buenas prácticas

- **Cachea** las respuestas en el cliente (los ficheros ya se sirven con `max-age=3600`).
- Para recorrer todo el bestiario/los objetos, descarga `monsters.json` / `items.json` **una vez** y luego consulta `monster/{id}.json` cuando lo necesites.
- **No sobrecargues** el servidor comunitario: evita miles de peticiones en ráfaga, añade un pequeño retraso en tus bucles.
- Los datos son **no oficiales** y pueden cambiar; informa de errores en el [Discord comunitario](https://wiki.moon-bot.io/).

---

## 🤝 Contribuir

Este repo documenta la API y ofrece ejemplos para toda la comunidad de Dofus Retro. Ejemplos en un nuevo lenguaje, correcciones de documentación, esquemas, wrappers… todo es bienvenido: consulta [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## 🔗 Enlaces

- 📖 **Wiki de Dofus Retro (fuente de datos)** → **[wiki.moon-bot.io](https://wiki.moon-bot.io/)**
- 📡 **Documentación de la API** → [wiki.moon-bot.io/api](https://wiki.moon-bot.io/api/)
- 🌙 **Moonbot Rétro (bot de Dofus Retro)** → **[moon-bot.io](https://moon-bot.io/)**

---

## 🔖 Palabras clave

`dofus retro api` · `dofus retro json` · `api dofus` · `dofus 1.29 api` · `bestiario dofus retro` · `recetas fabricación dofus` · `monstruos dofus retro` · `objetos dofus retro` · `datos dofus retro` · `wiki dofus retro` · `moonbot`

---

<sub>API y datos proporcionados por el Wiki comunitario de Dofus Retro (wiki.moon-bot.io). Proyecto no oficial — Dofus y Dofus Retro son marcas de Ankama Games. No afiliado a Ankama.</sub>
