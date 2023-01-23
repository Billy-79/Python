#!/usr/bin/env python3


class GameCharacter:
    def __init__(self, name, life):
        self.name = name
        self.life = life

    def attack(self):
        print(self.name + " kicks the enemy.")

    def life_check(self):
        if self.life <= 0:
            print(self.name + " was defeated.")
        else:
            print(self.name + " is still in the fight.")


class GameEnemy:
    def __init__(self, name, life):
        self.name = name
        self.life = life

    def attack(self):
        print(self.name + " attacks the heroes!")

    def life_check(self):
        if self.life <= 0:
            print(self.name + " was defeated.")
        else:
            print(self.name + " is still in the fight.")


player1 = GameCharacter("Roger", 100)
player2 = GameCharacter("Betty", 100)
enemy1 = GameEnemy("Bill", 150)
enemy2 = GameEnemy("Bob", 150)


player1.attack()
enemy1.life -= 50
print("Bill takes 50 damage, and has " + str(enemy1.life) + " life remaining.")
enemy1.life_check()

player2.attack()
enemy2.life -= 100
print("Bob takes 100 damage, and has " + str(enemy2.life) + " life remaining.")
enemy2.life_check()

player1.attack()
enemy2.life -= 50
print("Bob takes 50 damage, and has " + str(enemy2.life) + " life remaining.")
enemy2.life_check()

