ga = int(input("geométrique(1) ou arythmétique(2) : "))

if ga == 1:
    SM = int(input(" calculer la somme(1), la moyenne(2) ou une somme de terme(3) : "))
    if SM == 2:
        a = float(input("Entrez le premier terme : "))
        b = float(input("entrez le second terme : "))
        gmoyenne = sqrt(a*b)
        print("la moyenne de la suite geométrique est de", gmoyenne)
    elif SM == 1:
        n = int(input("entrez n :"))
        q = float(input("entrez la raison : "))
        U = float(input("entrez le premier terme :"))
        Qsomme = ((1-(q**(n+1)))/(1-q))*U
        print("la somme de cette suite est", Qsomme)
    elif SM == 3:
        UU = int(input("à partir de U0(1) OU U1(2) : "))
        q = float(input("entrez la raison : "))
        n = int(input("entrez n : "))
        if UU == 1:
            U0 = float(input("entrez la valeur de U0 : "))
            terme0 = U0 * (q**n)
            print(" la valeur pour le terme", n, "est", terme0)
        else:
            U1 = float(input("entrez la valeur de U1 : "))
            terme1 = U1 * (q**(n-1))
            print(" la valeur pour le terme", n, "est", terme1)
else:
    SA = int(input(" calculer la somme(1), la moyenne(2) ou une somme de terme(3) : "))
    if SA == 1:
        a = float(input("entrez le 1er teme : "))
        b = float(input("entrez le 2e terme : "))
        n = int(input(" entrez n : "))
        Ssomme = ((a + b)/2)*(n+1)
        print(" la somme de cette suite est", Ssomme)
    elif SA == 2:
        a = float(input("Entrez le premier terme : "))
        b = float(input("entrez le 2e terme : "))
        Amoyenne = (a+b)/2
        print("la moyenne de la suite est de", Amoyenne)
    elif SA == 3:
        UU = int(input("Voulez vous calculer à partir de U0(1) ou de U1(2)"))
        r = float(input("entrez la raison de la suite : "))
        n = int(input("entrez le terme à calculer"))
        if UU == 1:
            U0 = float(input("entrez U0 :"))
            terme0 = U0 + (r*n)
            print(" la valeur pour le terme", n, "est", terme0)
        else :  
            U1 = float(input("entrez U1 :"))
            terme1 = U1 + (r*(n-1))
            print(" la valeur pour le terme", n, "est", terme1)