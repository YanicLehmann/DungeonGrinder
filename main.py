import time
try:
    def gameplayMenu():
        """
        Displays the main game options and handles user input to navigate between fighting, shopping, checking status, ir exiting the game.
        """

        print("Was willst du als nächstes tun?")
        print("[1] Kämpfen")
        print("[2] Shop")
        print("[3] Status")
        print("[4] Beenden")

        case = int(input("Wähle eine Option: "))

        if case == 1:
            print("Alles klar. Das spiel beginnt. Kämpfe mit Gegnern um Gold zu bekommen.")
            time.sleep(3)
            print("Mit dem Gold kannst du im Schop upgrades kaufen, um deine Leben und deinen Schaden zu erhöhen.")
            time.sleep(4.5)
            print("Viel Glück!!!")
            time.sleep(2.5)
            import charakterUndGegenerKlassen
            enemy = charakterUndGegenerKlassen.Character.enemySelect()
            charakterUndGegenerKlassen.characterHero.fight(enemy, gameplayMenu)
        elif case == 2:
            import Shop
            Shop.shopAuswahl()
        elif case == 3:
            import Status
            Status.CharStatus()
        elif case == 4:
            exit()        
except TypeError:
    print("Ungültige Ausgabe")



        
     

def anfangsStory():
    """
    Displays the main storyline an then starts the game by calling gameplayManu(). 
    """
    name = input("Wie ist dein Name?: ")
    time.sleep(0.05)
    print(f"Willkommen {name} zu Dungeon Grinder.\n")
    time.sleep(3)
    print("Am anfang deiner Geschichte, warst du ein angesehener Held. Furchtlos und Stark.")
    time.sleep(3)
    print("Aber.... auch starke Helden können sterben. Und als ein neuer Feind namens Oryx ins Land kam besiegte er dich...")
    time.sleep(5.5)
    print("Aber die Götter sind gnädig mit dir....")
    time.sleep(3)
    print("Du wirst wiedergeboren. Ganz von Anfang....")
    time.sleep(3)
    print("Nun ist es deine Mission, deine Stärke und deine Leben zu erhöhen.")
    time.sleep(3)
    print("Du startest also schwach")
    time.sleep(3)
    print("Mit 100HP, 1Attack und mit 1000 Gold")
    time.sleep(3)
    print("Das Spiel startet in 5sek")
    time.sleep(5)
    gameplayMenu()

 


def gameMenu():
    """
    Initial menu where the user chooses to start the game, exit or skip the storyline.
    """
    print("Was willst du tun?")
    print("[1] Spiel starten")
    print("[2] Spiel beenden")
    print("[3] Spiel starten und Dialog überspringen")

    case = int(input("Wähle eine Option: "))

    if case == 1:
        anfangsStory()
    elif case == 2:
        print("Danke für's spielen!")
        time.sleep(1)
        exit()
    elif case == 3:
        gameplayMenu()
    else:
        print("Ungültige Ausgabe")

        
def start():
    """
    First function of the game. Displays the welcome message and calls the main menu
    """
    print("Willkommen im Spiel \n")
    time.sleep(1)
    print("Dungeon Grinder \n")
    time.sleep(2)
    gameMenu()


# Ensures the game starts only when file is executed directly, not when imported as a module.
if __name__ == "__main__":
    start()
