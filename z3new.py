import random
import networkx as nx
import matplotlib.pyplot as plt

graff=[[]]

i=0
j=0
while i < 100:
   graff.append([])
   i=i+1

i=0
j=0
while i < 100:
    while j < 100:
        graff[i].append(1)
        j=j+1
    i=i+1
    j=0 
i=0
j=0
while i < 100:
    while j < 100:
        if i==j:
            graff[i][j]=0
        j=j+1
    i=i+1
    j=0

i=0
j=0
rand=0
while i < 100:
    while j < 100:
        if (random.random()>=rand):
            graff[i][j]=0
        j=j+1
    i=i+1
    j=0

i=0
j=0


i=0
j=0
while i < 100:
    while j < 100:
        graff[j][i]=graff[i][j]
        j=j+1
    i=i+1
    j=i
i=0
j=0
'''
graff2=graff
while i < 100:
    while j < 100:
        graff2[j][i]=0
        j=j+1
    i=i+1
    j=i
'''
spectr=[]


i=0
j=0
ch=0
while i < 100:
    while j < 100:
        if graff[i][j]==1:
           ch=ch+1 
        j=j+1
    spectr.append(ch)
    ch=0
    i=i+1
    j=0



spsok=[]
i=0
j=0

while i < 100:
    while j < 100:
        if graff[i][j]==1:
            spsok.append([i,j])
        j=j+1
    i=i+1
    j=0
print(spectr)
#plt.hist(spectr,density=1,bins=100)
#plt.axis([0,100,0,1])
#plt.show() 
b=[]
b1=[]
bb=0
i=0
j=0
while i<20:
    b1.append(i*5)
    b.append(bb)
    bb=bb+0.05
    i=i+1
b[1]=0.06
b[3]=0.16
b[4]=0.19
b[7]=0.36
b[13]=0.66
b[15]=0.74
b[18]=0.89
plt.figure(figsize=(12, 7))
plt.plot(b1, b, 'o-r', alpha=0.7, label="p", lw=5, mec='b', mew=2, ms=10)
plt.legend()
plt.grid(True)
plt.show() 

comp=[]
Graf = nx.Graph() 
Graf.add_edges_from (spsok)

pos=nx.spring_layout(Graf)  

nx.draw(Graf,pos,node_color='#FF8C00',edge_color='#00008B',width=0.1,edge_cmap=plt.cm.Blues,with_labels=True)

print(nx.number_connected_components(Graf))
#plt.show() 


