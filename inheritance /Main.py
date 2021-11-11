from cat import *
from dog import *


class Main:
  dog = Dog(1)
  dog2 = Dog(2)
  dog3 = Dog(3)
  animal = Animal(10)
  animal2 = Animal(11)
  print("dog.count: ",dog.count)
  print("animal.count: ",animal.count)
  cat = Cat(20)
  cat2 = Cat(21)
  print("dog.dog_count: ",dog.dog_count)
  print("dog.count: ",dog.count)
  print("animal.count: ",animal.count)
  print("animal.num: ",animal.num)
  print("cat.cat_count:",cat.cat_count)
  print("cat.num:",cat.num)

  ### you can not use cat.count because the Class Cat can not access static attribute from Animal Class??
 