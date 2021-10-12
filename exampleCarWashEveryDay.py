from datetime import date

def washCar(money:int):
    today = date.today()
    day=int(today.strftime("%d"))
    
    countDay=0
    while money >=1:
        if day%2 == 0:
            money=money-1
           
        else:
            if money>=2:
                money=money-2
            else:
                break    

        print('count: {}, money: {} '.format(day,money))    
        day+=1
        countDay+=1
        
        

    print('you can wash your car for {} days on the row.'.format(countDay))

try:  
    money = int(input('Enter money you want to spend: '))
    washCar(money)
except:
    print('Insert integer ...')


