import pygame
import simpleGE
import random
import finalTBC


black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()



class Hero(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("dog.png")
        self.setSize(100,100)
        self.position = (300, 400)
        
             
             
class Enemy(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("evilDog.png")
        self.setSize(100,100)
        self.position = (1020, 400)
        
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        screen = pygame.display.set_mode((1400, 600))
        self.setImage("woods.png")
        self.setCaption("D&D TBC")
        self.hero = Hero(self)
        self.enemy = Enemy(self)
        
        
        self.sprites = [self.hero,
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
    
    game = Game()
    game.start()
    
    
    
main()
if __name__ == "__main__":
    main()