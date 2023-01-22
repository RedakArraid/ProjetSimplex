t=[[3,5,0,0,0,0],[1,2,1,0,0,10000],[2,3,0,1,0,12000],[1,4,0,0,1,15000]]
t=[[-1,1.75,0,0,0,-1.25,-18750],[0,0.5,0,1,0,-0.5,2500],[0,1.25,0,0,1,-0.75,750],[0,0.25,1,0,0,0.25,3750]]
m=[[12,12,0,0,0,0],[1,1,1,0,0,7],[2,1,0,1,0,9],[6,1,2,1,0,15]]
q=[[12,12,0,0,0],[1,1,1,0,7],[2,1,0,1,9]]
p=[[12,1,0,0,0],[1,1,1,0,7],[2,1,0,1,9]]
mat=[]
def joli(arg):
    d=str(arg)
    for i in range(len(d)):
        if d[i]==".":
            k=d[i+1:]
            f=i+1
    if k[:2]=="00" or k=="0":
        d=d[:f-1]
    else:
        d=d[:f-1]+","+k[:2]
        if len(k)>=3:
            if int(k[2])>=5:
                d=d[:f-1]+","+k[0]+str(int(k[1])+1)
    return d
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
    for i in range(len(t[0])):
        if t[0][i]==max(t[0]):
            res.append(i)
    return res
#fonction permettant de sauvegarder les resultats des calculs : element solution/element de la colonne pivot
def det_save_tab(matrice_initiale,colonne_pivot):
    #tableau permettant de sauvegarder les resultats des calculs : element solution/element de la colonne pivot
    tab=[]
    #...................................
    # calacul de : element solution/element de la colonne pivot
    for line in range(len(matrice_initiale)):
        if matrice_initiale[line][colonne_pivot]!=0:
            tab.append((matrice_initiale[line][len(matrice_initiale[line])-1])/matrice_initiale[line][colonne_pivot])
        else:
            tab.append("infini")
        #...................................
    return tab
#...................................
#fonction de determination du minimum de save_tab
def det_min_save_tab(tab):
    # determination du minimum de save_tab
    for line in range(1,len(tab)):
        if tab[line]!="infini":
            minimum_tab=tab[line]
            pass
    for line in range(1,len(tab)):
        if tab[line]!="infini" :
            if tab[line]<=minimum_tab and tab[line]>=0:
                minimum_tab=tab[line]
    return minimum_tab
#...................................
#fonction de determination du minimum des rapports pour les potentiels colonnes pivots
def det_tab_min_sav_tab_pot(t):
    tab=[]
    for i in range(len(t)):
        if "infini" in t[i]:
            tab.append("exclu")
        else:
            tab.append(min(t[i][1:len(t[i])]))
    return tab
#...................................
#fonction de determination du maximum des minimums des differents rapports pour les potentiels colonnes pivots
def det_max_des_min_tab_min_save_tab_pot(tab):
    mx=[]
    for i in range(len(tab)):
        if tab[i]!="exclu":
            mx=tab[i]
            pass
    for i in range(len(tab)):
        if tab[i]!="exclu" and tab[i]>mx:
            mx=tab[i]
    return mx
#Fonction permettant de determiner la ligne pivot connaissant la colonne pivot
def det_ligne_pivot(matrice_initiale,colonne_pivot):
        # Determination de save_tab
        save_tab=det_save_tab(matrice_initiale,colonne_pivot)
        #.....................................
        minimum_save_tab=det_min_save_tab(save_tab)
        #deduction de la ligne pivot a partir du minimum de save_tab
        return save_tab.index(minimum_save_tab)
        #...................................
