#t=[[3,6,9,0],[6,5,8,2]]
#t=[[-1,3,5,0,0,0,0], [0,1,2,1,0,0,10000], [0,2,3,0,1,0,12000], [0, 1, 4, 0, 0, 1, 15000]]
t=[[-1,1.75,0,0,0,-1.25,-18750],[0,0.5,0,1,0,-0.5,2500],[0,1.25,0,0,1,-0.75,750],[0,0.25,1,0,0,0.25,3750]]
p=[[2,1,0,0,0,0,],[1,5,1,0,0,10],[1,3,0,1,0,6],[1,1,0,0,1,4]]
def pivot(t):
    vt=[]
    cp=t[0].index(max(t[0]))
    for i in range(len(t)):
        if t[i][cp]!=0:
            vt.append((t[i][len(t[i])-1])/t[i][cp])
        else:
            vt.append("infini")
    vmin=vt[1]
    for i in range(1,len(vt)):
        if vt[i]!="infini" :
            if vt[i]<=vmin:
                vmin=vt[i]
    lp=vt.index(vmin)
    return (cp,lp)
#print(pivot(t))
def resoudre(t,cp,lp):
    ep=t[lp][cp]
    td=[[0 for i in range(len(t[0]))] for k in range(len(t))]
    for i in range(len(t)-1):
        for k in range(len(t[i])):
            td[i][k]=t[i][k]-((t[i][cp]*t[lp][k])/ep)
    td[len(td)-1]=[(t[len(t)-1][i])/ep for i in range(len(t[len(t)-1]))]
    return td
def simplexe0(t):
    u=pivot(t)
    v=resoudre(t,u[0],u[1])
    if max(v[0])>0:
        return simplexe0(v)
    else:
        return v
#print(pivot(p))
print(simplexe0(p))
    