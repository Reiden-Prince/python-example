impor
# Créaction de fonction

# afficher_information-personne
"""def afficher_information_personne(nom, age):
    print("Du heißst " + nom + ", du bist " + str(age) + " jahre alt.")
    print("Nachstes jahr, wirst du " + str(age + 1) + " Jahre alt.")

    # == egal
    # < inferieur
    # > superieur
    # <= inferieur ou egal
    # >= superieur ou egal
# afficher
    # age == 17 -> Vous etes presque majeur
    # age == 18 -> Vous etes tout juste majeur, felicitation
    # age >= 12 et age < 18  Vous etes adolescent
    # elif age >= 12 and age < 18: est la meme chose que elif  12 <= age < 18:
    #  age == 1 ou age == 2  Vous etes bebe
    # Nb: elif = else if
    if age == 17:
        print("Vous etes presque majeur")
    elif age >= 12 and age < 18:
        print("Vous etes adolescent")
    elif age == 1 or age == 2:
        print("Vous etes bebe")
    elif age < 10:
        print("Vous etes enfant")
    elif age == 18:
        print("Vous etes tout juste majeur, felicitation")
    elif age > 60:
        print("Vous etes senior")
    elif age >= 18:
        print("Vous etes majeur")
    else:
        print("Vous etes mineur")


# demander le nom
def demander_nom():
    rep_nom = ""
    while rep_nom == "":
        rep_nom = input("Wie heißst du?")
    return rep_nom


# demander l´age
def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Wie alt sind Sie?")
        # age = "nb entier" / int(age) = nb entier/ age_prochain = nb entier + 1
        try:
            age_int = int(age_str)
        except:
            print("Fehler: Sie müssen eine Nummer für das Alter eingeben")
    return age_int


# nom = "tata"

# print("Je m´appelle " + nom + ".")
# print()
# print("Mon nom c´est vraiment " + nom + ".")

# nom = input("Quel est votre nom?")
# print("Vous vous appelez " + nom + ".")

# nom = input("Quel est votre nom?")
# age = input("Quel est votre âge?")
# print("Vous vous appelez " + nom + ", et vous avez " + age + "ans.") ***

# demader le nom
# nom1 = demander_nom()
# nom2 = demander_nom()
# on peut forcer l´appel du nom
#nom1 = "Personne1"
#nom2 = "Personne2"
# demander l´age
#age1 = demander_age(nom1)
#age2 = demander_age(nom2)
# afficher information personne
#afficher_information_personne(nom1, age1)
#afficher_information_personne(nom2, age2)"""

# boucle for: il est utiliser en ecrivant: for i in ranger
"""PERSONNE = 15
for i in range(0, PERSONNE):
    print(i)

for i in range(0, PERSONNE):"""

"""NB_PERSONNE = 2
for i in range(0, NB_PERSONNE):
    nom = "personne" + str(i+1)
    age = demander_age(nom)
    afficher_information_personne(nom, age)



# affiffer les resultats
print("Du heißst " + rep_nom1 + ", du bist " + str(age_int1) + " jahre alt.")
print("Nachstes jahr, wirst du " + str(age_int1 + 1) + " Jahre alt.")

print("Du heißst " + rep_nom2 + ", du bist " + str(age_int2) + " jahre alt.")
print("Nachstes jahr, wirst du " + str(age_int2 + 1) + " Jahre alt.")
    # Boucle while : "tant que"
print("Debut de la boucle")
n = 0
print(n)
n = 1
print(n)
n = n + 1
print(n)
while n < 10:
    print("valeur de n:" + str(n))
    n = n + 2
#print("Fin de la boucle")"""

# Exp: Mot de passe
"""mot_de_passe = ""
while not mot_de_passe == "toto12":
    mot_de_passe = input("Quel est votre mot de passe")
print("Mot de passe correct, vous avez acces á votre compte")"""


# les fonctions

# on appelle la fonction print()
# exemple
"""nom = "toto"
print("Je m´appelle toto") # contient une seul parametre
print("je m´appelle " + nom)
print("je m´appelle", nom) # contient deux parametres
print("je m´appelle", nom, "j´ai", 30, "ans") # contient cinq parametres"""

"""nom = input("Votre Nom: ")
print("Votre nom est", nom)"""

"""nom1 = input(" nom de la personne 1")
age1 = input("age de La personne 1")
print("La peersonne 1 est", nom1, "son age est", age1, "ans")
# pour demande le nomnbre de lettre d´un parametre, on met len(le parametrre)"""

# creaction de fonction
# Pour creer une fonction on met
"""def afficher_information():
    nom = input(" nom de la personne 1")
    age = input("age de La personne 1")
    print("La personne 1 est", nom, "son age est", age, "ans")

# Maintenant on appel la fonction par:
afficher_information()"""

# nous allons appliquer des parametre pour s´adapter a plusieurs personne

def afficher_information(nom, age):
    print("La personne 1 est", nom, "son age est", age, "ans")
#afficher_information("nom", "age")
# si une parametre manque au niveau de l´appel il y a erreur.

# Nous definssons age comme un parametre optionnel
def afficher_information(nom, age=0):
    if age == 0:
        print("La personne 1 est", nom)
    else:
        print("La personne 1 est", nom, "son age est", age, "ans")
    print("Son nom comporte", len(nom), "lettres")
#afficher_information("nom", 34)

# Le return
# -> le return sert a sortir de la fontion
# -> le return sert aussi a retourner une variable (mais ce n4est pas obligatoire)

print("ich hieße Prince")
img = plt.imread("C:\Users\princ\OneDrive\Images\Captures d’écran\Capture d’écran 2022-08-21 160053.png")
def est_majeur(age):
    # vrai ou faux (True / False
    # si l´age >= 18 retourner True si non retourner False
    if age >= 18:
        return True
    return False

def afficher_information(nom, age=0):
    if nom == "":
        print("Vous n´avez pas donner de nom.")
        return
    if age == 0:
        print("La personne 1 est", nom)
    else:
        print("the first person is", nom, ", son age est", age, "ans")
    print("Son nom comporte", len(nom), "lettres")
    # dans ce cas le print(son nom comporte ne sera plus executer car nous avons demander de sortir de la fonction


afficher_information(nom="Prince", age=16)
print("est majeur:", est_majeur(15))
age = 0
if age != 0:
    exit
else:
    print("")

