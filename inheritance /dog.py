from animal import *

class Dog(Animal):

    dog_count=0

    def __init__(self,num):
        super().__init__(num)
        __class__.dog_count+=1
        print("dog")
    