
while True :
    
    print("1-Addition.")
    print("2-Soustraction")
    print("3-Multiplication")
    print("4-Division")
    print("5-Quiter le programme")
    operation=int(input("Selectionnez une des operations suivantes"))
    print("*******une simple calculatrice : MENU********")
    A=int(input("saisir le premier terme:"))
    B=int(input("saisir le deuxieme terme:"))
    if operation==1:
        print("Le resultat est:",A+B)
    elif operation==2:
        print("Le resultat est:",A-B)
    elif operation==3:
        print("Le resultat est:",A*B)
    elif operation==4:
        if B !=0:
            print("Le resultat est:",A/B)
        else:
            print("la division par 0 est impossible")
    else :
        print("Le resultat est incorrect")
    reponse= input("Veux-tu faire un autre calcul (O/N):")
    if reponse=="N":  
        break  

    