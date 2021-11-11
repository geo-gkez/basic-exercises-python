class Animal:

    count=0

    def __init__(self,num):
        self.num = num
        __class__.count+=1
       
        print("hi I am an animal!!! with num: ",self.num)


        