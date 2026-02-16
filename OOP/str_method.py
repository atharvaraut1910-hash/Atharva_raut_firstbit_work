class Player:
    def __init__(self,name,game,jersey_no):
        self.name = name
        self.game = game
        self.jersey = jersey_no

    def __str__(self):
        return f'NAME:{self.name}\nGAME:{self.game}\nJERSEY NO:{self.jersey}'

p1 = Player('Virat','Cricket',18)
print(p1)

#__dict__ attribute
print(p1.__dict__)


