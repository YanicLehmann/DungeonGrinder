import random
import time

class Character:
    def __init__(self, name, hp, attack, gold, goldDrop):
        """This class defines a character with attributes used to create hero and enemy objects."""
        self.name = name    
        self.hp = hp    
        self.attack = attack    
        self.gold = gold    
        self.goldDrop = goldDrop    
    
    @staticmethod # Genutzt für eine methode einer Klasse die keine Daten der Klasse benötigt.
    def enemySelect():
        """Selects a random enemy from a predefined list and returns it. Also prints a spawn message."""
        enemy_list = [enemyGoblin, enemyOgre, enemyWitch, enemyKnight]
        enemy = random.choice(enemy_list)
        print(f"Ein {enemy.name} ist gespawnt, nutze deine Attacke um ihn/sie zu töten")
        return enemy


    def fight(self, enemy, returnToMenu):
        """
        Simulates a battle between the hero and a randomly selected enemy. 
        The player can choose to attack or flee. The battle proceeds in turns. 
        """
        attackOrNot = input(f"Willst du eine Attacke benutzen, oder fliehen? Deine Attacke macht zurzeit {self.attack} Schaden: ")
        if attackOrNot.lower() in ["Angreifen", "angreifen", "Ja", "ja", "j"]:
            enemy.hp -= self.attack
            print(f"Du hast {enemy.name} angegriffen, und hast {self.attack} Schaden gemacht. Der Gegner hat jetzt noch {enemy.hp} Leben.")
            self.hp -= enemy.attack
            time.sleep(0.5)            
            print(f"Der Gegner greift jetzt an und macht {enemy.attack} Schaden. Du hast jetzt noch {self.hp}")
            time.sleep(0.5)
            continue2_ = input(f"Du hast jetzt die Möglichkeit wieder anzugreifen oder zu fliehen. Was willst du tun? Schreibe 'angreifen' oder 'fliehen'")
            if continue2_.lower() in ["Angreifen", "angreifen", "Ja", "ja"]:
                characterHero.fight(enemy, returnToMenu)
            else:
                print(f"Du bist geflohen und der Gegner hatte noch {enemy.hp}. Du hast den kampf verloren und kein Gold bekommen")
                time.sleep(2)
                returnToMenu()
        else: 
            print(f"Du bist geflohen und der Gegner hatte noch {enemy.hp}. Du hast den kampf verloren und kein Gold bekommen")
            time.sleep(2)
            returnToMenu()

#Create the hero character with initial stats            
characterHero = Character("Spieler", 100, 1, 1000, 0)

# Create enemy characters with different stats
enemyGoblin = Character("Goblin", 100, 1, 0, 24)
enemyOgre = Character("Oger", 500, 10, 0, 83)
enemyWitch = Character("Hexe", 350, 7.5, 0, 52)
enemyKnight = Character("Knight", 175, 5, 0, 35 )

"""
Ensures that the code below only runs when this file is executed directly,
not when imported as a module.
"""
if __name__ == "__main__":
    """This is used to put the random choosen enemy that is returned out of the enemySelect method in a variable to use it in other methods."""
    """If that's not given you can't use the random choosen enemy in other Methods."""

    # Select a random enemy and store it for use in the fight 
    enemy = Character.enemySelect()

 













