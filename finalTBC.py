import random

class Player(object):
    def __init__(self, name = "Cat Next Door",
               hitPoints = 10,
               hitChance = 50,
               maxDamage = 5,
               armor = 0):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor



    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def hitPoints(self):
        return self.__hitPoints

    @hitPoints.setter
    def hitPoints(self, value):
        if type(value) == int:
            newValue = value
        else:
            newValue = 1
        self.__hitPoints = newValue

    @property
    def hitChance(self):
        return self.__hitChance

    @hitChance.setter
    def hitChance(self, value):
        if type(value) == int:
            if value >= 0:
                if value <= 100:
                    newValue = value
                else:
                    newValue  = 100
            else:
                newValue = 0
        else:
            newValue = 0
        self.__hitChance = newValue

    @property
    def maxDamage(self):
        return self.__maxDamage

    @maxDamage.setter
    def maxDamage(self, value):
        if type(value) == int:
            newValue = value
        self.__maxDamage = newValue

    @property
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, value):
        if type(value) == int:
            newValue = value
        else:
            newValue = 0

        self.__armor = newValue


    def hit(self, enemy):
        
        if random.randint(1, 100) < self.hitChance:
            print(f"{self.name} hits {enemy.name}...")

            damage = random.randint(1, self.maxDamage)
            print(f"  for {damage} points of damage")
            
            print(f"  {enemy.name}'s armor can absorb {enemy.armor} points")
            
            damage -= enemy.armor
            
            if damage < 0:
                damage = 0
            enemy.hitPoints -= damage

class UserPlayer(Player):
    def __init__(self, name = "Knight Justin",
                 hitPoints = 10,
                 hitChance = 50,
                 maxDamage = 5,
                 armor = 0):
        
        super().__init__(name, hitPoints, hitChance, maxDamage, armor)

    

def playerFight(player1, player2):
    keepGoing = True
    userPlaying = False
    while keepGoing:
        if isinstance(player1, UserCharacter):
            userPlaying = True
            player1.chooseAction(player2)
        else:
            player1.hit(player2)

        if isinstance(player2, UserCharacter):
            userPlaying = True
            player2.chooseAction(player1)
        else:
            player2.hit(player1)

        print (f"{player1.name}: {player1.hitPoints} HP")
        print (f"{player2.name}: {player2.hitPoints} HP")
        print()

        if player2.hitPoints <= 0:
            print(f"{player1.name} wins!")
            keepGoing = False
        elif player1.hitPoints <= 0:
            print(f"{player2.name} wins!")
            keepGoing = False
        if userPlaying == False:
            dummy = input("press <ENTER> for another round: ")

def fight(player1, player2):
    keepGoing = True
    while keepGoing:
        player1.hit(player2)
        player2.hit(player1)

        print(f"{player1.name}: {player1.hitPoints}")
        print(f"{player2.name}: {player2.hitPoints}")

        if player2.hitPoints <= 0:
            print(f"{player1.name} wins!")
            keepGoing = False
        elif player1.hitPoints <= 0:
            print(f"{player2.name} wins!")
            keepGoing = False

        dummy = input("Press ENTER for another round...")

def main():


    
    player = Player("Knight Justin")
    enemy = Player("Cat Next Door")

    fight(player, enemy)

    playerFight(player, enemy)


if __name__ == "__main__":
    main()