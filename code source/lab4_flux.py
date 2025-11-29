#Etape1:
seuil = 10  # note minimale pour être admis
note_maximale=20
try:
    note = float(input("Entrez la note de l'étudiant : "))
except ValueError:
    print("Saisie invalide.")
    exit(1)
if note < 0 or note > note_maximale :
    print("Saisie invalide: Note hors plage!")
    exit(1)
if note >=16:
    print("Mention: tres bien")
elif note >=14:
    print("Mention: bien")
elif note >=12:
    print("Mention: assez bein")
elif note >= seuil:
    print("Admis")
elif note >= seuil / 2:
    print("Rattrapage")
else:
    print("Refusé")

#Etape2:
mot_cle = "stop"
message = ""

while message.lower() != mot_cle:
    message = input("Tapez un message (ou 'stop' pour quitter) : ")
    if message.strip() != "" and message.lower() != mot_cle:
        print(f"Vous avez saisi : {message}")
print("Boucle terminée, mot-clé détecté.")

#Etape3:
for i in range(1, 6):  # va de 1 inclus à 6 exclu
    print(f"Nombre {i}")
for i in range(0, 10,2):  # va de 0 inclus à 10 exclu avec un pas de 2 (AFFCHAGE DES NOMBRES PAIRES )
    print(f"Nombre {i}")
for i in range(10, 0,-1):  # va de 0 inclus à 10 exclu avec un pas de -1 (AFFCHAGE INVERSE  )
    print(f"Nombre {i}")
for i in range(8):  # va de 0 par default
    print(f"Nombre {i}")

#Etape4:
fruits = ["pomme", "banane", "cerise"]
for index, fruit in enumerate(fruits):
    print(f"{index} → {fruit}")

Nombres_impaires=[1,3,5,7,9]
for index, Nombres in enumerate(Nombres_impaires, start=1):
    print(f"{index} -> {Nombres}")

#Etape5:
seuil = 10
notes = []
compteur=0
max_notes = 10
while compteur < max_notes:
    entree = input("Entrez une note ou 'stop' : ").strip()
    if entree.lower() == "stop":
        break
    try:
        note = float(entree)
    except ValueError:
        print("Valeur incorrecte, merci d'entrer un nombre.")
        continue
    notes.append(note)
    compteur = compteur + 1
else:
    print("Nombre maximum de notes atteint.")
for index, note in enumerate(notes, start=1):
    statut = "Admis" if note >= seuil else "Refusé"
    print(f"Étudiant {index} : note {note} → {statut}")
# Calcul de la moyenne et mention globale:
somme = 0
for note in notes:
    somme = somme + note
moyenne = somme / len(notes)
print(f"Moyenne des etudiants est : {moyenne} ")
if moyenne >= 16:
    print("Mention de la class est  :Très bien")
elif moyenne >= 14:
    print("Mention de la class est  : bien")
elif moyenne >= 12:
    print("Mention de la class est  :Assez bien")
elif moyenne >= seuil:
    print("Mention de la class est  = Admis")
else:
    print("refuse")

