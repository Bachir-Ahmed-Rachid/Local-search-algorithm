
                                                       # Projet n°2 ICL - Recherche locale








#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                    Création de la fonction qui permets d ordonnancer les taches
#                                                    de manière à respecter les dates de disponibilité tout en minimisant
#                                                    le retard maximum et amélioration de la solution trouver :

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------


def Heuristique_constructive_et_Recherche_locale(n,r,p,d):  #tel que: n:Les taches
                                                            #r:Date de disponibilité
                                                            #p:Temps de traitement
                                                            #d:Date échue de tache
    
#                               --------------------------------------------------------------------------------------------------

#                                                   PARTIE 1: Construit une solution réalisable à partir
#                                                               des paramètres du problème

#                               --------------------------------------------------------------------------------------------------

#     Déclaration des vecteur et valeurs vides:
    r1=[]
    n1=[]
    c=[0]*len(n)
    t=[0]*len(n)
    T=[0]*len(n)
    valeur_intermediare1=0
    valeur_intermediare2=0
    
#    On crée une copie pour chaque vecteur de la date de disponibilité et vecteur de taches:
    
    for i in range(len(n)):
        r1.append(r[i])
        n1.append(n[i])
        
#    Modification du vecteur de taches et de Date de disponibilité tel que
#     les Date de disponibilité sont dans l'ordre croissant:
        
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if(r[i] > r[j]):
                valeur_intermediare2=r[j]
                r[j]=r[i]
                r[i]=valeur_intermediare2
                valeur_intermediare1=n[j]
                n[j]=n[i]
                n[i]=valeur_intermediare1
    o=n

    #Remplissage du vecteur de la date de début de traitement des tâche i (le vecteur t):
    t[o[0]-1]=r1[o[0]-1]
    for k in range(1,len(n)):
        if(r1[o[k]-1]>t[o[k-1]-1]+p[o[k-1]-1]):
            t[o[k]-1]=r1[o[k]-1]
        else:
            t[o[k]-1]=t[o[k-1]-1]+p[o[k-1]-1]

    #Remplissage du vecteur de dates de complétion et les retards c et T:       

    for i in range(len(n)):
        c[i]=t[i]+p[i]
        if(c[i]-d[i]<=0):
            T[i]=0
        else:
            T[i]=c[i]-d[i]

            
    #Calcule du retard maximum Tmax:

            
    Tmaxe=T[0]
    
    for i in range(len(T)):
        if(Tmaxe<T[i]):
            Tmaxe=T[i]
     #La solution realisable obtenue :
            
    print("La solution realisable obtenue :")        
    print('i       ', end='')
    for i in range(len(n)):
        print(n1[i]," ", end='')
    print("                   ")
    print("----------------------------------")
    print('o[k]    ', end='')
    for i in range(len(n)):
        print(o[i]," ", end='')
    print("                   ")
    print("----------------------------------")
    print('t[i]    ', end='')
    for i in range(len(n)):
        print(t[i]," ", end='')
    print("                   ")
    print('c[i]    ', end='')
    for i in range(len(n)):
        print(c[i]," ", end='')
    print("                   ")
    print('T[i]    ', end='')
    for i in range(len(n)):
        print(T[i]," ", end='')
    print("                   ")
    print('Le retard maximum est:',Tmaxe)
    print("                   ")



#                               --------------------------------------------------------------------------------------------------

#                                                   PARTIE 2: Recherche locale
#                                                               amélioration de la solution obtenue tant que possible
#                                                               jusqu’à arriver à un minimum local

#                               --------------------------------------------------------------------------------------------------







#   Création de la fonction qui fait une copie sur les vecteurs
    def creation_copie_vecteur(vect):
        copie_vecteur=[0]*len(vect)
        for i in range(len(vect)):
                copie_vecteur[i]=vect[i]
        return(copie_vecteur)
        

    
    
    amelioration=True
    while(amelioration==True):
        Tmaxe_nouvaux=Tmaxe
        amelioration=False
