

import re
import os

fichier="HELLO WORLD.PY"
with open (fichier, "r", encoding="utf-8") as f:
    contenu=f.read()

# séparer à chaque "#exercice"
parties = re.split(r'(?im)^\s*#\s*exercice\s*\d*\s*$', contenu)
# supprimer les parties vides
parties=[p.strip() for p in parties if p.strip()]

for i,exercice in enumerate(parties, start=1):
    nom = f"exercice_{i}.py"
    with open (nom, "w",encoding="utf-8") as f:
        f.write(exercice+"\n")

    print(f"{nom} créé")

print("tous les exercices ont été séparés !")