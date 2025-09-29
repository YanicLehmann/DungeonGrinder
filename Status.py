import time 
import random
import charakterUndGegenerKlassen
import os


def CharStatus():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Die Stats deines deines Charakters sind: \n")
    print(f"HP: {charakterUndGegenerKlassen.characterHero.hp}")
    print(f"Attack: {charakterUndGegenerKlassen.characterHero.attack}")
    print(f"Gold: {charakterUndGegenerKlassen.characterHero.gold}\n")
    exitStatus = input("Verlassen?: ")
    if exitStatus.lower() in ["Ja", "ja", "j", "J"]:
        from main import gameplayMenu
        gameplayMenu() 
