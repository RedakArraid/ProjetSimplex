t=[[3,5,0,0,0,0],[1,2,1,0,0,10000],[2,3,0,1,0,12000],[1,4,0,0,1,15000]]
mat=[]
def element_distint(t):
    v,c=True,0
    m=max(t)
    for i in range(len(t)):
        if m==t[i]:
            c+=1
    if c>=2:
        v=False
    return v
def potentiels_max(t):
    res=[]
    for i in range(len(t)):
        if t[i]==max(t):
            res.append(i)
    return res
#Fonction de determination de l'element pivot
def pivot(matrice_initiale):
    if element_distint(matrice_initiale):
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
    else:
        pm=potentiels_max(matrice_initiale)
        mcv=[]
        for i in range(len(matrice_initiale)):
#print(pivot(t))
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
        return [matrice_suivante,save_ecrasement]
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
def creates_matrice(hote,l,c):
    h=500
    v=500
    hinit,vinit,w,he,edv,edh=150,50,50,50,v-3*100,h-3*100
    cv,ch=edv//l,edh//c
    m=[]
    for i in range(l):
        n=[Entry(hote,font="Calibri "+str(w//5)) for i in range(c)]
        m.append(n)
    for i in range(len(m)):
        for k in range(len(m[i])):
            m[i][k].place(x=vinit+k*ch+15*k-50,y=hinit+i*cv-120,widt=cv,height=ch)
    return m
def recdim(t):
    global mat,f,fen
    try:
        f.destroy()
    except:
        ""
    f=Frame(fen)
    f.place(x=0,y=100,height=300,widt=500)
    try:
        mat=creates_matrice(f,int(t[0].get()),int(t[1].get()))
        #print(mat)
    except:
        print("entrez des valeurs correctes")
def rec():
    global mat
    res=[]
    for i in range(len(mat)):
        res.append([float(mat[i][k].get()) for k in range(len(mat[i]))])
    tab=solution(res)
    sol=""
    #print(tab)
    for i in range(len(tab[0])):
        sol+=tab[0][i]+" = "+str(tab[1][i])+"\n"
    c.configure(text=sol)

#.......................................
#print(solution(t))
from tkinter import*
fen=Tk()
fen.title("Simplexe")
fen.geometry("500x500+550+200")
fen.update()
fen["bg"]="turquoise"
tdim=[Entry(fen,font="Calibri 25") for i in range(2)]
tdim[0].place(x=100+25,y=30,widt=50,height=50)
tdim[1].place(x=100+25+50+50,y=30,widt=50,height=50)
f=Frame(fen)
f.place(x=0,y=100,height=300,widt=500)
c=Label(fen)
c.place(x=30,y=400)
be=Button(fen,relief="flat",bg="blue",text="Entrez",command=rec)
be.place(x=100+25+50+50+50+50,y=400,widt=50,height=50)
bv=Button(fen,relief="flat",bg="blue",text="Validez",command=lambda x=tdim:recdim(x))
bv.place(x=450,y=50,widt=50,height=50)






