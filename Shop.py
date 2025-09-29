import pprint
import time
import main

def shopAuswahl():
        """
        Handles the shop logic based on user input.
        Displays available items, processes purchases, and updates the hero's stats.

        """


        # Generates a dictionary containing shop items: a sword and amor, each with price and stat bonuses
        shop = {
            "Schwert" : {"preis" : 100, "plusSchaden" : 10},
            "Rüstung" : {"preis" : 100, "plusLeben" : 10}
            }



        for key, value in shop.items():
            print(f"{key}: kostet {value['preis']} Gold", end="")
            if "plusSchaden" in value:
                print(f", gibt +{value['plusSchaden']} Schaden")
            elif "plusLeben" in value:
                print(f", gibt +{value['plusLeben']} Leben")
            elif "Gehe zurück zum Menü!" in value:
                 print(f"{value['Gehe zurück zum Menü!']}")
        """Displays the shop items with their prices and bonuses in a readable format."""


        select = input("Welches Item willst du kaufen? 'Nichts' bringt dich zurück ins Menü: ")

        if select.lower() in ["Schwert", "schwert"]:
            swordSelect = input("Du willst also das Schwert kaufen? Bist du dir sicher? Es kostet 100 Gold Ja/Nein: ")
            if swordSelect.lower() in ["Ja", "ja", "j", "J"]:
                from charakterUndGegenerKlassen import characterHero
                characterHero.gold -= 100
                characterHero.attack += 10
                print("Super, dein Held hat jetzt plus 10 Schaden!!")
                print(f"Du machst jetzt bei jedem Schlag {characterHero.attack} Schaden")
                print(f"Du hast jetzt noch {characterHero.gold} Gold!!")
                anotherItem1 = input("Willst du noch ein Item kaufen?")
                if anotherItem1.lower() in ["Ja", "ja", "j", "J"]:
                    shopAuswahl()
                else:
                     main.gameplayMenu()
        elif select.lower() in ["Rüstung", "rüstung"]:
            armorSelect = input("Du willst also die Rüstung kaufen? Bist du dir sicher? Sie kostet 100 Gold Ja/Nein: ")
            if armorSelect.lower() in ["Ja", "ja", "j", "J"]:
                from charakterUndGegenerKlassen import characterHero
                characterHero.gold -= 100
                characterHero.hp += 10
                print("Super, dein Held hat jetzt plus 10 Leben!!")
                print(f"Du hast jetzt insgesammt {characterHero.hp} HP")
                print(f"Du hast jetzt noch {characterHero.gold} Gold!!")
                anotherItem = input("Willst du noch ein Item kaufen?")
                if anotherItem.lower() in ["Ja", "ja", "j", "J"]:
                     shopAuswahl()
                else:
                    main.gameplayMenu()
        elif select.lower() in ["Nichts", "nichts"]:
             print("Okay du kommst wieder zurück zum Menü")
             time.sleep(2)
             main.gameplayMenu()
        else:
             main.gameplayMenu()
        """
        Handles the shop logic based on user input. Updates the hero's attributes (attack or hp) depending in the purchased item.
        Imports the hero object from charakterUndGegenerKlassne.py to apply changes.
        """