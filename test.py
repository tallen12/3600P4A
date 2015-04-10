list=[]
l={}
l['t']=0
l['q']=1
list.append(l)
p={}
p['t']=1
p['q']=1
list.append(p)

p={}
p['t']=0
p['q']=2
list.append(p)

new=filter(lambda x:x['t']==0,list)

print new