import random

locations = ['America', 'China', 'Japan', 'Trinidad', 'Bangladesh', 'Zimbabwe']
class Player:

    
    def __init__(self, money: float, health: int, age: int):
        self.health = health
        self.placeOfBirth = random.choice(locations)
        self.money = money
        self.age = age
        self.happiness = 100
    
    def getPlaceOfBirth(self):
        return self.placeOfBirth
    
    def ageUp(self) -> int:
        self.age +=1 
    
    def getAge(self) -> int:
        return self.age

    def getHealth(self) -> int:
        return self.health
    
    def getMoney(self) -> float:
        return self.money   
    
    def changeMoney(self, newMoney: float) -> float:
        self.money= newMoney
        return self.getMoney
    
    def getHappiness(self) -> None:
        return self.happiness

    
    def addMoney(self, newMoney: float) -> float:
        self.money = self.money + newMoney
        return self.money
    
    def adjustHealth(self, healthChange: int) -> None:
        if self.health + healthChange <= 100:
            self.health += healthChange
        else:
            self.health = 100
    
    def adjustHappiness(self, happinessChange: int) -> None:
        if self.happiness + happinessChange <= 100:
            self.happiness += happinessChange
        else:
            self.happiness = 100




    