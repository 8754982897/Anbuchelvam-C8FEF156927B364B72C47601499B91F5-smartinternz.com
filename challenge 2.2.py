'''Implement a class player that represents a cricket player.The player class should have method play()
prints "The player is paying cricket."
Derived two class,batsman and bowler from player override the play() method print" the batsman is batting" and"the bowler is bowling"
batsman and bowler classes and call the play() method for each object'''
#Define the base class player
class player:
  def play(self):
    print("The player is playing cricket.")
#Define the derived class Batsman
class Batsman(player):
  def play(self):
    print("The batsman is batting.")
#Define the derived calss Bowler
class Bowler(player):
  def play(self):
    print("The bowler is bowling.")
#create objects of Batsman and Bowler classes
batsman=Batsman()
bowler=Bowler()
#call the play() method for each object
batsman.play()
bowler.play()
