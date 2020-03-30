# -*-coding:utf-8 *

import os
from random import randrange # importation du module de génération aléatoire
from math import ceil # permet d'arrondir un chiffre pour qu'il soit toujour entier
import test

#mon algorithme :
def main():
    """Main function."""
    player_wallet = input("indiquez le montant de votre porte-monnaie compris entre 10$ et 1000$:")
    player_wallet = int(player_wallet)
    while player_wallet > 1000 or player_wallet < 10:
        player_wallet = input("montant incorrect, choisissez un portefeuille compris entre 10$ et 1000$ :")
        if not player_wallet.isdigit():
            player_wallet = 0
            continue
        player_wallet = int(player_wallet)

    while player_wallet > 0:
        gain = casino_roulette(player_wallet)
        player_wallet += gain
    
    print("votre porte-monnaie est vide ! merci d'avoir joué !")

def is_player_number_true(player_number):
    return isinstance(player_number, int) and 0 <= player_number < 50

def casino_roulette(player_wallet):
    """this is a one turn on the casino roulette"""
    #créer un input pour que le joueur entre la valeur du chiffre qu'il veut jouer compris entre 0 et 49 
    #player_number = input("choisissez un chiffre compris entre 0 et 49 :")
    #player_number = int(player_number) #le chiffre rentré est reconnu comme un integer
    #ajout d'un message d'erreur si le chiffre donné est < 0 ou > 49
    player_number = -1
    message_base = message = "choisissez un chiffre compris entre 0 et 49 :"
    while not is_player_number_true(player_number):
        # "chiffre incorrect, choisissez un chiffre compris entre 0 et 49"
        
        player_number = input(message)
        try:  
            message = f"erreur: la valeur n'est pas correct, {message_base}"
            player_number = int(player_number)
        except ValueError:
            continue


    #ajout d'un input de la somme qu'il souhaite miser
    player_money = input("combien souhaitez vous miser :")
    player_money = int(player_money) # le chiffre rentré est reconnu comme un integer

    while player_money > player_wallet or player_money < 1:
        player_money = input(f"montant incorrect, entrez une mise comprise entre 1 et {player_wallet} :")
        if not player_money.isdigit():
            continue
        player_money = int(player_money)
        
    # je veux que le programme génère un chiffre aléatoire compris entre 0 et 49
    random_number = randrange(50)
    # la condition est mise dans une boucle while qui se relance tant que la mise de départ n'est pas égale à 0
    gain = 0
    #si le chiffre sorti correspond au chiffre choisie par le joueur, celui ci gagne 3x la somme misé
    if player_number == random_number:
        gain = player_money * 3
    #sinon si juste la couleur est identique au chiffre choisi, le joueur remporte 50% de la sa mise de départ
    elif player_number % 2 == random_number % 2:
        gain = ceil(player_money / 2)
    #autrement si le chiffre sorti n'a rien en commun avec celui misé le joueur de gagne rien

    print("les jeux sont fait, rien ne va plus !")
    print("le chiffre :", random_number, "est sorti, vous avez remporté :", gain, "$")
    return gain - player_money

if __name__ == "__main__":
    main()
