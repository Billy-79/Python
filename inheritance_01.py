#!/usr/bin/env python3


class GameCharacter:
    def __init__(self, name, life):
        self.name = name
        self.life = life


class Player(GameCharacter):
    def attack(self):
        print(self.name + " kicks the enemy.")

class Enemy(GameCharacter):
    def attack(self):
        print(self.name + " breathes fire!")


player1 = Player("Mario", 100)
enemy1 = Enemy("Bowser", 150)


print(player1.name)
print(player1.life)
print(enemy1.name)
print(enemy1.life)


player1.attack()
enemy1.attack()
