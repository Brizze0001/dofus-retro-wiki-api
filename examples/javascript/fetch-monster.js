// Exemples JavaScript pour l'API Dofus Rétro
// Fonctionne dans le navigateur (CORS ouvert) ou avec Node 18+ (fetch natif).
//   node fetch-monster.js

const API = "https://wiki.moon-bot.io/api";

/** Récupère le détail d'un monstre par son id. */
export async function getMonster(id) {
  const res = await fetch(`${API}/monster/${id}.json`);
  if (!res.ok) throw new Error(`Monstre ${id} introuvable (HTTP ${res.status})`);
  return res.json();
}

/** Récupère le détail d'un objet par son id. */
export async function getItem(id) {
  const res = await fetch(`${API}/item/${id}.json`);
  if (!res.ok) throw new Error(`Objet ${id} introuvable (HTTP ${res.status})`);
  return res.json();
}

/** Liste complète des objets (à mettre en cache !). */
export async function listItems() {
  return fetch(`${API}/items.json`).then((r) => r.json());
}

/**
 * Calcule le coût en ressources « brutes » d'un objet en descendant
 * récursivement dans les recettes (objets sans recette = matière première).
 */
export async function craftCost(id, multiplier = 1, acc = {}) {
  const item = await getItem(id);
  if (!item.recipe || item.recipe.length === 0) {
    acc[item.name] = (acc[item.name] || 0) + multiplier;
    return acc;
  }
  for (const ing of item.recipe) {
    await craftCost(ing.item_id, multiplier * ing.qty, acc);
  }
  return acc;
}

// --- Démo (exécutée uniquement avec Node) ---
if (typeof process !== "undefined" && process.argv[1]?.endsWith("fetch-monster.js")) {
  const craqueleur = await getMonster(37);
  console.log(`${craqueleur.name} → point faible : ${craqueleur.weakness}`);
  console.log("Résistances (dernier palier) :", craqueleur.grades.at(-1).resist);

  const epee = await getItem(42);
  console.log(`\n${epee.name} (niv. ${epee.level}) — recette :`);
  for (const ing of epee.recipe) console.log(`  - ${ing.qty}x ${ing.name}`);

  console.log("\nCoût en ressources brutes de l'Épée de Boisaille :");
  console.log(await craftCost(42));
}
