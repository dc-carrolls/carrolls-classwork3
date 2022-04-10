'Main Game Module'
from time import *

class Game:
  'Static Game Class'
  lives :int = 5
  score :int = 0

  @classmethod
  def run(cls, seconds :int):
    'main game method for starting game'
    print('Starting...')
    while cls.lives > -1:
      print('Score:',cls.score,'lives:',cls.lives)
      sleep(seconds)
      cls.lives-=1
      cls.score+=10
    #end while
    print('Game Finished')
  #end procedure
#end class


if __name__ == "__main__":
  Game.run(1)
else:
  print('loading',__name__ ,'as module')
#end if
