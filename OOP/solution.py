class character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_character(self):
        print(f'{self.name} attacks with {self.attack} damage!')

warrior = character('Thor', 100, 20)
mage = character('Merlin', 80, 25)

warrior.attack_character()
mage.attack_character()

#OOP solves the problem of code duplication by allowing us to create multiple instances of the character class, each with its own attributes and methods. This makes our code more efficient and easier to maintain.