#...................................
#Fonction de determination de l'element pivot
def pivot(matrice_initiale):
    if element_distint(matrice_initiale[0]):
        #Identification de la colonne pivot
        colonne_pivot=matrice_initiale[0].index(max(matrice_initiale[0]))
        #...................................
        #Determination de la ligne pivot
        ligne_pivot=det_ligne_pivot(matrice_initiale,colonne_pivot)
        #...................................
        return (colonne_pivot,ligne_pivot)
    else:
        #determination de la valeur des maximum du tableau
        potentiel_max=potentiels_max(matrice_initiale)
        #...................................
        #matrice des potentiels colonnes pivots
        save_tab_pot=[]
        #...................................
        #determination des elements de matrice des potentiels colonnes pivots
        for i in range(len(potentiel_max)):
            save_tab_pot.append(det_save_tab(matrice_initiale,potentiel_max[i]))
        #...................................
        #determination du minimum des rapports obtenus pour chaque matrice des potentiels colonnes pivots
        tab_min_save_tab_pot=det_tab_min_sav_tab_pot(save_tab_pot)
        #...................................
        #determination du maximum des minimums obtenus
        max_des_min=det_max_des_min_tab_min_save_tab_pot(tab_min_save_tab_pot)
        #deduction de la colonne pivot
        colonne_pivot=save_tab_pot.index(save_tab_pot[tab_min_save_tab_pot.index(max_des_min)])
        #...................................
        #Determination de la ligne pivot
        ligne_pivot=det_ligne_pivot(matrice_initiale,colonne_pivot)
        #...................................
        return (colonne_pivot,ligne_pivot)
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
    #arrangement des valeurs de matrice_finale
    """matrice_final_arrange=[matrice_finale[0][i] for i in range(len(matrice_finale[0]))]
    for i in range(len(matrice_final_arrange)):
        for j in range(len(matrice_final_arrange[]))
            matrice_final_arrange[][]=[joli(matrice_finale[0][i][j])"""
    #deduction des solutions dans la matrice finale
    matrice_solution=[matrice_finale[0][i][len(matrice_finale[0][i])-1] for i in range(len(matrice_finale[0]))]
    #...................................
    #matrice des variables ayant une valeur non nulle
    matrice_variables=["e"+str(i+1) for i in range(len(matrice_finale[0])-1)]
    matrice_variables.insert(0,"Z")
    #...................................
    for line in range(len(matrice_finale[1])):
        matrice_variables[matrice_finale[1][line][1]]="x"+str(matrice_finale[1][line][0]+1)
    return (matrice_variables,matrice_solution,matrice_finale)
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
    except:
        print("entrez des valeurs correctes")
def rec():
    global mat,be,mf
    res=[]
    for i in range(len(mat)):
        res.append([float(eval(mat[i][k].get())) for k in range(len(mat[i]))])
    tab=solution(res)
    sol=""
    for i in range(len(tab[0])):
        sol+=tab[0][i]+" = "+str(joli(tab[1][i]))+"\n"
    c.configure(text=sol)
    aff=""
    for i in range(len(tab[2][0])):
        for k in range(len(tab[2][0][i])):
            aff+=str(joli(tab[2][0][i][k]))+"  "
        aff+="\n"
    laf.configure(text=aff)
    laf.pack()
    be.place(x=420,y=400,widt=70,height=70)
i=0
def amf():
    global mf,fen,i
    if i==0:
        be.configure(text="Masquez"+"\n"+"matrice"+"\n"+"finale")
        mf.lift()
        mf.place(x=0,y=100,height=300,widt=500)
        i=1
    else:
        be.configure(text="Afficher"+"\n"+"matrice"+"\n"+"finale")
        mf.lower()
        mf.place(x=0,y=100,height=0,widt=0)
        i=0

#.......................................
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
mf=Frame(fen)
laf=Label(mf)
c=Label(fen)
c.place(x=30,y=400)
be=Button(fen,relief="flat",bg="blue",text="Entrez",command=rec)
be.place(x=350,y=400,widt=50,height=50)
bv=Button(fen,relief="flat",bg="blue",text="Validez",command=lambda x=tdim:recdim(x))
bv.place(x=450,y=50,widt=50,height=50)
be=Button(fen,relief="flat",bg="blue",text="Afficher"+"\n"+"matrice"+"\n"+"finale",command=amf)








