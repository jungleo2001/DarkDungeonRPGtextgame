import random

class Player:
    def __init__(self, name, hero_class, hp, attack):
        self.name = name
        self.hero_class = hero_class
        self.hp = hp
        self.attack = attack
        self.defense = 5
        self.gold = 0
        self.inventory = []

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage

    def attack_enemy(self):
        return self.attack + random.randint(-2, 2)

    def heal(self):
        self.hp += random.randint(10, 20)

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def use_item(self, item_name):
        if item_name in self.inventory:
            self.inventory.remove(item_name)
            print("You used {}.".format(item_name))
        else:
            print("You don't have {} in your inventory.".format(item_name))

class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage

    def attack_player(self):
        return self.attack + random.randint(-3, 3)

def main():
    print("Welcome to the Text RPG!")
    player_name, hero_class = create_hero()
    player = create_player(player_name, hero_class)
    print("Welcome, {}, the {} to the Text RPG!\n".format(player.name, player.hero_class))

    while player.is_alive():
        print("You find yourself in a room.")
        print("1. Search the room")
        print("2. View Stats")
        print("3. View Inventory")
        print("4. Exit Game")
        choice = input("Enter your choice: ")

        if choice == '1':
            explore_room(player)
        elif choice == '2':
            print("Name: {}".format(player.name))
            print("Class: {}".format(player.hero_class))
            print("HP: {}".format(player.hp))
            print("Gold: {}".format(player.gold))
        elif choice == '3':
            if player.inventory:
                print("Inventory:")
                for item in player.inventory:
                    print("-", item)
            else:
                print("Your inventory is empty.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

def create_hero():
    print("Create your hero:")
    name = input("Enter your hero's name: ")
    print("Choose your hero's class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    class_choice = input("Enter the number of your choice: ")
    if class_choice == '1':
        hero_class = "Warrior"
    elif class_choice == '2':
        hero_class = "Mage"
    elif class_choice == '3':
        hero_class = "Archer"
    else:
        print("Invalid choice, defaulting to Warrior.")
        hero_class = "Warrior"
    return name, hero_class

def create_player(name, hero_class):
    if hero_class == "Warrior":
        hp = 120
        attack = 12
    elif hero_class == "Mage":
        hp = 80
        attack = 15
    elif hero_class == "Archer":
        hp = 100
        attack = 10
    else:
        print("Invalid hero class, defaulting to Warrior.")
        hp = 120
        attack = 12
    return Player(name, hero_class, hp, attack)

def explore_room(player):
    monster = generate_monster()
    print("You encounter a {}!".format(monster.name))
    while player.is_alive() and monster.is_alive():
        print("\n1. Attack")
        print("2. Flee")
        action = input("Enter your choice: ")

        if action == '1':
            player_attack = player.attack_enemy()
            monster.take_damage(player_attack)
            print("You attack the {} for {} damage.".format(monster.name, player_attack))
            if not monster.is_alive():
                print("You defeated the {}!".format(monster.name))
                player.gold += 50
                item = generate_item()
                player.add_to_inventory(item)
                print("You found {} and added it to your inventory.".format(item))
        elif action == '2':
            if random.random() < 0.5:
                print("You successfully flee!")
                break
            else:
                print("You failed to flee!")
                monster_attack = monster.attack_player()
                player.take_damage(monster_attack)
                print("The {} attacks you for {} damage.".format(monster.name, monster_attack))
        else:
            print("Invalid choice, try again.")

    if not player.is_alive():
        print("You have been defeated. Game Over.")
    else:
        player.heal()
        print("You found a potion and healed yourself!")

def generate_monster():
    monsters = [
        Monster("Goblin", 30, 8),
        Monster("Skeleton", 40, 10),
        Monster("Orc", 50, 12),
        Monster("Dragon", 100, 20)
    ]
    return random.choice(monsters)

def generate_item():
    items = ["Health Potion", "Attack Potion", "Defense Potion"]
    return random.choice(items)

if __name__ == "__main__":
    main()
