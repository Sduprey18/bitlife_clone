import unittest
from src.person import Player
from src.events import Events

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Player(0,90,0)
        pass

    def testBabyEvents(self) -> None:
        testEvents =  Events(self.person)

        #Test Rand 1, health should go up to 100:
        testEvents.randomEventBaby(rand = 1)
        self.assertEqual(self.person.getHealth(), 100)

        #Test Rand 2, health should still be 100.
        testEvents.randomEventBaby(rand=2)
        self.assertEqual(self.person.getHealth(), 100)

        

        #Test Rand 3, happiness should be 85
        self.person.adjustHappiness(-25)
        testEvents.randomEventBaby(rand=3)
        self.assertEqual(self.person.getHappiness(), 85)

        #Test Rand 4, happiness should be 95
        testEvents.randomEventBaby(rand=4)
        self.assertEqual(self.person.getHappiness(), 95)

        #Test Rand 5, happiness should be 80
        testEvents.randomEventBaby(rand=5)
        self.assertEqual(self.person.getHappiness(), 80)

        #Test Rand 6,  happiness should be 75, health should be 95
        testEvents.randomEventBaby(rand=6)
        self.assertEqual(self.person.getHappiness(), 75)
        self.assertEqual(self.person.getHealth(),95)

        #Test rand 7,happiness should be 80
        testEvents.randomEventBaby(rand=7)
        self.assertEqual(self.person.getHappiness(), 80)

        #test rand 8, health should be 100
        testEvents.randomEventBaby(rand=8)
        self.assertEqual(self.person.getHealth(), 100)

        #test rand 9, happiness should be 73
        testEvents.randomEventBaby(rand=9)
        self.assertEqual(self.person.getHappiness(), 73)

        #test rand 10, health should be 97, happiness should be 70
        testEvents.randomEventBaby(rand=10)
        self.assertEqual(self.person.getHappiness(), 70)
        self.assertEqual(self.person.getHealth(), 97)
        return
    
if __name__ == '__main__':
    unittest.main()