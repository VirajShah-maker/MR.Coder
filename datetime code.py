import time
import datetime

a=input("Enter your card number:")
time.sleep(1.35)
if a=="20147":
    tday=datetime.date.today()
    exp=datetime.date(2019,3,1)
    val=exp-tday
    if val<0 :
        print("Your card is invalid")
        
    else :
        print("Your card is valid")
        
if a=="54785":
    tday=datetime.date.today()
    exp=datetime.date(2020,3,0)
    val=exp-tday
    if val<0 :
        print("Your card is invalid")
      
    else :
        print("Your card is valid")
       
        
if a=="85742" :
    now=datetime.datetime.now()
    exp=datetime.datetime(2020,4,1,17,0,0,00)
    val=exp-now
    if val.total_seconds()<0 :
        print("Your card is invalid")
       
    else :
        print("Your card is valid")
       

if a=="54654":
    tday=datetime.date.today()
    exp=datetime.date(2020,4,0)
    val=exp-tday
    if val<0 :
        print("Your card is invalid") 
    else :
        print("Your card is valid")
        


