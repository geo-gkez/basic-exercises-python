from animal import *

class Cat():

    cat_count=0
    

    def __init__(self,num):
        Animal.__init__(self,num)
        __class__.cat_count+=1
        print("cat!!! with num: ",self.num)