#      Recherche de la tâche qui possède le plus grand retard
        K=0
        for i in range(len(T)):
            if(Tmaxe==T[i]):
                K=i
        tache_de_retard_max=o[K]
        
#       Chercher les taches qui précèdent la tâche qui possède le retard maximum:

        for l in range(K):
            
#            créer des copies de: o,t,c,T:

            o_bar=creation_copie_vecteur(o)
            t_bar=creation_copie_vecteur(t)
            c_bar=creation_copie_vecteur(c)
            T_bar=creation_copie_vecteur(T)
            
#           replacement de la tâche o[k] à la position l et décaler les
#           tâches o[l], . . . , o[k − 1] d’une case vers la droite dans la copie o_bar:

            for j in range(K,l-1,-1):
                o_bar[j]=o_bar[j-1]
            o_bar[l-1]=tache_de_retard_max
            

#           recalcule Des composantes dU tableaux t,c et T 
#           à partir de l et les calculs sont effectués dans les copies: o_bar,t_bar,T_bar :

            t_bar[o_bar[0]-1]=r1[o_bar[0]-1]
            for k in range(1,len(n)):
                if(r1[o_bar[k]-1]>t_bar[o_bar[k-1]-1]+p[o_bar[k-1]-1]):
                    t_bar[o_bar[k]-1]=r1[o_bar[k]-1]
                else:
                    t_bar[o_bar[k]-1]=t_bar[o_bar[k-1]-1]+p[o_bar[k-1]-1]
                    
            for i in range(len(n)):
                c_bar[i]=t_bar[i]+p[i]
                if(c_bar[i]-d[i]<=0):
                    T_bar[i]=0
                else:
                    T_bar[i]=c_bar[i]-d[i]

#           Calcule du nouveaux retard maximum:

            Tmaxe_bar=T_bar[0]
            for i in range(len(T_bar)):
                if(Tmaxe_bar<T_bar[i]):
                    Tmaxe_bar=T_bar[i]

                  
            if(Tmaxe_bar<Tmaxe_nouvaux):
                
#               Mise à jour du t,c,T et l’entier Tmaxe_nouvaux;

                for i in range(len(n)):
                    t[i]=t_bar[i]
                    c[i]=c_bar[i]
                    T[i]=T_bar[i]
                Tmaxe_nouvaux=Tmaxe_bar

#       Vérifier si on peut améliorer la solution obtenue ou non et mise a jour de Tmax et o[i]:  

                
        if Tmaxe_nouvaux<Tmaxe:
            for i in range(len(n)):
                o[i]=o_bar[i]
            amelioration=True
            Tmaxe=Tmaxe_nouvaux
            
            
                
                    
#   Amélioration de la solution:
    print("----------------------------------------------------------")
    print("                             ")
    print("Amélioration de la solution:")                
    print('i        ', end='')
    for i in range(len(n)):
        print(n1[i]," ", end='')
    print("                   ")
    print("----------------------------------")
    print('o_bar[k] ', end='')
    for i in range(len(n)):
        print(o[i]," ", end='')
    print("                   ")
    print("----------------------------------")
    print('t_bar[i] ', end='')
    for i in range(len(n)):
        print(t[i]," ", end='')
    print("                   ")
    print('c_bar[i] ', end='')
    for i in range(len(n)):
        print(c[i]," ", end='')
    print("                   ")
    print('T_bar[i] ', end='')
    for i in range(len(n)):
        print(T[i]," ", end='')
    print("                   ")
    print('Le retard maximum amélioree est:',Tmaxe)
    
        
        
            
        
        
            
            
    
    



    



#Etude de cas:
n=[1,2,3,4,5,6,7]
r=[2,5,4,0,0,8,9]
p=[3,6,8,4,2,4,2]
d=[10,21,15,10,5,15,22]
Heuristique_constructive_et_Recherche_locale(n,r,p,d)



    
    


        


        
    
    
    
    

