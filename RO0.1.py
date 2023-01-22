#t=[[3,6,9,0],[6,5,8,2]]
#t=[[-1,3,5,0,0,0,0], [0,1,2,1,0,0,10000], [0,2,3,0,1,0,12000], [0, 1, 4, 0, 0, 1, 15000]]
o=[[3,5,0,0,0,0],[1,2,1,0,0,10000],[2,3,0,1,0,12000],[1,4,0,0,1,15000]]
t=[[-1,1.75,0,0,0,-1.25,-18750],[0,0.5,0,1,0,-0.5,2500],[0,1.25,0,0,1,-0.75,750],[0,0.25,1,0,0,0.25,3750]]
p=[[2,1,0,0,0,0,],[1,5,1,0,0,10],[1,3,0,1,0,6],[1,1,0,0,1,4]]
q=[[-1,240,160,0,0,0],[0,1,2,1,0,150],[0,4,2,0,1,400]]
r=[[3,5,0,0,0,0],[1,2,1,0,0,10000],[2,3,0,1,0,12000],[1,4,0,0,1,15000]]
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
def memodep(t,a,b):
    t.append(a,b)
def resoudre(t,cp,lp):
    ep=t[lp][cp]
    td=[[0 for i in range(len(t[0]))] for k in range(len(t))]
    for i in range(len(t)):
        for k in range(len(t[i])):
            td[i][k]=t[i][k]-((t[i][cp]*t[lp][k])/ep)
    td[lp]=[(t[lp][i])/ep for i in range(len(t[lp]))]
    return td
def simplexe0(t,gd):
    u=pivot(t)
    gd.append(u)
    v=resoudre(t,u[0],u[1])
    if max(v[0])>0:
        return simplexe0(v,gd)
    else:
        return (v,gd)
def solution(t):
    tf=simplexe0(t,[])
    ts=[tf[0][i][len(tf[0][i])-1] for i in range(len(tf[0]))]
    te=["e"+str(i+1) for i in range(len(tf[0])-1)]
    te.insert(0,"Z")
    for i in range(len(tf[1])):
        te[tf[1][i][1]]="x"+str(tf[1][i][0]+1)
    return (te,ts)
#print(pivot(p))
#print(simplexe0(t,[]))
#print(simplexe0(q,[]))
print(solution(t))
