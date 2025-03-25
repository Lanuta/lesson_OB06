import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)  # Добавляем случайность урона
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютерный Враг")

    def start(self):
        print(f"Начинается битва между {self.player.name} и {self.computer.name}!")

        while self.player.is_alive() and self.computer.is_alive():
            input("Нажмите Enter, чтобы атаковать!")
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен! {self.player.name} победил!")
                break

            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} повержен! {self.computer.name} победил!")
                break

            print(f"{self.player.name}: {self.player.health} HP | {self.computer.name}: {self.computer.health} HP")

        print("Игра окончена!")


# Запуск игры
player_name = input("Введите имя вашего героя: ")
game = Game(player_name)
game.start()