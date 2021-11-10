class Dog:
  def __init__(self):
    self.sound = "woof"

  def noise(self):
    print(self.sound)

class Cow:
  def __init__(self):
    self.sound = "moo"

  def noise(self):
    print(self.sound)

animals = []
animals.append(Dog())
animals.append(Cow())
for animal in animals:
  animal.noise()


