class Player:
    def __init__(self,placeOfBirth: str, money: float, health: int, age: int):
        self.health = health
        self.placeOfBirth = placeOfBirth
        self.money = money
        self.age = age
        
    def ageUp(self) -> int:
        self.age +=1 

    def getHealth(self) -> int:
        return self.health
    
    def getMoney(self) -> float:
        return self.money    
    
    def changeMoney(self, newMoney: float) -> float:
        self.money= newMoney
        return self.getMoney
    
    def addMoney(self, newMoney: float) -> float:
        self.money = self.money + newMoney
        return self.money
    
    def adjustHealth(self, healthChange: int) -> int:
        self.health += healthChange

    