class Player:
    def __init__(self,name,health,power):
     self.name = name
     self.health = health
     self.power = power
    
    def attack(self, other_player):
       print(f"{self.name} attacked {other_player}")
        
player1 = Player("Shaktiman",100,100)
player2 = Player("Shakal",80,120)

player1.attack(player2.name)
# Shaktiman attacked Shakal

print(type(player1))
# <class '__main__.Player'>