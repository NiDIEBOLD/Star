
#L'objectif de ce programme est de print un pattern specifique préparé a l'avance.
#Il y a également l'option de produire un pattern de taille supérieur si requis.
#Le code ci-dessous serra en Python

#Création du pattern manuellement via une liste un ensemble de liste, complété de 0 a 7, pour signifier toutes les conditions d'adjacences différentes.

def Star(multiple):
    
    if multiple > 0:

        a = [0,0,0,2,0,0,0,0]
        b = [3,4,1,0,4,4,5,0]
        c = [0,5,0,0,0,6,0,0]
        d = [4,4,6,0,7,4,1,0]
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
        
        number_cols = 8*multiple
        number_rows = 6*multiple
        
        List = [[0] * number_cols for i in range(number_rows)]
        
        #for x in range(len(List)) :
            #print(List[x])
                    
        # Utilisation de la Liste pour remplir la List("","*")
        Valide = [1,2,3,4,5,6,7]
        
        for i in range(len(Liste)) : 
            for j in range(len(Liste[i])) : 
                if Liste[i][j] == 0:
                    List[i*multiple][j*multiple] = " "
                
                if Liste[i][j] in Valide:
                    List[i*multiple][j*multiple] = "*"                    
                
                    #Complétion des adjacences, en loop en cas de multiple > 1

                    if Liste[i][j] == 2:
                        for x in range(multiple) :
                            List[(i*multiple)+x][(j*multiple)+x] = "*"
                            List[(i*multiple)+x][(j*multiple)-x] = "*"

                    if Liste[i][j] == 3:
                        for x in range(multiple) :
                            List[(i*multiple)+x][(j*multiple)+x] = "*"
                            List[(i*multiple)][(j*multiple)+x] = "*"
                    
                    if Liste[i][j] == 4:
                        for x in range(multiple) :
                            List[(i*multiple)][(j*multiple)+x] = "*"
                    
                    if Liste[i][j] == 5:
                        for x in range(multiple) :
                            List[(i*multiple)+x][(j*multiple)-x] = "*"
                    
                    if Liste[i][j] == 6:
                        for x in range(multiple) :
                            List[(i*multiple)+x][(j*multiple)+x] = "*"

                    if Liste[i][j] == 7:
                        for x in range(multiple) :
                            List[(i*multiple)][(j*multiple)+x] = "*"
                            List[(i*multiple)+x][(j*multiple)-x] = "*"

        # Nettoyage de List, remplacement des 0 par du vide
                              
        for i in range(len(List)) : 
            for j in range(len(List[i])) :
                if List[i][j] == 0:
                    List[i][j] = " "   

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

#Lancement de la fonction, semble fonctionner sous toutes les conditions requises

Star(5)

#La bonne journée à vous
