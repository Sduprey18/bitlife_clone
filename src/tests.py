import unittest
from src.person import Player
from src.events import Events

class Test:
    def __init__(self) -> None:
        self.person = Player(0,90,0)
        pass

    def testBabyEvents(self) -> None:
        testEvents =  Events(self.person)

        #Test Rand 1, health should go up to 100:
        testEvents.randomEventBaby(rand = 5)
        self.assertEqual(self.person.getHealth, 100)
        
        pass