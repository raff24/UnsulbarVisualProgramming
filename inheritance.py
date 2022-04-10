class Football:
  def __init__(self, club, country):
    self.club = club
    self.country = country
 
  def printname(self):
    print(self.club, 'From' ,self.country)

class Europe(Football):
  pass

club1 = Europe("Chelsea", "England")
club1.printname()
club1 = Europe("Real Madrid", "Spain")
club1.printname()
