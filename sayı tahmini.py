from random import randint, random


bakiye = int(input("yatırılan para"))
bahis = int(input("oynamak istediğiniz miktarı giriniz"))
hak = 3
rand = randint(0,9)
while True:

    sayı = random.randit(0,9)

    tahmin = input("bir sayı giriniz")

    hak -=  1
     
    if sayı == tahmin:
        bahis * 2 + bakiye
        print ("kazandınız")
        print(bakiye, hak )
        print(sayı)
        
    else:
        bakiye -= bahis 
        print("kaybettiniz")
        print(bakiye , hak )
        print(sayı)

    if hak == 0:
        print("oyun bitti")
        break
        
        
    



