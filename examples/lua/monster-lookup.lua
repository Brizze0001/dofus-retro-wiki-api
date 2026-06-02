--[[
  Exemple Lua — récupérer le point faible élémentaire d'un monstre
  via l'API Dofus Rétro (https://wiki.moon-bot.io/api/).

  Dépendances : LuaSocket + LuaSec (HTTPS) et un parseur JSON (ex. dkjson).
    luarocks install luasec
    luarocks install dkjson

  Cas d'usage : un outil/bot qui choisit l'élément optimal selon la
  résistance la plus négative du monstre.
]]

local https = require("ssl.https")
local json  = require("dkjson")

local API = "https://wiki.moon-bot.io/api"

--- Récupère le détail d'un monstre par son id.
local function getMonster(id)
  local body, code = https.request(API .. "/monster/" .. id .. ".json")
  if code ~= 200 or not body then
    error("Monstre " .. tostring(id) .. " introuvable (HTTP " .. tostring(code) .. ")")
  end
  return json.decode(body)
end

--- Renvoie l'élément le plus faible (résistance la plus négative) au dernier palier.
local function bestElement(monster)
  local grade = monster.grades[#monster.grades]
  local best, bestVal = nil, math.huge
  for element, value in pairs(grade.resist) do
    if value < bestVal then best, bestVal = element, value end
  end
  return best, bestVal
end

-- Démo
local craqueleur = getMonster(37)
print(craqueleur.name .. " -> point faible annonce : " .. tostring(craqueleur.weakness))

local element, value = bestElement(craqueleur)
print(string.format("Element optimal (resist mini) : %s (%d%%)", element, value))
