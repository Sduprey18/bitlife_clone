import random

stories = ['I was born in X, and my parents always joke that I was an \'oopsie baby.\' Apparently, I ruined their vacation plans!',
           'I came into this world in X after my mom sneezed so hard she went into labor. They say it’s a family tradition.',
           'I was born in X during a thunderstorm. My dad says it was so dramatic, he thought I was a superhero.',
           'In X, my parents were on a road trip when I decided to make my appearance—right on the side of the highway. Now, every family trip starts with, \'Let’s not repeat that mistake!',
           'I was born in X, but my parents were so unprepared that they didn’t even have a name for me for the first three days.',
           'I was born in X after my parents were told they couldn’t have kids. They were so surprised, they didn’t even have a crib ready—just a laundry basket!',
           'I was born in X, and the doctor delivered me while wearing a Halloween costume because it was a busy day in the maternity ward.',
           'I came into the world in X, but my parents were so late getting to the hospital, I was nearly born in an elevator!',
           'In X, my birth was so unexpected that my parents had to call a taxi to get to the hospital. They didn’t even make it halfway before I arrived!',
           'I was born in X, and apparently, I took so long to arrive that my dad fell asleep in the waiting room and missed my birth!']
class Stories:
    def generateBirth(self, countryName: str) -> str:
        stringToShow = random.choice(stories)
        stringToShow = stringToShow.replace('X', countryName)
        return stringToShow