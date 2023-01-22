#t=[[3,6,9,0],[6,5,8,2]]
#t=[[-1,3,5,0,0,0,0], [0,1,2,1,0,0,10000], [0,2,3,0,1,0,12000], [0, 1, 4, 0, 0, 1, 15000]]
o=[[3,5,0,0,0,0],[1,2,1,0,0,10000],[2,3,0,1,0,12000],[1,4,0,0,1,15000]]
t=[[-1,1.75,0,0,0,-1.25,-18750],[0,0.5,0,1,0,-0.5,2500],[0,1.25,0,0,1,-0.75,750],[0,0.25,1,0,0,0.25,3750]]
p=[[2,1,0,0,0,0,],[1,5,1,0,0,10],[1,3,0,1,0,6],[1,1,0,0,1,4]]
q=[[-1,240,160,0,0,0],[0,1,2,1,0,150],[0,4,2,0,1,400]]
r=[[3,5,0,0,0,0],[1,2,1,0,0,10000],[2,3,0,1,0,12000],[1,4,0,0,1,15000]]
#Fonction de determination de l'element pivot
def pivot(matrice_initiale):
    # Identification de la colonne pivot
    colonne_pivot=matrice_initiale[0].index(max(matrice_initiale[0]))
    #...................................
    #tableau permettant de sauvegarder les resultats des calculs : element solution/element de la colonne pivot
    save_tab=[]
    #...................................
    # calacul de : element solution/element de la colonne pivot
    for line in range(len(matrice_initiale)):
        if matrice_initiale[line][colonne_pivot]!=0:
            save_tab.append((matrice_initiale[line][len(matrice_initiale[line])-1])/matrice_initiale[line][colonne_pivot])
        else:
            save_tab.append("infini")
    #...................................
    # determination du minimum de save_tab
    minimum_save_tab=save_tab[1]
    for line in range(1,len(save_tab)):
        if save_tab[line]!="infini" :
            if save_tab[line]<=minimum_save_tab:
                minimum_save_tab=save_tab[line]
    #...................................
    #deduction de la ligne pivot a partir du minimum de save_tab
    ligne_pivot=save_tab.index(minimum_save_tab)
    #...................................
    return (colonne_pivot,ligne_pivot)
print(pivot(t))
#.......................................
#Fonction permettant de passer a la matrice suivante apres determintion de l'element pivot
def resoudre(matrice_courante,colonne_pivot,ligne_pivot):
    #element pivot
    element_pivot=matrice_courante[ligne_pivot][colonne_pivot]
    #...................................
    #calcul des element de la matrice suivante sans les elements de la ligne pivot
    matrice_suivante=[[0 for line in range(len(matrice_courante[0]))] for colonne in range(len(matrice_courante))]
    for line in range(len(matrice_courante)):
        for colonne in range(len(matrice_courante[line])):
            matrice_suivante[line][colonne]=matrice_courante[line][colonne]-((matrice_courante[line][colonne_pivot]*matrice_courante[ligne_pivot][colonne])/element_pivot)
    #...................................
    #calcul des elements de la ligne pivot de la matrice suivante
    matrice_suivante[ligne_pivot]=[(matrice_courante[ligne_pivot][line])/element_pivot for line in range(len(matrice_courante[ligne_pivot]))]
    #...................................
    return matrice_suivante
#.......................................
#Fonction Simplexe
def simplexe0(matrice_initiale,save_ecrasement):
    #recuperation des coordonnes du pivot de la matrice en cours de traitement
    coord_pivot=pivot(matrice_initiale)
    #...................................
    #sauvegarde des ecrasements de variable de la colonne et de la ligne pivot precedent
    save_ecrasement.append(coord_pivot)
    #...................................
    #determination de la matrice suivante
    matrice_suivante=resoudre(matrice_initiale,coord_pivot[0],coord_pivot[1])
    #...................................
    #verification de la condition d'arret
    if max(matrice_suivante[0])>0:
        return simplexe0(matrice_suivante,save_ecrasement)
    else:
        return (matrice_suivante,save_ecrasement)
#.......................................
#gestion des solutions
def solution(matrice_initiale):
    #determination de la matrice finale
    matrice_finale=simplexe0(matrice_initiale,[])
    #...................................
    #deduction des solutions dans la matrice finale
    matrice_solution=[matrice_finale[0][i][len(matrice_finale[0][i])-1] for i in range(len(matrice_finale[0]))]
    #...................................
    #matrice des variables ayant une valeur non nulle
    matrice_variables=["e"+str(i+1) for i in range(len(matrice_finale[0])-1)]
    matrice_variables.insert(0,"Z")
    #...................................
    for line in range(len(matrice_finale[1])):
        matrice_variables[matrice_finale[1][line][1]]="x"+str(matrice_finale[1][line][0]+1)
    return (matrice_variables,matrice_solution)
#.......................................
#print(pivot(p))
#print(simplexe0(t,[]))
#print(simplexe0(q,[]))
print(solution(o))

