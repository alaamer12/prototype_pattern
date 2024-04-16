import copy

class Prototype:
    def clone(self):
        pass

class Character(Prototype):
    def __init__(self, name, health, mana, abilities):
        self.name = name
        self.health = health
        self.mana = mana
        self.abilities = abilities

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.name} - Health: {self.health}, Mana: {self.mana}, Abilities: {', '.join(self.abilities)}"


class CharacterManager:
    def __init__(self):
        self.prototypes = {}

    def register_character(self, name, prototype):
        self.prototypes[name] = prototype

    def create_character(self, name):
        if name in self.prototypes:
            return self.prototypes[name].clone()
        else:
            raise ValueError("Character prototype not found")

def main():
    # Create a character manager
    manager = CharacterManager()

    # Define some initial character prototypes
    warrior = Character("Warrior", 100, 50, ["Slash", "Block"])
    mage = Character("Mage", 80, 100, ["Fireball", "Teleport"])

    # Register the prototypes with the manager
    manager.register_character("Warrior", warrior)
    manager.register_character("Mage", mage)

    # Create new characters based on prototypes
    player1 = manager.create_character("Warrior")
    player2 = manager.create_character("Mage")

    # Output the characters
    print("Player 1:", player1)
    print("Player 2:", player2)

if __name__ == "__main__":
    main()
