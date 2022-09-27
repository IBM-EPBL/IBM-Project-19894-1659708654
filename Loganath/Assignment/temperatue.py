import random
import time
while True:
    temp=random.randint(25,200)
    print(temp,"degree")
    Humidity=random.randint(0,100)
    print("Temperatrure in celsius: " +str(((temp-32)*5)//9)+"℃")
    print("The humidity is",Humidity,"%")
    if (temp>=100):
            print("Temperatrure is high,alarm rings..beep....!!!: "+ str(temp)+"°F")
    time.sleep(5)
