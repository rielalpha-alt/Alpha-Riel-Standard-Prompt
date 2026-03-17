# ---------------------------------------------------------
# © 2026 Alpha Riel. Tous droits réservés. [cite: 1, 2]
# Ce modèle reste toujours sous licence de Alpha Riel. [cite: 2]
# ---------------------------------------------------------

def main():
    # Définition de l'auteur
    auteur = "Alpha Riel"

    # Remplissage de donnée (Inputs)
    titre = input("Entrer un titre : ")
    version = input("Entrer une version : ")
    role = input("Décrivez un role : ")
    service = input("Ecrire un service : ")
    apropos = input("Décrivez vos apropos : ")
    editeur = input("Entrer votre nom d'editeur : ")
    arriereplan = input("Entrer la propriété design : ")
    theme = input("Entrer le theme : ")

    # Résultat de donnée (Outputs)
    print("\n------------------------------------------")
    print("Votre instruction de programmation est le suivant :")
    print(f"Titre : {titre}")
    print(f"Version : {version}")
    print(f"Caractéristique : {role}")
    print(f"Service : {service}")
    print(f"A propos : {apropos}")
    print(f"Editeur : {editeur}")
    print(f"Arriere plan : {arriereplan}")
    print(f"Thème : {theme}")

    print(f"\nCe programme est édité par le prompt pour AI de l'utilisateur : {editeur}")
    print(f"Mais reste toujours licencié par : {auteur}")

if __name__ == "__main__":
    main()
