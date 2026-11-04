jour=int(input("jour:"))
mois=int(input("mois:"))
année=int(input("année:"))
if mois <1 or mois>12 or jour <1:
    print("date invalide")
elif mois in (1,3,5,7,8,10):
  if  jour<31:
    jour=jour + 1
    print(jour,mois,année)
  elif jour == 31:
    jour=1
    mois=mois+1
    print(jour,mois,année)
elif mois ==12 and jour == 31:
    jour=1
    mois=1
    année=année+1
    print(jour,mois,année)
elif (mois in (4,6,9,11) )and( jour>=1 and jour<30):
    jour=jour +1
    print(jour,mois,année)
elif jour==30:
        jour=1
        mois=mois+1
        print(jour,mois,année)
elif mois==2 and année%400==0 and jour >=1 and jour<29 :
    print(jour,mois,année)
elif jour==29:
        jour=1
        mois=mois+1
        print(jour,mois,année)
elif mois ==2 and année%400!=0 and jour>=1 and jour<28:
     jour=jour+1
     print(jour,mois,annéé)
elif jour==28:
       jour=1
       mois=mois+1
       print(jour,mois,année)
    


    