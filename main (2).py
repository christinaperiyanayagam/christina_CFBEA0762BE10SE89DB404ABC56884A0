# Define the base class player
class player:
  def play(self):
    print("The player is playing cricket.")
    
class Batsman(player):
  def play(self):
    print("The batsman is batting.")

class Bowler(player):
  def play(self):
    print("The bowler is bowling.")

Batsman= Batsman()
bowler= Bowler()
Batsman.play()
bowler.play()