import pygame, simpleGE, finalTBC

pygame.init()


class Player(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("dog.png")
        self.setSize(100,100)
        self.position = (320, 400)
       
        
class UserPlayer(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("evilDog.png")
        self.setSize(100,100)
        self.position = (1020, 400)
    
        

        
              
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("woods.png")
        self.setCaption("D&D TBC")
        self.player = Player(self)
        self.enemy = UserPlayer(self)
        
        self.sprites = [self.player,
                        self.enemy]
            


def main():
    
    hero = finalTBC.Player()
    hero.name = "Knight Justin"
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 2
    
    enemy = finalTBC.Player("Cat Next Door", 20, 30, 5, 0)
    
    finalTBC.fight(hero, enemy)
    
    
main()
if __name__ == "__main__":
    main()