warrior_name = 'Thor'
warrior_health = 100
warrior_attack = 20

mage_name = 'Merlin'
mage_health = 80
mage_attack = 25

def attack_warrior():
    print('Warrior attacks with', warrior_attack, 'damage!')
def attack_mage():
    print('Mage attacks with', mage_attack, 'damage!')

attack_warrior()
attack_mage()

#the prblm without oop is that we have to create a new function for every new character we create. This is not efficient and can lead to code duplication.