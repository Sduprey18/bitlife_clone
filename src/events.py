from src.person import Player
import random
class Events:
    def __init__(self,person) -> None:
        self.person = person
        pass

    '''
    What should there be? In b-life there are random events based on age, life status, riches,
    health conditions, relationshsips

    For right now we could maybe add stuff that'll happen to babies, stuff that'll happen randomly,
    all of which could affect our money, health, happiness 
    '''

    def randomEventBaby(self, **kwargs) -> str:

        rand = kwargs.get("rand", random.randint(1, 10))

        match (rand):
            case 1:
                self.person.adjustHealth(10)
                return ("Your mother decides to breastfeed you instead of using formula.")
            case 2:
                self.person.adjustHealth(10)
                return ("Your parents take you to get vaccinated.")
            case 3:
                self.person.adjustHappiness(10)
                return ('You have your first word—it\'s \"mama\" or \"dada.\"')
            case 4:
                self.person.adjustHappiness(10)
                return ('Your parents take you on a family vacation.')
            case 5:
                self.person.adjustHappiness(-15)
                return ("Your father leaves your mother, and they get divorced.")
            case 6:
                self.person.adjustHappiness(-5)
                self.person.adjustHealth(-5)
                return ("You suffer from colic and cry nonstop for weeks.")
            case 7:
                self.person.adjustHappiness(5)
                return ("Your parents take you to a baby playgroup.")
            case 8:
                self.person.adjustHealth(10)
                return ("Your family gets a pet, and it seems to like you!")
            case 9:
                #CHANGE THIS IN THE FUTURE
                self.person.adjustHappiness(-7)
                return("Your older sibling is jealous of you and refuses to acknowledge you.")
            case 10:
                #CHANGE THIS IN THE FUTURE 
                self.person.adjustHealth(-3)
                self.person.adjustHealth(-3)
                return ("Your parents decide to circumcise you (if male)")

        pass
    
