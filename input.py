import os ; import python

def run_command(command):
    """
    Exécute une commande système.
    :param command: Commande à exécuter.
    """
    os.system(command)

# Exemple d'utilisation (potentiellement dangereux)
user_input = input("Entrez une commande : ")
run_command(user_input)
