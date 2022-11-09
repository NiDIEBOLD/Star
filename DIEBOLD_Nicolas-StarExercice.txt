
#L'objectif de ce programme est de print un pattern specifique préparé a l'avance.
#Il y a également l'option de produire un pattern de taille supérieur si requis.
#Le code ci-dessous serra en Python

#Création du pattern manuellement via une liste un ensemble de liste, complété en 1 et 0.

def Star(multiple):
    
    if multiple > 0:

        a = [0,0,0,1,0,0,0,0]
        b = [1,1,1,0,1,1,1,0]
        c = [0,1,0,0,0,1,0,0]
        d = [1,1,1,0,1,1,1,0]
        e = [0,0,0,1,0,0,0,0]
        f = [0,0,0,0,0,0,0,0]
        
        # Rassemblement des listes en une liste à double dimension.
        
        Liste = [a]+[b]+[c]+[d]+[e]+[f]
        #for x in range(len(Liste)) :
            #print(Liste[x])
        
            
        #Exemple de print de la liste et présentation du pattern initial
        
        #for i in range(len(Liste)) : 
            #for j in range(len(Liste[i])) : 
                #print(Liste[i][j], end=" ")
            #print()    
       
       #Création d'une liste vide en fonction du multiple, legerment surdimensionné pour limiter les problèmes d'index out of range
        
        number_cols = 9*multiple
        number_rows = 7*multiple
        
        List = [[0] * number_cols for i in range(number_rows)]
        
        #for x in range(len(List)) :
            #print(List[x])
                    
        # Utilisation de la Liste (1,0) pour remplir la List("","*")
        
        
        for i in range(len(Liste)) : 
            for j in range(len(Liste[i])) : 
                if Liste[i][j] == 0:
                    List[i*multiple][j*multiple] = " "
                    List[(i*multiple)+1][(j*multiple)] = " "
                    List[(i*multiple)][(j*multiple)+1] = " "
                    List[(i*multiple)+1][(j*multiple)+1] = " "
                
                if Liste[i][j] == 1:
                    List[i*multiple][j*multiple] = "*"
                    List[(i*multiple)+1][(j*multiple)] = " "
                    List[(i*multiple)][(j*multiple)+1] = " "
                    List[(i*multiple)+1][(j*multiple)+1] = " "
                    
                    if Liste[i][j+1] == 1:
                        List[i*multiple][j*multiple+1] = "*"
        
                    if Liste[i+1][j-1] == 1:
                        List[i*multiple+1][j*multiple-1] = "*"
                    
                    if Liste[i+1][j+1] == 1:
               		    List[i*multiple+1][j*multiple+1] = "*"
                    
                #for x in range(len(List)) :
                    #print(List[x])
                #print()
                
        #for x in range(multiple):
            #print()
           	        
        #Print en liste
        
        #for x in range(len(List)) :
            #print(List[x])
        
        #Print final
        
        print("------------------"*multiple)
        for i in range(len(List)) : 
            for j in range(len(List[i])) : 
                print(List[i][j], end=" ")
            print()   

#Lancement de la fonction, fonctionne au moins partiellement pour 0,1 et 2

Star(2)

#A ce point, j'ai arreté de modifier le code pour ne pas dépasser l'heure imposée, uniquement quelques ajustements de commentaires dont celui ci.
#Quelques manque par rapport à l'attente finale : 
#-Encore quelques boucles à ajouter pour le fonctionnement des multiples au delà de 2
#-L'etoile en multiple de 2 à 4 points supplémentaires par rapport à la demande, par la detection d'adjacence necessitant quelques ajustements supplémentaires
#-Un ajustement necessaire pour traiter le surdimensionnement de List et l'apparence des 0 en bordures

#La bonne journée à vous







