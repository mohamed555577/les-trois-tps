tb=input("saisir type d'abonné")
qt=int(input("saisir la quantité consommée"))
match tb:
    case "R":
        if qt<=150:
          factur=1.20*qt
        else:
          factur=1.50 *qt
    case "c":
       if (qt*2) <100:
         factur=100
       else:
         factur=qt*2
         
    case "i":
       if qt<=500:
        factur=2.50*qt
       else:
        factur=2*qt
print("factur est",factur)
       