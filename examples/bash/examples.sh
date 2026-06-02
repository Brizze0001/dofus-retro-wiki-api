#!/usr/bin/env bash
# Exemples d'utilisation de l'API Dofus Rétro avec curl + jq
# Dépendances : curl, jq   (https://stedolan.github.io/jq/)
set -euo pipefail

API="https://wiki.moon-bot.io/api"

echo "== 1) Nombre total de monstres =="
curl -s "$API/monsters.json" | jq 'length'

echo "== 2) Détail du Craqueleur (id 37) : point faible =="
curl -s "$API/monster/37.json" | jq '{name, weakness, level_max}'

echo "== 3) Résistances du Craqueleur au dernier palier =="
curl -s "$API/monster/37.json" | jq '.grades[-1].resist'

echo "== 4) Recette de l'Épée de Boisaille (id 42) =="
curl -s "$API/item/42.json" | jq '{name, recipe}'

echo "== 5) Chercher 'bouftou' dans l'index de recherche =="
curl -s "$API/search-index.json" | jq '[.[] | select(.n | ascii_downcase | contains("bouftou"))]'

echo "== 6) Lister les objets de type 'Amulette' de niveau <= 20 =="
curl -s "$API/items.json" | jq '[.[] | select(.type=="Amulette" and .level<=20)] | sort_by(.level)'
