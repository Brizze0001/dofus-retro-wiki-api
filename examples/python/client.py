"""Client d'exemple pour l'API Dofus Rétro (https://wiki.moon-bot.io/api/).

Aucune clé requise. Pensez à mettre en cache et à ne pas marteler le serveur.

    pip install -r requirements.txt
    python client.py
"""
from __future__ import annotations

import time
from functools import lru_cache

import requests

API = "https://wiki.moon-bot.io/api"
SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "dofus-retro-api-example/1.0"})


def get_monster(monster_id: int) -> dict:
    """Détail d'un monstre par son id."""
    r = SESSION.get(f"{API}/monster/{monster_id}.json", timeout=15)
    r.raise_for_status()
    return r.json()


def get_item(item_id: int) -> dict:
    """Détail d'un objet par son id."""
    r = SESSION.get(f"{API}/item/{item_id}.json", timeout=15)
    r.raise_for_status()
    return r.json()


@lru_cache(maxsize=1)
def list_items() -> tuple[dict, ...]:
    """Liste complète des objets (mise en cache en mémoire)."""
    r = SESSION.get(f"{API}/items.json", timeout=30)
    r.raise_for_status()
    return tuple(r.json())


def search_items(keyword: str) -> list[dict]:
    """Filtre la liste des objets par mot-clé (insensible à la casse)."""
    kw = keyword.lower()
    return [it for it in list_items() if kw in it["name"].lower()]


def craft_cost(item_id: int, multiplier: int = 1, acc: dict | None = None) -> dict:
    """Coût en ressources brutes (descente récursive dans les recettes)."""
    acc = acc if acc is not None else {}
    item = get_item(item_id)
    recipe = item.get("recipe") or []
    if not recipe:
        acc[item["name"]] = acc.get(item["name"], 0) + multiplier
        return acc
    for ing in recipe:
        craft_cost(ing["item_id"], multiplier * ing["qty"], acc)
        time.sleep(0.05)  # courtoisie envers le serveur communautaire
    return acc


if __name__ == "__main__":
    craqueleur = get_monster(37)
    print(f"{craqueleur['name']} → point faible : {craqueleur['weakness']}")
    print("Résistances (dernier palier) :", craqueleur["grades"][-1]["resist"])

    epee = get_item(42)
    print(f"\n{epee['name']} (niv. {epee['level']}) — recette :")
    for ing in epee["recipe"]:
        print(f"  - {ing['qty']}x {ing['name']}")

    print("\nObjets contenant 'amulette' (5 premiers) :")
    for it in search_items("amulette")[:5]:
        print(f"  - [{it['level']}] {it['name']} ({it['type']})")

    print("\nCoût en ressources brutes de l'Épée de Boisaille :")
    print(craft_cost(42))
